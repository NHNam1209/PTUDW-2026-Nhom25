"""
Database Seeding Script for Culinary Blog (Clean Architecture)
Requirements:
- Minimum 20 Categories
- Minimum 100 Recipes
- Each recipe has at least 10 ingredients
- Each recipe has at least 5 preparation steps with cooking timers
- Standard admin and author accounts
"""

import asyncio
import random
import uuid
from datetime import datetime, timezone

from sqlalchemy import select, func
from app.core.database import async_engine, AsyncSessionLocal, Base
from app.core.security import get_password_hash
from app.domain.models import User, Category, Recipe, RecipeStep, RecipeIngredient, RecipeImage
from app.domain.enums import RecipeDifficulty, RecipeStatus


CATEGORIES_DATA = [
    ("Món Khai Vị", "mon-khai-vi", "Các món gỏi, súp, khai vị kích thích vị giác", 1),
    ("Món Chính", "mon-chinh", "Các món ăn chính đậm đà hương vị gia đình", 2),
    ("Món Tráng Miệng", "mon-trang-mieng", "Chè, bánh ngọt và các món thanh mát sau bữa ăn", 3),
    ("Món Chay Thanh Đạm", "mon-chay-thanh-dam", "Món ăn thuần chay giàu dinh dưỡng, an lành", 4),
    ("Món Nướng BBQ", "mon-nuong-bbq", "Các món nướng than hoa, sốt ướp thơm lừng", 5),
    ("Món Hấp Cách Thủy", "mon-hap-cach-thuy", "Món hấp giữ trọn vị ngọt tự nhiên và dinh dưỡng", 6),
    ("Món Lẩu Gia Đình", "mon-lau-gia-dinh", "Nước dùng lẩu phong phú, ấm cúng quây quần", 7),
    ("Món Xào Nhanh", "mon-xao-nhanh", "Món xào lửa lớn giữ trọn độ giòn tươi của rau củ", 8),
    ("Món Kho Đậm Đà", "mon-kho-dam-da", "Món kho tộ truyền thống chuẩn cơm mẹ nấu", 9),
    ("Món Chiên Giòn", "mon-chien-gion", "Món chiên vàng ruộm, giòn rụm hấp dẫn", 10),
    ("Món Canh & Súp", "mon-canh-sup", "Các món canh thanh nhiệt giải khát bữa cơm", 11),
    ("Món Cuốn & Gỏi", "mon-cuon-goi", "Món cuốn rau sống tươi ngon cùng nước chấm chuẩn vị", 12),
    ("Bánh Truyền Thống", "banh-truyen-thong", "Bánh chưng, bánh giò, bánh tét, bánh xèo cổ truyền", 13),
    ("Đồ Uống & Trà Thảo Mộc", "do-uong-tra-thao-moc", "Thức uống tự nhiên thanh lọc cơ thể", 14),
    ("Điểm Tâm Sáng", "diem-tam-sang", "Món ăn sáng nhanh gọn, tràn đầy năng lượng", 15),
    ("Ẩm Thực Miền Bắc", "am-thuc-mien-bac", "Vị thanh tao, tinh tế đậm đà văn hóa Thăng Long", 16),
    ("Ẩm Thực Miền Trung", "am-thuc-mien-trung", "Hương vị cay nồng, đậm đà khó quên của xứ Huế", 17),
    ("Ẩm Thực Miền Nam", "am-thuc-mien-nam", "Vị ngọt thanh từ dừa tươi và hào sảng phương Nam", 18),
    ("Món Ăn Healthy & Eat Clean", "healthy-eat-clean", "Thực đơn giảm cân, cân bằng dinh dưỡng", 19),
    ("Nước Chấm & Sốt Gia Vị", "nuoc-cham-gia-vi", "Bí quyết pha các loại sốt chấm truyền thống", 20),
    ("Món Tiệc & Ngày Lễ", "mon-tiec-ngay-le", "Thực đơn sang trọng cho bữa tiệc sum họp", 21),
    ("Hải Sản Biển Tươi", "hai-san-bien-tuoi", "Món ngon từ tôm, cua, mực, cá biển tươi sống", 22),
]

INGREDIENTS_POOL = [
    ("Thịt thăn bò", "gram", [200, 300, 400, 500], "thái lát mỏng hoặc khúc vuông"),
    ("Xương ống hầm", "gram", [500, 1000, 1500], "chặt khúc, rửa sạch nước muối"),
    ("Thịt ba chỉ heo", "gram", [300, 400, 500], "chọn loại mỡ nạc đan xen"),
    ("Ức gà phi lê", "gram", [300, 400, 500], "rửa sạch, thấm khô nước"),
    ("Tôm sú tươi", "gram", [250, 300, 400], "lột vỏ, bỏ chỉ đen"),
    ("Mực lá tươi", "gram", [200, 300, 400], "khứa vảy rồng"),
    ("Cá hồi phi lê", "gram", [200, 300, 400], "cắt miếng vuông vừa ăn"),
    ("Đậu hũ non", "miếng", [2, 3, 4], "cắt khối vuông nhẹ tay"),
    ("Nấm hương khô", "gram", [30, 50, 80], "ngâm nở, rửa sạch cát"),
    ("Nấm rơm tươi", "gram", [100, 150, 200], "cắt gốc, ngâm muối"),
    ("Hành tây", "củ", [1, 2], "bổ múi cau"),
    ("Hành lá & Ngò rí", "gram", [50, 100], "rửa sạch thái nhỏ"),
    ("Tỏi khô cô đơn", "tép", [4, 6, 8], "băm nhuyễn thơm lừng"),
    ("Gừng củ già", "nhánh", [1, 2], "cạo vỏ, đập dập hoặc thái sợi"),
    ("Sả cây tươi", "cây", [3, 4, 5], "đập dập, cắt khúc"),
    ("Ớt sừng đỏ", "trái", [2, 3, 4], "bỏ hạt thái lát"),
    ("Nước mắm nhĩ Phú Quốc", "muỗng canh", [2, 3, 4], "loại 40 độ đạm"),
    ("Hạt nêm xương hầm", "muỗng cà phê", [1, 2, 3], "nêm nếm vừa khẩu vị"),
    ("Đường phèn tự nhiên", "muỗng cà phê", [1, 2], "tạo vị ngọt thanh tao"),
    ("Tiêu đen xay nguyên chất", "muỗng cà phê", [1, 2], "rắc thơm lúc hoàn thành"),
    ("Dầu hào cao cấp", "muỗng canh", [1, 2], "tạo độ sánh bóng"),
    ("Dầu mè thơm", "muỗng cà phê", [1, 2], "dậy mùi thơm đặc trưng"),
    ("Dầu ăn thực vật", "muỗng canh", [2, 3, 4], "dùng để phi thơm"),
    ("Bánh phở hoặc bún tươi", "gram", [400, 500, 600], "chần qua nước sôi"),
    ("Rau sống hỗn hợp", "gram", [200, 300], "xà lách, húng quế, kinh giới"),
]

STEPS_TEMPLATES = [
    ("Sơ chế nguyên liệu tươi sống", "Rửa sạch toàn bộ thịt, cá và rau củ với nước muối loãng. Để ráo nước hoàn toàn trước khi tẩm ướp để đảm bảo độ tươi ngọt.", 10),
    ("Ướp gia vị chuẩn vị", "Trộn đều nguyên liệu chính với nước mắm, tiêu, tỏi băm, hạt nêm và dầu hào. Để ngấm đều gia vị trong nhiệt độ mát.", 20),
    ("Phi thơm gia vị nền", "Bắc nồi hoặc chảo lên bếp, cho dầu ăn vào đun nóng. Phi thơm tỏi băm, hành khô và gừng đập dập đến khi dậy mùi thơm vàng ruộm.", 5),
    ("Nấu nước dùng / Xào săn nguyên liệu", "Cho nguyên liệu đã ướp vào đảo đều tay trên lửa lớn đến khi săn lại. Châm nước dùng sôi vào đun lăn tăn trên lửa nhỏ.", 25),
    ("Hầm kỹ lấy vị ngọt tự nhiên", "Hạ lửa liu riu, vớt bọt thường xuyên để nước dùng luôn trong vắt và thanh mát. Nêm nếm lại cho vừa vặn khẩu vị gia đình.", 40),
    ("Hoàn thiện và trình bày món ăn", "Bày món ăn ra đĩa hoặc tô sứ, rắc hành lá thái nhỏ, tiêu xay và ngò rí lên trên. Thưởng thức ngay khi còn nóng hổi cùng cơm hoặc bún.", 5),
    ("Pha chế nước chấm ăn kèm", "Pha nước mắm chua ngọt hoặc nước chấm gừng tỏi ớt theo tỷ lệ chuẩn để món ăn thêm tròn vị và bùng nổ hương sắc.", 8),
]

RECIPE_TITLES = [
    ("Phở Bò Tái Nạm Gia Truyền", "mon-chinh", RecipeDifficulty.Hard),
    ("Bún Chả Hà Nội Nướng Than Hoa", "am-thuc-mien-bac", RecipeDifficulty.Medium),
    ("Bánh Xèo Giòn Rụm Miền Tây", "banh-truyen-thong", RecipeDifficulty.Medium),
    ("Gỏi Cuốn Tôm Thịt Thanh Mát", "mon-cuon-goi", RecipeDifficulty.Easy),
    ("Cá Kho Tộ Đậm Đà Bắt Cơm", "mon-kho-dam-da", RecipeDifficulty.Medium),
    ("Canh Chua Cá Lóc Đồng", "mon-canh-sup", RecipeDifficulty.Medium),
    ("Bò Lúc Lắc Khoai Tây Chiên", "mon-chinh", RecipeDifficulty.Medium),
    ("Gà Hấp Lá Chanh Thơm Lừng", "mon-hap-cach-thuy", RecipeDifficulty.Easy),
    ("Sườn Xào Chua Ngọt Óng Ánh", "mon-chinh", RecipeDifficulty.Medium),
    ("Thịt Kho Hột Vịt Nước Dừa", "mon-kho-dam-da", RecipeDifficulty.Hard),
    ("Bún Bò Huế Cay Nồng Chuẩn Vị", "am-thuc-mien-trung", RecipeDifficulty.Hard),
    ("Nem Rán Hà Nội Vỏ Giòn", "mon-khai-vi", RecipeDifficulty.Medium),
    ("Chè Hạt Sen Long Nhãn Thanh Nhiệt", "mon-trang-mieng", RecipeDifficulty.Easy),
    ("Đậu Hũ Tứ Xuyên Cay Tê", "mon-chay-thanh-dam", RecipeDifficulty.Medium),
    ("Mực Hấp Gừng Hành Tươi", "hai-san-bien-tuoi", RecipeDifficulty.Easy),
    ("Lẩu Thái Hải Sản Tom Yum", "mon-lau-gia-dinh", RecipeDifficulty.Hard),
    ("Cơm Tấm Sườn Bì Chả Sài Gòn", "am-thuc-mien-nam", RecipeDifficulty.Hard),
    ("Mì Quảng Tôm Thịt Trứng Cút", "am-thuc-mien-trung", RecipeDifficulty.Medium),
    ("Bánh Mì Kẹp Thịt Nướng Giòn Tan", "diem-tam-sang", RecipeDifficulty.Easy),
    ("Canh Cua Rau Đay Mồng Tơi Cà Pháo", "mon-canh-sup", RecipeDifficulty.Medium),
    ("Tôm Sốt Bơ Tỏi Béo Ngậy", "hai-san-bien-tuoi", RecipeDifficulty.Easy),
    ("Salad Ức Gà Sốt Mè Rang Eat Clean", "healthy-eat-clean", RecipeDifficulty.Easy),
    ("Bò Cuốn Lá Lốt Nướng Chảo", "mon-nuong-bbq", RecipeDifficulty.Medium),
    ("Chả Giò Hải Sản Sốt Mayonnaise", "mon-khai-vi", RecipeDifficulty.Medium),
    ("Bánh Cuốn Nóng Tráng Chảo", "diem-tam-sang", RecipeDifficulty.Medium),
    ("Canh Sườn Hầm Rau Củ Thanh Ngọt", "mon-canh-sup", RecipeDifficulty.Easy),
    ("Lẩu Gà Lá É Phú Yên", "mon-lau-gia-dinh", RecipeDifficulty.Medium),
    ("Thịt Nướng Sa Tế Đậm Vị", "mon-nuong-bbq", RecipeDifficulty.Easy),
    ("Bún Đậu Mắm Tôm Thập Cẩm", "am-thuc-mien-bac", RecipeDifficulty.Easy),
    ("Rau Muống Xào Tỏi Xanh Mướt", "mon-xao-nhanh", RecipeDifficulty.Easy),
    ("Nấm Đùi Gà Xào Hạt Sen Chay", "mon-chay-thanh-dam", RecipeDifficulty.Easy),
    ("Cá Hồi Áp Chảo Sốt Cam", "healthy-eat-clean", RecipeDifficulty.Medium),
    ("Bánh Flan Caramen Mềm Mịn", "mon-trang-mieng", RecipeDifficulty.Easy),
    ("Nước Sốt Chấm Gà Luộc Tiêu Chanh", "nuoc-cham-gia-vi", RecipeDifficulty.Easy),
    ("Trà Đào Cam Sả Mát Lạnh", "do-uong-tra-thao-moc", RecipeDifficulty.Easy),
    ("Bò Sốt Vang Ăn Kèm Bánh Mì", "mon-chinh", RecipeDifficulty.Hard),
    ("Cơm Chiên Dương Châu Thập Cẩm", "mon-chinh", RecipeDifficulty.Medium),
    ("Vịt Nấu Chao Chuẩn Miền Tây", "am-thuc-mien-nam", RecipeDifficulty.Hard),
    ("Bánh Canh Cua Giò Heo", "mon-chinh", RecipeDifficulty.Hard),
    ("Hủ Tiếu Nam Vang Nước Súp Trong", "am-thuc-mien-nam", RecipeDifficulty.Hard),
    ("Cá Chẽm Hấp Hồng Kông", "hai-san-bien-tuoi", RecipeDifficulty.Medium),
    ("Gỏi Ngó Sen Tôm Thịt Chua Ngọt", "mon-cuon-goi", RecipeDifficulty.Easy),
    ("Bún Riêu Cua Đồng Thanh Ngọt", "am-thuc-mien-bac", RecipeDifficulty.Hard),
    ("Ốc Nhồi Thịt Hấp Sả Chấm Gừng", "mon-khai-vi", RecipeDifficulty.Medium),
    ("Gà Rang Muối Giòn Rụm", "mon-chien-gion", RecipeDifficulty.Medium),
    ("Súp Bào Ngư Vi Cá Bồi Bổ", "mon-tiec-ngay-le", RecipeDifficulty.Hard),
    ("Chè Bưởi An Giang Giòn Sần Sật", "mon-trang-mieng", RecipeDifficulty.Medium),
    ("Xôi Xéo Hà Nội Hành Phi Vàng", "diem-tam-sang", RecipeDifficulty.Medium),
    ("Trà Sen Vàng Kem Cheese", "do-uong-tra-thao-moc", RecipeDifficulty.Easy),
    ("Nước Mắm Chua Ngọt Chấm Nem", "nuoc-cham-gia-vi", RecipeDifficulty.Easy),
]


async def seed_database():
    print("🌱 Starting Clean Architecture database seeding...")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as db:
        # 1. Admin & Author Users
        admin_stmt = select(User).where(User.email == "admin@culinaryblog.com")
        admin = (await db.execute(admin_stmt)).scalar_one_or_none()
        if not admin:
            admin = User(
                full_name="Quản Trị Viên Hệ Thống",
                email="admin@culinaryblog.com",
                user_name="admin",
                password_hash=get_password_hash("Admin@123456"),
                role="Admin",
                is_active=True,
                email_confirmed=True,
            )
            db.add(admin)

        author_stmt = select(User).where(User.email == "namnh.tandt@gmail.com")
        author = (await db.execute(author_stmt)).scalar_one_or_none()
        if not author:
            author = User(
                full_name="Nguyễn Hoài Nam",
                email="namnh.tandt@gmail.com",
                user_name="nhnam1209",
                password_hash=get_password_hash("Nam@123456"),
                role="Author",
                is_active=True,
                email_confirmed=True,
                bio="Đam mê ẩm thực Việt Nam và nghiên cứu các món ăn truyền thống.",
            )
            db.add(author)

        await db.flush()
        print(f"  ✓ Users verified: {admin.email}, {author.email}")

        # 2. Seed >= 20 Categories
        cat_map = {}
        for name, slug, desc, order in CATEGORIES_DATA:
            stmt = select(Category).where(Category.slug == slug)
            cat = (await db.execute(stmt)).scalar_one_or_none()
            if not cat:
                cat = Category(name=name, slug=slug, description=desc, order_index=order)
                db.add(cat)
                await db.flush()
            cat_map[slug] = cat

        total_cats = (await db.execute(select(func.count(Category.id)))).scalar()
        print(f"  ✓ Categories verified: {total_cats} categories (Requirement: >= 20)")

        # 3. Seed >= 100 Recipes
        current_recipe_count = (await db.execute(select(func.count(Recipe.id)))).scalar() or 0
        target_count = 105
        needed = max(0, target_count - current_recipe_count)

        if needed > 0:
            print(f"  Generating {needed} recipes to reach {target_count} total recipes...")
            all_cat_slugs = list(cat_map.keys())

            for i in range(needed):
                base_idx = i % len(RECIPE_TITLES)
                title_template, cat_slug, diff = RECIPE_TITLES[base_idx]
                iteration = i // len(RECIPE_TITLES)
                suffix = f" Đặc Biệt #{iteration + 1}" if iteration > 0 else " Chuẩn Vị"
                title = f"{title_template}{suffix}"
                unique_slug = f"{cat_slug}-recipe-{uuid.uuid4().hex[:8]}"

                category = cat_map.get(cat_slug, cat_map[all_cat_slugs[0]])
                status = RecipeStatus.Published if (i % 5 != 0) else RecipeStatus.Draft

                recipe = Recipe(
                    title=title,
                    slug=unique_slug,
                    description=f"Hướng dẫn chi tiết cách chế biến món {title} thơm ngon, đậm đà với nguyên liệu tự nhiên.",
                    instructions="Thực hiện theo các bước tuần tự được hướng dẫn chi tiết, căn chuẩn thời gian hẹn giờ nấu.",
                    prep_time=random.randint(15, 45),
                    cook_time=random.randint(20, 90),
                    servings=random.choice([2, 4, 6, 8]),
                    difficulty=diff.value,
                    status=status.value,
                    category_id=category.id,
                    author_id=author.id,
                    nutrition_calories=random.randint(250, 650),
                    nutrition_protein=random.randint(18, 45),
                    nutrition_carbohydrates=random.randint(30, 80),
                    nutrition_fat=random.randint(8, 25),
                    nutrition_fiber=random.randint(2, 6),
                    nutrition_sodium=random.randint(400, 950),
                )
                db.add(recipe)
                await db.flush()

                # At least 10 ingredients per recipe
                shuffled_ingredients = random.sample(INGREDIENTS_POOL, k=random.randint(10, 14))
                for ing_idx, (ing_name, unit, qtys, note) in enumerate(shuffled_ingredients):
                    ing = RecipeIngredient(
                        recipe_id=recipe.id,
                        name=ing_name,
                        quantity=float(random.choice(qtys)),
                        unit=unit,
                        notes=note,
                        order_index=ing_idx + 1,
                    )
                    db.add(ing)

                # At least 5 steps per recipe
                selected_steps = STEPS_TEMPLATES[:random.randint(5, 7)]
                for step_idx, (st_title, st_desc, timer_m) in enumerate(selected_steps):
                    step = RecipeStep(
                        recipe_id=recipe.id,
                        step_number=step_idx + 1,
                        title=f"Bước {step_idx + 1}: {st_title}",
                        description=st_desc,
                        timer_minutes=timer_m,
                    )
                    db.add(step)

                # Primary Image
                img = RecipeImage(
                    recipe_id=recipe.id,
                    original_url="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop",
                    thumbnail_url="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400&auto=format&fit=crop",
                    alt_text=title,
                    is_primary=True,
                    order_index=1,
                )
                db.add(img)

            await db.commit()

        final_recipes = (await db.execute(select(func.count(Recipe.id)))).scalar()
        print(f"  ✓ Recipes verified: {final_recipes} recipes (Requirement: >= 100)")
        print(f"  ✓ Database seeding completed successfully!")


if __name__ == "__main__":
    asyncio.run(seed_database())
