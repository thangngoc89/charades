# 📱 Heads Up! Charades Web Game

A mobile-first party charades game featuring real gyroscope tilt motion detection, audio effects, haptics, rich international and holiday categories, and an automated workflow to fetch words from [The Game Gal Word Generator](https://www.thegamegal.com/word-generator/).

---

## 🌐 Live Access Portal

- **HTTPS Mobile Portal**: [https://continued-amended-hudson-servers.trycloudflare.com](https://continued-amended-hudson-servers.trycloudflare.com)
- **Local Access**: `http://localhost:9876`

> **Note**: Both the Node.js server and Cloudflare HTTPS tunnel run in detached background sessions (`setsid`) and **remain active even after your terminal session ends**.

---

## 🎯 Decks & Categories

The game now includes over **1,200+ curated words across 24 decks**:

### 1. 🇻🇳 Việt Nam
- **🧧 Tết & Lễ Hội Truyền Thống**: *Múa lân, Gói bánh chưng, Lì xì, Xem pháo hoa giao thừa, Xin chữ ông đồ, Dọn nhà cuối năm, Đi chợ hoa, Thả cá chép tiễn ông Táo, Rước đèn Trung thu, Phá cỗ, Trang trí cây thông Noel, Ông già Noel kẹt trong ống khói, Hái lộc, Chúc Tết họ hàng, Xông đất, Bày mâm ngũ quả, Đi viếng chùa đầu năm, Chơi bầu cua tôm cá, Mặc áo dài du xuân, Nấu bánh tét, Đốt pháo bông...*
- **🛵 Đời Sống Hài Hước & Thường Ngày**: *Chạy xe máy trời mưa, Kẹt xe giờ cao điểm, Chụp ảnh check-in, Hát karaoke, Đánh cầu lông, Tập thể dục buổi sáng ở công viên, Ngủ gật trong cuộc họp, Mặc cả ở chợ, Đánh răng, Gội đầu, Lau nhà, Phơi quần áo, Leo cầu thang khi thang máy hỏng, Tìm chìa khóa xe, Quét mã QR thanh toán, Nhảy TikTok, Câu cá, Đạp xe, Bơi ếch, Đá cầu, Đá bóng, Chạy trốn chó, Chụp ảnh tự sướng, Dắt xe qua đoạn ngập nước, Lướt điện thoại trên giường...*
- **🍲 Ẩm Thực & Quán Xá Việt Nam**: *Ăn phở, Cuốn gỏi cuốn, Ăn hột vịt lộn, Uống trà đá vỉa hè, Ăn lẩu, Nướng thịt, Ăn bánh mì, Ăn ốc bằng tăm, Pha cà phê phin, Ăn kem ốc quế, Ăn sầu riêng, Ăn bún đậu mắm tôm, Uống trà sữa trân châu, Ăn mì cay, Rán trứng, Ăn chè, Ăn cua, Ăn bánh tráng trộn, Ăn kẹo bông, Bổ dưa hấu, Húp nước lèo xì xụp, Gắp mì tôm ban đêm...*
- **📜 Thành Ngữ & Tục Ngữ Dân Gian**: *Đàn gảy tai trâu, Nước đổ lá khoai, Ếch ngồi đáy giếng, Vắt chanh bỏ vỏ, Cưỡi ngựa xem hoa, Nước đến chân mới nhảy, Đẽo cày giữa đường, Ném đá giấu tay, Dã tràng xe cát, Há miệng chờ sung, Chuột sa chĩnh gạo, Gậy ông đập lưng ông, Ăn cháo đá bát, Mò kim đáy bể, Rút dây động rừng, Múa rìu qua mắt thợ, Nói như vẹt, Đầu voi đuôi chuột, Thả con săn sắt bắt con cá rô, Có công mài sắt có ngày nên kim...*

### 2. 💍 Wedding & Bridal Party
- **Wedding Charades & Bridal Shower**: *Catching the bouquet, Walking down the aisle, Cutting the wedding cake, First dance, Giving a wedding toast, Exchanging wedding rings, Runaway bride, Bachelor party hangover, Catching the garter, Crying mother-of-the-bride, Saying "I Do", Popping champagne bottle, Flower girl dropping petals, Wedding cold feet, Packing honeymoon suitcase, Posing for 500 photos, Clinking glasses for a kiss, Best man losing the rings...*

### 3. 🎄 Western Popular Holidays
- **🌟 Western Holidays Mega Deck**: Best all-in-one curated holiday compilation.
- **🎅 Christmas & Giáng Sinh**: Santa Claus, Rudolph, Christmas tree, wrapping gifts, snowmen, mistletoe...
- **🎃 Halloween & Đêm Hội Ma**: Jack-o'-lantern, trick-or-treating, vampires, witches, haunted house...
- **🦃 Thanksgiving & Lễ Tạ Ơn**: Carving turkey, pumpkin pie, breaking wishbone, parade...
- **💖 Valentine's Day & Lễ Tình Nhân**: Cupid's arrow, heart chocolates, red roses, romantic dinner...
- **🥂 New Year's Eve & Giao Thừa**: Times Square ball drop, midnight kiss, popping champagne...
- **🎆 4th of July & Summer Fest**: Fireworks, backyard BBQ grilling, sparklers, hot dogs...
- **🐰 Easter & Spring Blooms**: Egg hunt, painting eggs, chocolate bunny, flowers...

### 4. 🎭 The Game Gal Featured Decks
- **🤸 Charades Actions & Situations**: 130+ dynamic physical actions.
- **🍿 Disney, Pixar & Animated Movies**: 150+ beloved movies.
- **💡 English Idioms & Sayings**: 400+ classic idioms.

### 5. 🥑 Millennials & 🧒 Kids (<10)
- Preserved with classic nostalgia, 90s/2000s music bangers, adulting struggles, zoo animals, cartoons, and silly actions.

---

## ⚡ Automated Workflow for The Game Gal

### Option A: In-App 1-Click Generator & Importer
Inside the web app under **✏️ Custom & Auto**, tap **⚡ Game Gal Auto Generator**:
1. Select any Game Theme (Holidays, Charades, Movies, Subjects, Wordplay, etc.).
2. Select Category (Christmas, Actions, Animals, Sports, Disney...).
3. Choose word count (25, 50, 100, or All).
4. Tap **⚡ Fetch & Preview Words** -> Preview words live!
5. Tap **💾 Save as New Deck** or **▶ Play Instantly**.

### Option B: Python CLI Workflow (`scripts/`)
Automated scripts are included to fetch, clean, and sync words directly from `thegamegal.com`:

```bash
# 1. View all available games and categories
python3 scripts/fetch_gamegal.py --list

# 2. Fetch specific theme (e.g. holidays, charades, movies, wordplay)
python3 scripts/fetch_gamegal.py --theme holidays

# 3. Fetch specific game & category
python3 scripts/fetch_gamegal.py --game 4 --cat 30 --output data/thegamegal/custom_christmas.json

# 4. Fetch all themes and categories
python3 scripts/fetch_gamegal.py --all

# 5. Recompile and sync all decks into decks.js
python3 scripts/sync_decks.py
```

---

## 🎮 How to Play

1. **Open the Portal URL** on your mobile browser (Safari, Chrome, etc.).
2. **Select a Category Tab**: *Việt Nam*, *Western Holidays*, *Wedding*, *The Game Gal*, *Millennials*, *Kids*, or *Custom & Auto*.
3. Tap **Play Deck** -> **Start Round**:
   - Hold phone **horizontally on your forehead** with screen facing your teammates.
4. **Motion Tilt Controls**:
   - 🟢 **Tilt Back / Up (Look at ceiling)**: **CORRECT! (+1 pt)**
   - 🟡 **Tilt Forward / Down (Nod down)**: **PASS (Skip word)**
   - ⚪ **Return to Neutral (Upright)** between guesses.
5. **Touch / Click Fallback**:
   - Tap right side = Correct, tap left side = Pass.
   - Desktop keyboard: `Space` / `Arrow Up` = Correct, `Enter` / `Arrow Down` = Pass.

---

## 🛠️ Server Management

```bash
# Start server & Cloudflare HTTPS tunnel
bash start.sh

# Stop server & tunnel
bash stop.sh

# View live logs
cat server.log
cat tunnel.log
```
