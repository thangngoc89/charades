# 📱 Heads Up! Charades Web Game

A mobile-first party charades game featuring real gyroscope tilt motion detection, audio effects, haptics, rich international and holiday categories, and an automated workflow to fetch words from [The Game Gal Word Generator](https://www.thegamegal.com/word-generator/).

---

## 🌐 Live Access Portal

- **HTTPS Mobile Portal**: [https://continued-amended-hudson-servers.trycloudflare.com](https://continued-amended-hudson-servers.trycloudflare.com)
- **Local Access**: `http://localhost:9876`

> **Note**: Both the Node.js server and Cloudflare HTTPS tunnel run in detached background sessions (`setsid`) and **remain active even after your terminal session ends**.

---

## 🎯 Decks & Categories

The game now includes over **1,300+ curated words across 31 decks**:

### 1. 🏙️ My Cities (Taipei, Sài Gòn, Tây Ninh, Bình Thuận, Đà Lạt)
- **🇹🇼 Đài Bắc (Taipei)**: *Trà sữa trân châu Đài Loan, Đậu phụ thối chợ đêm, Tiểu long bao Đỉnh Thái Phong, Tháp Taipei 101, Thả đèn trời phố cổ Thập Phần, Đi dạo phố cổ Cửu Phần (Jiufen), Quẹt thẻ EasyCard đi MRT, Đạp xe đạp YouBike công cộng, Tắm suối nước nóng Bắc Đầu, Cơm thịt kho Lỗ Nhục Phạn, Bánh mì kẹp xúc xích Đại Trường Bao Tiểu Trường, Xếp hàng trà sữa 50 Lan, Tàu điện ngầm MRT Đài Bắc, Uống sữa đậu nành Yonghe, Bánh bao kẹp thịt Guabao, Gà rán khổng lồ chợ đêm Shilin, Đậu hũ kem đá bào xoài, Chợ đêm Ninh Hạ, Cáp treo Maokong uống trà, Viếng đền Long Sơn Tự...*
- **🏙️ TP. Hồ Chí Minh (Sài Gòn)**: *Cà phê sữa đá vỉa hè, Cơm tấm sườn bì chả trứng ốp la, Ổ bánh mì thịt chả thập cẩm giòn rụm, Hủ tiếu gõ đêm khuya gõ lách cách, Bánh tráng trộn Hồ Con Rùa, Ngắm hoàng hôn nóc hầm Thủ Thiêm, Check-in chợ Bến Thành, Phố đi bộ Bùi Viện xập xình nhạc, Kẹt xe ngã tư Hàng Xanh giờ tan tầm, Đi xe buýt đường sông Waterbus, Uống bia hơi vỉa hè zô 100%, Bánh xèo miền Tây giòn rụm cuốn cải xanh, Trà tắc khổng lồ phố đi bộ Nguyễn Huệ, Tiếng rao ve chai đồng nát buổi trưa, Xếp hàng mua bánh mì Huỳnh Hoa, Chợ hoa Hồ Thị Kỷ rực rỡ, Đón hoàng hôn Landmark 81, Lẩu dê tía tô Trương Định, Chen chúc nhà xe miền Tây dịp lễ, Đi phà Cát Lái qua Nhơn Trạch...*
- **⛰️ Tây Ninh Đất Thánh**: *Muối tôm Tây Ninh cay mặn chấm trái cây, Bánh tráng phơi sương Trảng Bàng, Đi cáp treo lên đỉnh Núi Bà Đen, Viếng Tòa Thánh Tây Ninh, Bò tơ Tây Ninh nướng than hồng, Bánh canh Trảng Bàng giò heo nước trong, Cắm trại ngắm hoàng hôn Hồ Dầu Tiếng, Mãng cầu Bà Đen dai ngọt thanh, Săn mây cổng trời Ma Thiên Lãnh, Chùa Hang trên vách đá Núi Bà, Thèo lèo Tây Ninh giòn tan, Bánh tráng dẻo cay ớt me, Nước cốt mây rừng mát lạnh, Chợ Long Hoa nhộn nhịp, Đọt mây gai nướng chấm muối ớt, Tắm suối Trúc róc rách, Check-in cột mốc 986m nóc nhà Nam Bộ, Lễ hội Vía Bà Linh Sơn Thánh Mẫu...*
- **🏖️ Bình Thuận - Biển Mũi Né**: *Trượt cát Đồi Cát Bay Mũi Né, Xe jeep vượt cát trắng Bàu Trắng, Nước mắm cá cơm Phan Thiết truyền thống, Đổ bánh căn trứng cút xíu mại mỡ hành, Ăn lẩu thả Phan Thiết trên bẹ chuối, Bánh quai vạc dai giòn chấm mắm kẹo, Lội bộ ngắm vách đá đỏ Suối Tiên, Vườn thanh long chín đỏ trĩu cành, Lướt ván diều trên sóng biển Mũi Né, Thăm Làng chài Mũi Né đón thuyền thúng, Tháp Po Sah Inư Chăm Pa cổ kính, Ăn gỏi cá mai giòn ngọt bóp thính, Răng mực nướng xiên que sa tế, Bánh tráng nướng mắm ruốc giòn cay nức mũi, Ngọn hải đăng Kê Gà cổ nhất Việt Nam, Đi chợ hải sản đêm Phan Thiết, Đua thuyền rồng sông Cà Ty ngày Tết, Dậy sớm ngắm bình minh trên đồi cát...*
- **🌲 Đà Lạt Sương Mù**: *Bánh tráng nướng Đà Lạt (pizza Việt Nam), Lẩu gà lá é Tao Ngộ cay nồng, Săn mây đồi chè Cầu Đất lúc tờ mờ sáng, Sữa đậu nành nóng chợ đêm kèm bánh tiêu, Lẩu bò Ba Toa quán gỗ nghi ngút khói, Bánh mì xíu mại chén xé bánh giòn rụm, Kem bơ sáp chạm đầu lưỡi ngọt mát, Hái dâu tây chín đỏ tại vườn, Đạp vịt đôi Hồ Xuân Hương sương sớm, Check-in nụ hoa Atisô Quảng trường Lâm Viên, Đi chợ đêm Đà Lạt sắm áo len khăn quàng, Máng trượt thác Datanla băng qua rừng thông, Hồng treo gió dẻo tươm mật, Bánh ướt lòng gà chua ngọt, Ga xe lửa Đà Lạt đầu tàu hơi nước cổ, Lạc giữa vườn hoa Cẩm Tú Cầu bạt ngàn, Chinh phục đỉnh Langbiang ngắm Suối Vàng, Rừng thông reo trong gió se lạnh, Khói thở ra trong đêm đông, Hoa Dã Quỳ vàng rực triền đồi...*

### 2. 🇻🇳 Việt Nam (Lễ Hội, Đời Sống, Ẩm Thực, Thành Ngữ, Động Vật & Nghịch Ngợm)
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
