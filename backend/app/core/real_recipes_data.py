# -*- coding: utf-8 -*-
"""
Dữ liệu ẩm thực thật chuẩn theo chuyên mục 'Vào Bếp' - Điện Máy Xanh.
Bao gồm:
- 12 Danh mục ẩm thực thực tế.
- 60 Món ăn thực tế với đầy đủ nguyên liệu, các bước nấu, hẹn giờ và hình ảnh minh họa.
"""

REAL_CATEGORIES = [
    {
        "name": "Món Kho Đậm Đà",
        "slug": "mon-kho",
        "description": "Các món thịt kho, cá kho tộ đậm vị thơm lừng chuẩn cơm gia đình Việt.",
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&auto=format&fit=crop",
        "order_index": 1,
    },
    {
        "name": "Món Canh & Súp Thanh Mát",
        "slug": "mon-canh-sup",
        "description": "Canh chua, canh sườn, súp khai vị thanh mát giải nhiệt bữa cơm.",
        "image_url": "https://images.unsplash.com/photo-1547592180-85f173990554?w=800&auto=format&fit=crop",
        "order_index": 2,
    },
    {
        "name": "Món Xào Nhanh Giòn Ngon",
        "slug": "mon-xao",
        "description": "Món xào lửa lớn giữ trọn độ giòn tươi ngọt tự nhiên của rau củ và thịt.",
        "image_url": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=800&auto=format&fit=crop",
        "order_index": 3,
    },
    {
        "name": "Món Chiên & Rán Giòn Rụm",
        "slug": "mon-chien-ran",
        "description": "Các món chiên vàng ruộm, giòn rụm từ cánh gà chiên mắm đến nem rán truyền thống.",
        "image_url": "https://images.unsplash.com/photo-1562967914-608f82629710?w=800&auto=format&fit=crop",
        "order_index": 4,
    },
    {
        "name": "Món Nướng Thơm Lừng",
        "slug": "mon-nuong",
        "description": "Các món nướng than hoa, sốt ướp đậm đà thơm lừng cho bữa tiệc sum vầy.",
        "image_url": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&auto=format&fit=crop",
        "order_index": 5,
    },
    {
        "name": "Món Hấp Giữ Trọn Dinh Dưỡng",
        "slug": "mon-hap",
        "description": "Món hấp cách thủy giữ trọn vị ngọt thanh, tươi ngon nguyên bản của thực phẩm.",
        "image_url": "https://images.unsplash.com/photo-1541544741938-0af808871cc0?w=800&auto=format&fit=crop",
        "order_index": 6,
    },
    {
        "name": "Món Lẩu Sum Họp",
        "slug": "mon-lau",
        "description": "Lẩu Thái, lẩu gà, lẩu cua đồng với nước dùng phong phú, ấm cúng quây quần.",
        "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=800&auto=format&fit=crop",
        "order_index": 7,
    },
    {
        "name": "Món Cuốn & Gỏi Trộn",
        "slug": "mon-cuon-goi",
        "description": "Gỏi cuốn, nộm ngó sen tươi mát chấm cùng nước mắm chua ngọt chuẩn vị.",
        "image_url": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=800&auto=format&fit=crop",
        "order_index": 8,
    },
    {
        "name": "Bún - Phở - Mì Truyền Thống",
        "slug": "bun-pho-mi",
        "description": "Phở bò Hà Nội, bún bò Huế, bún riêu đậm đà tinh hoa ẩm thực ba miền.",
        "image_url": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=800&auto=format&fit=crop",
        "order_index": 9,
    },
    {
        "name": "Bánh & Điểm Tâm Sáng",
        "slug": "banh-diem-tam",
        "description": "Bánh xèo miền Tây, cơm tấm sườn bì chả, bánh cuốn nóng giòn rụm thơm ngon.",
        "image_url": "https://images.unsplash.com/photo-1509722747041-616f39b57569?w=800&auto=format&fit=crop",
        "order_index": 10,
    },
    {
        "name": "Món Chay Thanh Tịnh",
        "slug": "mon-chay",
        "description": "Món ăn thuần chay bổ dưỡng, an lành từ nấm, đậu hũ và rau củ tươi non.",
        "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=800&auto=format&fit=crop",
        "order_index": 11,
    },
    {
        "name": "Món Tráng Miệng & Chè Ngon",
        "slug": "mon-trang-mieng",
        "description": "Chè bưởi, chè hạt sen long nhãn, bánh flan giải nhiệt ngọt ngào sau bữa ăn.",
        "image_url": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=800&auto=format&fit=crop",
        "order_index": 12,
    },
]

REAL_RECIPES = [
    {
        "title": "Thịt Ba Chỉ Kho Tàu Nước Dừa",
        "slug": "thit-ba-chi-kho-tau-nuoc-dua",
        "category_slug": "mon-kho",
        "description": "Món thịt kho tàu truyền thống với từng miếng thịt ba chỉ vuông vức mềm rục, trứng vịt bùi bùi quyện trong nước dừa xiêm óng ả đậm đà chuẩn vị Tết miền Nam.",
        "prep_time": 25,
        "cook_time": 60,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 520,
            "protein": 28,
            "carbohydrates": 12,
            "fat": 40,
            "fiber": 1,
            "sodium": 890
        },
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt ba chỉ heo",
                "quantity": 600,
                "unit": "gram",
                "notes": "chọn loại nạc mỡ đan xen đều, bì mỏng"
            },
            {
                "name": "Trứng vịt",
                "quantity": 6,
                "unit": "quả",
                "notes": "luộc chín, bóc vỏ sạch"
            },
            {
                "name": "Nước dừa tươi",
                "quantity": 500,
                "unit": "ml",
                "notes": "dừa xiêm ngọt thanh"
            },
            {
                "name": "Hành tím băm",
                "quantity": 3,
                "unit": "củ",
                "notes": "băm nhuyễn"
            },
            {
                "name": "Tỏi băm",
                "quantity": 4,
                "unit": "tép",
                "notes": "băm nhuyễn"
            },
            {
                "name": "Nước mắm cá cơm",
                "quantity": 4,
                "unit": "muỗng canh",
                "notes": "loại 40 độ đạm truyền thống"
            },
            {
                "name": "Đường phèn",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "dùng thắng nước màu caramen"
            },
            {
                "name": "Hạt nêm",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "tăng vị đậm đà"
            },
            {
                "name": "Tiêu đen xay",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "tiêu Phú Quốc thơm nồng"
            },
            {
                "name": "Ớt sừng đỏ",
                "quantity": 2,
                "unit": "trái",
                "notes": "để nguyên trái kho lấy hương"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế và khử mùi thịt ba chỉ",
                "description": "Rửa sạch thịt ba chỉ với nước muối loãng và một chút rượu trắng, chần qua nước sôi 2 phút rồi vớt ra xả nước lạnh. Cắt thịt thành các khối vuông khoảng 4-5cm.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Ướp gia vị cho thịt thấm",
                "description": "Ướp thịt cùng hành tỏi băm, 3 muỗng nước mắm, 1 muỗng hạt nêm, tiêu xay và 1 muỗng đường. Trộn đều rồi để nghỉ tối thiểu 30 phút trong ngăn mát tủ lạnh.",
                "timer_minutes": 30
            },
            {
                "step_number": 3,
                "title": "Thắng nước màu caramen và xào săn",
                "description": "Bắc nồi lên bếp, cho 1 muỗng dầu và 1 muỗng đường đun lửa vừa đến khi đường ngả màu cánh gián đẹp mắt. Cho thịt vào đảo săn đến khi từng miếng thịt bám màu óng ánh.",
                "timer_minutes": 8
            },
            {
                "step_number": 4,
                "title": "Kho thịt với nước dừa tươi",
                "description": "Đổ 500ml nước dừa tươi ngập mặt thịt, đun sôi rồi vớt bọt sạch. Hạ lửa nhỏ liu riu hầm trong 35 phút cho thịt mềm dần.",
                "timer_minutes": 35
            },
            {
                "step_number": 5,
                "title": "Cho trứng và hoàn thiện món ăn",
                "description": "Cho trứng vịt đã bóc vỏ và ớt sừng vào nồi kho tiếp 20 phút đến khi nước cạn sánh sệt, thịt mềm rục, nêm nếm lại cho vừa vị. Múc ra tô dùng kèm cơm nóng và dưa giá.",
                "timer_minutes": 20
            }
        ]
    },
    {
        "title": "Cá Lóc Kho Tộ Đậm Đà",
        "slug": "ca-loc-kho-to-dam-da",
        "category_slug": "mon-kho",
        "description": "Cá lóc đồng tươi ngon kho trong tộ đất với nước màu dừa, tiêu đen cay nồng và thịt ba chỉ giòn ngậy thơm phức bữa cơm quê.",
        "prep_time": 20,
        "cook_time": 40,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 380,
            "protein": 34,
            "carbohydrates": 8,
            "fat": 22,
            "fiber": 1,
            "sodium": 920
        },
        "image_url": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Cá lóc đồng",
                "quantity": 700,
                "unit": "gram",
                "notes": "làm sạch vảy, cắt khúc vừa ăn"
            },
            {
                "name": "Thịt ba chỉ",
                "quantity": 150,
                "unit": "gram",
                "notes": "thái lát mỏng để kho cùng lấy mỡ béo"
            },
            {
                "name": "Hành tím băm",
                "quantity": 2,
                "unit": "củ",
                "notes": "băm nhỏ"
            },
            {
                "name": "Tỏi băm",
                "quantity": 3,
                "unit": "tép",
                "notes": "phi thơm"
            },
            {
                "name": "Nước mắm ngon",
                "quantity": 4,
                "unit": "muỗng canh",
                "notes": "loại truyền thống"
            },
            {
                "name": "Đường thốt nốt",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "tạo vị ngọt thanh và màu đẹp"
            },
            {
                "name": "Tiêu hạt đập dập",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "tiêu xanh hoặc tiêu đen"
            },
            {
                "name": "Hành lá",
                "quantity": 3,
                "unit": "nhánh",
                "notes": "đầu hành đập dập, lá cắt nhỏ"
            },
            {
                "name": "Ớt chỉ thiên",
                "quantity": 3,
                "unit": "trái",
                "notes": "tùy khẩu vị cay"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế cá lóc không bị tanh",
                "description": "Rửa cá lóc với muối hạt và nước cốt chanh hoặc rượu trắng để sạch nhớt tanh, rửa lại nước sạch rồi để ráo. Khứa nhẹ lên thân cá.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Ướp cá đậm đà",
                "description": "Ướp cá với 3 muỗng nước mắm, 1 muỗng đường, hành tím băm, đầu hành đập dập, ớt và tiêu giã dập trong 25 phút.",
                "timer_minutes": 25
            },
            {
                "step_number": 3,
                "title": "Xào thịt ba chỉ và xếp tộ",
                "description": "Bắc tộ đất lên bếp, cho thịt ba chỉ vào đảo cho tứa bớt mỡ, chắt bớt mỡ thừa rồi xếp từng lát cá lên trên lớp thịt.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Kho cá lửa liu riu",
                "description": "Bật lửa lớn cho cá sôi bùng và săn thịt lại, châm thêm nửa chén nước nóng. Hạ lửa nhỏ liu riu đậy nắp kho 25 phút cho nước cá sánh keo lại.",
                "timer_minutes": 25
            },
            {
                "step_number": 5,
                "title": "Hoàn thành và rắc tiêu",
                "description": "Mở nắp, rưới nước sốt lên mặt cá, rắc nhiều tiêu đen xay và hành lá cắt nhỏ. Tắt bếp, thưởng thức ngay khi nồi tộ còn sôi sùng sục.",
                "timer_minutes": 3
            }
        ]
    },
    {
        "title": "Gà Kho Gừng Thơm Ấm",
        "slug": "ga-kho-gung-thom-am",
        "category_slug": "mon-kho",
        "description": "Thịt gà ta săn chắc vàng ươm ngấm đượm gia vị mằn mặn ngọt ngọt, ấm nồng mùi gừng tươi thái sợi, món ăn khoái khẩu trong những ngày mưa lạnh.",
        "prep_time": 15,
        "cook_time": 30,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 420,
            "protein": 36,
            "carbohydrates": 6,
            "fat": 26,
            "fiber": 1,
            "sodium": 780
        },
        "image_url": "https://images.unsplash.com/photo-1562967914-608f82629710?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt gà ta",
                "quantity": 700,
                "unit": "gram",
                "notes": "chặt miếng vuông vừa ăn"
            },
            {
                "name": "Gừng tươi",
                "quantity": 50,
                "unit": "gram",
                "notes": "cạo vỏ, thái sợi chỉ"
            },
            {
                "name": "Hành khô",
                "quantity": 2,
                "unit": "củ",
                "notes": "thái lát mỏng"
            },
            {
                "name": "Tỏi băm",
                "quantity": 3,
                "unit": "tép",
                "notes": "băm nhuyễn"
            },
            {
                "name": "Nước mắm ngon",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "nước mắm nguyên chất"
            },
            {
                "name": "Hạt nêm",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "nêm gà"
            },
            {
                "name": "Đường cát vàng",
                "quantity": 1.5,
                "unit": "muỗng canh",
                "notes": "thắng nước màu"
            },
            {
                "name": "Dầu ăn",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "phi gừng hành"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế gà và gừng",
                "description": "Gà chà xát với muối và gừng đập dập khử sạch mùi hôi, rửa lại để ráo rồi chặt miếng vừa ăn. Gừng cạo vỏ, thái sợi chỉ dài đều.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Ướp thịt gà",
                "description": "Ướp gà với 2 muỗng nước mắm, 1 muỗng hạt nêm, tiêu xay, hành tím và 1/2 lượng gừng thái sợi trong 20 phút.",
                "timer_minutes": 20
            },
            {
                "step_number": 3,
                "title": "Thắng nước màu và phi thơm gừng",
                "description": "Đun nóng dầu ăn cùng đường vàng đến khi sủi bọt ngả màu cánh gián, cho tỏi và phần gừng còn lại vào phi dậy mùi thơm nức.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Xào săn và kho gà",
                "description": "Trút gà vào đảo đều tay trên lửa lớn cho săn chắc lại. Đổ thêm 100ml nước ấm, hạ lửa vừa kho trong 20 phút cho gà chín mềm ngấm đều sốt.",
                "timer_minutes": 20
            },
            {
                "step_number": 5,
                "title": "Trình bày món ăn",
                "description": "Khi nước kho sánh lại bao quanh từng miếng gà vàng óng, rắc hành lá và tiêu xay lên trên rồi tắt bếp. Dùng nóng cùng cơm trắng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Sườn Non Kho Tiêu Cay Nồng",
        "slug": "suon-non-kho-tieu-cay-nong",
        "category_slug": "mon-kho",
        "description": "Từng dẻ sườn non sụn giòn mềm rục, đẫm vị nước mắm tỏi ớt caramen và thơm nồng tiêu đen xay cay nồng kích thích vị giác.",
        "prep_time": 20,
        "cook_time": 35,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 480,
            "protein": 32,
            "carbohydrates": 10,
            "fat": 34,
            "fiber": 1,
            "sodium": 860
        },
        "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Sườn non heo",
                "quantity": 600,
                "unit": "gram",
                "notes": "chọn dẻ sườn có sụn non giòn"
            },
            {
                "name": "Hành tím băm",
                "quantity": 3,
                "unit": "củ",
                "notes": "băm nhỏ"
            },
            {
                "name": "Tỏi băm",
                "quantity": 4,
                "unit": "tép",
                "notes": "băm nhuyễn"
            },
            {
                "name": "Tiêu đen hạt giã dập",
                "quantity": 1.5,
                "unit": "muỗng canh",
                "notes": "tiêu xay mới"
            },
            {
                "name": "Nước mắm ngon",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "đậm đà"
            },
            {
                "name": "Nước hàng caramen",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "tạo màu cánh gián"
            },
            {
                "name": "Đường phèn",
                "quantity": 1.5,
                "unit": "muỗng canh",
                "notes": "hài hòa vị mặn"
            },
            {
                "name": "Hành lá",
                "quantity": 2,
                "unit": "nhánh",
                "notes": "thái nhỏ"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Chần sườn sạch mùi",
                "description": "Chặt sườn thành miếng dài 3-4cm, rửa nước muối loãng, chần qua nước sôi 3 phút rồi vớt ra xả sạch bọt bẩn, để ráo nước.",
                "timer_minutes": 8
            },
            {
                "step_number": 2,
                "title": "Ướp sườn ngấm vị",
                "description": "Ướp sườn với nước mắm, đường, nước màu, hành tỏi băm và một nửa lượng tiêu giã dập trong 25 phút.",
                "timer_minutes": 25
            },
            {
                "step_number": 3,
                "title": "Xào săn sườn",
                "description": "Bắc chảo lên bếp, cho chút dầu phi thơm hành tỏi, trút sườn vào xào trên lửa to đến khi sườn săn và cháy cạnh nhẹ.",
                "timer_minutes": 7
            },
            {
                "step_number": 4,
                "title": "Kho liu riu đượm vị",
                "description": "Châm nước sôi xăm xắp mặt sườn, đun sôi bùng rồi hạ lửa nhỏ liu riu đậy vung kho trong 25 phút cho sườn mềm rục.",
                "timer_minutes": 25
            },
            {
                "step_number": 5,
                "title": "Thêm tiêu và dọn món",
                "description": "Khi nước sốt cạn sền sệt, rắc nốt phần tiêu xay còn lại và hành hoa thái nhỏ vào đảo đều, múc ra đĩa thưởng thức.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Cá Thu Nhật Sốt Cà Chua Đậm Vị",
        "slug": "ca-thu-nhat-sot-ca-chua-dam-vi",
        "category_slug": "mon-kho",
        "description": "Cá thu Nhật chiên sơ vàng thơm, sau đó om ngập trong nước sốt cà chua đỏ mọng chua ngọt thanh tao, thịt cá bùi ngậy đậm đà.",
        "prep_time": 15,
        "cook_time": 30,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 360,
            "protein": 30,
            "carbohydrates": 14,
            "fat": 19,
            "fiber": 2,
            "sodium": 750
        },
        "image_url": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Cá thu Nhật",
                "quantity": 4,
                "unit": "con",
                "notes": "làm sạch mang ruột, cắt đôi"
            },
            {
                "name": "Cà chua chín mọng",
                "quantity": 4,
                "unit": "quả",
                "notes": "bỏ hạt băm nhỏ"
            },
            {
                "name": "Hành tím băm",
                "quantity": 2,
                "unit": "củ",
                "notes": "phi thơm"
            },
            {
                "name": "Tỏi băm",
                "quantity": 3,
                "unit": "tép",
                "notes": "băm nhuyễn"
            },
            {
                "name": "Nước mắm",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "nêm vị"
            },
            {
                "name": "Hành lá, thì là",
                "quantity": 50,
                "unit": "gram",
                "notes": "rửa sạch thái khúc"
            },
            {
                "name": "Dầu ăn",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "chiên cá và làm sốt"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế cá thu",
                "description": "Rửa sạch cá với nước muối và chanh khử tanh, lau khô từng con bằng khăn giấy sạch.",
                "timer_minutes": 8
            },
            {
                "step_number": 2,
                "title": "Chiên sơ cá thu",
                "description": "Đun nóng dầu ăn, cho cá vào chiên sơ hai mặt cho vàng giòn nhẹ bên ngoài, vớt ra đĩa lót giấy thấm dầu.",
                "timer_minutes": 10
            },
            {
                "step_number": 3,
                "title": "Làm sốt cà chua sánh mịn",
                "description": "Phi thơm hành tỏi, trút cà chua băm vào xào nhuyễn cùng chút gia vị đến khi cà chua chín mềm tạo thành sốt sệt.",
                "timer_minutes": 7
            },
            {
                "step_number": 4,
                "title": "Om cá cùng sốt cà chua",
                "description": "Xếp cá thu đã chiên vào chảo sốt cà chua, thêm 1/2 chén nước sôi, đậy nắp om lửa nhỏ trong 15 phút cho cá ngấm vị chua ngọt.",
                "timer_minutes": 15
            },
            {
                "step_number": 5,
                "title": "Thêm thì là hành hoa",
                "description": "Rắc thì là và hành lá thái khúc cùng chút tiêu xay lên trên mặt, tắt bếp và thưởng thức cùng cơm nóng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Canh Chua Cá Lóc Nam Bộ",
        "slug": "canh-chua-ca-loc-nam-bo",
        "category_slug": "mon-canh-sup",
        "description": "Món canh chua trứ danh miền Tây sông nước với cá lóc ngọt thịt, nước canh chua thanh dịu từ me chín, thơm mát cùng dọc mùng, giá đỗ, bắp chuối và ngò ôm thơm ngát.",
        "prep_time": 20,
        "cook_time": 25,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 280,
            "protein": 26,
            "carbohydrates": 18,
            "fat": 9,
            "fiber": 3,
            "sodium": 720
        },
        "image_url": "https://images.unsplash.com/photo-1547592180-85f173990554?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Cá lóc đồng",
                "quantity": 500,
                "unit": "gram",
                "notes": "cắt khoanh dày 3cm"
            },
            {
                "name": "Thơm (dứa)",
                "quantity": 0.25,
                "unit": "quả",
                "notes": "cắt lát tam giác"
            },
            {
                "name": "Cà chua",
                "quantity": 2,
                "unit": "quả",
                "notes": "cắt múi cau"
            },
            {
                "name": "Dọc mùng (bạc hà)",
                "quantity": 100,
                "unit": "gram",
                "notes": "tước vỏ, bóp muối vắt ráo"
            },
            {
                "name": "Đậu bắp",
                "quantity": 5,
                "unit": "trái",
                "notes": "cắt xéo vừa ăn"
            },
            {
                "name": "Giá đỗ sạch",
                "quantity": 100,
                "unit": "gram",
                "notes": "nhặt sạch gốc"
            },
            {
                "name": "Me chín",
                "quantity": 50,
                "unit": "gram",
                "notes": "dầm lấy nước cốt chua"
            },
            {
                "name": "Ngò gai, ngò ôm",
                "quantity": 30,
                "unit": "gram",
                "notes": "thái nhỏ tạo mùi đặc trưng"
            },
            {
                "name": "Tỏi phi vàng",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "rắc lên bề mặt canh"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế cá và rau củ",
                "description": "Cá lóc xát muối và chanh khử tanh, rửa sạch để ráo. Dọc mùng tước vỏ tước xơ, bóp kỹ với muối rồi xả sạch vắt ráo. Thơm, cà chua, đậu bắp rửa sạch cắt miếng.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Nấu nước cốt me",
                "description": "Đun sôi 1.2 lít nước, cho me vào dầm nát lọc lấy nước chua, bỏ hạt. Nêm 2 muỗng canh đường, 2 muỗng nước mắm và 1 muỗng hạt nêm.",
                "timer_minutes": 8
            },
            {
                "step_number": 3,
                "title": "Nấu chín cá lóc",
                "description": "Thả cá lóc vào nồi nước sôi, hạ lửa vừa đun trong 8-10 phút cho cá chín ngọt, vớt bọt thường xuyên để nước canh trong veo.",
                "timer_minutes": 10
            },
            {
                "step_number": 4,
                "title": "Cho rau củ vào nồi",
                "description": "Lần lượt cho thơm, cà chua, đậu bắp và dọc mùng vào nấu sôi 3 phút. Cuối cùng cho giá đỗ vào rồi tắt bếp ngay để giá giữ độ giòn.",
                "timer_minutes": 5
            },
            {
                "step_number": 5,
                "title": "Múc canh và trang trí",
                "description": "Múc cá và rau ra tô lớn, rắc ngò gai, ngò ôm, ớt xắt lát và tỏi phi thơm lên trên. Dùng kèm chén nước mắm ớt mặn.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Canh Cua Rau Đay Mướp Hương",
        "slug": "canh-cua-rau-day-muop-huong",
        "category_slug": "mon-canh-sup",
        "description": "Món canh dân dã giải nhiệt mùa hè của người Bắc với từng mảng riêu cua đồng đóng tảng béo ngậy, vị ngọt lịm từ mướp hương và rau đay non mướt ăn cùng cà pháo giòn tan.",
        "prep_time": 25,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 210,
            "protein": 18,
            "carbohydrates": 12,
            "fat": 8,
            "fiber": 3,
            "sodium": 650
        },
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Cua đồng xay nhuyễn",
                "quantity": 400,
                "unit": "gram",
                "notes": "lọc kỹ lấy nước thịt cua"
            },
            {
                "name": "Rau đay non",
                "quantity": 1,
                "unit": "bó",
                "notes": "nhặt lá non, rửa sạch thái nhỏ"
            },
            {
                "name": "Rau mồng tơi",
                "quantity": 1,
                "unit": "bó",
                "notes": "nhặt lá non rửa sạch"
            },
            {
                "name": "Mướp hương",
                "quantity": 1,
                "unit": "trái",
                "notes": "gọt vỏ, thái vát mỏng"
            },
            {
                "name": "Hành khô",
                "quantity": 2,
                "unit": "củ",
                "notes": "băm nhỏ phi thơm gạch cua"
            },
            {
                "name": "Mắm tôm Bắc",
                "quantity": 0.5,
                "unit": "muỗng cà phê",
                "notes": "dậy mùi riêu cua truyền thống"
            },
            {
                "name": "Nước mắm ngon",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "nêm canh"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Lọc nước thịt cua đồng",
                "description": "Khuấy cua xay với 1 lít nước sạch cùng chút muối hạt, lọc qua rây 2-3 lần để loại bỏ hoàn toàn sạn vỏ, thu lấy nước cua trong sánh.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Chưng gạch cua vàng óng",
                "description": "Khêu gạch cua trong mai ra chén. Phi thơm hành khô với chút dầu ăn, trút gạch cua vào chưng vàng thơm rồi trút riêng ra chén.",
                "timer_minutes": 4
            },
            {
                "step_number": 3,
                "title": "Nấu đóng tảng riêu cua",
                "description": "Đặt nồi nước cua lên bếp, thêm chút mắm tôm. Đun lửa vừa và khuấy nhẹ đáy nồi một chiều. Khi nước nóng dần và thịt cua nổi lên đóng tảng thì hạ lửa thật nhỏ, gạt nhẹ riêu sang một bên.",
                "timer_minutes": 10
            },
            {
                "step_number": 4,
                "title": "Nấu rau và mướp",
                "description": "Thả mướp hương vào trước đun 2 phút, tiếp tục cho rau đay và mồng tơi vào dìm nhẹ dưới nước sôi. Rưới chén gạch cua đã chưng lên trên riêu. Nước sôi bùng lại thì tắt bếp ngay.",
                "timer_minutes": 4
            },
            {
                "step_number": 5,
                "title": "Hoàn thiện món canh",
                "description": "Múc canh ra tô giữ nguyên tảng riêu cua vàng ươm nguyên vẹn trên mặt. Dùng nóng kèm cơm trắng và cà pháo muối giòn.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Canh Sườn Hầm Rau Củ Thập Cẩm",
        "slug": "canh-suon-ham-rau-cu-thap-cam",
        "category_slug": "mon-canh-sup",
        "description": "Vị ngọt thanh từ sườn heo ninh nhừ kết hợp cùng ngô ngọt, cà rốt, củ dền và khoai tây bở bùi, đem lại nguồn vitamin và khoáng chất dồi dào cho cả gia đình.",
        "prep_time": 15,
        "cook_time": 45,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 340,
            "protein": 24,
            "carbohydrates": 22,
            "fat": 16,
            "fiber": 4,
            "sodium": 610
        },
        "image_url": "https://images.unsplash.com/photo-1547592180-85f173990554?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Sườn non hoặc sườn thăn",
                "quantity": 500,
                "unit": "gram",
                "notes": "chặt miếng vừa ăn, chần sạch"
            },
            {
                "name": "Ngô ngọt",
                "quantity": 1,
                "unit": "bắp",
                "notes": "cắt khúc 3cm"
            },
            {
                "name": "Cà rốt",
                "quantity": 1,
                "unit": "củ",
                "notes": "tỉa hoa, cắt lát dày 1cm"
            },
            {
                "name": "Khoai tây",
                "quantity": 2,
                "unit": "củ",
                "notes": "gọt vỏ cắt khối vuông ngâm nước"
            },
            {
                "name": "Hành lá, ngò rí",
                "quantity": 30,
                "unit": "gram",
                "notes": "rửa sạch thái nhỏ"
            },
            {
                "name": "Hạt nêm xương hầm",
                "quantity": 2,
                "unit": "muỗng cà phê",
                "notes": "nêm vừa miệng"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Chần và sơ chế sườn",
                "description": "Chần sườn với nước sôi và muối trong 3 phút, rửa sạch bọt bẩn để nước canh được trong veo.",
                "timer_minutes": 5
            },
            {
                "step_number": 2,
                "title": "Ninh sườn lấy nước ngọt",
                "description": "Cho sườn vào nồi cùng 1.5 lít nước và ngô ngọt cắt khúc, đun sôi rồi hạ lửa nhỏ hầm liu riu trong 25 phút.",
                "timer_minutes": 25
            },
            {
                "step_number": 3,
                "title": "Cho rau củ vào hầm",
                "description": "Cho cà rốt và khoai tây vào nồi hầm tiếp 15 phút đến khi rau củ chín mềm bở nhưng không bị nát.",
                "timer_minutes": 15
            },
            {
                "step_number": 4,
                "title": "Nêm nếm gia vị",
                "description": "Nêm hạt nêm, chút nước mắm ngon và muối tiêu cho vừa khẩu vị gia đình.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Thành phẩm",
                "description": "Múc canh ra tô, rắc hành ngò thái nhỏ và tiêu xay lên trên, thưởng thức khi canh còn nóng ấm.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Canh Ngao Nấu Chua Thì Là",
        "slug": "canh-ngao-nau-chua-thi-la",
        "category_slug": "mon-canh-sup",
        "description": "Vị chua thanh mát của dứa cà chua kết hợp cùng vị ngọt tự nhiên của ngao biển và mùi thơm nồng đặc trưng của rau thì là giúp giải nhiệt sảng khoái.",
        "prep_time": 15,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 160,
            "protein": 15,
            "carbohydrates": 12,
            "fat": 4,
            "fiber": 2,
            "sodium": 590
        },
        "image_url": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Ngao biển (nghêu)",
                "quantity": 1000,
                "unit": "gram",
                "notes": "ngâm nước ớt nhả sạch cát"
            },
            {
                "name": "Cà chua",
                "quantity": 2,
                "unit": "quả",
                "notes": "bổ múi cau"
            },
            {
                "name": "Thơm (dứa)",
                "quantity": 0.5,
                "unit": "quả",
                "notes": "gọt mắt thái mỏng"
            },
            {
                "name": "Sấu tươi hoặc me",
                "quantity": 3,
                "unit": "quả",
                "notes": "tạo vị chua thanh"
            },
            {
                "name": "Hành tím băm",
                "quantity": 2,
                "unit": "củ",
                "notes": "phi thơm"
            },
            {
                "name": "Rau thì là, hành hoa",
                "quantity": 40,
                "unit": "gram",
                "notes": "thái khúc nhỏ"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Luộc ngao lấy nước trong",
                "description": "Ngao rửa sạch vỏ, cho vào nồi cùng 800ml nước đun sôi đến khi ngao mở miệng thì vớt ra ngay. Chắt lấy nước luộc ngao trong, bỏ cặn đáy.",
                "timer_minutes": 7
            },
            {
                "step_number": 2,
                "title": "Tách thịt ngao",
                "description": "Cạy lấy thịt ngao rửa lại cho sạch hết cát vụn, ướp chút hành tím và tiêu.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Xào thơm và cà chua",
                "description": "Phi thơm hành tím, trút cà chua và thơm vào xào mềm tạo màu đỏ đẹp mắt.",
                "timer_minutes": 4
            },
            {
                "step_number": 4,
                "title": "Nấu nước canh chua",
                "description": "Đổ nước luộc ngao vào nồi xào cà chua, thêm sấu tươi đun sôi 8 phút. Dầm nát sấu lấy vị chua thanh, nêm gia vị vừa miệng.",
                "timer_minutes": 8
            },
            {
                "step_number": 5,
                "title": "Hoàn thành canh ngao",
                "description": "Trút thịt ngao vào nồi sôi bùng trở lại, rắc thì là và hành hoa rồi tắt bếp ngay.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Canh Bắp Bò Hầm Hạt Sen",
        "slug": "canh-bap-bo-ham-hat-sen",
        "category_slug": "mon-canh-sup",
        "description": "Món canh bồi bổ sức khỏe hảo hạng với thịt bắp bò hoa giòn sần sật ninh mềm, hạt sen Huế bở bùi thơm mát giúp an thần, ngủ ngon giấc.",
        "prep_time": 20,
        "cook_time": 50,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 390,
            "protein": 32,
            "carbohydrates": 20,
            "fat": 16,
            "fiber": 3,
            "sodium": 580
        },
        "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Bắp bò hoa",
                "quantity": 500,
                "unit": "gram",
                "notes": "thái lát dày 1cm hoặc khúc vuông"
            },
            {
                "name": "Hạt sen tươi Huế",
                "quantity": 150,
                "unit": "gram",
                "notes": "bỏ tâm sen đắng, rửa sạch"
            },
            {
                "name": "Cà rốt",
                "quantity": 1,
                "unit": "củ",
                "notes": "cắt khoanh tỉa hoa"
            },
            {
                "name": "Kỷ tử",
                "quantity": 15,
                "unit": "gram",
                "notes": "rửa sạch để ráo"
            },
            {
                "name": "Gừng tươi",
                "quantity": 1,
                "unit": "nhánh",
                "notes": "đập dập khử mùi bò"
            },
            {
                "name": "Hành ngò",
                "quantity": 30,
                "unit": "gram",
                "notes": "rửa sạch thái nhỏ"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế và ướp bắp bò",
                "description": "Bắp bò chần qua nước sôi gừng để khử mùi gây, rửa sạch cắt miếng vừa ăn. Ướp với chút hạt nêm, tiêu và tỏi băm trong 15 phút.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Hầm bắp bò",
                "description": "Cho bắp bò vào nồi hầm cùng 1.2 lít nước, gừng đập dập. Hầm lửa nhỏ trong 35 phút cho thịt mềm dẻo.",
                "timer_minutes": 35
            },
            {
                "step_number": 3,
                "title": "Cho hạt sen và cà rốt",
                "description": "Thả hạt sen tươi và cà rốt vào hầm chung trong 15 phút đến khi hạt sen chín bở mềm tơi.",
                "timer_minutes": 15
            },
            {
                "step_number": 4,
                "title": "Nêm nếm gia vị thanh",
                "description": "Cho kỷ tử vào đun thêm 3 phút, nêm hạt nêm và chút muối hạt cho nước dùng ngọt thanh tao.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Múc canh và thưởng thức",
                "description": "Múc canh nóng ra tô sứ, rắc hành ngò thái nhỏ lên trên, ăn nóng bổ dưỡng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Canh Khổ Qua Nhồi Thịt Thanh Nhiệt",
        "slug": "canh-kho-qua-nhoi-thit-thanh-nhiet",
        "category_slug": "mon-canh-sup",
        "description": "Món canh mang ý nghĩa xua đi nỗi khổ đón chào may mắn, vị đắng dịu quyện cùng nhân thịt nạc mộc nhĩ ngọt đậm đà xua tan mệt mỏi.",
        "prep_time": 25,
        "cook_time": 30,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 260,
            "protein": 22,
            "carbohydrates": 10,
            "fat": 14,
            "fiber": 3,
            "sodium": 620
        },
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Khổ qua (mướp đắng)",
                "quantity": 3,
                "unit": "trái",
                "notes": "chọn trái nở gai đều, nạo ruột"
            },
            {
                "name": "Thịt nạc vai băm",
                "quantity": 300,
                "unit": "gram",
                "notes": "xay nhuyễn có chút mỡ"
            },
            {
                "name": "Mộc nhĩ (nấm mèo)",
                "quantity": 20,
                "unit": "gram",
                "notes": "ngâm nở thái sợi băm nhỏ"
            },
            {
                "name": "Miến dong",
                "quantity": 30,
                "unit": "gram",
                "notes": "ngâm mềm cắt khúc 1cm"
            },
            {
                "name": "Hành tím băm",
                "quantity": 2,
                "unit": "củ",
                "notes": "trộn nhân thịt"
            },
            {
                "name": "Hành lá",
                "quantity": 5,
                "unit": "nhánh",
                "notes": "trần nước sôi để buộc miệng khổ qua"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế khổ qua bớt đắng",
                "description": "Cắt khổ qua thành từng khúc 4cm hoặc rạch dọc thân, nạo sạch ruột trắng bên trong rồi rửa sạch để ráo.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Trộn nhân thịt nhồi",
                "description": "Trộn đều thịt băm, mộc nhĩ, miến, hành tím, 1 muỗng hạt nêm, tiêu xay và xíu nước mắm. Dùng muỗng nhồi chặt nhân vào từng khúc khổ qua.",
                "timer_minutes": 10
            },
            {
                "step_number": 3,
                "title": "Nấu nước dùng ngọt thanh",
                "description": "Đun sôi 1.2 lít nước luộc gà hoặc nước xương, nêm chút muối hạt cho nước canh trong.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Nấu chín khổ qua",
                "description": "Thả từng khúc khổ qua vào nồi nước sôi, hạ lửa vừa mở hé nắp để khổ qua giữ màu xanh tươi, nấu trong 20 phút đến khi khổ qua chín mềm.",
                "timer_minutes": 20
            },
            {
                "step_number": 5,
                "title": "Trình bày món canh",
                "description": "Múc canh ra tô, rắc hành lá ngò rí và tiêu xay. Dùng kèm chén nước mắm ớt nguyên chất.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Súp Cua Gà Ngô Non Khai Vị",
        "slug": "sup-cua-ga-ngo-non-khai-vi",
        "category_slug": "mon-canh-sup",
        "description": "Món súp khai vị sánh mịn óng ánh màu vàng ngô non, thịt cua biển ngọt lịm cùng ức gà xé phay, trứng cút bùi béo và nấm tuyết giòn sần sật.",
        "prep_time": 20,
        "cook_time": 25,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 230,
            "protein": 20,
            "carbohydrates": 16,
            "fat": 7,
            "fiber": 2,
            "sodium": 590
        },
        "image_url": "https://images.unsplash.com/photo-1547592180-85f173990554?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt cua biển bóc sẵn",
                "quantity": 150,
                "unit": "gram",
                "notes": "chọn thịt càng và thân tươi"
            },
            {
                "name": "Ức gà tươi",
                "quantity": 150,
                "unit": "gram",
                "notes": "luộc chín xé sợi nhỏ"
            },
            {
                "name": "Ngô ngọt tách hạt",
                "quantity": 1,
                "unit": "bắp",
                "notes": "hạt ngô tươi giòn ngọt"
            },
            {
                "name": "Nấm tuyết hoặc nấm hương",
                "quantity": 30,
                "unit": "gram",
                "notes": "ngâm nở băm nhỏ"
            },
            {
                "name": "Trứng cút luộc",
                "quantity": 8,
                "unit": "quả",
                "notes": "bóc sạch vỏ"
            },
            {
                "name": "Trứng gà",
                "quantity": 1,
                "unit": "quả",
                "notes": "đánh tan tạo vân mây"
            },
            {
                "name": "Bột năng",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "hòa tan với 1/2 chén nước lọc"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Chuẩn bị nguyên liệu",
                "description": "Xé nhỏ ức gà luộc, ướp chút tiêu. Nấm ngâm nở thái nhỏ. Thịt cua xào sơ với hành tỏi cho thơm.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Nấu nước súp",
                "description": "Đun sôi 1 lít nước luộc gà, cho ngô ngọt vào nấu trong 7 phút cho ngọt nước.",
                "timer_minutes": 7
            },
            {
                "step_number": 3,
                "title": "Nấu thịt cua gà và nấm",
                "description": "Cho thịt gà xé, thịt cua, nấm tuyết và trứng cút vào nồi đun sôi thêm 5 phút.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Tạo độ sánh và vân trứng",
                "description": "Rót từ từ nước bột năng vào khuấy đều tay theo một chiều tạo độ sánh mịn. Sau đó rót trứng gà qua rây khuấy nhẹ tạo vân sợi tơ đẹp mắt.",
                "timer_minutes": 5
            },
            {
                "step_number": 5,
                "title": "Hoàn thiện bát súp",
                "description": "Múc súp nóng ra bát, rưới chút dầu mè, rắc ngò rí và tiêu bột lên trên, thưởng thức ngay.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Bò Lúc Lắc Khoai Tây Chiên",
        "slug": "bo-luc-lac-khoai-tay-chien",
        "category_slug": "mon-xao",
        "description": "Từng khối thịt bò thăn mềm mọng xào lửa lớn cháy cạnh cùng ớt chuông ba màu, hành tây giòn ngọt, ăn kèm khoai tây chiên giòn rụm và sốt tiêu đen đậm đà.",
        "prep_time": 20,
        "cook_time": 15,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 490,
            "protein": 36,
            "carbohydrates": 28,
            "fat": 26,
            "fiber": 3,
            "sodium": 780
        },
        "image_url": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt thăn bò mềm",
                "quantity": 500,
                "unit": "gram",
                "notes": "cắt khối vuông quân cờ 2x2cm"
            },
            {
                "name": "Ớt chuông xanh, đỏ, vàng",
                "quantity": 1.5,
                "unit": "quả",
                "notes": "cắt khối vuông cùng cỡ"
            },
            {
                "name": "Hành tây",
                "quantity": 1,
                "unit": "củ",
                "notes": "cắt múi vuông"
            },
            {
                "name": "Khoai tây",
                "quantity": 2,
                "unit": "củ",
                "notes": "thái con chì chiên giòn"
            },
            {
                "name": "Bơ lạt",
                "quantity": 20,
                "unit": "gram",
                "notes": "tăng độ thơm ngậy lúc xào"
            },
            {
                "name": "Tỏi băm",
                "quantity": 5,
                "unit": "tép",
                "notes": "phi thơm"
            },
            {
                "name": "Dầu hào, xì dầu",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "sốt ướp bò"
            },
            {
                "name": "Tiêu đen xay",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "thơm nồng"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Ướp thịt bò mềm thơm",
                "description": "Ướp bò với 1 muỗng dầu hào, 1 muỗng nước tương, 1 muỗng dầu ăn, tiêu và tỏi băm trong 20 phút. Dầu ăn giúp giữ nước thịt không bị dai khô.",
                "timer_minutes": 20
            },
            {
                "step_number": 2,
                "title": "Chiên khoai tây giòn",
                "description": "Ngâm khoai tây vào nước muối loãng, luộc sơ 2 phút rồi vớt ra lau khô. Chiên ngập dầu đến khi vàng giòn rụm.",
                "timer_minutes": 10
            },
            {
                "step_number": 3,
                "title": "Xào ớt chuông và hành tây",
                "description": "Phi thơm tỏi trên chảo gang lửa lớn, cho ớt chuông và hành tây vào đảo nhanh tay trong 2 phút rồi trút ra đĩa riêng.",
                "timer_minutes": 3
            },
            {
                "step_number": 4,
                "title": "Xào bò lúc lắc lửa lớn",
                "description": "Đun chảo thật nóng với chút dầu và bơ lạt. Trút thịt bò vào lắc chảo đều tay trên lửa cực lớn trong 2-3 phút cho xém cạnh ngoài nhưng bên trong vẫn giữ độ mềm ngọt mọng nước.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Hoàn thiện đĩa bò lúc lắc",
                "description": "Trút ớt chuông hành tây vào đảo cùng thịt bò thêm 30 giây. Bày ra đĩa cùng khoai tây chiên, xà lách và cà chua.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Sườn Xào Chua Ngọt Óng Ánh",
        "slug": "suon-xao-chua-ngot-ong-anh",
        "category_slug": "mon-xao",
        "description": "Miếng sườn vàng ươm phủ lớp nước sốt sánh mịn chua chua ngọt ngọt từ giấm táo và cà chua, thịt sườn róc xương mềm ngọt đậm vị bắt cơm.",
        "prep_time": 20,
        "cook_time": 25,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 450,
            "protein": 28,
            "carbohydrates": 24,
            "fat": 27,
            "fiber": 2,
            "sodium": 790
        },
        "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Sườn non heo",
                "quantity": 600,
                "unit": "gram",
                "notes": "chặt khúc 3cm chần sạch"
            },
            {
                "name": "Hành tây",
                "quantity": 0.5,
                "unit": "củ",
                "notes": "cắt múi cau"
            },
            {
                "name": "Ớt chuông đỏ",
                "quantity": 0.5,
                "unit": "quả",
                "notes": "cắt miếng vuông"
            },
            {
                "name": "Giấm táo hoặc nước cốt chanh",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "tạo vị chua thanh"
            },
            {
                "name": "Đường cát",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "tạo vị ngọt"
            },
            {
                "name": "Nước mắm ngon",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "vị mặn đằm"
            },
            {
                "name": "Tương cà (ketchup)",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "tạo màu đỏ đẹp và độ sánh"
            },
            {
                "name": "Tỏi, hành khô băm",
                "quantity": 2,
                "unit": "củ",
                "notes": "phi thơm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế và luộc sơ sườn",
                "description": "Chặt sườn khúc vừa ăn, rửa sạch. Luộc sườn sơ 5 phút với chút muối rồi vớt ra thấm khô nước.",
                "timer_minutes": 8
            },
            {
                "step_number": 2,
                "title": "Rán vàng sườn",
                "description": "Cho sườn vào chảo dầu nóng rán nhanh cho vàng giòn mặt ngoài, vớt ra đĩa để ráo dầu.",
                "timer_minutes": 6
            },
            {
                "step_number": 3,
                "title": "Pha chén nước sốt chua ngọt chuẩn tỉ lệ",
                "description": "Hòa tan 3 muỗng giấm táo, 3 muỗng đường, 2 muỗng nước mắm, 2 muỗng tương cà và 4 muỗng nước lọc.",
                "timer_minutes": 4
            },
            {
                "step_number": 4,
                "title": "Xào sườn ngấm sốt",
                "description": "Phi thơm hành tỏi băm, trút sườn và chén nước sốt vào chảo, đun lửa vừa cho nước sốt ngấm sâu và sánh lại bao quanh từng miếng sườn.",
                "timer_minutes": 10
            },
            {
                "step_number": 5,
                "title": "Thêm ớt chuông hành tây",
                "description": "Cho ớt chuông và hành tây vào đảo thêm 2 phút cho bóng đẹp rồi tắt bếp, múc ra đĩa thưởng thức.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Mực Xào Cần Tỏi Giòn Ngọt",
        "slug": "muc-xao-can-toi-gion-ngot",
        "category_slug": "mon-xao",
        "description": "Mực ống tươi dày mình khứa vảy rồng giòn sần sật, xào cùng cần tây, tỏi tây và cà chua thơm nức mũi, không hề ra nước hay có mùi tanh.",
        "prep_time": 15,
        "cook_time": 12,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 240,
            "protein": 26,
            "carbohydrates": 12,
            "fat": 8,
            "fiber": 2,
            "sodium": 680
        },
        "image_url": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Mực ống tươi",
                "quantity": 500,
                "unit": "gram",
                "notes": "làm sạch túi mực, khứa vảy rồng"
            },
            {
                "name": "Cần tây",
                "quantity": 100,
                "unit": "gram",
                "notes": "cắt khúc 4cm"
            },
            {
                "name": "Tỏi tây (hành boa-rô)",
                "quantity": 1,
                "unit": "cây",
                "notes": "cắt vát xéo"
            },
            {
                "name": "Cà chua",
                "quantity": 2,
                "unit": "quả",
                "notes": "bổ múi cau"
            },
            {
                "name": "Hành tây",
                "quantity": 0.5,
                "unit": "củ",
                "notes": "thái múi cau"
            },
            {
                "name": "Tỏi băm",
                "quantity": 4,
                "unit": "tép",
                "notes": "phi thơm"
            },
            {
                "name": "Gừng tươi",
                "quantity": 1,
                "unit": "nhánh",
                "notes": "đập dập chần mực"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế và khứa mực",
                "description": "Mực rửa sạch với rượu trắng và gừng khử tanh, khứa chéo vảy rồng rồi cắt miếng vừa ăn.",
                "timer_minutes": 8
            },
            {
                "step_number": 2,
                "title": "Chần mực giữ độ giòn",
                "description": "Đun sôi nồi nước có lát gừng, thả mực vào chần nhanh 30 giây rồi vớt ra ngâm ngay vào âu nước đá để mực giòn sần sật.",
                "timer_minutes": 3
            },
            {
                "step_number": 3,
                "title": "Xào mực thơm nức",
                "description": "Phi thơm tỏi băm trên chảo nóng, trút mực vào xào lửa lớn trong 1 phút cùng chút hạt nêm và dầu hào rồi trút ra đĩa.",
                "timer_minutes": 2
            },
            {
                "step_number": 4,
                "title": "Xào rau cần tỏi tây",
                "description": "Dùng lại chảo, phi chút tỏi cho hành tây, cần tây, tỏi tây và cà chua vào đảo nhanh tay trong 2 phút trên lửa to.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Trộn đều và rắc tiêu",
                "description": "Trút mực trở lại chảo đảo đều cùng rau củ trong 1 phút, rắc nhiều tiêu đen rồi tắt bếp trút ra đĩa.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Bò Xào Bông Cải Xanh Tỏi Phi",
        "slug": "bo-xao-bong-cai-xanh-toi-phi",
        "category_slug": "mon-xao",
        "description": "Bông cải xanh mướt giòn ngọt tự nhiên kết hợp cùng thịt bò thăn thái lát mỏng mềm ngậy, dậy mùi tỏi phi vàng rụm thơm lừng.",
        "prep_time": 15,
        "cook_time": 12,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 280,
            "protein": 28,
            "carbohydrates": 14,
            "fat": 12,
            "fiber": 4,
            "sodium": 610
        },
        "image_url": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt thăn bò",
                "quantity": 350,
                "unit": "gram",
                "notes": "thái lát mỏng ngang thớ"
            },
            {
                "name": "Bông cải xanh (súp lơ)",
                "quantity": 400,
                "unit": "gram",
                "notes": "tách nhánh vừa ăn, ngâm muối"
            },
            {
                "name": "Cà rốt",
                "quantity": 0.5,
                "unit": "củ",
                "notes": "tỉa hoa thái mỏng"
            },
            {
                "name": "Tỏi ta",
                "quantity": 1,
                "unit": "củ",
                "notes": "băm nhỏ để phi thơm"
            },
            {
                "name": "Dầu hào",
                "quantity": 1.5,
                "unit": "muỗng canh",
                "notes": "tạo vị đậm"
            },
            {
                "name": "Dầu mè",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "tạo hương thơm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Ướp thịt bò",
                "description": "Ướp bò với 1 muỗng dầu hào, 1/2 muỗng hạt nêm, tiêu xay và 1 muỗng dầu ăn trong 15 phút.",
                "timer_minutes": 15
            },
            {
                "step_number": 2,
                "title": "Chần bông cải xanh",
                "description": "Chần bông cải và cà rốt qua nước sôi có chút muối trong 1 phút rồi ngâm nước lạnh để giữ màu xanh mướt.",
                "timer_minutes": 3
            },
            {
                "step_number": 3,
                "title": "Xào thịt bò tái chín",
                "description": "Phi thơm một nửa tỏi băm, xào thịt bò trên lửa lớn trong 2 phút đến khi chín tới thì trút riêng ra đĩa.",
                "timer_minutes": 3
            },
            {
                "step_number": 4,
                "title": "Xào bông cải giòn ngọt",
                "description": "Phi phần tỏi còn lại, cho bông cải và cà rốt vào xào nhanh 2 phút với chút gia vị.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Kết hợp và thưởng thức",
                "description": "Trút thịt bò vào đảo cùng bông cải 30 giây, rưới dầu mè và rắc tiêu, dọn ra đĩa ăn nóng.",
                "timer_minutes": 1
            }
        ]
    },
    {
        "title": "Ếch Xào Lăn Nước Cốt Dừa",
        "slug": "ech-xao-lan-nuoc-cot-dua",
        "category_slug": "mon-xao",
        "description": "Thịt ếch đồng săn chắc ngọt đậm, quyện trong sốt cà ri vàng óng, nước cốt dừa béo ngậy thơm lừng mùi sả ớt và đậu phộng rang giòn.",
        "prep_time": 20,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 410,
            "protein": 32,
            "carbohydrates": 16,
            "fat": 24,
            "fiber": 2,
            "sodium": 740
        },
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt ếch đồng làm sạch",
                "quantity": 500,
                "unit": "gram",
                "notes": "chặt miếng vừa ăn"
            },
            {
                "name": "Nước cốt dừa",
                "quantity": 150,
                "unit": "ml",
                "notes": "loại sánh béo nguyên chất"
            },
            {
                "name": "Bột cà ri",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "tạo màu và hương thơm"
            },
            {
                "name": "Sả băm và sả cắt khúc",
                "quantity": 3,
                "unit": "cây",
                "notes": "dậy mùi thơm"
            },
            {
                "name": "Hành tây",
                "quantity": 1,
                "unit": "củ",
                "notes": "thái múi cau"
            },
            {
                "name": "Nấm mèo (mộc nhĩ)",
                "quantity": 20,
                "unit": "gram",
                "notes": "ngâm nở cắt miếng"
            },
            {
                "name": "Đậu phộng rang giã dập",
                "quantity": 30,
                "unit": "gram",
                "notes": "rắc lên bề mặt"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Ướp thịt ếch đậm đà",
                "description": "Ướp ếch với bột cà ri, sả băm, tỏi băm, 1 muỗng hạt nêm, 1 muỗng đường và chút nước mắm trong 20 phút.",
                "timer_minutes": 20
            },
            {
                "step_number": 2,
                "title": "Xào săn thịt ếch",
                "description": "Phi thơm sả tỏi và ớt, cho thịt ếch vào xào săn chắc trên lửa lớn trong 5 phút.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Nấu cùng nước cốt dừa",
                "description": "Đổ nước cốt dừa vào nồi ếch, đun sôi nhẹ hạ lửa om trong 8 phút cho thịt ếch ngấm vị béo bùi.",
                "timer_minutes": 8
            },
            {
                "step_number": 4,
                "title": "Cho nấm mèo và hành tây",
                "description": "Thêm nấm mèo và hành tây vào đảo thêm 3 phút cho hành tây chín tới.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Thành phẩm",
                "description": "Múc ra đĩa sâu lòng, rắc đậu phộng rang và rau om lên trên. Dùng kèm bánh mì hoặc bún tươi.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Miến Xào Cua Tay Cầm",
        "slug": "mien-xao-cua-tay-cam",
        "category_slug": "mon-xao",
        "description": "Từng sợi miến dong tơi mềm ngấm trọn vị ngọt thanh từ thịt cua biển tươi, xào cùng mộc nhĩ, cà rốt và cần tây giòn rụm thơm ngon nức tiếng.",
        "prep_time": 25,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 380,
            "protein": 24,
            "carbohydrates": 46,
            "fat": 12,
            "fiber": 3,
            "sodium": 670
        },
        "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt cua biển hấp gỡ sẵn",
                "quantity": 200,
                "unit": "gram",
                "notes": "giữ nguyên thớ thịt ngọt"
            },
            {
                "name": "Miến dong cao cấp",
                "quantity": 200,
                "unit": "gram",
                "notes": "ngâm nước ấm 10 phút, cắt khúc"
            },
            {
                "name": "Cà rốt thái sợi",
                "quantity": 1,
                "unit": "củ",
                "notes": "thái chỉ mỏng"
            },
            {
                "name": "Cần tây",
                "quantity": 50,
                "unit": "gram",
                "notes": "rửa sạch cắt khúc"
            },
            {
                "name": "Mộc nhĩ",
                "quantity": 20,
                "unit": "gram",
                "notes": "thái sợi chỉ"
            },
            {
                "name": "Hành tím băm",
                "quantity": 2,
                "unit": "củ",
                "notes": "phi thơm thịt cua"
            },
            {
                "name": "Dầu hào, nước tương",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "nêm vị miến"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế và ướp miến",
                "description": "Trộn miến đã ngâm mềm với 1 muỗng dầu ăn và 1 lòng đỏ trứng hoặc chút nước tương để sợi miến tơi không bị dính nát khi xào.",
                "timer_minutes": 8
            },
            {
                "step_number": 2,
                "title": "Xào thơm thịt cua",
                "description": "Phi thơm hành tím, cho thịt cua vào xào nhanh cùng chút tiêu xay trong 2 phút rồi trút ra đĩa.",
                "timer_minutes": 3
            },
            {
                "step_number": 3,
                "title": "Xào rau củ",
                "description": "Cho cà rốt, mộc nhĩ và cần tây vào chảo xào chín tới trong 3 phút.",
                "timer_minutes": 3
            },
            {
                "step_number": 4,
                "title": "Xào miến tơi sợi",
                "description": "Trút miến vào đảo đều tay trên lửa vừa, rưới nước sốt dầu hào xì dầu đảo cho miến chín trong suốt và ngấm đều gia vị.",
                "timer_minutes": 5
            },
            {
                "step_number": 5,
                "title": "Kết hợp và dọn món",
                "description": "Trút thịt cua và rau củ vào đảo đều cùng miến trong 1 phút, rắc tiêu xay và hành phi thơm lừng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Cánh Gà Chiên Nước Mắm Tỏi Ớt",
        "slug": "canh-ga-chien-nuoc-mam-toi-ot",
        "category_slug": "mon-chien-ran",
        "description": "Cánh gà chiên lớp da vàng ươm giòn rụm bên ngoài, thịt bên trong mềm ngọt mọng nước, áo đều lớp sốt nước mắm tỏi ớt kẹo dẻo mặn ngọt gây nghiện.",
        "prep_time": 20,
        "cook_time": 25,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 480,
            "protein": 34,
            "carbohydrates": 14,
            "fat": 32,
            "fiber": 1,
            "sodium": 840
        },
        "image_url": "https://images.unsplash.com/photo-1562967914-608f82629710?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Cánh gà khúc giữa",
                "quantity": 600,
                "unit": "gram",
                "notes": "rửa sạch, khứa nhẹ mặt trong"
            },
            {
                "name": "Tỏi băm nhỏ",
                "quantity": 2,
                "unit": "củ",
                "notes": "phi thơm lấy cả tỏi phi"
            },
            {
                "name": "Ớt hiểm đỏ băm",
                "quantity": 2,
                "unit": "trái",
                "notes": "tùy độ cay"
            },
            {
                "name": "Nước mắm ngon",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "đậm đà"
            },
            {
                "name": "Đường cát",
                "quantity": 2.5,
                "unit": "muỗng canh",
                "notes": "tạo độ sánh keo"
            },
            {
                "name": "Bột bắp hoặc bột chiên giòn",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "áo mỏng mặt da gà"
            },
            {
                "name": "Dầu ăn",
                "quantity": 300,
                "unit": "ml",
                "notes": "chiên giòn cánh gà"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế cánh gà",
                "description": "Cánh gà rửa nước muối và gừng, để thật ráo nước. Áo đều một lớp bột bắp mỏng quanh cánh gà để khi chiên da giòn rụm không bắn dầu.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Chiên cánh gà vàng giòn 2 lần",
                "description": "Đun nóng dầu ăn, thả cánh gà vào chiên lửa vừa trong 12 phút đến khi chín vàng đều, vớt ra để ráo dầu.",
                "timer_minutes": 15
            },
            {
                "step_number": 3,
                "title": "Làm sốt nước mắm tỏi ớt kẹo dẻo",
                "description": "Khuấy tan nước mắm, đường, chút tương ớt và 2 muỗng nước ấm trong một chiếc chén.",
                "timer_minutes": 3
            },
            {
                "step_number": 4,
                "title": "Áo sốt nước mắm quanh cánh gà",
                "description": "Phi thơm tỏi ớt trong chảo, đổ chén sốt vào đun sôi sủi bọt sánh lại. Trút toàn bộ cánh gà vào đảo nhanh tay cho sốt bám đều óng ánh.",
                "timer_minutes": 4
            },
            {
                "step_number": 5,
                "title": "Trình bày món ăn",
                "description": "Bày cánh gà ra đĩa ăn kèm dưa leo, cà chua và rau răm, dùng ngay khi còn giòn nóng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Nem Rán Hà Nội Giòn Rụm",
        "slug": "nem-ran-ha-noi-gion-rum",
        "category_slug": "mon-chien-ran",
        "description": "Chiếc nem rán truyền thống đất kinh kỳ với lớp vỏ bánh đa nem giòn rụm vàng ươm, nhân thịt nạc vai thơm lừng nấm hương, mộc nhĩ, miến dong, củ đậu và trứng gà.",
        "prep_time": 30,
        "cook_time": 30,
        "servings": 6,
        "difficulty": 2,
        "nutrition": {
            "calories": 380,
            "protein": 22,
            "carbohydrates": 26,
            "fat": 22,
            "fiber": 3,
            "sodium": 690
        },
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt nạc dăm xay",
                "quantity": 400,
                "unit": "gram",
                "notes": "chọn loại có chút mỡ"
            },
            {
                "name": "Tôm tươi băm nhỏ",
                "quantity": 150,
                "unit": "gram",
                "notes": "tăng độ ngọt cho nem"
            },
            {
                "name": "Bánh đa nem (vỏ ram)",
                "quantity": 30,
                "unit": "lá",
                "notes": "loại phơi sương giòn lâu"
            },
            {
                "name": "Trứng gà",
                "quantity": 2,
                "unit": "quả",
                "notes": "chỉ dùng lòng đỏ hoặc 1 quả nguyên"
            },
            {
                "name": "Miến dong, mộc nhĩ, nấm hương",
                "quantity": 60,
                "unit": "gram",
                "notes": "ngâm nở băm nhỏ"
            },
            {
                "name": "Cà rốt, củ đậu",
                "quantity": 100,
                "unit": "gram",
                "notes": "thái sợi chỉ vắt ráo nước"
            },
            {
                "name": "Hành lá, rau mùi",
                "quantity": 40,
                "unit": "gram",
                "notes": "rửa sạch thái nhỏ"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Chuẩn bị nhân nem",
                "description": "Trộn đều thịt xay, tôm, miến, mộc nhĩ, nấm hương, cà rốt, củ đậu và hành mùi cùng hạt tiêu và chút hạt nêm. Cho trứng gà vào trộn vừa độ ẩm.",
                "timer_minutes": 15
            },
            {
                "step_number": 2,
                "title": "Gói nem đều tay",
                "description": "Trải bánh đa nem ra mặt phẳng, cho lượng nhân vừa phải vào cuốn tròn đều tay, gấp hai mép lại thật gọn gàng.",
                "timer_minutes": 15
            },
            {
                "step_number": 3,
                "title": "Rán nem lần 1 (chín sơ)",
                "description": "Đun nóng dầu ăn ngập nửa chiếc nem, thả nem vào rán lửa vừa cho chín se mặt ngoài rồi vớt ra giấy thấm dầu.",
                "timer_minutes": 12
            },
            {
                "step_number": 4,
                "title": "Rán nem lần 2 (giòn rụm)",
                "description": "Trước khi ăn, đun sôi dầu rồi cho nem vào chiên nhanh ở lửa lớn 3-4 phút cho vỏ vàng ruộm và giòn tan.",
                "timer_minutes": 5
            },
            {
                "step_number": 5,
                "title": "Pha nước chấm nem chua ngọt",
                "description": "Pha nước mắm, đường, giấm, nước lọc theo tỉ lệ 1:1:1:5, thêm tỏi ớt băm nổi trên mặt, dưa góp đu đủ cà rốt ăn kèm.",
                "timer_minutes": 5
            }
        ]
    },
    {
        "title": "Tôm Lăn Bột Chiên Xù Giòn Tan",
        "slug": "tom-lan-bot-chien-xu-gion-tan",
        "category_slug": "mon-chien-ran",
        "description": "Tôm sú tươi lột vỏ để lại đuôi đẹp mắt, lăn qua lớp bột chiên giòn và bột chiên xù xốp nhẹ, rán vàng ruộm chấm sốt mayonnaise tương ớt thơm béo.",
        "prep_time": 15,
        "cook_time": 15,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 350,
            "protein": 24,
            "carbohydrates": 28,
            "fat": 18,
            "fiber": 1,
            "sodium": 560
        },
        "image_url": "https://images.unsplash.com/photo-1562967914-608f82629710?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Tôm sú tươi",
                "quantity": 400,
                "unit": "gram",
                "notes": "bóc vỏ chừa đuôi, rút chỉ đen"
            },
            {
                "name": "Bột chiên giòn",
                "quantity": 100,
                "unit": "gram",
                "notes": "hòa với nước sệt"
            },
            {
                "name": "Bột chiên xù",
                "quantity": 150,
                "unit": "gram",
                "notes": "đổ ra đĩa rộng"
            },
            {
                "name": "Trứng gà",
                "quantity": 1,
                "unit": "quả",
                "notes": "đánh tan cùng bột giòn"
            },
            {
                "name": "Hạt tiêu, muối",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "ướp tôm sơ"
            },
            {
                "name": "Sốt mayonnaise, tương ớt",
                "quantity": 50,
                "unit": "gram",
                "notes": "chấm kèm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế và ướp tôm",
                "description": "Tôm lột vỏ chừa đuôi, dùng dao khía nhẹ bụng tôm để tôm thẳng đẹp khi chiên. Ướp tôm với chút muối tiêu trong 10 phút.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Lăn bột tuần tự",
                "description": "Cầm đuôi tôm nhúng qua bát bột chiên giòn pha trứng, sau đó lăn đều qua lớp bột chiên xù cho bột bám kín thân tôm.",
                "timer_minutes": 8
            },
            {
                "step_number": 3,
                "title": "Chiên tôm vàng giòn",
                "description": "Thả từng con tôm vào chảo dầu sôi ngập, chiên lửa vừa khoảng 3-4 phút đến khi lớp vỏ phồng xốp vàng rụm thì vớt ra.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Thấm ráo dầu",
                "description": "Đặt tôm lên khay ráo dầu hoặc đĩa lót giấy thấm dầu ăn.",
                "timer_minutes": 2
            },
            {
                "step_number": 5,
                "title": "Trình bày và thưởng thức",
                "description": "Xếp tôm xòe hình cánh quạt, chấm kèm sốt tương ớt pha mayonnaise béo ngậy.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Cá Tai Tượng Chiên Xù Miền Tây",
        "slug": "ca-tai-tuong-chien-xu-mien-tay",
        "category_slug": "mon-chien-ran",
        "description": "Đặc sản sông nước Nam Bộ với nguyên con cá tai tượng chiên xòe vây giòn rụm dựng đứng, thịt cá trắng ngọt thanh cuộn bánh tráng rau rừng chấm mắm nêm đậm đà.",
        "prep_time": 20,
        "cook_time": 25,
        "servings": 4,
        "difficulty": 3,
        "nutrition": {
            "calories": 420,
            "protein": 35,
            "carbohydrates": 18,
            "fat": 24,
            "fiber": 3,
            "sodium": 680
        },
        "image_url": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Cá tai tượng sống",
                "quantity": 1000,
                "unit": "gram",
                "notes": "để nguyên vảy, làm sạch ruột mang"
            },
            {
                "name": "Bánh tráng phơi sương",
                "quantity": 1,
                "unit": "xấp",
                "notes": "dùng để cuốn cá"
            },
            {
                "name": "Rau thơm, chuối chát, khế chua",
                "quantity": 200,
                "unit": "gram",
                "notes": "rửa sạch thái lát mỏng"
            },
            {
                "name": "Bún tươi",
                "quantity": 300,
                "unit": "gram",
                "notes": "ăn kèm cuốn"
            },
            {
                "name": "Mắm nêm pha sẵn thơm tỏi ớt",
                "quantity": 150,
                "unit": "ml",
                "notes": "nước chấm đặc trưng"
            },
            {
                "name": "Dầu ăn",
                "quantity": 1000,
                "unit": "ml",
                "notes": "chiên cá ngập dầu"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế cá tai tượng giữ vảy",
                "description": "Cá mổ bụng bỏ ruột mang, rửa thật sạch và lau thật khô ráo cả trong lẫn ngoài thân cá.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Đun dầu nóng già",
                "description": "Cho nhiều dầu vào chảo sâu lòng đun nóng già. Dùng vá múc dầu sôi xối liên tục lên mình cá.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Chiên xù vây và vảy cá",
                "description": "Hạ cá vào chảo dầu chiên giòn, múc dầu sôi rưới đều hai bên thân cá để từng chiếc vảy xòe bung giòn rụm trong 15 phút.",
                "timer_minutes": 15
            },
            {
                "step_number": 4,
                "title": "Vớt cá dựng đứng trên giá",
                "description": "Cá chín vàng ruộm vớt ra khay có giá dựng đứng hình sống lưng cá để róc hết dầu thừa.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Thưởng thức phong cách miền Tây",
                "description": "Gắp miếng thịt cá giòn rụm cuộn cùng bánh tráng, bún tươi, chuối khế và rau sống, chấm đẫm mắm nêm chua ngọt.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Chả Giò Hải Sản Sốt Mayonnaise",
        "slug": "cha-gio-hai-san-sot-mayonnaise",
        "category_slug": "mon-chien-ran",
        "description": "Từng cuốn chả giò nhân tôm mực tươi béo ngậy sốt mayonnaise bên trong, bọc ngoài lớp bánh tráng xốp giòn tan vỡ vụn trong khoang miệng khi cắn.",
        "prep_time": 25,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 420,
            "protein": 20,
            "carbohydrates": 28,
            "fat": 26,
            "fiber": 2,
            "sodium": 610
        },
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Tôm sú tươi lột vỏ băm nhỏ",
                "quantity": 200,
                "unit": "gram",
                "notes": "tươi giòn"
            },
            {
                "name": "Mực ống băm nhỏ",
                "quantity": 150,
                "unit": "gram",
                "notes": "lau khô trước khi băm"
            },
            {
                "name": "Sốt mayonnaise",
                "quantity": 4,
                "unit": "muỗng canh",
                "notes": "trộn cùng nhân tạo độ ngậy mềm"
            },
            {
                "name": "Cà rốt băm hạt lựu",
                "quantity": 50,
                "unit": "gram",
                "notes": "thấm khô"
            },
            {
                "name": "Hành tây băm hạt lựu",
                "quantity": 50,
                "unit": "gram",
                "notes": "vắt ráo nước"
            },
            {
                "name": "Bánh tráng bò bía xốp",
                "quantity": 20,
                "unit": "lá",
                "notes": "loại cuốn chả giò hải sản"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Xào sơ nhân hải sản",
                "description": "Xào tôm mực cà rốt hành tây trên lửa lớn cho vừa chín tới và cạn hết nước, để thật nguội.",
                "timer_minutes": 5
            },
            {
                "step_number": 2,
                "title": "Trộn sốt mayonnaise vào nhân",
                "description": "Trút sốt mayonnaise và chút tiêu vào âu nhân hải sản đã nguội, trộn đều nhẹ tay.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Cuốn chả giò",
                "description": "Múc nhân đặt vào lá bò bía, cuốn chặt tay vừa phải, dán mép bằng chút lòng trắng trứng.",
                "timer_minutes": 10
            },
            {
                "step_number": 4,
                "title": "Chiên giòn chả giò",
                "description": "Chiên trong dầu sôi lửa vừa khoảng 5-6 phút đến khi vỏ ngoài vàng xốp giòn rụm.",
                "timer_minutes": 6
            },
            {
                "step_number": 5,
                "title": "Thưởng thức",
                "description": "Gắp ra đĩa lót giấy thấm dầu, ăn kèm xà lách và tương xí muội chua ngọt.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Gà Nướng Muối Ớt Da Giòn",
        "slug": "ga-nuong-muoi-ot-da-gion",
        "category_slug": "mon-nuong",
        "description": "Gà thả vườn nướng than hoa hoặc nồi chiên không dầu với lớp da giòn rụm vàng ươm, cay cay thơm nồng vị muối hột và ớt hiểm đỏ, thịt ngọt mọng nước.",
        "prep_time": 25,
        "cook_time": 45,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 460,
            "protein": 38,
            "carbohydrates": 8,
            "fat": 30,
            "fiber": 1,
            "sodium": 820
        },
        "image_url": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Gà ta nguyên con",
                "quantity": 1300,
                "unit": "gram",
                "notes": "mổ phanh hình cánh bướm"
            },
            {
                "name": "Muối hạt",
                "quantity": 1.5,
                "unit": "muỗng canh",
                "notes": "giã nhuyễn cùng ớt"
            },
            {
                "name": "Ớt sừng và ớt hiểm",
                "quantity": 4,
                "unit": "trái",
                "notes": "tạo vị cay nồng và màu đẹp"
            },
            {
                "name": "Tỏi, hành khô",
                "quantity": 1,
                "unit": "củ",
                "notes": "ép lấy nước cốt ướp"
            },
            {
                "name": "Dầu màu điều",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "quết da cho vàng óng"
            },
            {
                "name": "Mật ong nguyên chất",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "quết da lần cuối"
            },
            {
                "name": "Lá chanh tươi",
                "quantity": 10,
                "unit": "lá",
                "notes": "thái chỉ mỏng"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế gà mổ phanh",
                "description": "Gà làm sạch, chặt phanh sống lưng ép phẳng, khía nhẹ mặt trong để ngấm đều sốt ướp.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Giã muối ớt và ướp gà",
                "description": "Giã nhuyễn muối hạt, ớt sừng, ớt hiểm, nước cốt hành tỏi và dầu điều. Thoa đều lên khắp thân gà (tránh quết mật ong lên da sớm kẻo cháy). Ướp 40 phút.",
                "timer_minutes": 40
            },
            {
                "step_number": 3,
                "title": "Nướng gà giai đoạn 1",
                "description": "Nướng than hoa hoặc nồi chiên không dầu ở nhiệt độ 175°C trong 25 phút cho gà chín đều bên trong.",
                "timer_minutes": 25
            },
            {
                "step_number": 4,
                "title": "Quết sốt mật ong nướng giòn da",
                "description": "Trộn mật ong với chút dầu điều, quét đều lên bề mặt da gà. Tăng nhiệt độ lên 200°C nướng thêm 10 phút cho da phồng rộp vàng giòn.",
                "timer_minutes": 10
            },
            {
                "step_number": 5,
                "title": "Chặt gà và chấm muối ớt chanh",
                "description": "Chặt gà thành miếng vừa ăn bày ra mẹt lót lá chuối, rắc lá chanh thái chỉ, chấm muối tiêu chanh ớt hiểm.",
                "timer_minutes": 5
            }
        ]
    },
    {
        "title": "Bò Nướng Lá Lốt Thơm Lừng",
        "slug": "bo-nuong-la-lot-thom-lung",
        "category_slug": "mon-nuong",
        "description": "Từng cuốn bò nướng lá lốt xèo xèo trên bếp than hồng, tỏa hương thơm quyến rũ nức mũi, thịt bò mềm ngọt quyện mỡ chài béo ngậy chấm mắm nêm đậm đà.",
        "prep_time": 30,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 410,
            "protein": 32,
            "carbohydrates": 14,
            "fat": 26,
            "fiber": 3,
            "sodium": 710
        },
        "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt bò thăn xay",
                "quantity": 350,
                "unit": "gram",
                "notes": "xay nhuyễn"
            },
            {
                "name": "Thịt ba chỉ heo xay",
                "quantity": 150,
                "unit": "gram",
                "notes": "giữ độ ẩm béo cho cuốn bò"
            },
            {
                "name": "Lá lốt tươi bánh tẻ",
                "quantity": 40,
                "unit": "lá",
                "notes": "chọn lá to lành lặn, rửa sạch lau khô"
            },
            {
                "name": "Sả băm nhuyễn",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "dậy mùi thơm nồng"
            },
            {
                "name": "Hành tím băm, tỏi băm",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "ướp thịt"
            },
            {
                "name": "Đậu phộng rang",
                "quantity": 40,
                "unit": "gram",
                "notes": "giã dập rắc mặt"
            },
            {
                "name": "Mỡ hành",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "rưới lên cuốn bò khi chín"
            },
            {
                "name": "Bánh hỏi, bánh tráng, rau sống",
                "quantity": 1,
                "unit": "phần",
                "notes": "ăn kèm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Trộn nhân thịt bò lá lốt",
                "description": "Trộn đều thịt bò, thịt heo, sả băm, tỏi hành băm, vài lá lốt băm nhỏ, dầu hào, tiêu và hạt nêm. Ướp trong 20 phút.",
                "timer_minutes": 20
            },
            {
                "step_number": 2,
                "title": "Cuốn bò lá lốt",
                "description": "Đặt mặt trái lá lốt lên thớt, múc một muỗng nhân thịt cho vào giữa rồi cuộn tròn chặt tay, dùng cuống lá găm lại giữ nếp.",
                "timer_minutes": 15
            },
            {
                "step_number": 3,
                "title": "Nướng trên than hoa hoặc vỉ nướng",
                "description": "Xếp cuốn bò lên vỉ, phết chút dầu ăn lên mặt lá lốt để không bị khô. Nướng lật mặt đều tay trong 10-12 phút đến khi lá lốt sém cạnh dậy mùi thơm ngát.",
                "timer_minutes": 12
            },
            {
                "step_number": 4,
                "title": "Rưới mỡ hành đậu phộng",
                "description": "Xếp các cuốn bò nướng ra đĩa, rưới đều mỡ hành óng ả và rắc đậu phộng rang giòn lên trên.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Thưởng thức",
                "description": "Cuốn cùng bánh tráng, bánh hỏi và các loại rau rừng, chấm ngập chén mắm nêm thơm cay.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Sườn Heo Nướng Mật Ong Than Hoa",
        "slug": "suon-heo-nuong-mat-ong-than-hoa",
        "category_slug": "mon-nuong",
        "description": "Từng dẻ sườn cây nướng than hoa vàng rực óng ánh men mật ong, thịt sườn thơm ngọt mềm ngậy róc xương đậm đà hương vị BBQ.",
        "prep_time": 25,
        "cook_time": 35,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 490,
            "protein": 34,
            "carbohydrates": 16,
            "fat": 32,
            "fiber": 1,
            "sodium": 780
        },
        "image_url": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Sườn cây nguyên dẻ",
                "quantity": 800,
                "unit": "gram",
                "notes": "lột bỏ màng trắng phía sau sườn"
            },
            {
                "name": "Mật ong rừng",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "tạo độ bóng và vị ngọt"
            },
            {
                "name": "Dầu hào cao cấp",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "vị mặn đằm"
            },
            {
                "name": "Tương cà, tương ớt",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "tạo màu đẹp"
            },
            {
                "name": "Tỏi, hành khô giã nhuyễn",
                "quantity": 3,
                "unit": "củ",
                "notes": "vắt lấy nước cốt"
            },
            {
                "name": "Tiêu đen xay",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "thơm nồng"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Làm sạch và khía sườn",
                "description": "Sườn rửa sạch lau khô, lột màng mỏng mặt sau dẻ sườn để thịt ngấm sốt mềm rục.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Pha sốt ướp mật ong đậm vị",
                "description": "Trộn mật ong, dầu hào, tương cà, tương ớt, nước cốt hành tỏi và tiêu đen. Thoa đều 2 mặt sườn ướp 1 tiếng.",
                "timer_minutes": 60
            },
            {
                "step_number": 3,
                "title": "Nướng sườn đợt đầu",
                "description": "Xếp sườn lên vỉ than hoa hoặc lò nướng 180°C nướng trong 25 phút đến khi thịt chín đều.",
                "timer_minutes": 25
            },
            {
                "step_number": 4,
                "title": "Quết men mật ong vàng bóng",
                "description": "Quét nước sốt ướp pha thêm mật ong lên mặt sườn, nướng thêm 8 phút cho sườn lên màu cánh gián óng ả.",
                "timer_minutes": 8
            },
            {
                "step_number": 5,
                "title": "Cắt dẻ sườn và thưởng thức",
                "description": "Cắt sườn theo từng dẻ xương, ăn kèm kim chi hoặc salad bắp cải giòn giòn.",
                "timer_minutes": 3
            }
        ]
    },
    {
        "title": "Thịt Ba Chỉ Nướng Riềng Mẻ",
        "slug": "thit-ba-chi-nuong-rieng-me",
        "category_slug": "mon-nuong",
        "description": "Vị chua thanh dịu của mẻ hòa quyện cùng mùi thơm nồng nàn của củ riềng già giã nhỏ và mắm tôm nguyên chất, từng miếng ba chỉ cháy cạnh giòn ngọt đê mê.",
        "prep_time": 20,
        "cook_time": 25,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 470,
            "protein": 26,
            "carbohydrates": 10,
            "fat": 36,
            "fiber": 1,
            "sodium": 820
        },
        "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt ba chỉ heo",
                "quantity": 600,
                "unit": "gram",
                "notes": "thái lát dày 0.7cm"
            },
            {
                "name": "Riềng già giã nhuyễn",
                "quantity": 70,
                "unit": "gram",
                "notes": "tạo hương vị đặc trưng"
            },
            {
                "name": "Cơm mẻ ngấu",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "lọc lấy nước cốt chua thanh"
            },
            {
                "name": "Mắm tôm Bắc",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "linh hồn món nướng riềng mẻ"
            },
            {
                "name": "Bột nghệ hoặc nghệ tươi",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "tạo màu vàng tươi"
            },
            {
                "name": "Hành tím băm",
                "quantity": 2,
                "unit": "củ",
                "notes": "phi thơm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế thịt ba chỉ",
                "description": "Thịt rửa sạch, thái lát dày bản khoảng 0.7cm để khi nướng không bị teo khô.",
                "timer_minutes": 8
            },
            {
                "step_number": 2,
                "title": "Ướp riềng mẻ mắm tôm",
                "description": "Trộn riềng giã nhỏ, nước mẻ, mắm tôm, nghệ, hành tím, 1 muỗng đường và chút dầu ăn. Ướp thịt 30 phút.",
                "timer_minutes": 30
            },
            {
                "step_number": 3,
                "title": "Kẹp vỉ nướng than",
                "description": "Xếp thịt dàn đều trên vỉ nướng, kẹp chặt lại.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Nướng thịt cháy cạnh",
                "description": "Nướng trên bếp than hoa đỏ rực, lật vỉ liên tục trong 15-18 phút cho thịt chín vàng thơm nức và hơi xém cạnh.",
                "timer_minutes": 18
            },
            {
                "step_number": 5,
                "title": "Trình bày",
                "description": "Gỡ thịt nướng ra đĩa, cuốn cùng lá mơ lông, rau ngổ, húng quế và chấm nước mắm tỏi ớt.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Tôm Sú Nướng Sa Tế Muối Ớt",
        "slug": "tom-su-nuong-sa-te-muoi-ot",
        "category_slug": "mon-nuong",
        "description": "Tôm sú biển to tươi rói nguyên vỏ, nướng đỏ au phủ đều lớp sốt sa tế muối ớt cay nồng thơm phức mùi sả tỏi, vị ngọt đậm tự nhiên của thịt tôm bùng nổ.",
        "prep_time": 15,
        "cook_time": 15,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 260,
            "protein": 28,
            "carbohydrates": 8,
            "fat": 12,
            "fiber": 1,
            "sodium": 740
        },
        "image_url": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Tôm sú tươi lớn",
                "quantity": 500,
                "unit": "gram",
                "notes": "cắt bớt râu chân, rút chỉ lưng"
            },
            {
                "name": "Sa tế tôm",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "tạo vị cay nồng óng đỏ"
            },
            {
                "name": "Muối hạt giã nhuyễn",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "vị mặn đằm"
            },
            {
                "name": "Ớt bột hoặc ớt hiểm",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "tăng độ cay"
            },
            {
                "name": "Tỏi băm, sả băm",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "phi thơm làm sốt"
            },
            {
                "name": "Xiên tre",
                "quantity": 12,
                "unit": "que",
                "notes": "ngâm nước trước khi xiên"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Làm sạch và xiên tôm",
                "description": "Tôm rửa sạch, dùng tăm rút chỉ đen ở sống lưng. Dùng que tre xiên thẳng từ đuôi lên đầu tôm.",
                "timer_minutes": 8
            },
            {
                "step_number": 2,
                "title": "Làm sốt sa tế ướp",
                "description": "Trộn sa tế tôm, muối giã nhuyễn, tỏi băm, sả băm, 1 muỗng mật ong và 1 muỗng dầu ăn.",
                "timer_minutes": 3
            },
            {
                "step_number": 3,
                "title": "Ướp tôm ngấm vị",
                "description": "Quét đều sốt sa tế lên vỏ tôm, ướp trong 15 phút.",
                "timer_minutes": 15
            },
            {
                "step_number": 4,
                "title": "Nướng tôm đỏ au",
                "description": "Nướng trên than hoa khoảng 8-10 phút, trở đều tay đến khi vỏ tôm chuyển màu đỏ au và thơm lừng.",
                "timer_minutes": 10
            },
            {
                "step_number": 5,
                "title": "Thưởng thức",
                "description": "Bày tôm nướng ra đĩa, ăn nóng chấm muối tiêu chanh hoặc muối ớt xanh thơm lừng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Gà Hấp Lá Chanh Vàng Óng",
        "slug": "ga-hap-la-chanh-vang-ong",
        "category_slug": "mon-hap",
        "description": "Thịt gà ta hấp cách thủy giữ nguyên vị ngọt đậm đà tự nhiên, da vàng óng mỡ màng giòn sần sật, thoang thoảng mùi thơm thanh mát của lá chanh tươi vườn nhà.",
        "prep_time": 20,
        "cook_time": 35,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 380,
            "protein": 36,
            "carbohydrates": 4,
            "fat": 24,
            "fiber": 1,
            "sodium": 620
        },
        "image_url": "https://images.unsplash.com/photo-1541544741938-0af808871cc0?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Gà ta thả vườn",
                "quantity": 1400,
                "unit": "gram",
                "notes": "chọn gà mái tơ da vàng ươm"
            },
            {
                "name": "Lá chanh bánh tẻ",
                "quantity": 25,
                "unit": "lá",
                "notes": "rửa sạch, 1/2 lót đáy, 1/2 thái chỉ"
            },
            {
                "name": "Gừng tươi",
                "quantity": 1,
                "unit": "củ",
                "notes": "thái lát mỏng"
            },
            {
                "name": "Hành tím",
                "quantity": 3,
                "unit": "củ",
                "notes": "đập dập nhồi bụng gà"
            },
            {
                "name": "Bột nghệ hoặc củ nghệ tươi",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "quết da lấy màu vàng óng"
            },
            {
                "name": "Muối hạt, tiêu sọ",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "ướp trong ngoài gà"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Khử mùi và quết màu gà",
                "description": "Gà chà xát với muối gừng khử sạch mùi, rửa ráo. Hòa chút bột nghệ với dầu ăn quết mỏng lên khắp da gà để sau khi hấp da lên màu vàng ươm bóng mượt.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Nhồi bụng gà gia vị thơm",
                "description": "Xoa muối tiêu vào khoang bụng gà, nhồi hành tím đập dập, gừng lát và một nửa lượng lá chanh vò nát.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Hấp cách thủy giữ trọn vị ngọt",
                "description": "Lót lớp lá chanh dưới xửng hấp, đặt gà lên trên. Đun sôi nước rồi hạ lửa vừa đậy kín nắp hấp trong 30-35 phút đến khi dùng tăm xiên đùi không thấy nước đỏ chảy ra.",
                "timer_minutes": 35
            },
            {
                "step_number": 4,
                "title": "Ủ gà và thái miếng",
                "description": "Tắt bếp ủ gà trong nồi 5 phút cho da se lại giòn ngon, vớt gà ra để nguội bớt rồi chặt miếng vuông vức vừa ăn.",
                "timer_minutes": 10
            },
            {
                "step_number": 5,
                "title": "Rắc lá chanh và pha muối tiêu",
                "description": "Xếp gà ra đĩa da quay lên trên, rắc lá chanh thái sợi chỉ mỏng như sợi tơ. Chấm cùng muối tiêu chanh ớt hiểm bùng nổ hương vị.",
                "timer_minutes": 3
            }
        ]
    },
    {
        "title": "Mực Trứng Hấp Gừng Sả Tươi Giòn",
        "slug": "muc-trung-hap-gung-sa-tuoi-gion",
        "category_slug": "mon-hap",
        "description": "Mực trứng tươi sống hấp chín tới căng tròn đầy ắp trứng bùi béo, thịt mực giòn ngọt sần sật nức mùi gừng già và sả đập dập chấm muối ớt xanh.",
        "prep_time": 15,
        "cook_time": 12,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 210,
            "protein": 26,
            "carbohydrates": 6,
            "fat": 8,
            "fiber": 1,
            "sodium": 580
        },
        "image_url": "https://images.unsplash.com/photo-1541544741938-0af808871cc0?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Mực trứng tươi sống",
                "quantity": 600,
                "unit": "gram",
                "notes": "chọn con căng tròn đầy ắp trứng"
            },
            {
                "name": "Gừng tươi",
                "quantity": 50,
                "unit": "gram",
                "notes": "thái chỉ mỏng"
            },
            {
                "name": "Sả cây",
                "quantity": 4,
                "unit": "cây",
                "notes": "đập dập cắt khúc"
            },
            {
                "name": "Hành lá",
                "quantity": 40,
                "unit": "gram",
                "notes": "thái khúc dài 4cm"
            },
            {
                "name": "Ớt sừng",
                "quantity": 2,
                "unit": "trái",
                "notes": "thái sợi chỉ"
            },
            {
                "name": "Bia hoặc rượu trắng",
                "quantity": 50,
                "unit": "ml",
                "notes": "rưới lên khử tanh lúc hấp"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Làm sạch mực nhẹ tay",
                "description": "Rửa nhẹ mực trứng dưới vòi nước lạnh, lấy sạch túi mực cẩn thận không làm vỡ bọc trứng bên trong bụng mực.",
                "timer_minutes": 7
            },
            {
                "step_number": 2,
                "title": "Xếp xửng hấp thơm nức",
                "description": "Lót sả đập dập và 1/2 lượng gừng dưới đáy đĩa hấp, xếp mực trứng lên trên rồi rắc phần gừng ớt sợi và hành hoa lên bề mặt, rưới chút bia.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Hấp chín tới",
                "description": "Đặt đĩa mực vào xửng hấp nước sôi sùng sục, đậy nắp kín hấp lửa lớn trong 8-10 phút là mực chín căng tròn hoàn hảo.",
                "timer_minutes": 10
            },
            {
                "step_number": 4,
                "title": "Lấy mực ra đĩa",
                "description": "Mở nắp, cẩn thận nhấc đĩa mực nóng hổi ra bàn ăn.",
                "timer_minutes": 2
            },
            {
                "step_number": 5,
                "title": "Thưởng thức nóng",
                "description": "Thưởng thức ngay khi mực còn bốc khói, chấm đẫm chén muối ớt xanh Nha Trang chua cay.",
                "timer_minutes": 1
            }
        ]
    },
    {
        "title": "Cá Điêu Hồng Hấp Xì Dầu Gừng Hành",
        "slug": "ca-dieu-hong-hap-xi-dau-gung-hanh",
        "category_slug": "mon-hap",
        "description": "Thịt cá điêu hồng trắng phau ngọt thanh, ngập trong nước sốt xì dầu thơm nồng gừng sợi và hành hoa chần dầu sôi xèo xèo chuẩn vị ẩm thực Quảng Đông.",
        "prep_time": 20,
        "cook_time": 25,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 310,
            "protein": 32,
            "carbohydrates": 12,
            "fat": 14,
            "fiber": 2,
            "sodium": 690
        },
        "image_url": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Cá điêu hồng tươi sống",
                "quantity": 1000,
                "unit": "gram",
                "notes": "đánh vảy sạch, khứa chéo thân"
            },
            {
                "name": "Hành lá",
                "quantity": 100,
                "unit": "gram",
                "notes": "chẻ sợi dài ngâm nước uốn cong"
            },
            {
                "name": "Gừng tươi",
                "quantity": 50,
                "unit": "gram",
                "notes": "thái chỉ mỏng"
            },
            {
                "name": "Xì dầu (nước tương ngon)",
                "quantity": 4,
                "unit": "muỗng canh",
                "notes": "loại dùng hấp hải sản"
            },
            {
                "name": "Dầu hào",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "tạo vị ngọt đậm"
            },
            {
                "name": "Dầu mè thơm",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "hương thơm đặc trưng"
            },
            {
                "name": "Dầu ăn sôi",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "xối lên hành gừng"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế cá sạch khử tanh",
                "description": "Rửa cá với rượu gừng, khứa chéo nhẹ hai bên thân cá. Lót vài lát gừng và đầu hành vào bụng cá.",
                "timer_minutes": 8
            },
            {
                "step_number": 2,
                "title": "Hấp chín cá",
                "description": "Đặt cá vào đĩa sâu lòng, cho vào nồi hấp cách thủy trong 18-20 phút đến khi thịt cá chín trắng tinh.",
                "timer_minutes": 20
            },
            {
                "step_number": 3,
                "title": "Nấu sốt xì dầu hấp",
                "description": "Đun sôi hỗn hợp nước tương, dầu hào, đường, dầu mè và 3 muỗng nước luộc cá cho tan đều.",
                "timer_minutes": 4
            },
            {
                "step_number": 4,
                "title": "Xối dầu sôi lên hành gừng",
                "description": "Chắt bỏ nước tanh trong đĩa cá, rải đều gừng thái chỉ và hành hoa chẻ sợi lên mình cá. Đun sôi 3 muỗng dầu ăn rưới xèo xèo lên trên làm dậy mùi thơm ngất ngây.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Rưới sốt xì dầu",
                "description": "Rưới nước sốt xì dầu nóng quanh thân cá, dọn lên ăn nóng cùng cơm trắng hoặc cuộn bánh tráng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Tôm Hấp Nước Dừa Xiêm",
        "slug": "tom-hap-nuoc-dua-xiem",
        "category_slug": "mon-hap",
        "description": "Món ăn đơn giản mà đỉnh cao tinh túy sông nước Bến Tre, tôm hấp trong nước dừa tươi ngọt lịm tự nhiên, thịt tôm chắc nịch đỏ au bắt mắt.",
        "prep_time": 10,
        "cook_time": 15,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 230,
            "protein": 26,
            "carbohydrates": 8,
            "fat": 6,
            "fiber": 1,
            "sodium": 520
        },
        "image_url": "https://images.unsplash.com/photo-1541544741938-0af808871cc0?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Tôm sú hoặc tôm càng xanh",
                "quantity": 500,
                "unit": "gram",
                "notes": "tươi sống đang bơi"
            },
            {
                "name": "Nước dừa xiêm tươi",
                "quantity": 1,
                "unit": "trái",
                "notes": "chắt lấy nước ngọt thanh"
            },
            {
                "name": "Cơm dừa nạo sợi",
                "quantity": 50,
                "unit": "gram",
                "notes": "lót đáy đĩa trang trí"
            },
            {
                "name": "Hành tím thái lát",
                "quantity": 2,
                "unit": "củ",
                "notes": "thêm vào nước dừa"
            },
            {
                "name": "Muối tiêu chanh ớt",
                "quantity": 1,
                "unit": "phần",
                "notes": "nước chấm tôm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế tôm",
                "description": "Tôm rửa sạch, cắt bớt râu và ngạnh nhọn, để ráo nước.",
                "timer_minutes": 5
            },
            {
                "step_number": 2,
                "title": "Đun sôi nước dừa xiêm",
                "description": "Đổ nước dừa tươi vào nồi cùng chút hành tím và xíu muối hạt, đun sôi bùng.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Hấp tôm chín đỏ",
                "description": "Thả tôm vào nồi nước dừa sôi, đậy nắp đun lửa lớn trong 5-7 phút đến khi tôm cong đều chuyển màu đỏ rực rỡ thì vớt ra ngay.",
                "timer_minutes": 7
            },
            {
                "step_number": 4,
                "title": "Xếp tôm quanh trái dừa",
                "description": "Gọt miệng trái dừa tròn, xếp tôm móc đều quanh vành miệng trái dừa cho đẹp mắt.",
                "timer_minutes": 4
            },
            {
                "step_number": 5,
                "title": "Thưởng thức vị ngọt nguyên bản",
                "description": "Thưởng thức khi tôm còn nóng hổi, chấm muối tiêu chanh tươi.",
                "timer_minutes": 1
            }
        ]
    },
    {
        "title": "Lẩu Thái Hải Sản Thập Cẩm Chua Cay",
        "slug": "lau-thai-hai-san-thap-cam-chua-cay",
        "category_slug": "mon-lau",
        "description": "Nồi lẩu Thái sôi sùng sục đỏ au màu sa tế, thơm lừng cốt sả lá chúc riềng non, vị chua cay mặn ngọt bùng nổ nhúng cùng tôm sú, mực lá, bò Mỹ và nấm tươi.",
        "prep_time": 30,
        "cook_time": 40,
        "servings": 6,
        "difficulty": 2,
        "nutrition": {
            "calories": 450,
            "protein": 38,
            "carbohydrates": 26,
            "fat": 18,
            "fiber": 4,
            "sodium": 890
        },
        "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Xương ống hầm nước dùng",
                "quantity": 800,
                "unit": "gram",
                "notes": "ninh lấy 2 lít nước ngọt"
            },
            {
                "name": "Tôm sú tươi",
                "quantity": 300,
                "unit": "gram",
                "notes": "bỏ đầu chừa đuôi"
            },
            {
                "name": "Mực lá tươi",
                "quantity": 300,
                "unit": "gram",
                "notes": "khứa vảy rồng cắt miếng"
            },
            {
                "name": "Nghêu sống",
                "quantity": 400,
                "unit": "gram",
                "notes": "ngâm rửa sạch cát"
            },
            {
                "name": "Ba chỉ bò Mỹ cuộn",
                "quantity": 300,
                "unit": "gram",
                "notes": "thái mỏng nhúng lẩu"
            },
            {
                "name": "Gói cốt lẩu Thái Tomyum",
                "quantity": 1,
                "unit": "gói",
                "notes": "tạo hương vị chuẩn Thái"
            },
            {
                "name": "Sả cây, riềng non, lá chanh chúc",
                "quantity": 80,
                "unit": "gram",
                "notes": "đập dập vò nát"
            },
            {
                "name": "Rau muống, bắp chuối, nấm kim châm",
                "quantity": 400,
                "unit": "gram",
                "notes": "rau nhúng lẩu"
            },
            {
                "name": "Bún tươi hoặc mì tôm",
                "quantity": 500,
                "unit": "gram",
                "notes": "ăn kèm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Ninh nước hầm xương",
                "description": "Xương ống chần sạch, cho vào nồi hầm cùng 2.5 lít nước trong 45 phút lấy nước dùng trong ngọt đậm.",
                "timer_minutes": 45
            },
            {
                "step_number": 2,
                "title": "Nấu nước lẩu Thái chuẩn vị",
                "description": "Phi thơm sả, riềng, hành tỏi và ớt với dầu màu điều. Trút nước hầm xương vào, thêm gói sốt lẩu Thái, lá chanh chúc, nước cốt me và nước mắm nêm vừa vị chua cay béo ngậy.",
                "timer_minutes": 15
            },
            {
                "step_number": 3,
                "title": "Sơ chế đĩa hải sản và thịt bò",
                "description": "Bày tôm sú, mực lá khứa hoa, nghêu và ba chỉ bò cuộn hoa hồng ra đĩa lớn thật bắt mắt.",
                "timer_minutes": 10
            },
            {
                "step_number": 4,
                "title": "Chuẩn bị rổ rau nấm nhúng",
                "description": "Rau muống vặt lá bớt cọng, bắp chuối bào ngâm nước chanh khử thâm, nấm kim châm cắt gốc rửa sạch xếp ra rổ.",
                "timer_minutes": 8
            },
            {
                "step_number": 5,
                "title": "Thưởng thức lẩu sum vầy",
                "description": "Đặt nồi lẩu lên bếp từ giữa bàn ăn đun sôi sùng sục. Nhúng hải sản, thịt bò và rau nấm ăn kèm bún tươi và nước chấm muối ớt xanh.",
                "timer_minutes": 5
            }
        ]
    },
    {
        "title": "Lẩu Gà Lá É Đặc Sản Phú Yên",
        "slug": "lau-ga-la-e-dac-san-phu-yen",
        "category_slug": "mon-lau",
        "description": "Đặc sản đất Phú Yên làm say lòng thực khách với thịt gà ta đồi săn chắc, nước dùng ngọt thanh hầm cùng măng le và nấm bào ngư, nhúng lá é thơm lừng the cay giải cảm tuyệt vời.",
        "prep_time": 25,
        "cook_time": 35,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 410,
            "protein": 36,
            "carbohydrates": 18,
            "fat": 22,
            "fiber": 3,
            "sodium": 720
        },
        "image_url": "https://images.unsplash.com/photo-1547592180-85f173990554?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Gà ta thả vườn",
                "quantity": 1300,
                "unit": "gram",
                "notes": "chặt miếng vuông vừa ăn"
            },
            {
                "name": "Lá é trắng tươi",
                "quantity": 250,
                "unit": "gram",
                "notes": "nhặt ngọn non rửa sạch để ráo"
            },
            {
                "name": "Măng le tươi hoặc măng luộc",
                "quantity": 250,
                "unit": "gram",
                "notes": "luộc sạch thái lát xéo"
            },
            {
                "name": "Nấm bào ngư xám",
                "quantity": 150,
                "unit": "gram",
                "notes": "xé miếng vừa ăn"
            },
            {
                "name": "Ớt xiêm xanh miền Trung",
                "quantity": 15,
                "unit": "trái",
                "notes": "giã nhuyễn cùng lá é và muối"
            },
            {
                "name": "Hành tím băm, sả đập dập",
                "quantity": 4,
                "unit": "củ",
                "notes": "phi xào gà"
            },
            {
                "name": "Bún tươi sợi nhỏ",
                "quantity": 500,
                "unit": "gram",
                "notes": "ăn kèm lẩu"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế gà và giã muối ớt xiêm",
                "description": "Gà rửa sạch với muối và gừng, chặt miếng vừa ăn. Giã nhuyễn 1/3 lượng lá é với ớt xiêm xanh và muối hạt.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Ướp thịt gà ngấm vị cay the",
                "description": "Ướp gà với hỗn hợp muối ớt xiêm lá é vừa giã, thêm 1 muỗng hạt nêm và nước mắm trong 20 phút.",
                "timer_minutes": 20
            },
            {
                "step_number": 3,
                "title": "Xào săn gà và nấu nước lẩu",
                "description": "Phi thơm hành tím và sả, cho gà vào xào săn chắc thịt. Đổ 1.8 lít nước sôi vào đun lửa vừa hớt bọt trong 20 phút cho gà chín mềm ngọt nước.",
                "timer_minutes": 20
            },
            {
                "step_number": 4,
                "title": "Cho măng và nấm bào ngư",
                "description": "Thả măng le luộc và nấm bào ngư vào nồi lẩu đun thêm 5 phút cho măng ngấm nước gà ngọt lịm.",
                "timer_minutes": 5
            },
            {
                "step_number": 5,
                "title": "Nhúng lá é thưởng thức",
                "description": "Khi ăn, đun nước lẩu sôi bùng, vò nhẹ lá é thả vào nồi nhúng tái rồi vớt ra ăn ngay cùng thịt gà và bún tươi.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Lẩu Bò Nhúng Giấm Thơm Nồng",
        "slug": "lau-bo-nhung-giam-thom-nong",
        "category_slug": "mon-lau",
        "description": "Nước giấm nấu cùng nước dừa xiêm, sả đập dập và dứa thơm ngọt thanh chua dịu, nhúng từng lát bắp bò hoa và gầu bò tươi mềm cuộn bánh tráng chấm mắm nêm đậm đà.",
        "prep_time": 25,
        "cook_time": 30,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 440,
            "protein": 36,
            "carbohydrates": 22,
            "fat": 22,
            "fiber": 3,
            "sodium": 750
        },
        "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Bắp bò hoa tươi",
                "quantity": 400,
                "unit": "gram",
                "notes": "thái lát mỏng ngang thớ"
            },
            {
                "name": "Gầu bò hoặc thăn bò",
                "quantity": 300,
                "unit": "gram",
                "notes": "thái lát mỏng"
            },
            {
                "name": "Nước dừa tươi ngọt",
                "quantity": 700,
                "unit": "ml",
                "notes": "dừa xiêm"
            },
            {
                "name": "Giấm gạo ngon",
                "quantity": 150,
                "unit": "ml",
                "notes": "tạo độ chua dịu"
            },
            {
                "name": "Thơm (dứa)",
                "quantity": 0.5,
                "unit": "quả",
                "notes": "thái lát nấu nước và băm làm mắm nêm"
            },
            {
                "name": "Sả cây, hành tây",
                "quantity": 4,
                "unit": "cây",
                "notes": "đập dập cắt khúc"
            },
            {
                "name": "Bánh tráng phơi sương, rau sống, chuối chát",
                "quantity": 1,
                "unit": "mẹt",
                "notes": "cuốn kèm"
            },
            {
                "name": "Mắm nêm pha sẵn chua ngọt",
                "quantity": 1,
                "unit": "chén",
                "notes": "chấm bò"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Thái thịt bò mỏng đẹp",
                "description": "Thịt bò để ngăn đá 20 phút cho se lại rồi dùng dao sắc thái lát mỏng bản to, xếp xòe đều ra đĩa rắc chút mè rang.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Nấu nước giấm dừa thơm",
                "description": "Cho nước dừa tươi, giấm gạo, thơm cắt lát, sả đập dập, hành tây và 2 muỗng đường vào nồi đun sôi lăn tăn nếm có vị chua ngọt hài hòa.",
                "timer_minutes": 10
            },
            {
                "step_number": 3,
                "title": "Pha mắm nêm chấm bò",
                "description": "Mắm nêm khuấy đều cùng thơm băm nhuyễn, tỏi ớt giã nhỏ, nước cốt chanh và đường cho vừa độ mặn ngọt cay nồng.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Chuẩn bị mẹt cuốn",
                "description": "Bày chuối chát khế chua thái mỏng, dưa leo, rau sống, bún tươi và bánh tráng quanh bàn ăn.",
                "timer_minutes": 5
            },
            {
                "step_number": 5,
                "title": "Nhúng bò và cuộn thưởng thức",
                "description": "Gắp từng miếng thịt bò nhúng vào nồi nước giấm sôi 15-20 giây cho chín tái mềm ngọt, cuộn bánh tráng rau sống chấm mắm nêm.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Lẩu Riêu Cua Bắp Bò Sườn Sụn",
        "slug": "lau-rieu-cua-bap-bo-suon-sun",
        "category_slug": "mon-lau",
        "description": "Nồi lẩu riêu cua vàng óng nổi bật mảng gạch cua đồng thơm ngậy, nước dùng thanh chua ngọt từ giấm bỗng và cà chua, nhúng sườn sụn giòn sần sật và bắp bò tươi rói.",
        "prep_time": 35,
        "cook_time": 40,
        "servings": 6,
        "difficulty": 2,
        "nutrition": {
            "calories": 480,
            "protein": 42,
            "carbohydrates": 24,
            "fat": 25,
            "fiber": 4,
            "sodium": 880
        },
        "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Cua đồng giã nhuyễn",
                "quantity": 600,
                "unit": "gram",
                "notes": "lọc lấy 1.8 lít nước thịt cua"
            },
            {
                "name": "Bắp bò tươi thái mỏng",
                "quantity": 400,
                "unit": "gram",
                "notes": "nhúng lẩu"
            },
            {
                "name": "Sườn sụn non",
                "quantity": 400,
                "unit": "gram",
                "notes": "thái mỏng chần sạch ninh mềm"
            },
            {
                "name": "Đậu phụ (đậu hũ)",
                "quantity": 4,
                "unit": "miếng",
                "notes": "cắt vuông chiên vàng giòn"
            },
            {
                "name": "Giấm bỗng nếp",
                "quantity": 150,
                "unit": "ml",
                "notes": "linh hồn vị chua thanh riêu cua"
            },
            {
                "name": "Cà chua",
                "quantity": 3,
                "unit": "quả",
                "notes": "bổ múi cau xào màu"
            },
            {
                "name": "Rau muống chẻ, hoa chuối, xà lách",
                "quantity": 400,
                "unit": "gram",
                "notes": "rau nhúng lẩu"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Lọc riêu cua và chưng gạch",
                "description": "Lọc nước cua qua rây nhiều lần. Chưng gạch cua với hành khô và dầu điều cho vàng thơm bóng bẩy.",
                "timer_minutes": 15
            },
            {
                "step_number": 2,
                "title": "Ninh sườn sụn non",
                "description": "Chần sườn sụn non, cho vào nồi áp suất ninh 15 phút cho sụn mềm giòn ngọt nước.",
                "timer_minutes": 15
            },
            {
                "step_number": 3,
                "title": "Nấu đóng tảng riêu cua",
                "description": "Đun nồi nước cua trên lửa vừa, khuấy nhẹ đáy nồi đến khi thịt cua nổi lên đóng tảng thì gạt riêu sang một bên, múc bớt riêu ra đĩa tránh vỡ nát.",
                "timer_minutes": 10
            },
            {
                "step_number": 4,
                "title": "Hoàn thiện nước lẩu riêu",
                "description": "Trút nước hầm sườn sụn, cà chua xào, đậu phụ chiên và giấm bỗng nếp vào nồi nước riêu, nêm gia vị vừa miệng chua thanh.",
                "timer_minutes": 8
            },
            {
                "step_number": 5,
                "title": "Bày bàn lẩu thịnh soạn",
                "description": "Đặt nồi lẩu lên bếp, trút phần riêu cua và gạch chưng lên mặt nước lẩu. Nhúng bắp bò, sườn sụn và rau sống ăn kèm bún tươi.",
                "timer_minutes": 3
            }
        ]
    },
    {
        "title": "Vịt Nấu Chao Đậm Đà Cần Thơ",
        "slug": "vit-nau-chao-dam-da-can-tho",
        "category_slug": "mon-lau",
        "description": "Đặc sản miền Tây sông nước với thịt vịt xiêm béo mềm không chút mùi tanh, quyện sốt chao trắng chao đỏ bùi ngậy đậm đà, khoai môn dẻo bở ngọt bùi.",
        "prep_time": 30,
        "cook_time": 45,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 490,
            "protein": 35,
            "carbohydrates": 28,
            "fat": 28,
            "fiber": 3,
            "sodium": 850
        },
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt vịt xiêm",
                "quantity": 1000,
                "unit": "gram",
                "notes": "chặt miếng vuông vừa ăn"
            },
            {
                "name": "Chao môn (chao trắng & đỏ)",
                "quantity": 6,
                "unit": "viên",
                "notes": "tán nhuyễn cùng nước chao"
            },
            {
                "name": "Khoai môn cao",
                "quantity": 350,
                "unit": "gram",
                "notes": "gọt vỏ cắt khối chiên sơ"
            },
            {
                "name": "Nước dừa tươi",
                "quantity": 600,
                "unit": "ml",
                "notes": "tạo vị ngọt thanh"
            },
            {
                "name": "Sả đập dập, tỏi, hành khô băm",
                "quantity": 50,
                "unit": "gram",
                "notes": "phi xào thịt vịt"
            },
            {
                "name": "Rau muống non, cải cúc",
                "quantity": 300,
                "unit": "gram",
                "notes": "rau nhúng lẩu"
            },
            {
                "name": "Bún tươi hoặc mì trứng",
                "quantity": 400,
                "unit": "gram",
                "notes": "ăn kèm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Khử mùi tanh thịt vịt",
                "description": "Chà xát vịt kỹ bằng rượu trắng và gừng giã nhuyễn trong 5 phút, rửa sạch để ráo rồi chặt miếng vừa ăn.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Ướp vịt với sốt chao",
                "description": "Tán nhuyễn chao cùng tỏi hành băm, 1 muỗng đường, tiêu và chút hạt nêm. Ướp vào thịt vịt trong 30 phút cho ngấm sâu.",
                "timer_minutes": 30
            },
            {
                "step_number": 3,
                "title": "Chiên sơ khoai môn",
                "description": "Chiên khoai môn ngập dầu 3-4 phút cho se mặt ngoài để khi nấu vào lẩu không bị rã nát đục nước.",
                "timer_minutes": 8
            },
            {
                "step_number": 4,
                "title": "Xào săn và hầm thịt vịt",
                "description": "Phi thơm sả tỏi, trút vịt vào xào thật săn chắc. Đổ nước dừa tươi vào đun sôi, hạ lửa nhỏ hầm 25 phút cho thịt vịt mềm rục.",
                "timer_minutes": 25
            },
            {
                "step_number": 5,
                "title": "Cho khoai môn và thưởng thức",
                "description": "Cho khoai môn vào nấu tiếp 10 phút đến khi khoai bở mềm dẻo quánh. Đặt lên bếp lẩu nhúng rau muống ăn kèm chén chao chấm chua cay.",
                "timer_minutes": 10
            }
        ]
    },
    {
        "title": "Gỏi Cuốn Tôm Thịt Tươi Mát",
        "slug": "goi-cuon-tom-thit-tuoi-mat",
        "category_slug": "mon-cuon-goi",
        "description": "Món ăn thanh mát nổi danh thế giới với từng con tôm sú đỏ au, thịt ba chỉ luộc thái mỏng, bún tươi và các loại rau thơm cuộn tròn trong bánh tráng dẻo dai chấm tương đậu phộng béo ngậy.",
        "prep_time": 25,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 260,
            "protein": 20,
            "carbohydrates": 32,
            "fat": 6,
            "fiber": 3,
            "sodium": 490
        },
        "image_url": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Tôm sú tươi sống",
                "quantity": 300,
                "unit": "gram",
                "notes": "luộc chín bóc vỏ chẻ đôi"
            },
            {
                "name": "Thịt ba chỉ heo",
                "quantity": 300,
                "unit": "gram",
                "notes": "luộc chín thái lát mỏng"
            },
            {
                "name": "Bánh tráng dẻo phơi sương",
                "quantity": 20,
                "unit": "lá",
                "notes": "loại cuốn gỏi không rách"
            },
            {
                "name": "Bún tươi sợi nhỏ",
                "quantity": 300,
                "unit": "gram",
                "notes": "tơi sợi"
            },
            {
                "name": "Rau xà lách, rau thơm, hẹ",
                "quantity": 200,
                "unit": "gram",
                "notes": "rửa sạch để ráo nước"
            },
            {
                "name": "Tương đen (tương hột xay)",
                "quantity": 100,
                "unit": "gram",
                "notes": "nấu sốt chấm bơ đậu phộng"
            },
            {
                "name": "Đậu phộng rang giã dập",
                "quantity": 30,
                "unit": "gram",
                "notes": "rắc lên chén tương chấm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Luộc tôm và thịt ba chỉ",
                "description": "Luộc thịt ba chỉ với củ hành tím đập dập trong 15 phút đến khi chín tới, ngâm nước đá rồi thái mỏng. Luộc tôm đỏ au, bóc vỏ chẻ đôi sống lưng.",
                "timer_minutes": 20
            },
            {
                "step_number": 2,
                "title": "Chuẩn bị rau sống và hẹ",
                "description": "Rau sống nhặt rửa sạch, vẩy thật ráo nước. Hẹ rửa sạch cắt khúc dài bằng nửa cuốn gỏi.",
                "timer_minutes": 8
            },
            {
                "step_number": 3,
                "title": "Pha tương chấm bơ đậu phộng",
                "description": "Phi thơm tỏi băm, cho tương đen và 2 muỗng bơ đậu phộng vào khuấy đều trên lửa nhỏ cùng chút đường và nước cốt dừa tạo sốt chấm sánh mịn béo ngậy.",
                "timer_minutes": 6
            },
            {
                "step_number": 4,
                "title": "Cuốn gỏi cuốn khéo léo",
                "description": "Thấm ướt nhẹ bánh tráng, đặt xà lách rau thơm và bún lên trước rồi cuộn 1 vòng. Xếp tôm màu đỏ áp ra ngoài bánh tráng, vài lát thịt và nhánh hẹ thò đầu ra ngoài, cuộn chặt tay thật tròn đều.",
                "timer_minutes": 15
            },
            {
                "step_number": 5,
                "title": "Trình bày món ăn",
                "description": "Xếp gỏi cuốn ra đĩa, múc chén sốt tương rắc đậu phộng rang và ớt băm, thưởng thức tươi mát.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Gỏi Ngó Sen Tai Heo Tôm Thịt",
        "slug": "goi-ngo-sen-tai-heo-tom-thit",
        "category_slug": "mon-cuon-goi",
        "description": "Ngó sen trắng muốt giòn sần sật thấm đẫm vị nước mắm chua ngọt, trộn cùng tai heo luộc giòn sừn sựt, tôm sú bùi bọt và rau răm thơm nồng rắc phồng tôm giòn tan.",
        "prep_time": 30,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 310,
            "protein": 24,
            "carbohydrates": 26,
            "fat": 12,
            "fiber": 4,
            "sodium": 620
        },
        "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Ngó sen tươi",
                "quantity": 300,
                "unit": "gram",
                "notes": "chẻ đôi ngâm nước giấm đường giữ độ trắng giòn"
            },
            {
                "name": "Tai heo",
                "quantity": 1,
                "unit": "cái",
                "notes": "luộc chín ngâm nước đá thái sợi mỏng"
            },
            {
                "name": "Tôm sú",
                "quantity": 200,
                "unit": "gram",
                "notes": "luộc bóc vỏ chẻ đôi"
            },
            {
                "name": "Cà rốt thái sợi",
                "quantity": 1,
                "unit": "củ",
                "notes": "bóp muối vắt ráo"
            },
            {
                "name": "Rau răm, húng lủi",
                "quantity": 50,
                "unit": "gram",
                "notes": "nhặt sạch thái thô"
            },
            {
                "name": "Đậu phộng rang, hành phi",
                "quantity": 40,
                "unit": "gram",
                "notes": "rắc lên mặt gỏi"
            },
            {
                "name": "Bánh phồng tôm chiên giòn",
                "quantity": 10,
                "unit": "cái",
                "notes": "ăn kèm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế ngó sen trắng giòn",
                "description": "Ngó sen bẻ khúc 5cm, chẻ đôi ngâm vào âu nước đá pha nước cốt chanh và giấm đường trong 15 phút rồi vớt ra vắt nhẹ ráo nước.",
                "timer_minutes": 15
            },
            {
                "step_number": 2,
                "title": "Luộc tai heo giòn sần sật",
                "description": "Tai heo cạo rửa sạch với muối giấm, luộc chín trong 20 phút rồi vớt ngâm ngay vào âu nước đá lạnh cho tai trắng giòn, thái lát mỏng.",
                "timer_minutes": 25
            },
            {
                "step_number": 3,
                "title": "Pha nước mắm trộn gỏi thần thánh",
                "description": "Khuấy tan 3 muỗng nước mắm cốt, 3 muỗng đường, 3 muỗng nước cốt chanh tươi và tỏi ớt băm nhuyễn sánh quyện.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Trộn gỏi thấm vị",
                "description": "Cho ngó sen, cà rốt, tai heo và tôm vào âu lớn, rưới 2/3 lượng nước sốt vào trộn đều tay để 5 phút cho ngấm, chắt bớt nước tiết ra.",
                "timer_minutes": 8
            },
            {
                "step_number": 5,
                "title": "Bày đĩa và rắc đậu phộng",
                "description": "Cho rau răm húng lủi vào trộn nhẹ, gắp gỏi ra đĩa vun ngọn, rắc đậu phộng và hành phi giòn tan, ăn kèm bánh phồng tôm.",
                "timer_minutes": 3
            }
        ]
    },
    {
        "title": "Phở Cuốn Thịt Bò Rau Mùi Hà Nội",
        "slug": "pho-cuon-thit-bo-rau-mui-ha-noi",
        "category_slug": "mon-cuon-goi",
        "description": "Đặc sản thanh nhã của phố Ngũ Xã Hà Nội với từng tấm bánh phở mềm mướt cuộn chặt thịt bò xào lăn thơm phức tỏi phi và rau mùi, chấm ngập nước mắm chua ngọt dưa góp.",
        "prep_time": 20,
        "cook_time": 15,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 330,
            "protein": 25,
            "carbohydrates": 34,
            "fat": 10,
            "fiber": 2,
            "sodium": 610
        },
        "image_url": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Bánh phở cuốn nguyên tấm",
                "quantity": 500,
                "unit": "gram",
                "notes": "bánh phở mỏng dai mướt"
            },
            {
                "name": "Thịt thăn bò",
                "quantity": 350,
                "unit": "gram",
                "notes": "thái lát mỏng ngang thớ"
            },
            {
                "name": "Tỏi băm",
                "quantity": 1,
                "unit": "củ",
                "notes": "phi thơm xào bò"
            },
            {
                "name": "Rau xà lách, rau mùi ta, kinh giới",
                "quantity": 200,
                "unit": "gram",
                "notes": "rửa sạch để thật ráo"
            },
            {
                "name": "Dầu hào, tiêu đen",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "ướp thịt bò"
            },
            {
                "name": "Nước mắm chấm nem chua ngọt",
                "quantity": 1,
                "unit": "bát",
                "notes": "kèm dưa góp đu đủ cà rốt"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Ướp và xào thịt bò",
                "description": "Ướp thịt bò với tỏi băm, dầu hào, tiêu trong 15 phút. Phi tỏi thơm trên lửa lớn, trút bò vào xào nhanh 2 phút vừa chín tới rồi trút ra đĩa.",
                "timer_minutes": 15
            },
            {
                "step_number": 2,
                "title": "Chuẩn bị bánh phở và rau",
                "description": "Tách từng lá bánh phở vuông vức đặt lên thớt sạch. Rau sống rửa sạch vẩy ráo nước.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Cuốn phở cuốn",
                "description": "Trải lá bánh phở ra thớt, xếp xà lách rau mùi kinh giới và múc thịt bò xào rải đều lên trên, cuộn tròn chặt tay thật khéo léo.",
                "timer_minutes": 10
            },
            {
                "step_number": 4,
                "title": "Cắt khúc xếp đĩa",
                "description": "Cắt đôi cuốn phở nếu dài, xếp đều lên đĩa trắng tinh tế.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Thưởng thức",
                "description": "Chấm ngập cuốn phở vào bát nước mắm chua ngọt có nổi tỏi ớt và đu đủ giòn sần sật.",
                "timer_minutes": 1
            }
        ]
    },
    {
        "title": "Nộm Bắp Chuối Thịt Gà Xé Phay",
        "slug": "nom-bap-chuoi-thit-ga-xe-phay",
        "category_slug": "mon-cuon-goi",
        "description": "Hoa chuối bào mỏng giòn sần sật trắng tinh, thịt gà ta xé sợi dai ngọt quyện vị chua thanh của chanh, thơm nồng lá chanh và rau răm đậm đà hương vị đồng quê.",
        "prep_time": 20,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 290,
            "protein": 26,
            "carbohydrates": 18,
            "fat": 12,
            "fiber": 4,
            "sodium": 580
        },
        "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Bắp chuối (hoa chuối) bào sợi",
                "quantity": 300,
                "unit": "gram",
                "notes": "ngâm nước chanh muối cho trắng giòn"
            },
            {
                "name": "Thịt gà luộc xé phay",
                "quantity": 300,
                "unit": "gram",
                "notes": "chọn phần ức và đùi gà ta"
            },
            {
                "name": "Hành tây thái mỏng",
                "quantity": 0.5,
                "unit": "củ",
                "notes": "ngâm nước đá khử hăng"
            },
            {
                "name": "Rau răm, lá chanh",
                "quantity": 40,
                "unit": "gram",
                "notes": "thái nhỏ"
            },
            {
                "name": "Đậu phộng rang giã dập",
                "quantity": 40,
                "unit": "gram",
                "notes": "rắc mặt nộm"
            },
            {
                "name": "Nước cốt chanh, đường, nước mắm",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "nước sốt trộn nộm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Bào và ngâm hoa chuối",
                "description": "Bắp chuối tước bớt bẹ già, dùng dao sắc bào mỏng ngâm ngay vào âu nước lạnh pha nước cốt 1 quả chanh và muối trong 15 phút để không bị thâm đen.",
                "timer_minutes": 15
            },
            {
                "step_number": 2,
                "title": "Xé gà và ngâm hành tây",
                "description": "Thịt gà luộc xé miếng dài vừa ăn. Hành tây thái mỏng ngâm giấm đường đá lạnh khử hăng.",
                "timer_minutes": 8
            },
            {
                "step_number": 3,
                "title": "Pha sốt trộn nộm chua ngọt",
                "description": "Pha 2 muỗng nước mắm, 2 muỗng đường, 2 muỗng nước cốt chanh và tỏi ớt băm nhuyễn.",
                "timer_minutes": 4
            },
            {
                "step_number": 4,
                "title": "Trộn nộm gà hoa chuối",
                "description": "Vớt hoa chuối và hành tây vắt nhẹ cho ráo nước, cho vào âu cùng thịt gà xé, rưới nước sốt trộn đều tay trong 3 phút.",
                "timer_minutes": 5
            },
            {
                "step_number": 5,
                "title": "Hoàn thiện đĩa nộm",
                "description": "Trộn thêm rau răm và lá chanh thái chỉ, múc ra đĩa rắc đậu phộng rang giòn thơm lừng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Phở Bò Tái Nạm Hà Nội Gia Truyền",
        "slug": "pho-bo-tai-nam-ha-noi-gia-truyen",
        "category_slug": "bun-pho-mi",
        "description": "Bát phở bò nóng hổi thơm nức hương hoa hồi, quế chi, thảo quả và gừng nướng, nước dùng trong veo ngọt lịm từ xương bò ninh 8 tiếng, thịt bò tái mềm ngọt tan.",
        "prep_time": 40,
        "cook_time": 90,
        "servings": 4,
        "difficulty": 3,
        "nutrition": {
            "calories": 520,
            "protein": 36,
            "carbohydrates": 65,
            "fat": 14,
            "fiber": 3,
            "sodium": 980
        },
        "image_url": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Xương ống bò tươi",
                "quantity": 1200,
                "unit": "gram",
                "notes": "chặt khúc, ngâm nước muối chần sạch"
            },
            {
                "name": "Thịt nạm bò",
                "quantity": 400,
                "unit": "gram",
                "notes": "luộc trong nước dùng rồi thái lát mỏng"
            },
            {
                "name": "Thịt thăn bò tươi",
                "quantity": 250,
                "unit": "gram",
                "notes": "thái lát mỏng dùng làm thịt tái"
            },
            {
                "name": "Bánh phở tươi Hà Nội",
                "quantity": 600,
                "unit": "gram",
                "notes": "sợi phở mềm dai mướt"
            },
            {
                "name": "Hoa hồi, quế chi, thảo quả, tiểu hồi",
                "quantity": 30,
                "unit": "gram",
                "notes": "rang thơm cho vào túi lọc"
            },
            {
                "name": "Gừng già, hành tây",
                "quantity": 2,
                "unit": "củ",
                "notes": "nướng xém vỏ cạo sạch đập dập"
            },
            {
                "name": "Hành hoa, rau mùi, ngò gai",
                "quantity": 60,
                "unit": "gram",
                "notes": "thái nhỏ rắc bát phở"
            },
            {
                "name": "Chanh tươi, ớt hiểm, dấm tỏi",
                "quantity": 1,
                "unit": "phần",
                "notes": "gia vị ăn kèm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế và khử hôi xương bò",
                "description": "Ngâm xương bò trong nước muối 1 tiếng, chần nước sôi cùng gừng và rượu trắng trong 10 phút, cạo sạch phần tủy đen rồi rửa thật sạch dưới vòi nước lạnh.",
                "timer_minutes": 25
            },
            {
                "step_number": 2,
                "title": "Nướng gia vị phở dậy mùi thơm",
                "description": "Nướng hành tây và gừng trên lửa than cho xém cạnh thơm nức, cạo sạch tro đen đập dập. Rang thơm hoa hồi, quế, thảo quả cho vào túi lọc vải buộc kín miệng.",
                "timer_minutes": 15
            },
            {
                "step_number": 3,
                "title": "Ninh nước dùng phở bò trong veo",
                "description": "Cho xương bò, thịt nạm vào nồi cùng 3.5 lít nước, đun sôi rồi vớt bọt liên tục. Thả túi thảo mộc và gừng nướng vào. Hạ lửa nhỏ ninh liu riu mở hé vung trong 60-90 phút. Nêm nước mắm cốt và muối hạt vừa vị ngọt thanh.",
                "timer_minutes": 90
            },
            {
                "step_number": 4,
                "title": "Vớt thịt nạm và chuẩn bị bánh phở",
                "description": "Vớt miếng nạm bò chín mềm ngâm vào âu nước đá để thịt săn chắc, thái lát mỏng đều. Chần bánh phở qua nồi nước sôi nóng hổi rồi xốc ráo, chia đều vào 4 bát tô.",
                "timer_minutes": 10
            },
            {
                "step_number": 5,
                "title": "Chan nước dùng phở sôi sùng sục",
                "description": "Xếp thịt nạm, thịt bò tươi tái đập dập lên mặt bánh phở, rắc nhiều hành hoa, đầu hành chẻ và ngò gai. Múc nước dùng đang sôi sùng sục chan ngập bát thịt bò chín tái hồng hào. Thưởng thức nóng cùng quẩy giòn và giấm tỏi ớt.",
                "timer_minutes": 5
            }
        ]
    },
    {
        "title": "Bún Bò Huế Cay Nồng Chuẩn Vị Cố Đô",
        "slug": "bun-bo-hue-cay-nong-chuan-vi-co-do",
        "category_slug": "bun-pho-mi",
        "description": "Tô bún bò Huế đỏ rực màu ớt sa tế, ngào ngạt mùi sả cây và mắm ruốc Huế đậm đà, sợi bún to tròn mướt mát cùng nạm bò, giò heo, chả cua và huyết luộc béo bùi.",
        "prep_time": 35,
        "cook_time": 75,
        "servings": 4,
        "difficulty": 3,
        "nutrition": {
            "calories": 560,
            "protein": 40,
            "carbohydrates": 60,
            "fat": 18,
            "fiber": 3,
            "sodium": 990
        },
        "image_url": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Bắp bò hoa và nạm bò",
                "quantity": 500,
                "unit": "gram",
                "notes": "cuộn tròn luộc chín thái mỏng"
            },
            {
                "name": "Móng giò heo",
                "quantity": 500,
                "unit": "gram",
                "notes": "chặt khoanh chần sạch luộc mềm"
            },
            {
                "name": "Mắm ruốc Huế nguyên chất",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "hòa nước lạnh gạn lấy nước trong"
            },
            {
                "name": "Sả cây",
                "quantity": 8,
                "unit": "cây",
                "notes": "đập dập bó lại thả nồi nước dùng"
            },
            {
                "name": "Ớt bột Huế, ớt sa tế",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "phi với dầu màu điều"
            },
            {
                "name": "Chả cua Huế và huyết heo luộc",
                "quantity": 200,
                "unit": "gram",
                "notes": "topping bún bò"
            },
            {
                "name": "Bún sợi to Huế",
                "quantity": 600,
                "unit": "gram",
                "notes": "chần qua nước sôi"
            },
            {
                "name": "Bắp chuối bào, giá đỗ, rau muống chẻ",
                "quantity": 300,
                "unit": "gram",
                "notes": "rau sống ăn kèm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Hầm xương và luộc thịt bò, giò heo",
                "description": "Chần sạch xương bò, nạm bò và móng giò. Cho vào nồi cùng 3 lít nước và bó sả đập dập hầm trong 50 phút đến khi thịt chín mềm thì vớt ra ngâm nước đá rồi thái mỏng.",
                "timer_minutes": 50
            },
            {
                "step_number": 2,
                "title": "Pha và nấu mắm ruốc Huế",
                "description": "Hòa mắm ruốc với 200ml nước lạnh, khuấy tan để lắng cặn. Chắt lấy phần nước trong đổ vào nồi nước dùng đun sôi dậy mùi thơm nồng nàn.",
                "timer_minutes": 10
            },
            {
                "step_number": 3,
                "title": "Làm ớt màu sa tế cay nồng",
                "description": "Đun nóng dầu điều, phi thơm sả băm, tỏi băm và ớt bột Huế tạo lớp váng dầu sa tế đỏ rực rỡ trút vào nồi nước lẩu.",
                "timer_minutes": 6
            },
            {
                "step_number": 4,
                "title": "Nấu chả cua và huyết heo",
                "description": "Múc từng viên chả cua và thả miếng huyết luộc vào nồi nước lẩu đang sôi cho nổi chín phồng.",
                "timer_minutes": 8
            },
            {
                "step_number": 5,
                "title": "Hoàn thiện bát bún bò Huế",
                "description": "Chần bún sợi to cho vào tô, xếp bắp bò, giò heo, chả cua, huyết luộc, rắc hành tây thái mỏng và rau răm. Chan nước dùng sôi sùng sục đỏ au, ăn kèm đĩa rau sống bắp chuối vắt chanh.",
                "timer_minutes": 5
            }
        ]
    },
    {
        "title": "Bún Chả Hà Nội Nướng Than Hoa",
        "slug": "bun-cha-ha-noi-nuong-than-hoa",
        "category_slug": "bun-pho-mi",
        "description": "Từng miếng chả băm chả miếng nướng xém cạnh trên than hoa đượm khói thơm nức, thả vào bát nước chấm dưa góp chua ngọt ấm nóng, ăn kèm đĩa bún sợi nhỏ thanh tao.",
        "prep_time": 30,
        "cook_time": 25,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 490,
            "protein": 32,
            "carbohydrates": 54,
            "fat": 18,
            "fiber": 2,
            "sodium": 790
        },
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Thịt ba chỉ heo",
                "quantity": 400,
                "unit": "gram",
                "notes": "thái lát mỏng vừa làm chả miếng"
            },
            {
                "name": "Thịt nạc vai băm",
                "quantity": 400,
                "unit": "gram",
                "notes": "xay nhuyễn có chút mỡ làm chả băm"
            },
            {
                "name": "Nước hàng caramen",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "tạo màu cánh gián cho chả"
            },
            {
                "name": "Hành khô, tỏi băm",
                "quantity": 3,
                "unit": "củ",
                "notes": "vắt lấy nước cốt ướp thịt"
            },
            {
                "name": "Bún tươi sợi nhỏ lá",
                "quantity": 600,
                "unit": "gram",
                "notes": "tơi mềm"
            },
            {
                "name": "Đu đủ xanh, cà rốt",
                "quantity": 150,
                "unit": "gram",
                "notes": "thái mỏng bóp giấm đường làm dưa góp"
            },
            {
                "name": "Rau xà lách, tía tô, kinh giới",
                "quantity": 200,
                "unit": "gram",
                "notes": "rau sống ăn kèm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Ướp chả miếng và chả băm",
                "description": "Ướp thịt ba chỉ và thịt nạc vai với nước mắm, đường, nước màu, nước cốt hành tỏi và tiêu đen trong 30 phút. Viên thịt nạc vai thành từng viên chả tròn dẹt.",
                "timer_minutes": 30
            },
            {
                "step_number": 2,
                "title": "Nướng chả trên than hoa",
                "description": "Kẹp chả vào vỉ nướng trên than hoa đỏ hồng. Quét chút dầu ăn cho chả không khô, lật đều tay 12-15 phút đến khi chả chín vàng ươm xém cạnh thơm nức.",
                "timer_minutes": 15
            },
            {
                "step_number": 3,
                "title": "Làm dưa góp đu đủ cà rốt",
                "description": "Đu đủ cà rốt thái mỏng bóp muối rửa sạch, ngâm giấm đường chua ngọt cho giòn sần sật.",
                "timer_minutes": 10
            },
            {
                "step_number": 4,
                "title": "Pha nước chấm bún chả ấm nóng",
                "description": "Pha nước mắm, đường, giấm và nước ấm theo tỉ lệ 1:1:1:5, đun ấm nóng nêm vị chua ngọt dịu, thả tỏi ớt băm và dưa góp vào bát.",
                "timer_minutes": 5
            },
            {
                "step_number": 5,
                "title": "Thưởng thức bún chả",
                "description": "Thả chả viên và chả miếng nướng nóng hổi vào bát nước chấm. Ăn kèm đĩa bún tươi và rổ rau sống kinh giới tía tô ngát hương.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Bún Riêu Cua Đồng Đậm Đà Miền Bắc",
        "slug": "bun-rieu-cua-dong-dam-da-mien-bac",
        "category_slug": "bun-pho-mi",
        "description": "Tô bún riêu thanh mát quyến rũ với mảng thịt riêu cua đồng xốp mềm thơm ngậy, cà chua đỏ mọng xào bóng bẩy, đậu mơ chiên vàng giòn và nước dùng chua thanh vị giấm bỗng nếp.",
        "prep_time": 30,
        "cook_time": 35,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 450,
            "protein": 26,
            "carbohydrates": 58,
            "fat": 14,
            "fiber": 3,
            "sodium": 820
        },
        "image_url": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Cua đồng giã nhuyễn",
                "quantity": 500,
                "unit": "gram",
                "notes": "lọc lấy 1.5 lít nước thịt cua"
            },
            {
                "name": "Cà chua",
                "quantity": 4,
                "unit": "quả",
                "notes": "bổ múi cau xào màu"
            },
            {
                "name": "Đậu phụ Mơ",
                "quantity": 3,
                "unit": "miếng",
                "notes": "cắt vuông chiên vàng giòn"
            },
            {
                "name": "Giấm bỗng nếp",
                "quantity": 100,
                "unit": "ml",
                "notes": "vị chua dịu thanh tao"
            },
            {
                "name": "Mắm tôm Bắc",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "dậy mùi riêu cua"
            },
            {
                "name": "Bún tươi sợi nhỏ",
                "quantity": 600,
                "unit": "gram",
                "notes": "chần nước sôi"
            },
            {
                "name": "Hành hoa, kinh giới, bắp chuối bào",
                "quantity": 250,
                "unit": "gram",
                "notes": "rau sống ăn kèm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Lọc nước cua đồng",
                "description": "Hòa cua xay với nước sạch và muối, lọc qua rây 2-3 lần lấy nước cốt cua trong sánh.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Chưng gạch cua và xào cà chua",
                "description": "Phi hành khô chưng gạch cua vàng óng. Xào cà chua với chút dầu ăn tạo màu đỏ bắt mắt.",
                "timer_minutes": 6
            },
            {
                "step_number": 3,
                "title": "Nấu đóng bánh riêu cua",
                "description": "Đun nồi nước cua lửa vừa, khuấy nhẹ đến khi riêu nổi đóng mảng thì hạ lửa nhỏ, vớt mảng riêu ra đĩa riêng.",
                "timer_minutes": 10
            },
            {
                "step_number": 4,
                "title": "Nấu nước dùng riêu chua thanh",
                "description": "Cho cà chua xào, đậu phụ chiên, giấm bỗng nếp và mắm tôm vào nồi nước cua, nêm gia vị vừa miệng.",
                "timer_minutes": 8
            },
            {
                "step_number": 5,
                "title": "Trình bày bát bún riêu",
                "description": "Cho bún vào tô, múc riêu cua, đậu chiên lên mặt, rưới nước dùng chua nóng rực rỡ, rắc hành hoa thưởng thức.",
                "timer_minutes": 3
            }
        ]
    },
    {
        "title": "Hủ Tiếu Nam Vang Sườn Tôm Thịt",
        "slug": "hu-tieu-nam-vang-suon-tom-thit",
        "category_slug": "bun-pho-mi",
        "description": "Tô hủ tiếu Nam Vang đặc sắc miền Nam với sợi hủ tiếu dai dai, nước lèo trong veo ngọt lịm từ xương ống và mực khô, ngập tràn topping tôm sú, thịt nạc, gan, cật heo và tỏi phi thơm nức.",
        "prep_time": 35,
        "cook_time": 60,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 510,
            "protein": 36,
            "carbohydrates": 62,
            "fat": 14,
            "fiber": 2,
            "sodium": 880
        },
        "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Xương ống heo",
                "quantity": 800,
                "unit": "gram",
                "notes": "hầm lấy 2.5 lít nước dùng ngọt"
            },
            {
                "name": "Mực khô, tôm khô",
                "quantity": 50,
                "unit": "gram",
                "notes": "nướng thơm thả nồi hầm lấy vị ngọt"
            },
            {
                "name": "Tôm sú",
                "quantity": 300,
                "unit": "gram",
                "notes": "luộc chín bóc vỏ chừa đuôi"
            },
            {
                "name": "Thịt nạc heo băm",
                "quantity": 200,
                "unit": "gram",
                "notes": "xào săn với tỏi phi"
            },
            {
                "name": "Gan heo, tim heo",
                "quantity": 200,
                "unit": "gram",
                "notes": "luộc chín thái mỏng"
            },
            {
                "name": "Trứng cút luộc",
                "quantity": 8,
                "unit": "quả",
                "notes": "bóc sạch vỏ"
            },
            {
                "name": "Hủ tiếu dai Sa Đéc",
                "quantity": 500,
                "unit": "gram",
                "notes": "chần nước sôi xốc ráo"
            },
            {
                "name": "Cần tàu, hẹ, giá đỗ",
                "quantity": 200,
                "unit": "gram",
                "notes": "rau ăn kèm"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Hầm nước lèo ngọt thanh",
                "description": "Ninh xương ống heo cùng mực khô và tôm khô nướng trong 50 phút, vớt bọt liên tục để nước lèo trong veo ngọt đậm.",
                "timer_minutes": 50
            },
            {
                "step_number": 2,
                "title": "Sơ chế thịt xào và nội tạng",
                "description": "Phi thơm tỏi băm, xào săn thịt heo xay. Luộc chín gan tim và tôm sú, thái lát mỏng vừa ăn.",
                "timer_minutes": 15
            },
            {
                "step_number": 3,
                "title": "Phi tỏi vàng giòn rụm",
                "description": "Băm nhiều tỏi, phi vàng giòn trong dầu ăn làm tóp tỏi phi thơm nức rắc mặt tô hủ tiếu.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Chần sợi hủ tiếu dai",
                "description": "Chần hủ tiếu qua nước sôi cho sợi trong mềm dai, xốc chút mỡ tỏi phi chống dính chia vào 4 tô.",
                "timer_minutes": 5
            },
            {
                "step_number": 5,
                "title": "Chan nước dùng và dọn ăn",
                "description": "Xếp tôm, thịt băm, gan cật, trứng cút, cần tàu và hẹ lên tô. Chan nước lèo sôi sùng sục, rắc tỏi phi vàng giòn lên trên.",
                "timer_minutes": 3
            }
        ]
    },
    {
        "title": "Bánh Xèo Miền Tây Giòn Rụm Tôm Thịt",
        "slug": "banh-xeo-mien-tay-gion-rum-tom-thit",
        "category_slug": "banh-diem-tam",
        "description": "Vỏ bánh xèo vàng ươm mỏng tanh giòn rụm thơm nức mùi nước cốt dừa và bột nghệ, ôm trọn nhân tôm sông ngọt lịm, thịt ba rọi béo ngậy, giá đỗ và đậu xanh cuốn đĩa rau rừng tươi mướt.",
        "prep_time": 30,
        "cook_time": 30,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 480,
            "protein": 24,
            "carbohydrates": 48,
            "fat": 22,
            "fiber": 3,
            "sodium": 690
        },
        "image_url": "https://images.unsplash.com/photo-1509722747041-616f39b57569?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Bột bánh xèo pha sẵn",
                "quantity": 400,
                "unit": "gram",
                "notes": "có sẵn bột nghệ và hành lá"
            },
            {
                "name": "Nước cốt dừa",
                "quantity": 250,
                "unit": "ml",
                "notes": "tạo độ béo thơm giòn xốp"
            },
            {
                "name": "Bia lon",
                "quantity": 100,
                "unit": "ml",
                "notes": "bí quyết giúp vỏ bánh giòn lâu"
            },
            {
                "name": "Tôm đất hoặc tôm sú nhỏ",
                "quantity": 250,
                "unit": "gram",
                "notes": "rửa sạch để nguyên vỏ giòn"
            },
            {
                "name": "Thịt ba chỉ heo",
                "quantity": 250,
                "unit": "gram",
                "notes": "thái lát mỏng xào sơ"
            },
            {
                "name": "Đậu xanh đãi vỏ",
                "quantity": 100,
                "unit": "gram",
                "notes": "hấp chín mềm bở"
            },
            {
                "name": "Giá đỗ tươi",
                "quantity": 200,
                "unit": "gram",
                "notes": "rửa sạch để ráo"
            },
            {
                "name": "Rau cải xanh, xà lách, rau rừng",
                "quantity": 300,
                "unit": "gram",
                "notes": "cuốn bánh xèo"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Pha bột bánh xèo giòn lâu",
                "description": "Khuấy đều bột bánh xèo cùng nước lọc, nước cốt dừa, 100ml bia và hành lá thái nhỏ. Để bột nghỉ 30 phút cho nở đều.",
                "timer_minutes": 30
            },
            {
                "step_number": 2,
                "title": "Xào sơ nhân tôm thịt",
                "description": "Xào tôm và thịt ba rọi trên chảo với chút hành tỏi và hạt nêm cho vừa chín tới.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Đổ bánh xèo xèo giòn tan",
                "description": "Quét lớp dầu mỏng lên chảo lớn thật nóng. Cho tôm thịt vào, múc một vá bột tráng mỏng đều quanh lòng chảo nghe tiếng 'xèo' giòn tai. Đậy nắp 2 phút.",
                "timer_minutes": 4
            },
            {
                "step_number": 4,
                "title": "Cho đậu xanh giá đỗ và gấp bánh",
                "description": "Mở nắp, rải đậu xanh hấp và giá đỗ lên nửa mặt bánh. Rưới chút dầu quanh viền chảo đun lửa nhỏ thêm 2 phút cho đáy bánh giòn rụm rồi gập đôi bánh lại.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Thưởng thức cùng rau rừng",
                "description": "Gắp bánh xèo ra đĩa, cắt miếng vừa ăn cuốn cùng lá cải bẹ xanh, rau thơm chấm nước mắm chua ngọt dưa chua cà rốt.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Cơm Tấm Sườn Bì Chả Sài Gòn",
        "slug": "com-tam-suon-bi-cha-sai-gon",
        "category_slug": "banh-diem-tam",
        "description": "Đĩa cơm tấm gạo tấm thơm nức quyện mỡ hành óng ả, sườn cốt lết nướng mật ong sém cạnh thơm lừng, chả trứng hấp béo bùi, bì heo dai giòn và nước mắm kẹo ớt tỏi.",
        "prep_time": 35,
        "cook_time": 45,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 620,
            "protein": 38,
            "carbohydrates": 68,
            "fat": 24,
            "fiber": 2,
            "sodium": 890
        },
        "image_url": "https://images.unsplash.com/photo-1509722747041-616f39b57569?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Gạo tấm thơm",
                "quantity": 400,
                "unit": "gram",
                "notes": "nấu chín tới xới tơi"
            },
            {
                "name": "Sườn cốt lết heo",
                "quantity": 4,
                "unit": "miếng",
                "notes": "dần mềm thịt trước khi ướp"
            },
            {
                "name": "Bì heo thái sợi và thính gạo",
                "quantity": 150,
                "unit": "gram",
                "notes": "trộn đều thơm bùi"
            },
            {
                "name": "Trứng gà và thịt băm làm chả trứng",
                "quantity": 3,
                "unit": "quả",
                "notes": "hấp vàng mặt lòng đỏ"
            },
            {
                "name": "Mỡ hành",
                "quantity": 4,
                "unit": "muỗng canh",
                "notes": "hành lá phi dầu sôi rưới cơm"
            },
            {
                "name": "Đồ chua củ cải cà rốt",
                "quantity": 100,
                "unit": "gram",
                "notes": "ăn kèm chống ngấy"
            },
            {
                "name": "Nước mắm kẹo chua ngọt",
                "quantity": 1,
                "unit": "chén",
                "notes": "nước mắm cơm tấm chuẩn vị"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Ướp sườn nướng đậm đà",
                "description": "Dần mềm miếng sườn, ướp với mật ong, nước tương, dầu hào, tỏi băm, sữa đặc và nước cốt hành trong 45 phút.",
                "timer_minutes": 45
            },
            {
                "step_number": 2,
                "title": "Làm chả trứng hấp",
                "description": "Trộn thịt băm, mộc nhĩ, miến, 2 lòng đỏ và lòng trắng trứng hấp cách thủy 20 phút. Quét 1 lòng đỏ trứng lên mặt hấp thêm 5 phút không đậy nắp cho vàng đẹp.",
                "timer_minutes": 25
            },
            {
                "step_number": 3,
                "title": "Nướng sườn cốt lết than hoa",
                "description": "Nướng sườn trên than hồng khoảng 15 phút, trở đều hai mặt đến khi sườn chín vàng óng và cháy cạnh thơm ngát.",
                "timer_minutes": 15
            },
            {
                "step_number": 4,
                "title": "Nấu cơm tấm xới tơi",
                "description": "Vo gạo tấm nấu chín vừa nước, xới tơi xốp giữ nóng ấm trong nồi.",
                "timer_minutes": 20
            },
            {
                "step_number": 5,
                "title": "Bày đĩa cơm tấm Sài Gòn",
                "description": "Xới cơm tấm vào đĩa, đặt miếng sườn nướng, lát chả trứng, nhúm bì trộn thính, rưới mỡ hành bóng bẩy, ăn kèm đồ chua dưa leo và nước mắm kẹo.",
                "timer_minutes": 3
            }
        ]
    },
    {
        "title": "Bánh Cuốn Nóng Thịt Băm Mộc Nhĩ",
        "slug": "banh-cuon-nong-thit-bam-moc-nhi",
        "category_slug": "banh-diem-tam",
        "description": "Từng cuốn bánh tráng mỏng tang trắng muốt mềm mượt, cuộn đầy ắp nhân thịt nạc băm xào mộc nhĩ hành khô thơm lừng, rắc ruốc tôm và hành phi giòn rụm chấm nước mắm cà cuống.",
        "prep_time": 30,
        "cook_time": 25,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 360,
            "protein": 20,
            "carbohydrates": 48,
            "fat": 12,
            "fiber": 2,
            "sodium": 680
        },
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Bột bánh cuốn (bột gạo & bột năng)",
                "quantity": 400,
                "unit": "gram",
                "notes": "pha nước tỷ lệ chuẩn ngâm qua đêm"
            },
            {
                "name": "Thịt nạc vai băm",
                "quantity": 300,
                "unit": "gram",
                "notes": "xào nhân"
            },
            {
                "name": "Mộc nhĩ, nấm hương băm nhỏ",
                "quantity": 40,
                "unit": "gram",
                "notes": "ngâm nở băm nhuyễn"
            },
            {
                "name": "Hành phi vàng giòn rụm",
                "quantity": 50,
                "unit": "gram",
                "notes": "rắc lên mặt bánh"
            },
            {
                "name": "Chả lụa hoặc chả quế",
                "quantity": 200,
                "unit": "gram",
                "notes": "thái lát ăn kèm"
            },
            {
                "name": "Nước mắm chấm bánh cuốn pha ấm",
                "quantity": 1,
                "unit": "bát",
                "notes": "chua ngọt dịu nhẹ"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Pha bột bánh cuốn mỏng mượt",
                "description": "Hòa tan bột gạo, bột năng với nước lọc, 1 muỗng dầu ăn và chút muối, để bột nghỉ cho lắng trong.",
                "timer_minutes": 15
            },
            {
                "step_number": 2,
                "title": "Xào nhân thịt mộc nhĩ thơm lừng",
                "description": "Phi thơm hành tím, trút thịt băm, mộc nhĩ và nấm hương vào xào săn trên lửa lớn, nêm chút hạt tiêu và nước mắm.",
                "timer_minutes": 8
            },
            {
                "step_number": 3,
                "title": "Tráng bánh cuốn mỏng tang",
                "description": "Múc bột láng thật mỏng lên mặt chảo chống dính hoặc nồi căng vải hấp trong 40 giây cho bánh trong suốt chín mượt.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Cuộn bánh nhanh tay",
                "description": "Úp bánh ra mâm thoa dầu, múc nhân thịt rải đều rồi cuộn tròn lại.",
                "timer_minutes": 10
            },
            {
                "step_number": 5,
                "title": "Thưởng thức đĩa bánh cuốn nóng",
                "description": "Cắt bánh thành khúc, xếp chả quế, rắc nhiều hành phi giòn tan và rau mùi ta, chấm nước mắm pha ấm nóng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Bánh Mì Chảo Pa Tê Trứng Lòng Đào",
        "slug": "banh-mi-chao-pa-te-trung-long-dao",
        "category_slug": "banh-diem-tam",
        "description": "Chiếc chảo gang nóng rực xèo xèo với pa-tê gan béo ngậy tan chảy, trứng gà ốp la lòng đào vàng ươm, xúc xích rán giòn và sốt cà chua sánh đỏ chấm ổ bánh mì nóng giòn rụm.",
        "prep_time": 15,
        "cook_time": 12,
        "servings": 2,
        "difficulty": 1,
        "nutrition": {
            "calories": 520,
            "protein": 26,
            "carbohydrates": 46,
            "fat": 28,
            "fiber": 2,
            "sodium": 850
        },
        "image_url": "https://images.unsplash.com/photo-1509722747041-616f39b57569?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Bánh mì giòn",
                "quantity": 2,
                "unit": "ổ",
                "notes": "nướng giòn rụm"
            },
            {
                "name": "Pa-tê gan heo thơm béo",
                "quantity": 100,
                "unit": "gram",
                "notes": "cắt lát dày"
            },
            {
                "name": "Trứng gà tươi",
                "quantity": 2,
                "unit": "quả",
                "notes": "ốp la lòng đào"
            },
            {
                "name": "Xúc xích Đức hoặc xông khói",
                "quantity": 2,
                "unit": "cây",
                "notes": "khía xéo chiên giòn"
            },
            {
                "name": "Bò thăn thái mỏng",
                "quantity": 100,
                "unit": "gram",
                "notes": "xào sơ"
            },
            {
                "name": "Nước sốt cà chua tiêu đen",
                "quantity": 100,
                "unit": "ml",
                "notes": "đun sền sệt rưới chảo"
            },
            {
                "name": "Bơ lạt",
                "quantity": 15,
                "unit": "gram",
                "notes": "đun tan chảy xèo xèo"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Làm nóng chảo gang và đun bơ",
                "description": "Đặt chảo gang nhỏ lên bếp đun thật nóng, cho miếng bơ lạt vào đun tan chảy thơm lừng.",
                "timer_minutes": 2
            },
            {
                "step_number": 2,
                "title": "Chiên xúc xích và áp chảo pa-tê",
                "description": "Cho xúc xích khía hoa và miếng pa-tê gan vào áp chảo cho sém cạnh dậy mùi thơm.",
                "timer_minutes": 3
            },
            {
                "step_number": 3,
                "title": "Ốp la trứng lòng đào",
                "description": "Đập trứng gà vào giữa chảo, chiên lửa vừa giữ lòng đỏ còn béo ngậy mềm ướt.",
                "timer_minutes": 3
            },
            {
                "step_number": 4,
                "title": "Rưới sốt cà chua tiêu sánh đỏ",
                "description": "Đổ sốt cà chua sánh đỏ vào chảo đun sôi sùng sục quanh các nguyên liệu.",
                "timer_minutes": 2
            },
            {
                "step_number": 5,
                "title": "Thưởng thức chảo bánh mì nóng hổi",
                "description": "Nhấc chảo ra đế lót gỗ, rắc tiêu xay và ngò rí, bẻ bánh mì giòn tan chấm đẫm sốt và lòng đỏ trứng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Nấm Đùi Gà Kho Tiêu Chay Đậm Vị",
        "slug": "nam-dui-ga-kho-tieu-chay-dam-vi",
        "category_slug": "mon-chay",
        "description": "Nấm đùi gà dai ngọt tự nhiên cắt khoanh khía hoa ngấm đẫm sốt nước tương caramen, thơm nồng tiêu đen xay cay cay, món kho chay hao cơm số một.",
        "prep_time": 15,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 180,
            "protein": 10,
            "carbohydrates": 22,
            "fat": 6,
            "fiber": 4,
            "sodium": 580
        },
        "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Nấm đùi gà tươi",
                "quantity": 400,
                "unit": "gram",
                "notes": "cắt khoanh dày 2cm, khía vảy rồng hai mặt"
            },
            {
                "name": "Nước tương ngon (xì dầu)",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "tạo vị đậm đà thanh tịnh"
            },
            {
                "name": "Dầu hào chay",
                "quantity": 1.5,
                "unit": "muỗng canh",
                "notes": "tạo độ sánh bóng"
            },
            {
                "name": "Đường nâu",
                "quantity": 1.5,
                "unit": "muỗng canh",
                "notes": "thắng màu cánh gián"
            },
            {
                "name": "Tiêu xanh hoặc tiêu đen xay",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "tiêu giã dập thơm nồng"
            },
            {
                "name": "Hành boa-rô (tỏi tây)",
                "quantity": 1,
                "unit": "cây",
                "notes": "thay thế hành tỏi cho món chay"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế nấm đùi gà",
                "description": "Nấm ngâm nước muối loãng 5 phút, rửa sạch vắt nhẹ ráo nước, cắt khoanh tròn và dùng dao khía caro hai mặt để ngấm sốt.",
                "timer_minutes": 7
            },
            {
                "step_number": 2,
                "title": "Áp chảo nấm vàng thơm",
                "description": "Cho chút dầu vào chảo chiên áp chảo hai mặt nấm đùi gà cho vàng xém nhẹ giúp nấm dai giòn ngon.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Thắng sốt kho tiêu",
                "description": "Phi thơm hành boa-rô, cho nước tương, dầu hào chay, đường nâu và tiêu vào đun sôi sền sệt.",
                "timer_minutes": 3
            },
            {
                "step_number": 4,
                "title": "Kho nấm đùi gà ngấm vị",
                "description": "Trút nấm vào nồi sốt, thêm 1/2 chén nước ấm, đun lửa nhỏ liu riu trong 10 phút đến khi nước sốt keo lại bám đều quanh từng khoanh nấm.",
                "timer_minutes": 10
            },
            {
                "step_number": 5,
                "title": "Hoàn thiện món kho chay",
                "description": "Rắc nhiều tiêu xay và ớt hiểm cắt lát, múc ra tộ đất ăn cùng cơm gạo lứt hoặc cơm trắng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Đậu Hũ Sốt Cà Chua Nấm Hương Chay",
        "slug": "dau-hu-sot-ca-chua-nam-huong-chay",
        "category_slug": "mon-chay",
        "description": "Đậu hũ chiên vàng giòn bên ngoài mềm béo bên trong, om cùng sốt cà chua đỏ tươi và nấm hương ngát hương thanh khiết cho bữa cơm chay gia đình.",
        "prep_time": 15,
        "cook_time": 15,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 220,
            "protein": 14,
            "carbohydrates": 16,
            "fat": 12,
            "fiber": 3,
            "sodium": 520
        },
        "image_url": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Đậu hũ trắng miếng",
                "quantity": 4,
                "unit": "miếng",
                "notes": "cắt khối vuông chiên vàng"
            },
            {
                "name": "Cà chua chín mọng",
                "quantity": 3,
                "unit": "quả",
                "notes": "băm nhỏ làm sốt"
            },
            {
                "name": "Nấm hương khô",
                "quantity": 10,
                "unit": "cái",
                "notes": "ngâm nở giữ lại nước nấm"
            },
            {
                "name": "Hành boa-rô",
                "quantity": 1,
                "unit": "cây",
                "notes": "phi thơm"
            },
            {
                "name": "Hạt nêm nấm chay",
                "quantity": 1.5,
                "unit": "muỗng cà phê",
                "notes": "vị thanh"
            },
            {
                "name": "Rau mùi, hành ngò",
                "quantity": 30,
                "unit": "gram",
                "notes": "rắc lên bề mặt"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Chiên vàng đậu hũ",
                "description": "Cắt đậu hũ thành khối vuông nhỏ, chiên trong chảo dầu nóng đến khi vàng đều các mặt rồi vớt ra ráo dầu.",
                "timer_minutes": 6
            },
            {
                "step_number": 2,
                "title": "Nấm hương ngâm nở",
                "description": "Nấm hương ngâm nước ấm cho mềm, rửa sạch cắt đôi, giữ lại phần nước nấm trong.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Làm sốt cà chua nấm",
                "description": "Phi thơm hành boa-rô, trút cà chua băm và nấm hương vào xào mềm nhừ cùng chút hạt nêm chay.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Om đậu hũ ngấm sốt",
                "description": "Cho đậu hũ chiên vào chảo sốt, châm thêm 1/2 chén nước ngâm nấm đun lửa nhỏ trong 6 phút cho đậu ngấm đượm sốt cà chua.",
                "timer_minutes": 6
            },
            {
                "step_number": 5,
                "title": "Trình bày",
                "description": "Múc ra đĩa sâu lòng, rắc ngò rí và tiêu xay lên trên, ăn nóng cùng cơm trắng.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Canh Chua Chay Nấm Rơm Đậu Bắp",
        "slug": "canh-chua-chay-nam-rom-dau-bap",
        "category_slug": "mon-chay",
        "description": "Nồi canh chua thuần chay mát lành với vị chua dịu từ me chín, ngọt thanh từ nấm rơm tươi và thơm chín mọng, giòn mát từ dọc mùng đậu bắp giá đỗ.",
        "prep_time": 20,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 160,
            "protein": 8,
            "carbohydrates": 24,
            "fat": 4,
            "fiber": 4,
            "sodium": 490
        },
        "image_url": "https://images.unsplash.com/photo-1547592180-85f173990554?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Nấm rơm tươi",
                "quantity": 200,
                "unit": "gram",
                "notes": "cắt chân ngâm muối chẻ đôi"
            },
            {
                "name": "Đậu hũ non",
                "quantity": 1,
                "unit": "hộp",
                "notes": "cắt khối vuông nhỏ"
            },
            {
                "name": "Thơm (dứa)",
                "quantity": 0.25,
                "unit": "quả",
                "notes": "cắt lát tam giác"
            },
            {
                "name": "Cà chua",
                "quantity": 2,
                "unit": "quả",
                "notes": "bổ múi cau"
            },
            {
                "name": "Đậu bắp, dọc mùng",
                "quantity": 100,
                "unit": "gram",
                "notes": "rửa sạch thái xéo"
            },
            {
                "name": "Giá đỗ sạch",
                "quantity": 100,
                "unit": "gram",
                "notes": "nhặt sạch gốc"
            },
            {
                "name": "Nước cốt me chua",
                "quantity": 3,
                "unit": "muỗng canh",
                "notes": "tạo vị chua thanh"
            },
            {
                "name": "Ngò gai, ngò ôm",
                "quantity": 30,
                "unit": "gram",
                "notes": "thái nhỏ"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Sơ chế nấm và rau củ",
                "description": "Nấm rơm làm sạch chẻ đôi. Dọc mùng bóp muối xả sạch vắt ráo. Thơm và cà chua cắt miếng vừa ăn.",
                "timer_minutes": 8
            },
            {
                "step_number": 2,
                "title": "Xào thơm nấm rơm",
                "description": "Phi thơm hành boa-rô, cho nấm rơm, thơm và cà chua vào xào sơ 2 phút cho dậy mùi.",
                "timer_minutes": 3
            },
            {
                "step_number": 3,
                "title": "Nấu nước canh chua thanh",
                "description": "Đổ 1 lít nước sôi vào nồi, thêm nước cốt me, đường phèn, muối hạt và hạt nêm chay nêm vừa khẩu vị chua thanh ngọt dịu.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Cho đậu bắp dọc mùng và đậu hũ",
                "description": "Cho đậu bắp, dọc mùng và đậu hũ non vào nấu sôi thêm 3 phút. Cuối cùng cho giá đỗ vào tắt bếp.",
                "timer_minutes": 4
            },
            {
                "step_number": 5,
                "title": "Hoàn thành tô canh chua chay",
                "description": "Múc canh ra tô, rắc ngò ôm ngò gai thái nhỏ và vài lát ớt sừng, dùng kèm cơm nóng thanh đạm.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Sườn Non Chay Chiên Giòn Lắc Phô Mai",
        "slug": "suon-non-chay-chien-gion-lac-pho-mai",
        "category_slug": "mon-chay",
        "description": "Sườn non chay làm từ đậu nành ngâm mềm ép ráo chiên phồng giòn rụm ráo dầu, lắc đều lớp bột phô mai béo mặn thơm lừng món ăn vặt hoặc ăn cơm đều mê ly.",
        "prep_time": 20,
        "cook_time": 15,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 310,
            "protein": 18,
            "carbohydrates": 28,
            "fat": 14,
            "fiber": 4,
            "sodium": 560
        },
        "image_url": "https://images.unsplash.com/photo-1562967914-608f82629710?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Sườn non đậu nành chay",
                "quantity": 200,
                "unit": "gram",
                "notes": "ngâm nước ấm 20 phút cho nở mềm"
            },
            {
                "name": "Bột phô mai lắc",
                "quantity": 30,
                "unit": "gram",
                "notes": "loại phô mai mặn ngọt thơm béo"
            },
            {
                "name": "Hạt nêm chay",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "ướp nhẹ sườn"
            },
            {
                "name": "Dầu ăn",
                "quantity": 300,
                "unit": "ml",
                "notes": "chiên giòn ngập dầu"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Ngâm và vắt ráo sườn chay",
                "description": "Ngâm miếng sườn chay vào nước ấm đến khi nở mềm hoàn toàn, rửa lại nhiều lần và dùng tay vắt kiệt nước để khi chiên sườn giòn tan.",
                "timer_minutes": 15
            },
            {
                "step_number": 2,
                "title": "Xé sợi hoặc cắt miếng",
                "description": "Xé sườn chay thành sợi bản vừa hoặc cắt miếng vuông vừa ăn, rắc xíu hạt nêm trộn đều.",
                "timer_minutes": 5
            },
            {
                "step_number": 3,
                "title": "Chiên giòn sườn chay",
                "description": "Đun sôi dầu ăn, thả sườn chay vào chiên lửa vừa đến khi sườn phồng xốp và ngả màu vàng giòn rụm thì vớt ra khay ráo dầu.",
                "timer_minutes": 8
            },
            {
                "step_number": 4,
                "title": "Lắc bột phô mai",
                "description": "Cho sườn chiên còn ấm vào hộp kín, rắc bột phô mai lên đậy nắp lắc đều tay cho bột bám kín quanh từng miếng sườn.",
                "timer_minutes": 2
            },
            {
                "step_number": 5,
                "title": "Thưởng thức giòn tan",
                "description": "Đổ ra đĩa ăn ngay cảm nhận độ giòn tan rụm và vị béo mặn thơm ngậy của phô mai.",
                "timer_minutes": 1
            }
        ]
    },
    {
        "title": "Chả Giò Chay Khoai Môn Đậu Xanh",
        "slug": "cha-gio-chay-khoai-mon-dau-xanh",
        "category_slug": "mon-chay",
        "description": "Cuốn chả giò chay vàng ruộm giòn tan rôm rốp, nhân khoai môn bở bùi quyện đậu xanh thơm ngậy, mộc nhĩ nấm hương giòn sần sật chấm tương xí muội chua ngọt.",
        "prep_time": 25,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 330,
            "protein": 12,
            "carbohydrates": 42,
            "fat": 14,
            "fiber": 4,
            "sodium": 490
        },
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Khoai môn cao bào sợi",
                "quantity": 200,
                "unit": "gram",
                "notes": "vắt ráo nước"
            },
            {
                "name": "Đậu xanh cà vỏ",
                "quantity": 100,
                "unit": "gram",
                "notes": "hấp chín tán nhuyễn"
            },
            {
                "name": "Nấm mèo, nấm hương",
                "quantity": 30,
                "unit": "gram",
                "notes": "ngâm nở thái sợi"
            },
            {
                "name": "Cà rốt thái sợi chỉ",
                "quantity": 1,
                "unit": "củ",
                "notes": "tạo màu đẹp"
            },
            {
                "name": "Miến dong cắt ngắn",
                "quantity": 30,
                "unit": "gram",
                "notes": "ngâm mềm"
            },
            {
                "name": "Bánh tráng bía xốp",
                "quantity": 25,
                "unit": "lá",
                "notes": "cuốn chả giò"
            },
            {
                "name": "Hạt nêm chay, tiêu xay",
                "quantity": 1,
                "unit": "muỗng canh",
                "notes": "nêm nhân"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Trộn nhân chả giò chay",
                "description": "Trộn khoai môn bào sợi, đậu xanh tán nhuyễn, nấm mèo, nấm hương, cà rốt và miến cùng hạt nêm chay, tiêu xay thật đều.",
                "timer_minutes": 10
            },
            {
                "step_number": 2,
                "title": "Cuốn chả giò đều đẹp",
                "description": "Trải bánh tráng bía ra, cho nhân vào giữa cuộn tròn chặt tay, dán mép bánh bằng hồ nước bột năng.",
                "timer_minutes": 12
            },
            {
                "step_number": 3,
                "title": "Chiên chả giò giòn rụm",
                "description": "Thả từng cuốn chả giò vào chảo dầu sôi ngập, chiên lửa vừa khoảng 6-8 phút cho vàng giòn đều rồi vớt ra giấy thấm dầu.",
                "timer_minutes": 8
            },
            {
                "step_number": 4,
                "title": "Thấm dầu và giữ giòn",
                "description": "Để chả giò đứng trên khay lưới cho róc hết dầu thừa giữ độ giòn lâu.",
                "timer_minutes": 3
            },
            {
                "step_number": 5,
                "title": "Trình bày và thưởng thức",
                "description": "Xếp ra đĩa ăn kèm xà lách, rau thơm và chấm tương xí muội hoặc nước mắm chua ngọt chay.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Chè Bưởi An Giang Giòn Sần Sật Nước Cốt Dừa",
        "slug": "che-buoi-an-giang-gion-san-sat-nuoc-cot-dua",
        "category_slug": "mon-trang-mieng",
        "description": "Từng viên cùi bưởi trong veo giòn sần sật không chút đắng chát, hòa quyện đậu xanh bở bùi trong nước đường phèn hoa bưởi thoang thoảng, chan nước cốt dừa béo ngậy mê ly.",
        "prep_time": 40,
        "cook_time": 30,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 320,
            "protein": 8,
            "carbohydrates": 56,
            "fat": 9,
            "fiber": 3,
            "sodium": 120
        },
        "image_url": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Cùi bưởi da xanh hoặc năm roi",
                "quantity": 1,
                "unit": "trái",
                "notes": "gọt bỏ vỏ xanh, lấy phần cùi trắng xốp thái hạt lựu"
            },
            {
                "name": "Đậu xanh đãi vỏ",
                "quantity": 150,
                "unit": "gram",
                "notes": "ngâm nở hấp chín nguyên hạt"
            },
            {
                "name": "Bột năng cao cấp",
                "quantity": 150,
                "unit": "gram",
                "notes": "áo cùi bưởi và tạo độ sánh cho chè"
            },
            {
                "name": "Đường phèn",
                "quantity": 200,
                "unit": "gram",
                "notes": "tạo vị ngọt thanh tao"
            },
            {
                "name": "Nước cốt dừa sánh béo",
                "quantity": 250,
                "unit": "ml",
                "notes": "nấu cốt dừa chan lên mặt chè"
            },
            {
                "name": "Tinh dầu hoa bưởi",
                "quantity": 3,
                "unit": "giọt",
                "notes": "tạo hương thơm cổ truyền"
            },
            {
                "name": "Muối hạt",
                "quantity": 2,
                "unit": "muỗng canh",
                "notes": "bóp khử đắng cùi bưởi"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Khử đắng cùi bưởi giòn tan",
                "description": "Thái cùi bưởi hạt lựu 1.5cm. Bóp kỹ với muối hạt nhiều lần và xả nước sạch 5-6 lần đến khi nếm cùi bưởi hết sạch vị đắng. Luộc cùi bưởi qua nước sôi 1 phút rồi vớt ngâm ngay nước đá lạnh, vắt nhẹ ráo nước.",
                "timer_minutes": 25
            },
            {
                "step_number": 2,
                "title": "Sên đường và áo bột năng cùi bưởi",
                "description": "Trộn cùi bưởi với 50g đường cho ngấm ngọt trong veo. Lăn cùi bưởi qua lớp bột năng thật dày cho bám đều từng viên.",
                "timer_minutes": 10
            },
            {
                "step_number": 3,
                "title": "Luộc cùi bưởi trong suốt",
                "description": "Thả cùi bưởi áo bột vào nồi nước sôi luộc đến khi cùi nổi lên trong suốt, vớt ra ngâm ngay vào âu nước đá để cùi bưởi giòn sần sật.",
                "timer_minutes": 6
            },
            {
                "step_number": 4,
                "title": "Nấu chè đậu xanh sánh mịn",
                "description": "Đun sôi 1 lít nước với đường phèn. Hòa tan 3 muỗng bột năng rót từ từ khuấy đều tạo độ sánh trong. Cho đậu xanh đã hấp chín và cùi bưởi vào khuấy đều, thêm vài giọt tinh dầu hoa bưởi rồi tắt bếp.",
                "timer_minutes": 10
            },
            {
                "step_number": 5,
                "title": "Thưởng thức chè bưởi",
                "description": "Múc chè ra ly hoặc chén, chan nước cốt dừa béo ngậy lên trên, thêm đá bào mát lạnh giải nhiệt sảng khoái.",
                "timer_minutes": 2
            }
        ]
    },
    {
        "title": "Chè Hạt Sen Long Nhãn Thanh Nhiệt",
        "slug": "che-hat-sen-long-nhan-thanh-nhiet",
        "category_slug": "mon-trang-mieng",
        "description": "Món tráng miệng cung đình Huế thanh tao với từng viên hạt sen bùi bở bọc khéo léo trong cùi nhãn lồng giòn ngọt mọng nước, nước đường phèn trong vắt dịu ngọt êm ái.",
        "prep_time": 30,
        "cook_time": 25,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 240,
            "protein": 6,
            "carbohydrates": 52,
            "fat": 2,
            "fiber": 2,
            "sodium": 80
        },
        "image_url": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Hạt sen tươi Huế",
                "quantity": 250,
                "unit": "gram",
                "notes": "thông tâm sen đắng, rửa sạch"
            },
            {
                "name": "Nhãn lồng tươi (hoặc long nhãn khô)",
                "quantity": 500,
                "unit": "gram",
                "notes": "tách vỏ bóc hạt khéo léo"
            },
            {
                "name": "Đường phèn kết tinh",
                "quantity": 180,
                "unit": "gram",
                "notes": "vị ngọt thanh không gắt"
            },
            {
                "name": "Lá dứa (lá nếp)",
                "quantity": 3,
                "unit": "lá",
                "notes": "bó lại nấu lấy hương thơm mát"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Hấp chín hạt sen bở bùi",
                "description": "Hạt sen tươi thông tâm, cho vào xửng hấp chín tới trong 15 phút để hạt sen bở bùi nhưng không bị nát vỡ.",
                "timer_minutes": 15
            },
            {
                "step_number": 2,
                "title": "Tách cùi nhãn lồng",
                "description": "Dùng mũi dao nhỏ khía quanh cuống hạt nhãn tách bỏ hạt, giữ cùi nhãn nguyên vẹn không rách.",
                "timer_minutes": 15
            },
            {
                "step_number": 3,
                "title": "Lồng hạt sen vào cùi nhãn",
                "description": "Khéo léo nhồi từng viên hạt sen hấp vào trong ruột cùi nhãn ôm trọn tròn xoe.",
                "timer_minutes": 10
            },
            {
                "step_number": 4,
                "title": "Nấu nước đường phèn lá dứa",
                "description": "Đun sôi 800ml nước với đường phèn và bó lá dứa cho tan trong vắt, vớt bỏ lá dứa.",
                "timer_minutes": 8
            },
            {
                "step_number": 5,
                "title": "Nấu chè và thưởng thức",
                "description": "Thả long nhãn bọc hạt sen vào nước đường đun sôi lăn tăn 2 phút rồi tắt bếp ngay để nhãn giữ độ giòn ngọt. Dùng lạnh kèm đá bào.",
                "timer_minutes": 3
            }
        ]
    },
    {
        "title": "Bánh Flan Caramel Mềm Mịn Thơm Béo",
        "slug": "banh-flan-caramel-mem-min-thom-beo",
        "category_slug": "mon-trang-mieng",
        "description": "Từng chiếc bánh flan caramel núng nính mềm mịn tan ngay trên đầu lưỡi, vị béo ngậy thơm lừng của trứng sữa tươi quyện sốt caramel đắng ngọt và cà phê đen đá.",
        "prep_time": 20,
        "cook_time": 35,
        "servings": 6,
        "difficulty": 2,
        "nutrition": {
            "calories": 280,
            "protein": 8,
            "carbohydrates": 36,
            "fat": 12,
            "fiber": 1,
            "sodium": 140
        },
        "image_url": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Trứng gà tươi",
                "quantity": 5,
                "unit": "quả",
                "notes": "dùng 3 quả nguyên và 2 lòng đỏ"
            },
            {
                "name": "Sữa tươi không đường",
                "quantity": 400,
                "unit": "ml",
                "notes": "hâm ấm nóng"
            },
            {
                "name": "Sữa đặc có đường",
                "quantity": 120,
                "unit": "gram",
                "notes": "tạo vị ngọt béo"
            },
            {
                "name": "Đường cát trắng",
                "quantity": 80,
                "unit": "gram",
                "notes": "thắng sốt caramel"
            },
            {
                "name": "Vani chiết xuất",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "khử mùi tanh trứng"
            },
            {
                "name": "Khuôn nhôm hoặc hũ thủy tinh",
                "quantity": 8,
                "unit": "khuôn",
                "notes": "đựng bánh flan"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Thắng sốt caramel cánh gián",
                "description": "Đun đường với chút nước trên lửa nhỏ đến khi chuyển màu cánh gián hổ phách, nhanh tay múc tráng một lớp mỏng đáy khuôn.",
                "timer_minutes": 7
            },
            {
                "step_number": 2,
                "title": "Khuấy hỗn hợp trứng sữa mịn màng",
                "description": "Đánh tan trứng nhẹ tay một chiều không tạo bọt khí. Đun ấm sữa tươi cùng sữa đặc rồi rót từ từ vào âu trứng khuấy đều cùng vani.",
                "timer_minutes": 8
            },
            {
                "step_number": 3,
                "title": "Lọc hỗn hợp qua rây 2 lần",
                "description": "Rây hỗn hợp trứng sữa 2-3 lần để loại bỏ hoàn toàn lợn cợn giúp bánh flan khi hấp láng mịn không bị rỗ.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Hấp cách thủy lửa thật nhỏ",
                "description": "Rót hỗn hợp vào các khuôn caramel, đậy nắp hoặc bọc giấy bạc. Hấp lửa thật nhỏ trong 25-30 phút không để nước sôi sùng sục làm rỗ bánh.",
                "timer_minutes": 30
            },
            {
                "step_number": 5,
                "title": "Ướp lạnh và thưởng thức",
                "description": "Bánh chín để nguội cho vào ngăn mát tủ lạnh 3 tiếng. Úp ngược bánh ra đĩa, chan chút cà phê đen đá bào mát rượi.",
                "timer_minutes": 3
            }
        ]
    },
    {
        "title": "Chè Khúc Bạch Hạnh Nhân Thanh Mát",
        "slug": "che-khuc-bach-hanh-nhan-thanh-mat",
        "category_slug": "mon-trang-mieng",
        "description": "Từng viên khúc bạch sữa phô mai và matcha mềm dẻo béo ngậy cắt lượn sóng bắt mắt, ăn cùng nhãn tươi giòn ngọt, hạnh nhân lát rang vàng ruộm và nước đường phèn ướp hoa bưởi thanh khiết.",
        "prep_time": 30,
        "cook_time": 20,
        "servings": 4,
        "difficulty": 2,
        "nutrition": {
            "calories": 290,
            "protein": 8,
            "carbohydrates": 42,
            "fat": 10,
            "fiber": 2,
            "sodium": 90
        },
        "image_url": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Whipping cream (kem sữa béo)",
                "quantity": 250,
                "unit": "ml",
                "notes": "tạo độ béo ngậy mềm mịn"
            },
            {
                "name": "Sữa tươi không đường",
                "quantity": 250,
                "unit": "ml",
                "notes": "nấu cùng gelatin"
            },
            {
                "name": "Gelatin lá hoặc bột",
                "quantity": 25,
                "unit": "gram",
                "notes": "ngâm nở tạo độ dẻo núng nính"
            },
            {
                "name": "Bột trà xanh matcha",
                "quantity": 1,
                "unit": "muỗng cà phê",
                "notes": "làm khúc bạch màu xanh"
            },
            {
                "name": "Hạnh nhân lát",
                "quantity": 40,
                "unit": "gram",
                "notes": "rang vàng giòn thơm"
            },
            {
                "name": "Trái vải hoặc nhãn tươi",
                "quantity": 300,
                "unit": "gram",
                "notes": "bóc vỏ bỏ hạt"
            },
            {
                "name": "Đường phèn",
                "quantity": 150,
                "unit": "gram",
                "notes": "nấu nước đường thanh mát"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Nấu hỗn hợp khúc bạch sữa",
                "description": "Ngâm nở gelatin. Đun ấm whipping cream, sữa tươi và đường, cho gelatin đã vắt ráo vào khuấy tan hoàn toàn.",
                "timer_minutes": 8
            },
            {
                "step_number": 2,
                "title": "Đổ khuôn tạo màu trắng và matcha",
                "description": "Chia hỗn hợp làm 2 phần: 1 phần giữ nguyên màu trắng, 1 phần hòa tan bột trà xanh matcha. Rót vào khuôn để ngăn mát tủ lạnh 4 tiếng cho đông dẻo.",
                "timer_minutes": 10
            },
            {
                "step_number": 3,
                "title": "Nấu nước đường vải nhãn",
                "description": "Đun sôi nước với đường phèn cho tan, thả cùi vải/nhãn vào đun 2 phút rồi tắt bếp để nguội ướp lạnh.",
                "timer_minutes": 8
            },
            {
                "step_number": 4,
                "title": "Cắt khúc bạch lượn sóng",
                "description": "Dùng dao lượn sóng cắt thạch khúc bạch thành các khối vuông quân cờ đều đặn.",
                "timer_minutes": 5
            },
            {
                "step_number": 5,
                "title": "Múc chè và rắc hạnh nhân",
                "description": "Xếp các viên khúc bạch trắng và xanh vào bát, múc vải nhãn và nước đường thanh mát chan ngập, rắc hạnh nhân lát rang giòn lên trên.",
                "timer_minutes": 3
            }
        ]
    },
    {
        "title": "Trà Đào Cam Sả Tươi Mát Giải Nhiệt",
        "slug": "tra-dao-cam-sa-tuoi-mat-giai-nhiet",
        "category_slug": "mon-trang-mieng",
        "description": "Thức uống giải khát quốc dân với vị trà đen đậm đà thơm ngát hương sả tươi, vị chua ngọt sảng khoái của cam vàng mọng nước và từng miếng đào ngâm giòn sần sật mát lạnh.",
        "prep_time": 15,
        "cook_time": 10,
        "servings": 4,
        "difficulty": 1,
        "nutrition": {
            "calories": 160,
            "protein": 2,
            "carbohydrates": 38,
            "fat": 1,
            "fiber": 2,
            "sodium": 40
        },
        "image_url": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=1200&auto=format&fit=crop",
        "ingredients": [
            {
                "name": "Trà đen túi lọc (hoặc trà Earl Grey)",
                "quantity": 4,
                "unit": "gói",
                "notes": "ủ lấy cốt trà đậm đà"
            },
            {
                "name": "Đào ngâm đóng hộp",
                "quantity": 1,
                "unit": "hộp",
                "notes": "lấy 8 miếng đào giòn và nước sốt đào"
            },
            {
                "name": "Cam vàng Mỹ hoặc cam sành",
                "quantity": 2,
                "unit": "trái",
                "notes": "vắt nước và cắt lát trang trí"
            },
            {
                "name": "Sả cây",
                "quantity": 4,
                "unit": "cây",
                "notes": "đập dập cắt khúc nấu lấy nước cốt sả"
            },
            {
                "name": "Đường phèn hoặc mật ong",
                "quantity": 50,
                "unit": "gram",
                "notes": "tạo vị ngọt dịu thanh"
            },
            {
                "name": "Đá viên mát lạnh",
                "quantity": 1,
                "unit": "tô",
                "notes": "pha chế"
            }
        ],
        "steps": [
            {
                "step_number": 1,
                "title": "Nấu nước cốt sả thơm nồng",
                "description": "Sả cây đập dập cắt khúc, cho vào nồi cùng 500ml nước và đường phèn đun sôi 8 phút cho tiết trọn hương thơm tinh dầu sả.",
                "timer_minutes": 8
            },
            {
                "step_number": 2,
                "title": "Ủ trà đen thơm ngát",
                "description": "Thả 4 gói trà đen vào nồi nước sả nóng đậy nắp ủ trong 10 phút, sau đó vớt bỏ túi trà để nguội.",
                "timer_minutes": 10
            },
            {
                "step_number": 3,
                "title": "Vắt cam và cắt đào giòn",
                "description": "Vắt lấy nước cốt 1 trái cam vàng. Trái còn lại thái lát mỏng tròn. Đào ngâm cắt miếng cau vừa miệng.",
                "timer_minutes": 5
            },
            {
                "step_number": 4,
                "title": "Pha chế trà đào cam sả",
                "description": "Cho cốt trà sả, nước cam tươi, 2 muỗng nước siro đào vào bình lắc cùng thật nhiều đá viên, lắc mạnh tay 15 giây cho sủi bọt mát lạnh.",
                "timer_minutes": 2
            },
            {
                "step_number": 5,
                "title": "Trình bày ly trà đào",
                "description": "Rót trà ra ly cao, xếp các lát đào ngâm giòn sần sật, lát cam vàng tươi và cọng sả trang trí lên miệng ly thưởng thức sảng khoái.",
                "timer_minutes": 2
            }
        ]
    }
]

# Tích hợp dữ liệu công thức ẩm thực chuyên nghiệp từ CET (Trường Trung cấp Kinh Tế - Du Lịch TP.HCM)
try:
    from app.core.cet_recipes_data import CET_CATEGORIES, CET_RECIPES
    REAL_CATEGORIES.extend(CET_CATEGORIES)
    REAL_RECIPES.extend(CET_RECIPES)
except ImportError:
    pass

