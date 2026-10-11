#!/usr/bin/env python3
"""
fetch_gamegal.py
----------------
Automated workflow tool to fetch, clean, and organize word lists
from The Game Gal Word Generator (https://www.thegamegal.com/word-generator/).

Usage:
    # List all available games and categories
    python3 scripts/fetch_gamegal.py --list

    # Fetch a specific game and category
    python3 scripts/fetch_gamegal.py --game 4 --cat 30 --output data/thegamegal/christmas.json

    # Fetch all Western Holidays
    python3 scripts/fetch_gamegal.py --theme holidays

    # Fetch all themes and save to data/thegamegal/
    python3 scripts/fetch_gamegal.py --all

    # Fetch and rebuild decks.js automatically
    python3 scripts/sync_decks.py
"""

import sys
import os
import re
import json
import time
import argparse
import urllib.request
import urllib.error

# Registry of known Game Gal games and categories
GAMEGAL_CATALOG = {
    "holidays": {
        "game_id": 4,
        "name": "Western Holidays & Seasons",
        "categories": [
            {"id": 45, "name": "Valentine's Day", "icon": "💖"},
            {"id": 23, "name": "Fourth of July", "icon": "🎆"},
            {"id": 24, "name": "Halloween", "icon": "🎃"},
            {"id": 29, "name": "Thanksgiving", "icon": "🦃"},
            {"id": 30, "name": "Christmas", "icon": "🎄"},
            {"id": 31, "name": "Christmas Songs", "icon": "🎶"},
            {"id": 37, "name": "New Year's", "icon": "🥂"},
            {"id": 35, "name": "Spring & Easter", "icon": "🌸"},
            {"id": 39, "name": "Summer", "icon": "☀️"},
            {"id": 40, "name": "Fall / Autumn", "icon": "🍂"},
            {"id": 38, "name": "Winter", "icon": "❄️"},
            {"id": 44, "name": "Summer Olympics", "icon": "🥇"},
        ]
    },
    "charades": {
        "game_id": 5,
        "name": "Classic Charades & Actions",
        "categories": [
            {"id": 36, "name": "Actions", "icon": "🤸"},
            {"id": 25, "name": "Easy Charades", "icon": "⭐"},
            {"id": 26, "name": "Medium Charades", "icon": "🌟"},
            {"id": 27, "name": "Hard Charades", "icon": "⚡"},
            {"id": 28, "name": "Really Hard Charades", "icon": "🔥"},
        ]
    },
    "pictionary": {
        "game_id": 2,
        "name": "Pictionary Words",
        "categories": [
            {"id": 6, "name": "Easy", "icon": "✏️"},
            {"id": 7, "name": "Medium", "icon": "🎨"},
            {"id": 8, "name": "Hard", "icon": "🖌️"},
        ]
    },
    "catchphrase": {
        "game_id": 3,
        "name": "Catchphrase Party Words",
        "categories": [
            {"id": 13, "name": "Easy", "icon": "🗣️"},
            {"id": 14, "name": "Medium", "icon": "🎯"},
            {"id": 15, "name": "Hard", "icon": "🧠"},
        ]
    },
    "wordplay": {
        "game_id": 7,
        "name": "Wordplay & Sayings",
        "categories": [
            {"id": 69, "name": "Idioms and Sayings", "icon": "💡"},
            {"id": 71, "name": "Opposites", "icon": "🔄"},
            {"id": 72, "name": "Pairs", "icon": "👯"},
        ]
    },
    "movies": {
        "game_id": 8,
        "name": "Movies & Entertainment",
        "categories": [
            {"id": 82, "name": "Disney and Pixar Movies", "icon": "🏰"},
            {"id": 80, "name": "Animated Movies", "icon": "🦁"},
            {"id": 81, "name": "Comedies", "icon": "😂"},
            {"id": 84, "name": "Family Movies", "icon": "🍿"},
            {"id": 90, "name": "Sci-Fi Movies", "icon": "🚀"},
            {"id": 76, "name": "All Movies", "icon": "🎬"},
        ]
    },
    "subjects": {
        "game_id": 1,
        "name": "Themes & Subjects",
        "categories": [
            {"id": 1, "name": "Animals", "icon": "🦁"},
            {"id": 56, "name": "Common Animals", "icon": "🐶"},
            {"id": 4, "name": "Places", "icon": "🌍"},
            {"id": 65, "name": "Sports", "icon": "⚽"},
            {"id": 2, "name": "Food and Cooking", "icon": "🍕"},
            {"id": 63, "name": "Nature", "icon": "🌲"},
            {"id": 52, "name": "Around the House", "icon": "🏠"},
            {"id": 66, "name": "Travel", "icon": "✈️"},
            {"id": 59, "name": "Feelings and Emotions", "icon": "🎭"},
        ]
    },
    "individuals": {
        "game_id": 9,
        "name": "People & Characters",
        "categories": [
            {"id": 92, "name": "Celebrities", "icon": "🌟"},
            {"id": 93, "name": "Characters", "icon": "🦸"},
            {"id": 94, "name": "Historical People", "icon": "📜"},
        ]
    }
}

API_URL = "https://www.thegamegal.com/wordgenerator/generator.php"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def clean_word(w: str) -> str:
    """Clean corrupted encodings, BOM markers, and strip excess whitespace."""
    if not w:
        return ""
    # Strip UTF-8 BOM artifacts and corrupted byte sequences
    w = re.sub(r'[\ufeff\u200b\u200c\u200d]', '', w)
    w = w.replace('Ã¯Â»Â¿', '').replace('ï»¿', '').replace('\ufeff', '')
    w = w.strip()
    return w


def fetch_category_words(game_id: int, category_id: int, retries: int = 3) -> list:
    """Fetch words array from The Game Gal API endpoint."""
    url = f"{API_URL}?game={game_id}&category={category_id}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                raw_bytes = resp.read()
                try:
                    text = raw_bytes.decode('utf-8')
                except UnicodeDecodeError:
                    text = raw_bytes.decode('latin-1')

                data = json.loads(text)
                if data.get("success") and "words" in data:
                    cleaned = []
                    seen = set()
                    for item in data["words"]:
                        word = clean_word(item)
                        if word and word.lower() not in seen:
                            seen.add(word.lower())
                            cleaned.append(word)
                    return cleaned
                else:
                    return []
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(1.0)
            else:
                print(f"[ERROR] Failed to fetch game {game_id}, cat {category_id}: {e}", file=sys.stderr)
                return []
    return []


def generate_hint_for_word(word: str, category_name: str) -> str:
    """Generate a helpful, fun charades hint for words that don't have one."""
    w_lower = word.lower()

    # Action detection
    if re.match(r'^[a-z]+ing\b', w_lower):
        return f"Act out: {word}"

    # Holiday hints
    if "christmas" in category_name.lower():
        if "tree" in w_lower: return "Holiday fir decorated with lights & ornaments"
        if "santa" in w_lower: return "Ho ho ho! Brings presents down the chimney"
        if "snowman" in w_lower: return "Three snowballs, carrot nose, and a top hat"
        if "reindeer" in w_lower: return "Antlers, flying Santa's sleigh"
        return "Christmas & winter holiday favorite!"

    if "halloween" in category_name.lower():
        if "vampire" in w_lower: return "Fangs, cape, allergic to garlic & sunlight"
        if "witch" in w_lower: return "Pointy hat, broomstick, cackling over a cauldron"
        if "zombie" in w_lower: return "Shuffling feet, arms outstretched: Braaains!"
        if "pumpkin" in w_lower: return "Carving a spooky face for a Jack-o'-lantern"
        return "Spooky Halloween character or tradition!"

    if "valentine" in category_name.lower():
        if "cupid" in w_lower: return "Flying baby with bow & love arrows"
        if "chocolate" in w_lower: return "Sweet heart-shaped box of treats"
        return "Valentine's Day romance & sweetness!"

    if "thanksgiving" in category_name.lower():
        if "turkey" in w_lower: return "Gobble gobble! The main Thanksgiving feast"
        return "Thanksgiving feast & grateful family gathering!"

    if "movie" in category_name.lower():
        return "Classic movie title to act out!"

    if "action" in category_name.lower():
        return "Act out this scene silently for your team!"

    return f"Guess this {category_name.lower()} term!"


def fetch_theme(theme_name: str, output_dir: str = "data/thegamegal") -> dict:
    """Fetch all categories for a theme and save them to output directory."""
    if theme_name not in GAMEGAL_CATALOG:
        print(f"Unknown theme: {theme_name}. Available: {list(GAMEGAL_CATALOG.keys())}")
        return {}

    os.makedirs(output_dir, exist_ok=True)
    theme_info = GAMEGAL_CATALOG[theme_name]
    game_id = theme_info["game_id"]
    results = {}

    print(f"\n==========================================")
    print(f"🌐 Fetching Theme: {theme_info['name']} (Game ID {game_id})")
    print(f"==========================================")

    for cat in theme_info["categories"]:
        cat_id = cat["id"]
        cat_name = cat["name"]
        icon = cat.get("icon", "🎯")
        print(f"-> Fetching '{cat_name}' (ID {cat_id})...", end="", flush=True)

        words = fetch_category_words(game_id, cat_id)
        print(f" found {len(words)} words.")

        word_items = []
        for w in words:
            hint = generate_hint_for_word(w, cat_name)
            word_items.append({"word": w, "hint": hint})

        results[cat_id] = {
            "id": f"gamegal-{theme_name}-{cat_id}",
            "name": cat_name,
            "icon": icon,
            "game_id": game_id,
            "category_id": cat_id,
            "theme": theme_name,
            "count": len(word_items),
            "words": word_items
        }

        # Save single category file
        slug = re.sub(r'[^a-z0-9]+', '-', cat_name.lower()).strip('-')
        filepath = os.path.join(output_dir, f"{theme_name}_{cat_id}_{slug}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(results[cat_id], f, ensure_ascii=False, indent=2)

        time.sleep(0.15)  # Be polite to the server

    return results


def fetch_all(output_dir: str = "data/thegamegal") -> dict:
    """Fetch all known Game Gal themes."""
    all_data = {}
    for theme_name in GAMEGAL_CATALOG:
        theme_data = fetch_theme(theme_name, output_dir=output_dir)
        all_data[theme_name] = theme_data

    # Save summary
    summary_path = os.path.join(output_dir, "all_themes_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ All Game Gal themes fetched and saved to {output_dir}/")
    return all_data


def list_catalog():
    """Print the complete catalog of games and categories."""
    print("\n📚 Available The Game Gal Categories Catalog:")
    print("=" * 60)
    for theme_key, theme_data in GAMEGAL_CATALOG.items():
        print(f"\n📂 Theme: [{theme_key.upper()}] - {theme_data['name']} (Game {theme_data['game_id']})")
        for cat in theme_data["categories"]:
            print(f"   • Cat ID {cat['id']:<3} {cat.get('icon', '')}  {cat['name']}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Fetch words from The Game Gal word generator")
    parser.add_argument("--list", action="store_true", help="List all available games and categories")
    parser.add_argument("--theme", type=str, help="Fetch all categories for a theme (e.g. holidays, charades, movies)")
    parser.add_argument("--game", type=int, help="Fetch by specific Game ID")
    parser.add_argument("--cat", type=int, help="Fetch by specific Category ID")
    parser.add_argument("--all", action="store_true", help="Fetch all themes from The Game Gal")
    parser.add_argument("--output", type=str, default="data/thegamegal", help="Output directory or JSON file")

    args = parser.parse_args()

    if args.list:
        list_catalog()
        return

    if args.all:
        fetch_all(output_dir=args.output)
        return

    if args.theme:
        fetch_theme(args.theme, output_dir=args.output)
        return

    if args.game is not None and args.cat is not None:
        words = fetch_category_words(args.game, args.cat)
        print(f"Fetched {len(words)} words for Game {args.game}, Category {args.cat}:")
        for w in words[:15]:
            print(f" - {w}")
        if len(words) > 15:
            print(f" ... and {len(words) - 15} more.")

        if args.output.endswith(".json"):
            os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump({"game": args.game, "category": args.cat, "words": words}, f, indent=2)
            print(f"Saved to {args.output}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
