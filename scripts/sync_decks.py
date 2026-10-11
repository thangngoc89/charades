#!/usr/bin/env python3
"""
sync_decks.py
-------------
Compiles all curated decks, Vietnamese decks, wedding decks,
Game Gal fetched categories, and millennial/kids decks into the main decks.js file.
Expanded with massive Animal and Silly Action decks!
"""

import os
import json
import re

# Load fetched Game Gal categories if present
def load_gamegal_json(filename):
    path = os.path.join("data/thegamegal", filename)
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None
    return None

def main():
    print("🔄 Building and synchronizing charades decks with expanded collections...")

    # Load any fetched files
    actions_data = load_gamegal_json("charades_36_actions.json")
    animals_data = load_gamegal_json("subjects_1_animals.json")
    christmas_data = load_gamegal_json("holidays_30_christmas.json")
    christmas_songs = load_gamegal_json("holidays_31_christmas-songs.json")
    halloween_data = load_gamegal_json("holidays_24_halloween.json")
    thanksgiving_data = load_gamegal_json("holidays_29_thanksgiving.json")
    valentine_data = load_gamegal_json("holidays_45_valentine-s-day.json")
    newyear_data = load_gamegal_json("holidays_37_new-year-s.json")
    july4_data = load_gamegal_json("holidays_23_fourth-of-july.json")
    easter_data = load_gamegal_json("holidays_35_spring-easter.json")
    disney_data = load_gamegal_json("movies_82_disney-and-pixar-movies.json")
    idioms_data = load_gamegal_json("wordplay_69_idioms-and-sayings.json")

    # --- 1. VIETNAMESE DECKS ---
    vn_holidays_deck = {
        "id": "vn-holidays-tet",
        "name": "🧧 Tết & Lễ Hội Việt Nam",
        "icon": "🏮",
        "color": "#ef4444",
        "description": "Các phong tục, hoạt động truyền thống ngày Tết và lễ hội rực rỡ!",
        "words": [
            {"word": "Múa lân", "hint": "Đội đầu lân nhảy múa theo tiếng trống tùng cheng"},
            {"word": "Gói bánh chưng", "hint": "Xếp lá dong, đổ gạo nếp, đậu xanh, thịt mỡ buộc lạt vuông vắn"},
            {"word": "Lì xì", "hint": "Trao bao bao đỏ chúc mừng năm mới may mắn"},
            {"word": "Xem pháo hoa giao thừa", "hint": "Ngước nhìn bầu trời đếm ngược khoảnh khắc đầu năm mới"},
            {"word": "Xin chữ ông đồ", "hint": "Ngồi chiếu hoa xin câu đối chữ thư pháp mực tàu"},
            {"word": "Dọn nhà cuối năm", "hint": "Quét mạng nhện, lau chùi bàn ghế sáng bóng đón Tết"},
            {"word": "Đi chợ hoa", "hint": "Ngắm và khiêng cành đào, chậu mai, quất trĩu quả về nhà"},
            {"word": "Thả cá chép tiễn ông Táo", "hint": "Thả cá chép đỏ xuống sông ngày 23 tháng Chạp"},
            {"word": "Rước đèn Trung thu", "hint": "Cầm lồng đèn ông sao hát bài rước đèn dưới trăng rằm"},
            {"word": "Phá cỗ", "hint": "Cùng bạn bè chia nhau bánh nướng bánh dẻo mâm cỗ Trung thu"},
            {"word": "Trang trí cây thông Noel", "hint": "Treo quả châu, dây kim tuyến và gắn ngôi sao lên ngọn cây"},
            {"word": "Ông già Noel kẹt trong ống khói", "hint": "Bụng bự mang túi quà chui ống khói bị kẹt lúng túng"},
            {"word": "Hái lộc", "hint": "Ngắt cành lộc non đầu xuân mang may mắn về nhà"},
            {"word": "Chúc Tết họ hàng", "hint": "Khoanh tay cúi chào chúc ông bà cô chú vạn sự như ý"},
            {"word": "Xông đất", "hint": "Người đầu tiên bước vào nhà đạp đất năm mới mang tài lộc"},
            {"word": "Bày mâm ngũ quả", "hint": "Cầu dừa đủ xoài sung xếp ngay ngắn lên bàn thờ"},
            {"word": "Chơi bầu cua tôm cá", "hint": "Lắc đĩa xúc xắc đặt cược vui nhộn ngày Tết"},
            {"word": "Mặc áo dài du xuân", "hint": "Tạo dáng thướt tha chụp hình bên cành mai cành đào"},
            {"word": "Nấu bánh tét thâu đêm", "hint": "Quây quần bên nồi bánh to bập bùng ánh lửa đêm giao thừa"},
            {"word": "Đốt pháo bông cầm tay", "hint": "Cầm que pháo bông sáng lấp lánh xoay tròn vẫy vẫy"},
            {"word": "Đi chùa hái hoa lộc", "hint": "Thắp nén nhang cầu bình an cho cả gia đình"},
            {"word": "Rửa lá dong gói bánh", "hint": "Dùng khăn lau từng chiếc lá dong xanh mướt cho sạch sẽ"},
            {"word": "Ăn mứt gừng cay nồng", "hint": "Cắn miếng mứt gừng cay xè vừa nhai vừa uống trà nóng"},
            {"word": "Bê chậu mai vàng", "hint": "Hai người cùng khiêng chậu mai nặng trĩu hoa nở toe toét"}
        ]
    }

    vn_daily_actions_deck = {
        "id": "vn-daily-life",
        "name": "🛵 Đời Sống Hài Hước & Đời Thường",
        "icon": "🤪",
        "color": "#f59e0b",
        "description": "Những khoảnh khắc sinh hoạt 'cười ra nước mắt' quen thuộc của người Việt!",
        "words": [
            {"word": "Chạy xe máy trời mưa", "hint": "Mặc áo mưa cánh dơi bay phần phật, vuốt nước trên kính"},
            {"word": "Kẹt xe giờ cao điểm", "hint": "Nhích từng xăng-ti-mét giữa dòng xe cộ bóp còi inh ỏi"},
            {"word": "Chụp ảnh check-in", "hint": "Đổi 10 tư thế trước gương quán cà phê sang chảnh"},
            {"word": "Hát karaoke", "hint": "Cầm micro gào thét hết mình nốt cao không tới"},
            {"word": "Đánh cầu lông", "hint": "Nhảy lên đập cầu thật mạnh nhưng vợt đánh vào không khí"},
            {"word": "Tập thể dục buổi sáng ở công viên", "hint": "Xoay khớp vỗ tay đi giật lùi kiểu các cô chú trung niên"},
            {"word": "Ngủ gật trong cuộc họp", "hint": "Cố chống cằm mở mắt nhưng đầu gật lên gật xuống"},
            {"word": "Mặc cả ở chợ", "hint": "Chê đắt giả vờ bỏ đi để người bán gọi giật lại"},
            {"word": "Đánh răng", "hint": "Bôi kem chải răng súc miệng nhổ bọt xèo xèo"},
            {"word": "Gội đầu", "hint": "Cào gãi da đầu xà phòng đầy mắt nhắm tịt"},
            {"word": "Lau nhà", "hint": "Cầm cây lau sàn xoay vòng vắt nước sạch bóng"},
            {"word": "Phơi quần áo", "hint": "Giũ đồ phành phạch móc lên sào kẹp chặt"},
            {"word": "Leo cầu thang khi thang máy hỏng", "hint": "Thở hổn hển ôm đùi leo lên tầng 10"},
            {"word": "Tìm chìa khóa xe", "hint": "Lục tung balo móc túi áo quần không nhớ để đâu"},
            {"word": "Quét mã QR thanh toán", "hint": "Cầm điện thoại căn góc máy quét mã nhưng mạng quay vòng vòng"},
            {"word": "Nhảy TikTok", "hint": "Lắc lư theo nhạc xu hướng làm điệu trước camera"},
            {"word": "Câu cá", "hint": "Móc mồi quăng cần giật mạnh con cá to tướng"},
            {"word": "Đạp xe", "hint": "Gò lưng đạp dốc đứng mồ hôi nhễ nhại"},
            {"word": "Bơi ếch", "hint": "Hai tay quạt ngang đạp chân ếch ngoi đầu thở"},
            {"word": "Đá cầu", "hint": "Tâng cầu bằng má trong má ngoài rồi tung móc gót"},
            {"word": "Đá bóng", "hint": "Dẫn bóng qua người sút vào góc chữ A ăn mừng"},
            {"word": "Chạy trốn chó", "hint": "Bị chó rượt chạy hết tốc lực nhảy tót lên tường rào"},
            {"word": "Chụp ảnh tự sướng", "hint": "Giơ máy lên cao chu môi giơ tay chữ V"},
            {"word": "Dắt xe qua đoạn ngập nước", "hint": "Nước ngập đến yên xe lội bì bõm dắt xe chết máy"},
            {"word": "Lướt điện thoại trên giường", "hint": "Nằm ngửa cầm điện thoại vô tình tuột tay rơi trúng mặt"},
            {"word": "Gạt chân chống xe máy", "hint": "Đang chạy bị người bên cạnh hô 'Gạt chân chống kìa!'"},
            {"word": "Xem livestream chốt đơn", "hint": "Gõ bình luận mã số kèm số điện thoại lia lịa"},
            {"word": "Uống bia dô dô", "hint": "Cùng đứng dậy cầm cốc bia hô 1 2 3 DÔ!"},
            {"word": "Quên mật khẩu wifi", "hint": "Ngước nhìn dưới đáy cục router bấm từng ký tự nhỏ xíu"},
            {"word": "Đứng chờ thang máy đông đúc", "hint": "Cố chen một chân vào thang máy kêu tít tít quá tải"},
            {"word": "Nặn mụn trước gương", "hint": "Nhăn mặt nhe răng bóp thật mạnh giật bắn người"},
            {"word": "Bị điện giật nhẹ", "hint": "Chạm vào vỏ máy tính nhảy dựng người giật thót"},
            {"word": "Giả vờ xem giờ khi quê độ", "hint": "Vừa vấp ngã vội vàng nhìn đồng hồ làm bộ đang vội"}
        ]
    }

    vn_food_deck = {
        "id": "vn-food-culture",
        "name": "🍲 Ẩm Thực & Quán Xá Việt Nam",
        "icon": "🍜",
        "color": "#ec4899",
        "description": "Các món ăn đường phố và nét ăn uống đặc trưng không lẫn đi đâu được!",
        "words": [
            {"word": "Ăn phở", "hint": "Vắt chanh thêm ớt gắp sợi phở húp nước dùng nóng hổi"},
            {"word": "Cuốn gỏi cuốn", "hint": "Thấm bánh tráng xếp rau tôm thịt cuộn tròn chấm tương đậu"},
            {"word": "Ăn hột vịt lộn", "hint": "Đập đầu trứng gắp mề mề chấm muối tiêu chanh kèm rau răm"},
            {"word": "Uống trà đá vỉa hè", "hint": "Ngồi ghế nhựa thấp cắn hạt hướng dương ngụm trà mát lạnh"},
            {"word": "Ăn lẩu", "hint": "Gắp đồ nhúng vào nồi nước lẩu đang sôi sùng sục khói nghi ngút"},
            {"word": "Nướng thịt", "hint": "Lật miếng sườn xèo xèo trên vỉ than hồng khói bay thơm phức"},
            {"word": "Ăn bánh mì", "hint": "Cầm ổ bánh mì giòn rụm cắn rộp một miếng rơi vụn bánh"},
            {"word": "Ăn ốc bằng tăm", "hint": "Dùng gai hoặc tăm nhọn khều ruột con ốc béo ngậy chấm mắm gừng"},
            {"word": "Pha cà phê phin", "hint": "Nén bột cà phê rót nước sôi đợi từng giọt rơi xuống cốc sữa đặc"},
            {"word": "Ăn kem ốc quế", "hint": "Liếm kem tròn xoe xoay cây ốc quế giòn rụm"},
            {"word": "Ăn sầu riêng", "hint": "Tách múi sầu vàng óng thơm lừng béo ngậy nhai ngon lành"},
            {"word": "Ăn bún đậu mắm tôm", "hint": "Vắt quất đánh sủi bọt mắm tôm chấm miếng đậu mơ giòn tan"},
            {"word": "Uống trà sữa trân châu", "hint": "Cắm ống hút bự hút trân châu phồng má nhai dai dai"},
            {"word": "Ăn mì cay", "hint": "Nước mì đỏ au vừa ăn vừa hít hà lau nước mắt nước mũi"},
            {"word": "Rán trứng", "hint": "Đập trứng vào bát đánh tan đổ vào chảo dầu xèo xèo lật mặt"},
            {"word": "Ăn chè", "hint": "Múc từng muỗng chè thập cẩm đậu thạch cốt dừa mát rượi"},
            {"word": "Ăn cua", "hint": "Dùng kẹp bẻ càng cua gỡ từng miếng thịt thơm ngọt"},
            {"word": "Ăn bánh tráng trộn", "hint": "Dùng đũa trộn đều bò khô trứng cút xoài chua rồi gắp ăn"},
            {"word": "Ăn kẹo bông", "hint": "Cầm que kẹo mây to đùng cắn một miếng tan ngay trong miệng"},
            {"word": "Bổ dưa hấu", "hint": "Dùng dao to bổ đôi quả dưa lộ ruột đỏ cắt từng lát tam giác"},
            {"word": "Ăn cơm tấm sườn trứng", "hint": "Chan nước mắm tỏi ớt xắn miếng sườn nướng thơm phức"},
            {"word": "Uống nước mía ép", "hint": "Cho cây mía vào máy ép quay kẽo kẹt rót ra ly đầy đá"},
            {"word": "Gắp mì tôm đêm muộn", "hint": "Úp gói mì tôm xì xụp ăn trong đêm tĩnh mịch"},
            {"word": "Trộn gỏi tai heo", "hint": "Đeo bao tay bóp thấu tai heo giòn sần sật với rau thơm"}
        ]
    }

    vn_idioms_deck = {
        "id": "vn-idioms-proverbs",
        "name": "📜 Thành Ngữ & Tục Ngữ Dân Gian",
        "icon": "🎭",
        "color": "#8b5cf6",
        "description": "Diễn tả những câu thành ngữ, tục ngữ quen thuộc bằng cử chỉ hình thể độc đáo!",
        "words": [
            {"word": "Đàn gảy tai trâu", "hint": "Cầm đàn gảy say sưa cho con trâu đứng ngơ ngác nhai cỏ"},
            {"word": "Nước đổ lá khoai", "hint": "Cầm gáo nước dội lên chiếc lá, nước trôi tuột không đọng lại"},
            {"word": "Ếch ngồi đáy giếng", "hint": "Ngồi co ro dưới hố sâu ngước nhìn lên bầu trời bằng vung"},
            {"word": "Vắt chanh bỏ vỏ", "hint": "Vắt kiệt nước quả chanh rồi ném vỏ qua một bên"},
            {"word": "Cưỡi ngựa xem hoa", "hint": "Ngồi trên lưng ngựa phi nhanh chỉ kịp liếc nhìn hoa bên đường"},
            {"word": "Nước đến chân mới nhảy", "hint": "Nước ngập đến mắt cá chân mới hốt hoảng nhảy tưng tưng"},
            {"word": "Đẽo cày giữa đường", "hint": "Cầm rìu đẽo khúc gỗ, ai đi qua góp ý cũng nghe theo sửa lại"},
            {"word": "Ném đá giấu tay", "hint": "Cầm hòn đá ném thật mạnh rồi giấu vội hai tay ra sau lưng"},
            {"word": "Dã tràng xe cát", "hint": "Con còng nhỏ miệt mài vê từng viên cát bị sóng biển cuốn trôi"},
            {"word": "Há miệng chờ sung", "hint": "Nằm ngửa dưới gốc cây há hốc mồm đợi quả sung rụng vào"},
            {"word": "Chuột sa chĩnh gạo", "hint": "Con chuột rơi tọt vào chum gạo đầy ăn no nê sung sướng"},
            {"word": "Gậy ông đập lưng ông", "hint": "Cầm cây gậy vung lên bỗng trúng lưng mình đau điếng"},
            {"word": "Ăn cháo đá bát", "hint": "Húp xong bát cháo nóng rồi vung chân đá vỡ chiếc bát"},
            {"word": "Mò kim đáy bể", "hint": "Lặn xuống đáy biển mò mẫm tìm cây kim bé tí teo"},
            {"word": "Rút dây động rừng", "hint": "Kéo nhẹ một sợi dây khiến cả khu rừng rung chuyển ầm ầm"},
            {"word": "Múa rìu qua mắt thợ", "hint": "Cầm chiếc búa nhỏ múa may khoe khoang trước mặt bác thợ lành nghề"},
            {"word": "Nói như vẹt", "hint": "Lặp đi lặp lại lời nói người khác không hiểu ý nghĩa"},
            {"word": "Đầu voi đuôi chuột", "hint": "Vẽ con voi to tướng nhưng đuôi lại bé tí như đuôi chuột"},
            {"word": "Thả con săn sắt bắt con cá rô", "hint": "Thả con cá nhỏ xíu xuống nước để nhử câu con cá bự"},
            {"word": "Có công mài sắt có ngày nên kim", "hint": "Kiên trì mài thanh sắt to đùng thành chiếc kim khâu nhỏ xíu"},
            {"word": "Thùng rỗng kêu to", "hint": "Gõ vào chiếc thùng không có gì phát ra tiếng kêu vang rỗng tuếch"},
            {"word": "Giấu đầu hở đuôi", "hint": "Chui đầu vào bụi cây trốn nhưng cái đuôi lòi ra ngoài"},
            {"word": "Khẩu phật tâm xà", "hint": "Miệng niệm phật từ bi nhưng tay làm điệu rắn độc cắn trộm"},
            {"word": "Mèo mù vớ cá rán", "hint": "Mắt nhắm tịt quờ quạng bỗng tóm được đĩa cá rán thơm lừng"}
        ]
    }

    # Vietnamese Animals Deck (Expanded!)
    vn_animals_deck = {
        "id": "vn-animals-fun",
        "name": "🐾 Thế Giới Động Vật Vui Nhộn",
        "icon": "🐶",
        "color": "#10b981",
        "description": "Bắt chước tiếng kêu và điệu bộ các con vật quen thuộc cực hài hước!",
        "words": [
            {"word": "Con Chó Vẫy Đuôi", "hint": "Gâu gâu, thè lưỡi mừng rỡ vẫy đuôi rối rít"},
            {"word": "Con Mèo Rửa Mặt", "hint": "Meo meo, liếm bàn chân rồi xoa xoa lên má"},
            {"word": "Con Khỉ Gãi Đầu", "hint": "Khẹc khẹc, gãi nách nhảy tưng tưng thích ăn chuối"},
            {"word": "Con Ếch Nhảy Lò Cò", "hint": "Ộp ộp, ngồi xổm nhảy phốc thè lưỡi đớp muỗi"},
            {"word": "Con Voi Vẫy Tai", "hint": "Vung hai tay làm vòi dài hút nước phe phẩy tai to"},
            {"word": "Con Gà Trống Gáy", "hint": "Vỗ cánh phành phạch ngửa cổ ò ó o sáng sớm"},
            {"word": "Con Cá Mập Săn Mồi", "hint": "Đặt bàn tay lên đầu làm vây bơi lượn chomp chomp!"},
            {"word": "Con Chuột Túi Kangaroo", "hint": "Nhảy boing boing hai tay ôm túi trước bụng"},
            {"word": "Con Cọp (Hổ) Rình Mồi", "hint": "Chầm chậm bò rón rén rồi gầm to vồ mồi"},
            {"word": "Con Cua Bò Ngang", "hint": "Hai tay giơ lên làm càng kẹp kẹp đi ngang"},
            {"word": "Con Ngựa Phi Nước Đại", "hint": "Cộc cộc cộc, phi nước đại hí vang trời"},
            {"word": "Con Vịt Bơi Dưới Ao", "hint": "Cạp cạp! Lắc lắc mông bơi lạch bạch dưới ao"},
            {"word": "Chim Cánh Cụt Trên Băng", "hint": "Hai tay khép sát hông đi lạch bạch trượt bụng"},
            {"word": "Con Rùa Rụt Cổ", "hint": "Bò chậm chạp thấy nguy hiểm rụt đầu vào mai"},
            {"word": "Con Thỏ Nhảy Gặm Cà Rốt", "hint": "Hai ngón tay làm tai thỏ nhảy nhót nhai nhồm nhoàm"},
            {"word": "Con Heo Nằm Vũng Bùn", "hint": "Ụt ịt ụt ịt, béo tròn nằm lăn lộn phơi bụng"},
            {"word": "Con Sâu Đo Uốn Éo", "hint": "Co lưng lại rồi duỗi dài bò trên cành cây"},
            {"word": "Khủng Long Bạo Chúa T-Rex", "hint": "Hai tay co ngắn trước ngực dậm chân đùng đùng"},
            {"word": "Con Muỗi Vo Ve", "hint": "Vo ve bên tai tìm chỗ chích rồi bị đập bẹp"},
            {"word": "Con Bướm Vờn Hoa", "hint": "Đập cánh nhẹ nhàng bay lượn hút mật hoa"},
            {"word": "Con Bò Nhai Lại", "hint": "Moo! Mắt lờ đờ quay hàm nhai cỏ chậm chạp"},
            {"word": "Con Sói Hú Trăng", "hint": "Ngửa mặt lên trời tru dài ú uuu đêm rằm"},
            {"word": "Con Gấu Ngủ Đông", "hint": "Gãi lưng vào thân cây rồi nằm cuộn tròn ngáy khò khò"},
            {"word": "Con Chim Gõ Kiến", "hint": "Gật đầu liên hồi mổ mỏ cộc cộc vào thân cây"},
            {"word": "Con Dơi Treo Ngược", "hint": "Chắp tay móc chân treo ngược đầu xuống ngủ"},
            {"word": "Con Lừa Bướng Bỉnh", "hint": "I-a i-a! Ghì chân xuống đất kéo không chịu đi"},
            {"word": "Con Nhím Xù Lông", "hint": "Cuộn tròn người chìa gai nhọn hoắt ra ngoài"},
            {"word": "Con Đà Điểu Giấu Đầu", "hint": "Chạy chân dài rồi cắm đầu xuống đất trốn"},
            {"word": "Con Tinh Tinh Đập Ngực", "hint": "Đấm thùm thụp vào ngực hú to thị uy"},
            {"word": "Con Hà Mã Ngáp Dài", "hint": "Há hốc cái miệng to đùng ngâm mình dưới nước"}
        ]
    }

    # Vietnamese Silly Actions Deck (Expanded!)
    vn_silly_actions_deck = {
        "id": "vn-silly-actions",
        "name": "🤪 Hành Động Tinh Nghịch & Khó Đỡ",
        "icon": "🤸",
        "color": "#06b6d4",
        "description": "Các cử chỉ nghịch ngợm, bắt chước siêu bựa khiến cả phòng cười bò!",
        "words": [
            {"word": "Bị Kiến Lửa Cắn Gãi Ngứa", "hint": "Gãi lưng gãi nách nhảy tưng tưng xoa xoa chỗ đau"},
            {"word": "Thổi Nến Sinh Nhật Bị Tắt Hụt", "hint": "Lấy hơi phù phù 3 lần nến không chịu tắt"},
            {"word": "Ăn Ớt Hiểm Cay Xè", "hint": "Thè lưỡi quạt gió lia lịa, hít hà tìm cốc nước uống"},
            {"word": "Trượt Vỏ Chuối Ngã Bật Ngửa", "hint": "Chân đá văng lên trời ngã bẹp mông xuống sàn"},
            {"word": "Ngủ Gật Trong Lớp Học", "hint": "Đầu gục xuống giật mình tỉnh dậy chùi nước miếng"},
            {"word": "Đập Muỗi Hụt Trúng Mặt", "hint": "Vỗ hai tay cái bốp nhưng tự tát vào má mình"},
            {"word": "Uống Trà Sữa Bị Nghẹn Trân Châu", "hint": "Hút mạnh hạt trân châu bắn thẳng vào họng ho sặc sụa"},
            {"word": "Đi Cầu Khỉ Chênh Vênh", "hint": "Hai tay dang ngang giữ thăng bằng chân run bần bật"},
            {"word": "Mặc Áo Ngược Ra Đường", "hint": "Đang đi tự nhiên nhìn xuống cổ áo thấy mác lòi ra ngoài"},
            {"word": "Giẫm Phải Đinh Nhón Gót", "hint": "Mắt trợn ngược co một chân lên nhảy lò cò la oai oái"},
            {"word": "Bị Mẹ Cầm Chổi Rượt", "hint": "Vừa chạy vòng quanh bàn vừa giơ tay xin tha"},
            {"word": "Giả Vờ Ngất Xỉu Ăn Vạ", "hint": "Mắt đảo tròng từ từ đổ nghiêng người xuống đất"},
            {"word": "Cười Mót Quá Ôm Bụng", "hint": "Cười không ngậm được miệng hai chân kẹp chặt chạy vội"},
            {"word": "Quên Lời Bài Hát Khi Hát", "hint": "Cầm mic tự tin đến đoạn điệp khúc bỗng ú ớ lí nhí"},
            {"word": "Nặn Mụn Bị Bắn Lên Gương", "hint": "Bóp cái phụt giật mình nhìn vết bẩn trên gương"},
            {"word": "Chui Gầm Giường Tìm Dép", "hint": "Nằm bò soài tay quờ quạng dưới gầm giường bụi mù"},
            {"word": "Hít Drama Trên Mạng", "hint": "Mắt sáng rực bấm điện thoại ngóng hóng tin sốt dẻo"},
            {"word": "Giật Mình Vì Tiếng Sấm", "hint": "Đang điềm tĩnh bỗng giật bắn người ôm chầm người bên cạnh"},
            {"word": "Trốn Trả Tiền Chầu Nước", "hint": "Giả vờ nghe điện thoại bận rộn đi lùi ra cửa"},
            {"word": "Ngáp Dài Sái Quai Hàm", "hint": "Há họng to ngáp bỗng khớp kêu cục một cái không khép lại được"}
        ]
    }

    # --- 2. WEDDING DECK ---
    wedding_deck = {
        "id": "theme-wedding-celebration",
        "name": "💍 Wedding & Bridal Party",
        "icon": "👰",
        "color": "#f43f5e",
        "description": "Hilarious and unforgettable wedding moments, vows, and party games!",
        "words": [
            {"word": "Catching the Bouquet", "hint": "Bridesmaids jostling and jumping to catch the thrown flowers"},
            {"word": "Walking Down the Aisle", "hint": "Slow romantic walk towards the altar holding a flower bouquet"},
            {"word": "Cutting the Wedding Cake", "hint": "Couple holding knife together slicing the multi-tier cake"},
            {"word": "First Dance", "hint": "Romantic slow twirling dance with arms around each other"},
            {"word": "Giving a Wedding Toast", "hint": "Tapping champagne glass with a fork and giving an emotional speech"},
            {"word": "Exchanging Wedding Rings", "hint": "Nervously sliding the gold band onto the partner's finger"},
            {"word": "Runaway Bride", "hint": "Lifting wedding gown and sprinting away in high heels!"},
            {"word": "Bachelor Party Hangover", "hint": "Groomsmen wearing sunglasses nursing bad morning headaches"},
            {"word": "Catching the Garter", "hint": "Groom tossing the lace garter to the rowdy groomsmen"},
            {"word": "Crying Mother-of-the-Bride", "hint": "Dabbing tears with a handkerchief as daughter says 'I do'"},
            {"word": "Saying 'I Do'", "hint": "Nodding emotional promise at the altar: 'I do!'"},
            {"word": "Popping Champagne Bottle", "hint": "Popping the cork with a loud POP and fizz spraying everywhere"},
            {"word": "Flower Girl Dropping Petals", "hint": "Little girl tossing flower petals along the carpet walkway"},
            {"word": "Fixing the Long Wedding Train", "hint": "Maid of honor straightening the huge dress train on the floor"},
            {"word": "Wedding Cold Feet", "hint": "Pacing back and forth sweating bullets before opening church doors"},
            {"word": "Packing Honeymoon Suitcase", "hint": "Stuffing swimsuits, sunscreen, and passports into a rolling bag"},
            {"word": "Posing for 500 Photos", "hint": "Stiff aching cheeks from smiling for the wedding photographer"},
            {"word": "Clinking Glasses for a Kiss", "hint": "Guests clinking wine glasses demanding bride & groom kiss"},
            {"word": "Throwing Confetti / Rice", "hint": "Showering the newlyweds with paper confetti and birdseed"},
            {"word": "Best Man Losing the Rings", "hint": "Panicked patting of pockets searching for the wedding ring box"},
            {"word": "Bridal Makeup & Hair", "hint": "Spraying clouds of hairspray and applying waterproof mascara"},
            {"word": "Stealing Wedding Cake Frosting", "hint": "Smearing frosting on spouse's nose during cake tasting"},
            {"word": "Father Giving Away the Bride", "hint": "Proud emotional dad placing daughter's hand into the groom's"},
            {"word": "Cheesy Wedding DJ", "hint": "Spinning the YMCA, Cha Cha Slide, and shouting into the microphone"},
            {"word": "Dancing with the Mother-in-Law", "hint": "Careful polite ballroom twirl with mom-in-law"},
            {"word": "Wedding Photobooth Props", "hint": "Wearing oversized sunglasses, feather boa, and mustache on a stick"}
        ]
    }

    # --- 3. WESTERN HOLIDAYS DECKS ---
    all_holidays_deck = {
        "id": "western-holidays-mega",
        "name": "🌟 Western Popular Holidays",
        "icon": "🎉",
        "color": "#10b981",
        "description": "Best curated mix of Christmas, Halloween, Thanksgiving, Valentine's, and New Year's!",
        "words": [
            {"word": "Carving a Pumpkin", "hint": "Scooping seeds and cutting spooky face for Halloween"},
            {"word": "Decorating Christmas Tree", "hint": "Hanging shiny ornaments and stringing twinkle lights"},
            {"word": "Trick or Treating", "hint": "Knocking on doors holding candy bag: Trick or Treat!"},
            {"word": "Carving the Thanksgiving Turkey", "hint": "Slicing roast poultry at the big family dinner table"},
            {"word": "Cupid Shooting Love Arrows", "hint": "Flying baby aiming heart-tipped arrow at lovers"},
            {"word": "Midnight New Year's Countdown", "hint": "Counting 5-4-3-2-1 Happy New Year! Kissing and shouting"},
            {"word": "Santa Stuck in Chimney", "hint": "Red coat, big belly jammed halfway down the brick fireplace"},
            {"word": "Easter Egg Hunt", "hint": "Searching behind bushes with basket collecting painted eggs"},
            {"word": "Backyard 4th of July BBQ", "hint": "Grilling hot dogs and waving sparklers on summer evening"},
            {"word": "Kiss Under the Mistletoe", "hint": "Looking up at green berry sprig and leaning in for a kiss"},
            {"word": "Building a Snowman", "hint": "Rolling three giant snowballs, adding carrot nose and stick arms"},
            {"word": "Wrapping Christmas Presents", "hint": "Struggling with tape, colorful paper, and big red ribbon"},
            {"word": "Bobbing for Apples", "hint": "Hands behind back plunging face into bucket of water for floating fruit"},
            {"word": "Popping Party Poppers", "hint": "Pulling string for loud pop with streamers flying everywhere"},
            {"word": "Watching Holiday Fireworks", "hint": "Oohing and aahing at giant colorful explosions in sky"},
            {"word": "Breaking the Wishbone", "hint": "Two people pulling bone ends to see who gets the wish"},
            {"word": "Heart-Shaped Box of Chocolates", "hint": "Unwrapping ribbon and guessing which candy has caramel"},
            {"word": "Gingerbread House Making", "hint": "Icing walls together and sticking gumdrop candies on roof"},
            {"word": "Rudolph's Shiny Red Nose", "hint": "Glowing beacon guiding Santa's sleigh through the blizzard"},
            {"word": "Spooky Haunted House", "hint": "Creeping through dark hallway jumping at fake spider webs"}
        ]
    }

    # Christmas Deck
    xmas_words = [
        {"word": "Santa Claus", "hint": "Ho ho ho! Big red suit, beard, delivering gifts down chimney"},
        {"word": "Christmas Tree", "hint": "Decorating pine tree with lights, garland, and topper star"},
        {"word": "Rudolph the Red-Nosed Reindeer", "hint": "Nose glows bright red to lead the flying sleigh"},
        {"word": "Frosty the Snowman", "hint": "Magic old silk hat brought him to life dancing around"},
        {"word": "Mistletoe", "hint": "Hanging green plant: tradition says you must kiss under it"},
        {"word": "Gingerbread House", "hint": "Walls made of cookie dough glued with sugar icing"},
        {"word": "Stocking by Fireplace", "hint": "Hanging big red socks filled with small gifts and candy"},
        {"word": "Snowball Fight", "hint": "Packing snow tight and hurling it at friends while ducking"},
        {"word": "Santa's Elves", "hint": "Pointy ears, green clothes, hammering wooden toys in North Pole workshop"},
        {"word": "Candy Cane", "hint": "Red and white peppermint hook sweet treat"},
        {"word": "Opening Gifts on Christmas Morning", "hint": "Ripping wrapping paper off boxes in excitement"},
        {"word": "The Grinch", "hint": "Green mean creature stealing all of Whoville's presents"},
        {"word": "Sleigh Ride", "hint": "Jingle bells ringing while gliding across snowy hills"},
        {"word": "Chimney", "hint": "Brick tunnel Santa slides down to get into living room"},
        {"word": "Jingle Bells", "hint": "Dashing through the snow in a one-horse open sleigh"},
        {"word": "Hot Chocolate with Marshmallows", "hint": "Sipping warm cocoa with fluffy white marshmallows"}
    ]
    if christmas_data and "words" in christmas_data:
        extra_xmas = [w for w in christmas_data["words"] if w["word"] not in [x["word"] for x in xmas_words]]
        xmas_words.extend(extra_xmas[:25])

    christmas_deck = {
        "id": "holiday-christmas",
        "name": "🎄 Christmas & Giáng Sinh",
        "icon": "🎅",
        "color": "#dc2626",
        "description": "Santa, snowmen, holiday traditions, and jingle bells!",
        "words": xmas_words
    }

    # Halloween Deck
    halloween_words = [
        {"word": "Jack-o'-Lantern", "hint": "Carved glowing pumpkin with candle inside on the porch"},
        {"word": "Trick-or-Treating", "hint": "Going house to house in costume collecting bucket of candy"},
        {"word": "Vampire Dracula", "hint": "Fangs, black cape, turns into a bat, allergic to garlic"},
        {"word": "Witch Flying on Broomstick", "hint": "Pointy black hat, cackling laugh, stirring cauldron brew"},
        {"word": "Haunted House", "hint": "Creaky floorboards, ghost sounds, spider webs on doors"},
        {"word": "Mummy Wrapped in Bandages", "hint": "Walking with stiff outstretched arms wrapped in white cloth"},
        {"word": "Zombie Walk", "hint": "Limping slowly, groaning 'Braaains!' with arms forward"},
        {"word": "Black Cat", "hint": "Arched back, hissing, superstition bad luck crossing path"},
        {"word": "Werewolf Howling at Full Moon", "hint": "Growling, sprouting fur, howling at nighttime sky"},
        {"word": "Frankenstein's Monster", "hint": "Bolts in neck, flat head, stomping heavy boots"},
        {"word": "Bobbing for Apples", "hint": "Dipping face in bucket trying to bite floating red fruit"},
        {"word": "Scary Ghost", "hint": "White sheet floating shouting 'BOO!' in attic"},
        {"word": "Spooky Skeleton", "hint": "Clicking rattling bones dancing under moonlight"},
        {"word": "Candy Corn", "hint": "Yellow, orange, and white striped Halloween sweet"}
    ]
    if halloween_data and "words" in halloween_data:
        extra_hallow = [w for w in halloween_data["words"] if w["word"] not in [x["word"] for x in halloween_words]]
        halloween_words.extend(extra_hallow[:25])

    halloween_deck = {
        "id": "holiday-halloween",
        "name": "🎃 Halloween & Đêm Hội Ma",
        "icon": "👻",
        "color": "#ea580c",
        "description": "Spooky costumes, monsters, pumpkins, and haunted antics!",
        "words": halloween_words
    }

    # Thanksgiving Deck
    thanksgiving_words = [
        {"word": "Roast Turkey", "hint": "Golden brown bird carved with large fork and knife"},
        {"word": "Pumpkin Pie with Whipped Cream", "hint": "Classic orange spiced pie with dollop of white cream"},
        {"word": "Mashed Potatoes and Gravy", "hint": "Scooping creamy potatoes and pouring brown sauce over it"},
        {"word": "Breaking the Wishbone", "hint": "Pulling ends of the Y-bone for good luck"},
        {"word": "Thanksgiving Day Parade", "hint": "Giant cartoon balloons floating through New York streets"},
        {"word": "Food Coma on the Couch", "hint": "Unbuttoning pants and falling asleep after eating too much"},
        {"word": "Cranberry Sauce", "hint": "Tart red jellied condiment served alongside turkey"},
        {"word": "Stuffing", "hint": "Herbed bread crumbs seasoned inside the turkey"},
        {"word": "Watching Football on Thanksgiving", "hint": "Cheering on the couch with a plate full of turkey"}
    ]
    if thanksgiving_data and "words" in thanksgiving_data:
        extra_tg = [w for w in thanksgiving_data["words"] if w["word"] not in [x["word"] for x in thanksgiving_words]]
        thanksgiving_words.extend(extra_tg[:20])

    thanksgiving_deck = {
        "id": "holiday-thanksgiving",
        "name": "🦃 Thanksgiving & Lễ Tạ Ơn",
        "icon": "🍂",
        "color": "#b45309",
        "description": "Feasts, football, family gratitude, and pumpkin pies!",
        "words": thanksgiving_words
    }

    # Valentine Deck
    valentine_words = [
        {"word": "Cupid's Bow and Arrow", "hint": "Wings flapping, drawing heart arrow aimed at someone's chest"},
        {"word": "Box of Heart Chocolates", "hint": "Unwrapping big red velvet heart box filled with sweets"},
        {"word": "Bouquet of Red Roses", "hint": "Sniffing sweet flowers and getting pricked by a thorn"},
        {"word": "Romantic Candlelight Dinner", "hint": "Clinking wine glasses over soft flicker of tabletop candles"},
        {"word": "Giant Teddy Bear Gift", "hint": "Carrying huge stuffed animal that's bigger than you"},
        {"word": "Secret Admirer Love Letter", "hint": "Sealing pink envelope with a kiss and dropping in mailbox"},
        {"word": "Proposing on One Knee", "hint": "Dropping to one knee and opening shiny velvet ring box"},
        {"word": "Heart Eyes Emoji", "hint": "Hands over cheeks swooning in love"},
        {"word": "Serenading with Acoustic Guitar", "hint": "Singing romantic love ballad under balcony window"}
    ]
    if valentine_data and "words" in valentine_data:
        extra_val = [w for w in valentine_data["words"] if w["word"] not in [x["word"] for x in valentine_words]]
        valentine_words.extend(extra_val[:20])

    valentine_deck = {
        "id": "holiday-valentine",
        "name": "💖 Valentine's Day & Lễ Tình Nhân",
        "icon": "💌",
        "color": "#e11d48",
        "description": "Cupid, romance, chocolate boxes, and secret admirers!",
        "words": valentine_words
    }

    # New Year's Deck
    newyear_words = [
        {"word": "Times Square Ball Drop", "hint": "Giant glittering crystal ball descending at midnight"},
        {"word": "Popping Champagne at Midnight", "hint": "Loud cork pop and filling flutes as clock hits 12:00"},
        {"word": "New Year's Resolution", "hint": "Writing down gym goals you will probably give up in February"},
        {"word": "Blowing Party Noise Makers", "hint": "Paper horn unraveling with funny squeaky noise"},
        {"word": "Midnight Kiss", "hint": "Grabbing party companion for romantic embrace as clock strikes 12"},
        {"word": "Sparklers in the Dark", "hint": "Spinning glittering firework stick writing 2026 in the air"},
        {"word": "Singing Auld Lang Syne", "hint": "Swaying arm in arm singing the classic end-of-year tune"}
    ]
    if newyear_data and "words" in newyear_data:
        extra_ny = [w for w in newyear_data["words"] if w["word"] not in [x["word"] for x in newyear_words]]
        newyear_words.extend(extra_ny[:20])

    newyear_deck = {
        "id": "holiday-newyear",
        "name": "🥂 New Year's Eve & Đêm Giao Thừa",
        "icon": "🎆",
        "color": "#6366f1",
        "description": "Midnight countdown, resolutions, noise makers, and celebration!",
        "words": newyear_words
    }

    # 4th of July Deck
    july4_words = [
        {"word": "Fireworks Finale", "hint": "Rapid colorful explosions illuminating the night sky"},
        {"word": "Waving the American Flag", "hint": "Holding flagpole proudly marching in hometown parade"},
        {"word": "Grilling Burgers & Hot Dogs", "hint": "Flipping patties with spatula over smoky charcoal grill"},
        {"word": "Watermelon Eating Contest", "hint": "Hands behind back biting fast into red fruit slice spitting seeds"},
        {"word": "Summer Pool Party Cannonball", "hint": "Running and tucking knees for huge splash into water"},
        {"word": "Chasing the Ice Cream Truck", "hint": "Running down sidewalk waving dollars to catch the musical truck"}
    ]
    if july4_data and "words" in july4_data:
        extra_j4 = [w for w in july4_data["words"] if w["word"] not in [x["word"] for x in july4_words]]
        july4_words.extend(extra_j4[:25])

    july4_deck = {
        "id": "holiday-july4",
        "name": "🎆 4th of July & Summer Fest",
        "icon": "🎇",
        "color": "#2563eb",
        "description": "Sparklers, backyard BBQ grills, parades, and fireworks!",
        "words": july4_words
    }

    # Easter & Spring Deck
    easter_words = [
        {"word": "Easter Bunny Hopping", "hint": "Hands as bunny ears hopping around hiding eggs"},
        {"word": "Dyeing Colorful Easter Eggs", "hint": "Dipping boiled eggs into cups of pink, blue, and green dye"},
        {"word": "Chocolate Bunny with Ears", "hint": "Biting off the chocolate rabbit's ears first"},
        {"word": "Easter Egg Hunt in the Garden", "hint": "Peeking under bushes filling woven basket with plastic eggs"},
        {"word": "Spring Flowers Blooming", "hint": "Tulips and cherry blossoms opening under bright sun"},
        {"word": "Catching Butterflies with Net", "hint": "Creeping up quietly and swiping net over colorful insect"}
    ]
    if easter_data and "words" in easter_data:
        extra_east = [w for w in easter_data["words"] if w["word"] not in [x["word"] for x in easter_words]]
        easter_words.extend(extra_east[:20])

    easter_deck = {
        "id": "holiday-easter",
        "name": "🐰 Easter & Spring Blooms",
        "icon": "🌸",
        "color": "#14b8a6",
        "description": "Egg hunts, chocolate bunnies, pastel colors, and spring fun!",
        "words": easter_words
    }

    # --- 4. THE GAME GAL FEATURE DECKS ---
    actions_words = actions_data["words"] if actions_data else [
        {"word": "putting on sunscreen", "hint": "Rubbing white lotion on nose and shoulders"},
        {"word": "watching a sad movie", "hint": "Dabbing tears with tissue watching screen"},
        {"word": "waiting at doctor's office", "hint": "Flipping through old magazine tapping foot nervously"},
        {"word": "ordering food at drive-thru", "hint": "Leaning out driver window shouting order into speaker"}
    ]

    gamegal_actions_deck = {
        "id": "gamegal-actions",
        "name": "🤸 Charades Actions & Situations",
        "icon": "🎭",
        "color": "#10b981",
        "description": f"Over {len(actions_words)} hilarious real-world actions straight from The Game Gal!",
        "words": actions_words
    }

    # Game Gal Wild Animals Deck
    gamegal_animals_words = []
    if animals_data and "words" in animals_data:
        gamegal_animals_words = animals_data["words"][:65]
    else:
        gamegal_animals_words = [
            {"word": "lemur", "hint": "Striped ring-tail jumping around"},
            {"word": "kangaroo", "hint": "Hopping with joey in pouch"},
            {"word": "tiger", "hint": "Striped predator stalking silent"},
            {"word": "elephant", "hint": "Swinging long trunk and trumpeting"}
        ]

    gamegal_animals_deck = {
        "id": "gamegal-animals-wild",
        "name": "🦁 Wildlife & Safari Animals",
        "icon": "🦒",
        "color": "#f59e0b",
        "description": f"Over {len(gamegal_animals_words)} animals from The Game Gal!",
        "words": gamegal_animals_words
    }

    disney_words = disney_data["words"] if disney_data else [
        {"word": "The Lion King", "hint": "Holding baby cub Simba high over Pride Rock"},
        {"word": "Frozen", "hint": "Elsa singing Let It Go building ice castle"},
        {"word": "Toy Story", "hint": "Woody and Buzz Lightyear flying to infinity and beyond"},
        {"word": "Finding Nemo", "hint": "Little clownfish with lucky fin lost in giant ocean"}
    ]

    gamegal_disney_deck = {
        "id": "gamegal-disney-movies",
        "name": "🍿 Disney & Animated Movies",
        "icon": "🏰",
        "color": "#3b82f6",
        "description": f"Over {len(disney_words)} beloved animated blockbusters from The Game Gal!",
        "words": disney_words
    }

    idioms_words = idioms_data["words"] if idioms_data else [
        {"word": "piece of cake", "hint": "Something super easy to do"},
        {"word": "bite the bullet", "hint": "Facing tough situation bravely"},
        {"word": "break a leg", "hint": "Wishing theatrical good luck before going on stage"},
        {"word": "spill the beans", "hint": "Accidentally revealing the big secret"}
    ]

    gamegal_idioms_deck = {
        "id": "gamegal-idioms",
        "name": "💡 English Idioms & Sayings",
        "icon": "💬",
        "color": "#8b5cf6",
        "description": f"Classic English figures of speech and famous expressions to act out!",
        "words": idioms_words
    }

    # --- 5. EXPANDED KIDS DECKS ---
    kids_animals_expanded = [
        {"word": "Lion", "hint": "Roar! King of the jungle shaking big mane"},
        {"word": "Penguin", "hint": "Waddle waddle on ice floes, sliding on belly"},
        {"word": "Monkey", "hint": "Ooh ooh aah aah, scratching head, peeling banana"},
        {"word": "Frog", "hint": "Ribbit! Squatting down and jumping with tongue zap"},
        {"word": "Kangaroo", "hint": "Boing! Hopping with baby joey in belly pouch"},
        {"word": "Elephant", "hint": "Swinging long trunk and flapping giant ears"},
        {"word": "Snake", "hint": "Slithering on floor, flicking forked tongue sss"},
        {"word": "Chicken", "hint": "Bawk bawk! Flapping elbow wings and laying an egg"},
        {"word": "Dog", "hint": "Panting, wagging tail, chasing own tail woof!"},
        {"word": "Cat", "hint": "Meow! Licking paws, arching back, coughing hairball"},
        {"word": "Dolphin", "hint": "Clicking sounds, leaping in high arc over ocean"},
        {"word": "T-Rex Dinosaur", "hint": "Tiny arms, stomping heavy feet, giant roar!"},
        {"word": "Butterfly", "hint": "Flapping delicate colorful wings from flower to flower"},
        {"word": "Giraffe", "hint": "Super tall stretched neck reaching high leaves"},
        {"word": "Bunny Rabbit", "hint": "Twitching nose and hopping quickly, munching carrot"},
        {"word": "Sleeping Bear", "hint": "Hibernating curled in cave snoring loudly"},
        {"word": "Duck", "hint": "Quack quack! Swimming in pond with tail wiggling"},
        {"word": "Cow", "hint": "Moo! Chewing grass with big slow jaw"},
        {"word": "Horse", "hint": "Galloping clip-clop, whinnying and kicking back legs"},
        {"word": "Shark", "hint": "Fin slicing water, snapping giant jaws chomp!"},
        {"word": "Owl", "hint": "Twisting head all the way around, hoo hoo!"},
        {"word": "Gorilla", "hint": "Beating chest with both fists roaring"},
        {"word": "Crab", "hint": "Scuttling sideways with pinchers snipping snip!"},
        {"word": "Cheetah", "hint": "Sprinting at lightning speed across savanna"},
        {"word": "Flamingo", "hint": "Standing gracefully balanced on one thin leg"},
        {"word": "Seal", "hint": "Clapping flippers together barking arf arf!"},
        {"word": "Hippopotamus", "hint": "Opening giant yawning mouth in muddy water"},
        {"word": "Wolf", "hint": "Prowling in pack and howling long owoooo at moon"},
        {"word": "Zebra", "hint": "Black and white stripes running and kicking"},
        {"word": "Chameleon", "hint": "Eyes rotating separately, shooting lightning-fast tongue"},
        {"word": "Sloth", "hint": "Moving in hilarious ultra-slow motion hanging from branch"},
        {"word": "Koala", "hint": "Hugging tree trunk chewing sleepy eucalyptus"},
        {"word": "Meerkat", "hint": "Standing tall on tiptoes looking sharply left and right"},
        {"word": "Bat", "hint": "Sleeping upside down wrapped in dark wings"},
        {"word": "Panda", "hint": "Rolling over on back crunching green bamboo shoot"},
        {"word": "Peacock", "hint": "Shaking and fanning out dazzling tail feathers"},
        {"word": "Beaver", "hint": "Slapping flat tail on water and chomping tree bark"},
        {"word": "Skunk", "hint": "Backing up, lifting tail to spray stinky cloud phew!"},
        {"word": "Ostrich", "hint": "Burying head in sand then sprinting super fast"},
        {"word": "Alligator", "hint": "Floating still like a log then snapping massive jaws"},
        {"word": "Walrus", "hint": "Scratching belly with giant tusks on ice floe"},
        {"word": "Mosquito", "hint": "High-pitched buzz near someone's ear then biting"},
        {"word": "Goat", "hint": "Lowering horns to headbutt and eating cardboard"},
        {"word": "Pig", "hint": "Rolling in messy mud snorting oink oink"},
        {"word": "Squirrel", "hint": "Stuffing acorns into puffed cheeks and scampering up tree"},
        {"word": "Camel", "hint": "Two humps swaying slowly across hot desert dunes"},
        {"word": "Rhinoceros", "hint": "Lowering sharp nasal horn and charging forward"},
        {"word": "Octopus", "hint": "Eight wavy tentacles gliding and squirting ink"},
        {"word": "Woodpecker", "hint": "Rapidly hammering beak against tree trunk rat-a-tat!"},
        {"word": "Turkey", "hint": "Puffing feathers, bobbing red wattle gobble gobble!"},
        {"word": "Sheep", "hint": "Fluffy white wool jumping fence baa baa!"},
        {"word": "Blue Whale", "hint": "Giant swimming, spouting huge water fountain from blowhole"},
        {"word": "Jellyfish", "hint": "Pulsing translucent dome with dangling stingers"},
        {"word": "Hedgehog", "hint": "Curling into a prickly spiky tight ball"},
        {"word": "Parrot", "hint": "Perching on pirate shoulder squawking Polly wants cracker!"},
        {"word": "Mouse", "hint": "Sneaking tiny footsteps, nibbling cheese, squeak!"},
        {"word": "Hamster", "hint": "Running furiously on squeaky spinning wheel"},
        {"word": "Lobster", "hint": "Snapping heavy claws walking backwards on sea floor"},
        {"word": "Polar Bear", "hint": "Shivering in Arctic snow sniffing hole in ice"},
        {"word": "Caterpillar", "hint": "Inching forward scrunched up, preparing for cocoon"},
        {"word": "Swan", "hint": "Curving elegant S-neck gliding across serene lake"}
    ]

    kids_actions_expanded = [
        {"word": "Brushing Teeth", "hint": "Squeeze paste, scrub scrub, spit and rinse"},
        {"word": "Eating Spicy Noodles", "hint": "Slurping hot noodles, fanning red face and panting"},
        {"word": "Riding a Rollercoaster", "hint": "Gripping lap bar, thrown sideways screaming in terror"},
        {"word": "Walking a Giant Dog", "hint": "Leash yanked forward struggling to keep balance"},
        {"word": "Swimming in Freezing Water", "hint": "Shivering teeth chattering brrr splashing arms"},
        {"word": "Baking a Messy Cake", "hint": "Stirring batter, flour flying, licking sweet spoon"},
        {"word": "Tying Shoelaces in a Knot", "hint": "Making bunny ears and ending with impossible knot"},
        {"word": "Loud Snoring & Waking Up", "hint": "Deep vibrating snore, suddenly choking awake startled"},
        {"word": "Kicking Winning Soccer Goal", "hint": "Running up, power kick, slide on knees celebrating GOAL!"},
        {"word": "Blowing Birthday Candles", "hint": "Making wish, taking massive deep breath and puffing!"},
        {"word": "Robot Dance", "hint": "Stiff 90-degree robotic clicks and motor buzzes"},
        {"word": "Climbing a Tall Tree", "hint": "Reaching branch by branch, looking down getting scared"},
        {"word": "Flying an Airplane in Turbulence", "hint": "Wings tilted, shaking steering wheel bouncing around"},
        {"word": "Melting Ice Cream Cone", "hint": "Licking dripping sides frantically before it drops"},
        {"word": "Reeling in a Huge Fish", "hint": "Rod bent double, reeling hard, falling backwards"},
        {"word": "Playing Rock Drums", "hint": "Kicking bass pedal, smashing cymbals crash crash!"},
        {"word": "Jumping on a Trampoline", "hint": "Higher and higher bounces with mid-air flips"},
        {"word": "Looking Through Binoculars", "hint": "Hands over eyes adjusting dial pointing at bird"},
        {"word": "Washing a Dirty Car", "hint": "Soaping sponge, scrubbing hood, hose spraying water"},
        {"word": "Ice Skating Wobble", "hint": "Gliding smoothly then ankles giving out flailing arms"},
        {"word": "Slipping on a Banana Peel", "hint": "Foot shoots out, arms windmill, landing flat on butt!"},
        {"word": "Stepping on a Lego Brick", "hint": "Silent scream of agony, hopping on one foot clutching toes"},
        {"word": "Sneezing 5 Times in a Row", "hint": "Big buildup... achoo! achoo! achoo! sniffing"},
        {"word": "Moonwalking Like Michael Jackson", "hint": "Sliding feet backward smoothly, tipping fedora hat"},
        {"word": "Eating a Super Sour Lemon", "hint": "Biting in, face shrivels up, eyes squeezed tight"},
        {"word": "Brain Freeze from Ice Slushie", "hint": "Drinking fast through straw, clutching temples shivering"},
        {"word": "Walking Against 100mph Hurricane Wind", "hint": "Leaning at 45 degree angle pushing against invisible blast"},
        {"word": "Hula Hooping Nonstop", "hint": "Swiveling hips faster and faster to keep hoop spinning"},
        {"word": "Falling Asleep Standing Up", "hint": "Head nods slowly, knees buckle, jerk awake startled"},
        {"word": "Balancing a Spoon on Your Nose", "hint": "Tilting head back with crossed eyes breathing carefully"},
        {"word": "Shoe Stuck in Chewing Gum", "hint": "Lifting foot, sticky gum stretching a mile high"},
        {"word": "Juggling 3 Invisible Balls", "hint": "Throwing objects in circles, dropping them frantically"},
        {"word": "Walking on Burning Hot Beach Sand", "hint": "Ouch ouch ouch tiptoe running to ocean water"},
        {"word": "Catching a Fly with Chopsticks", "hint": "Staring intensely, snapping wooden chopsticks in air"},
        {"word": "Spilling Hot Soup on Your Lap", "hint": "Jumping out of chair waving hands fanning pants"},
        {"word": "Singing with Shampoo Bottle Microphone", "hint": "Rocking out in the shower lathering hair"},
        {"word": "Air Guitar Solo at Concert", "hint": "Headbanging wildly, shredding imaginary guitar strings"},
        {"word": "Opening an Impossible Pickle Jar", "hint": "Turning bright red straining, banging bottom on counter"},
        {"word": "Threading a Tiny Needle", "hint": "Squinting with one eye, licking thread, missing hole"},
        {"word": "Midnight Fridge Raiding Sneak", "hint": "Tiptoeing past creaky floorboards grabbing snack"},
        {"word": "Popping a Giant Bubblegum Bubble", "hint": "Blowing huge pink bubble until POP! stuck all over face"},
        {"word": "Dodging Red Laser Beams like a Spy", "hint": "Limbo underneath, cartwheel over, sliding across floor"},
        {"word": "Tangled in Sticky Packing Tape", "hint": "Trying to peel tape off finger, gets stuck to other hand"},
        {"word": "Trying to Fold a Fitted Sheet", "hint": "Tucking random corners, giving up and rolling into a ball"},
        {"word": "Waving at a Stranger by Mistake", "hint": "Enthusiastic wave, realizing mistake, pretending to scratch hair"},
        {"word": "Searching for Glasses on Your Head", "hint": "Checking pockets in panic while glasses are on forehead"},
        {"word": "Licking Your Own Elbow", "hint": "Twisting arm and craning neck trying the impossible"},
        {"word": "Getting Chased by a Swarm of Bees", "hint": "Swatting arms in circles, ducking and sprinting"},
        {"word": "Putting in Contact Lenses", "hint": "Holding eyelid open with fingers poking eyeball"},
        {"word": "Awkward Handshake into Fist Bump", "hint": "They offer hand, you offer fist, turning into weird grab"},
        {"word": "Balancing a Book on Your Head", "hint": "Walking with stiff neck trying not to let heavy book fall"},
        {"word": "Pumping Up a Flat Bike Tire", "hint": "Frantically pumping t-bar handle sweating hard"},
        {"word": "Pretending to Be a Ventriloquist Dummy", "hint": "Mouth opening and shutting with wooden jerky head moves"},
        {"word": "Tug of War Mud Pull", "hint": "Leaning completely back pulling rope with all your might"},
        {"word": "Spinning Around in an Office Chair", "hint": "Spinning 20 times then trying to walk straight and stumbling"},
        {"word": "Trying on Way Too Small Jeans", "hint": "Hopping on one foot sucking in gut trying to pull zipper"},
        {"word": "Drinking Through 5 Connected Straws", "hint": "Sucking with giant puffed cheeks waiting for soda to rise"},
        {"word": "Playing Tug of War with a Puppy", "hint": "Holding toy sock while puppy growls and shakes head"},
        {"word": "Pretending to Walk Down Fake Stairs", "hint": "Sinking behind couch inch by inch like descending staircase"},
        {"word": "Petting an Angry Hedgehog", "hint": "Slowly reaching out hand, getting pricked ouch!"}
    ]

    # --- 6. ASSEMBLE ALL DECKS ---
    compiled_decks = {
        "vietnam": [
            vn_holidays_deck,
            vn_daily_actions_deck,
            vn_food_deck,
            vn_idioms_deck,
            vn_animals_deck,
            vn_silly_actions_deck
        ],
        "wedding": [
            wedding_deck
        ],
        "holidays": [
            all_holidays_deck,
            christmas_deck,
            halloween_deck,
            thanksgiving_deck,
            valentine_deck,
            newyear_deck,
            july4_deck,
            easter_deck
        ],
        "gamegal": [
            gamegal_actions_deck,
            gamegal_animals_deck,
            gamegal_disney_deck,
            gamegal_idioms_deck
        ]
    }

    # Generate new decks.js content
    js_code = """// Auto-generated by scripts/sync_decks.py
// Full word decks catalog supporting Vietnamese, Wedding, Western Holidays, The Game Gal, Millennials, and Kids!

export const DECKS = {
  // 🇻🇳 VIỆT NAM DECKS
  vietnam: """ + json.dumps(compiled_decks["vietnam"], ensure_ascii=False, indent=4) + """,

  // 💍 WEDDING & PARTY DECKS
  wedding: """ + json.dumps(compiled_decks["wedding"], ensure_ascii=False, indent=4) + """,

  // 🎄 WESTERN HOLIDAYS & SEASONS
  holidays: """ + json.dumps(compiled_decks["holidays"], ensure_ascii=False, indent=4) + """,

  // 🎭 THE GAME GAL WORD GENERATOR THEMES
  gamegal: """ + json.dumps(compiled_decks["gamegal"], ensure_ascii=False, indent=4) + """,

  // 🧒 KIDS UNDER 10
  kids: [
    {
      id: "kids-animals",
      name: "Zoo & Animals",
      icon: "🦁",
      color: "#f59e0b",
      description: "Act out or sound like these fun animals! (""" + str(len(kids_animals_expanded)) + """ words)",
      words: """ + json.dumps(kids_animals_expanded, ensure_ascii=False, indent=8) + """
    },
    {
      id: "kids-actions",
      name: "Silly Actions",
      icon: "🤸",
      color: "#10b981",
      description: "Hilarious physical actions and funny fails to act out! (""" + str(len(kids_actions_expanded)) + """ words)",
      words: """ + json.dumps(kids_actions_expanded, ensure_ascii=False, indent=8) + """
    },
    {
      id: "kids-cartoons",
      name: "Disney & Cartoons",
      icon: "🎬",
      color: "#3b82f6",
      description: "Favorite animated characters and heroes!",
      words: [
        { word: "Elsa", hint: "Frozen: Let It Go!" },
        { word: "Mickey Mouse", hint: "Big round ears & red shorts" },
        { word: "SpongeBob", hint: "Lives in a pineapple under the sea" },
        { word: "Pikachu", hint: "Pika Pika! Electric yellow mouse" },
        { word: "Buzz Lightyear", hint: "To infinity and beyond!" },
        { word: "Spider-Man", hint: "Shooting webs from wrists" },
        { word: "Olaf", hint: "Snowman who loves warm hugs" },
        { word: "Peppa Pig", hint: "Jumping in muddy puddles" },
        { word: "Simba", hint: "Lion cub from Pride Rock" },
        { word: "Minion", hint: "Yellow with goggles: Banana!" },
        { word: "Sonic the Hedgehog", hint: "Super fast blue speedster" },
        { word: "Shrek", hint: "Big green ogre in a swamp" },
        { word: "Nemo", hint: "Little clownfish with lucky fin" },
        { word: "Winnie the Pooh", hint: "Loves eating golden honey" },
        { word: "Batman", hint: "Dark Knight with bat cape" },
        { word: "Woody", hint: "Cowboy with pull-string" },
        { word: "Mario", hint: "Mustache plumber jumping on mushrooms" },
        { word: "Moana", hint: "Sailing across the ocean" },
        { word: "The Hulk", hint: "Hulk smash! Turning green" },
        { word: "Iron Man", hint: "Flying in high-tech metal suit" }
      ]
    },
    {
      id: "kids-food",
      name: "Yummy Treats & Food",
      icon: "🍕",
      color: "#ec4899",
      description: "Delicious foods everyone loves!",
      words: [
        { word: "Cheesy Pizza", hint: "Pulling gooey cheese slice" },
        { word: "Popcorn", hint: "Popping in microwave, eating at movies" },
        { word: "Messy Spaghetti", hint: "Slurping long sauce noodles" },
        { word: "Ice Cream Cone", hint: "Double scoop with sprinkles" },
        { word: "Watermelon", hint: "Spitting out black seeds" },
        { word: "Cotton Candy", hint: "Fluffy pink sugary cloud" },
        { word: "Peeled Banana", hint: "Peeling down the yellow skin" },
        { word: "Hot Dog", hint: "Ketchup and mustard in a bun" },
        { word: "Crispy French Fries", hint: "Dipping in red ketchup" },
        { word: "Birthday Cake", hint: "Slicing sweet frosted cake" },
        { word: "Glazed Donut", hint: "Round pastry with a hole" },
        { word: "Crunchy Taco", hint: "Tilting head sideways to bite" },
        { word: "Chocolate Bar", hint: "Breaking off a tasty square" },
        { word: "Pancakes with Syrup", hint: "Stack dripping with maple syrup" },
        { word: "Lollipop", hint: "Swirly sweet on a stick" },
        { word: "Crispy Bacon", hint: "Sizzling in the frying pan" },
        { word: "Juicy Burger", hint: "Two hands holding big bite" },
        { word: "Cupcake", hint: "Licking frosting off top" },
        { word: "Strawberries", hint: "Dipping in sweet cream" },
        { word: "Boba Bubble Tea", hint: "Chewing tapioca pearls with fat straw" }
      ]
    }
  ],

  // 🥑 MILLENNIAL ADULTS
  adults: [
    {
      id: "millennial-nostalgia",
      name: "90s & 2000s Nostalgia",
      icon: "📼",
      color: "#8b5cf6",
      description: "Artifacts and rituals of our youth!",
      words: [
        { word: "Dial-up Internet", hint: "Screeching modem connecting sound" },
        { word: "Tamagotchi Dying", hint: "Forgot to feed virtual pet in pocket" },
        { word: "Rewinding a VHS Tape", hint: "Be kind, rewind before returning" },
        { word: "LimeWire Download", hint: "Song title.mp3 took 3 hours (got a virus)" },
        { word: "MySpace Top 8", hint: "Ranking best friends drama" },
        { word: "Blockbuster Late Fee", hint: "Forgot to return DVD on Friday night" },
        { word: "Nokia 3310 Snake", hint: "Indestructible phone, record score" },
        { word: "Walkman Skipping", hint: "Jogging made the CD player skip" },
        { word: "AIM Away Message", hint: "Cryptic emo lyrics: ~*away*~" },
        { word: "Scholastic Book Fair", hint: "Lamborghini posters & spy pens" },
        { word: "Furby Waking Up", hint: "Talking at 3 AM from closet" },
        { word: "T9 Texting", hint: "Pressing 4-4-3-3-5-5-5-5-6-6-6 blindly" },
        { word: "Capri Sun Pouch", hint: "Straw stabbed all the way through the back" },
        { word: "Heelys Shoes", hint: "Rolling through the shopping mall" },
        { word: "Blowing Nintendo Cartridge", hint: "Fixing gray cartridge with a blow" },
        { word: "Burning a Mix CD", hint: "Sharpie labels for high school crush" },
        { word: "Game Boy Under Covers", hint: "Playing with worm light past bedtime" },
        { word: "Slap Bracelets", hint: "Slapping metal bands on wrists" },
        { word: "Gel Pens Collection", hint: "Sparkly glitter pens on black paper" },
        { word: "MSN Messenger Nudge", hint: "Shaking the chat screen to get attention" }
      ]
    },
    {
      id: "millennial-media",
      name: "Iconic TV & Movies",
      icon: "📺",
      color: "#06b6d4",
      description: "Quotable movies and binge-worthy shows!",
      words: [
        { word: "Friends: Pivot!", hint: "Ross, Chandler, and Rachel on stairs" },
        { word: "The Office: Jim Look", hint: "Staring deadpan at the camera" },
        { word: "Mean Girls: Pink", hint: "On Wednesdays we wear pink" },
        { word: "Harry Potter: Golden Snitch", hint: "Catching the winged golden ball" },
        { word: "Shrek's Swamp", hint: "What are you doing in my swamp?!" },
        { word: "Legally Blonde Bend & Snap", hint: "Elle Woods teaching salon patrons" },
        { word: "High School Musical", hint: "We're all in this together jump" },
        { word: "The Matrix Bullet Dodge", hint: "Neo bending backwards in slow motion" },
        { word: "Titanic: I'm Flying", hint: "Jack and Rose at the bow of the ship" },
        { word: "Lord of the Rings: My Precious", hint: "Gollum crouching over the One Ring" },
        { word: "Gordon Ramsay: Idiot Sandwich", hint: "Holding bread against someone's face" },
        { word: "Twilight: Sparkling Vampire", hint: "Skin of a killer, Bella!" },
        { word: "Superbad: McLovin", hint: "Fake Hawaiian driver license ID" },
        { word: "Zoolander: Blue Steel", hint: "Male model duckface pout" },
        { word: "Borat: Very Nice!", hint: "High five, great success!" },
        { word: "Napoleon Dynamite Dance", hint: "Vote for Pedro auditorium routine" },
        { word: "Kill Bill Whistle", hint: "Yellow tracksuit katana duel" },
        { word: "Devil Wears Prada", hint: "That's all. Throwing coat on desk" }
      ]
    },
    {
      id: "millennial-adulting",
      name: "Adulting & Struggles",
      icon: "🥑",
      color: "#14b8a6",
      description: "The painful humor of turning 30+!",
      words: [
        { word: "Avocado Toast & Iced Latte", hint: "Why we can't afford a house" },
        { word: "Can We Just Text?", hint: "Refusing to pick up unexpected phone call" },
        { word: "Mysterious Back Pain", hint: "Slept slightly wrong on pillow" },
        { word: "Canceling Friday Plans", hint: "Relief of staying home in sweatpants" },
        { word: "Sunday Scaries", hint: "Dread of Monday morning creeping in" },
        { word: "Overthinking an Emoji", hint: "Did they mean that passively aggressively?" },
        { word: "Ghosting", hint: "Vanishing into thin air mid-conversation" },
        { word: "Plant Parent", hint: "Talking to monsteras and fiddle leaf figs" },
        { word: "87 Open Browser Tabs", hint: "I'll read these eventually, I promise" },
        { word: "Costco Bulk Run", hint: "48 rolls of toilet paper and $1.50 hot dog" },
        { word: "Unsubscribing from Emails", hint: "Daily battle against 100 newsletters" },
        { word: "Air Fryer Obsession", hint: "Reheats anything in 5 minutes" },
        { word: "Closing 40 Apps", hint: "Swiping up furiously to save battery" },
        { word: "Checking Zillow for Fun", hint: "Mansions we will never buy" },
        { word: "Leaving Party Without Saying Bye", hint: "The Irish goodbye masterclass" },
        { word: "Drinking from Giant Stanley Cup", hint: "40oz tumbler clanking everywhere" },
        { word: "Meal Prep Sunday", hint: "Same chicken and broccoli for 5 days" },
        { word: "Target Impulse Buy", hint: "Came for milk, spent $180" }
      ]
    },
    {
      id: "millennial-music",
      name: "90s & 2000s Bangers",
      icon: "🎤",
      color: "#e11d48",
      description: "Radio anthems we all still know by heart!",
      words: [
        { word: "Britney Spears: Hit Me Baby", hint: "Pigtails, schoolgirl uniform dance" },
        { word: "Backstreet Boys", hint: "Tell me why! Ain't nothing but a heartache" },
        { word: "Blink-182", hint: "Running naked in What's My Age Again" },
        { word: "Eminem: Mom's Spaghetti", hint: "Palms are sweaty, knees weak, arms are heavy" },
        { word: "Beyoncé: Single Ladies", hint: "Put a ring on it hand flick" },
        { word: "Linkin Park Screaming", hint: "In the end it doesn't even matter!" },
        { word: "Outkast: Hey Ya!", hint: "Shake it like a Polaroid picture" },
        { word: "Spice Girls: Wannabe", hint: "If you wanna be my lover" },
        { word: "Rickroll", hint: "Never gonna give you up dancing" },
        { word: "Avril Lavigne: Sk8er Boi", hint: "He was a boy, she was a girl" },
        { word: "Smash Mouth: All Star", hint: "Somebody once told me the world is gonna roll me" },
        { word: "Evanescence: Bring Me to Life", hint: "Wake me up inside! Can't wake up!" },
        { word: "Nelly: Hot in Herre", hint: "Band-aid on the cheek" },
        { word: "T-Pain Autotune", hint: "Robot singing about Apple Bottom Jeans" },
        { word: "Green Day: Boulevard", hint: "I walk a lonely road, the only one I have ever known" }
      ]
    }
  ]
};
"""

    with open("decks.js", "w", encoding="utf-8") as f:
        f.write(js_code)

    print("✅ decks.js successfully updated with expanded animals and silly actions!")

if __name__ == "__main__":
    main()
