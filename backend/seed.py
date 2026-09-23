import asyncio
from datetime import datetime, timezone
from sqlalchemy import select
from app.core.database import async_engine, AsyncSessionLocal, Base
from app.core.security import get_password_hash
from app.domain.models import User, Category, Recipe, RecipeStep, RecipeIngredient, RecipeImage
from app.domain.enums import RecipeDifficulty, RecipeStatus


async def seed_data():
    print("🌱 Starting database seeding...")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as db:
        # 1. Seed Admin User
        admin_stmt = select(User).where(User.email == "admin@culinaryblog.com")
        res_admin = await db.execute(admin_stmt)
        admin = res_admin.scalar_one_or_none()

        if not admin:
            admin = User(
                full_name="Quản Trị Viên",
                email="admin@culinaryblog.com",
                user_name="admin",
                password_hash=get_password_hash("Admin@123456"),
                role="Admin",
                is_active=True,
                email_confirmed=True,
            )
            db.add(admin)
            print("  Created Admin user: admin@culinaryblog.com / Admin@123456")

        # 2. Seed Author User (Nguyễn Hoài Nam)
        author_stmt = select(User).where(User.email == "namnh.tandt@gmail.com")
        res_author = await db.execute(author_stmt)
        author = res_author.scalar_one_or_none()

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
            print("  Created Author user: namnh.tandt@gmail.com / Nam@123456")

        await db.flush()

        # 3. Seed Categories
        categories_data = [
            ("Món Khai Vị", "mon-khai-vi", "Các món gỏi, súp, khai vị kích thích vị giác", 1),
            ("Món Chính", "mon-chinh", "Các món ăn chính đậm đà hương vị gia đình", 2),
            ("Món Tráng Miệng", "mon-trang-mieng", "Chè, bánh ngọt và các món thanh mát sau bữa ăn", 3),
            ("Món Chay", "mon-chay", "Món ăn thuần chay thanh đạm, dinh dưỡng", 4),
            ("Đồ Uống", "do-uong", "Thức uống giải khát, trà và nước ép hoa quả tự nhiên", 5),
        ]

        created_categories = {}
        for name, slug, desc, order in categories_data:
            stmt = select(Category).where(Category.slug == slug)
            res = await db.execute(stmt)
            cat = res.scalar_one_or_none()
            if not cat:
                cat = Category(
                    name=name,
                    slug=slug,
                    description=desc,
                    order_index=order,
                )
                db.add(cat)
                await db.flush()
                print(f"  Created Category: {name}")
            created_categories[slug] = cat

        # 4. Seed Recipes
        recipes_data = [
            {
                "title": "Phở Bò Tái Nạm Gia Truyền",
                "slug": "pho-bo-tai-nam-gia-truyen",
                "description": "Bí quyết nấu nước dùng phở bò trong vắt, ngọt thanh từ xương ống cùng hương quế hồi thơm nức.",
                "instructions": "Ninh xương ống kỹ, thêm gia vị quế hồi thảo quả nướng thơm, chần bánh phở và thưởng thức nóng.",
                "prep_time": 45,
                "cook_time": 180,
                "servings": 6,
                "difficulty": RecipeDifficulty.Hard.value,
                "status": RecipeStatus.Published.value,
                "category_slug": "mon-chinh",
                "nutrition": {"calories": 480, "protein": 32, "carbohydrates": 55, "fat": 14, "fiber": 3, "sodium": 890},
                "ingredients": [
                    ("Bánh phở tươi", 500, "gram", "loại sợi mỏng mềm"),
                    ("Xương ống bò", 1500, "gram", "chặt khúc vừa phải"),
                    ("Thịt bò thăn", 300, "gram", "thái lát mỏng để làm tái"),
                    ("Nạm bò", 400, "gram", "luộc chín thái miếng vừa ăn"),
                    ("Gừng và hành khô", 100, "gram", "nướng thơm đập dập"),
                    ("Hoa hồi, quế, thảo quả", 30, "gram", "rang vàng tỏa mùi thơm"),
                ],
                "steps": [
                    ("Sơ chế xương bò", "Rửa sạch xương ống bằng nước muối loãng, luộc sơ qua 5 phút để loại bỏ bọt bẩn rồi rửa lại sạch sẽ.", 15),
                    ("Ninh nước dùng phở", "Cho xương vào nồi cùng 4 lít nước, thả gừng và hành khô nướng, quế hồi vào túi thơm rồi ninh lửa nhỏ trong 3 tiếng.", 180),
                    ("Trình bày và thưởng thức", "Chần bánh phở qua nước sôi, xếp vào bát, thêm thịt nạm bò, thịt tái, hành lá, rau mùi rồi chan nước dùng sôi sùng sục lên trên.", 10),
                ]
            },
            {
                "title": "Nem Rán Hà Nội Giòn Rụm",
                "slug": "nem-ran-ha-noi-gion-rum",
                "description": "Món chả giò truyền thống của người miền Bắc với lớp vỏ vàng ươm, nhân thịt nấm mộc nhĩ giòn ngọt.",
                "instructions": "Trộn đều nhân nem, cuộn chặt tay với bánh đa nem và rán ngập dầu ở lửa vừa đến khi vàng ruộm.",
                "prep_time": 30,
                "cook_time": 30,
                "servings": 4,
                "difficulty": RecipeDifficulty.Medium.value,
                "status": RecipeStatus.Published.value,
                "category_slug": "mon-khai-vi",
                "nutrition": {"calories": 350, "protein": 18, "carbohydrates": 28, "fat": 19, "fiber": 2, "sodium": 620},
                "ingredients": [
                    ("Thịt heo xay", 300, "gram", "chọn thịt nạc dăm có chút mỡ"),
                    ("Tôm tươi", 150, "gram", "bóc vỏ băm nhỏ"),
                    ("Mộc nhĩ, nấm hương", 50, "gram", "ngâm nở thái sợi nhỏ"),
                    ("Miến dong", 50, "gram", "ngâm mềm cắt khúc ngắn"),
                    ("Trứng gà", 2, "quả", "để tạo độ kết dính"),
                    ("Bánh đa nem", 30, "cái", "loại mỏng dai"),
                ],
                "steps": [
                    ("Trộn nhân nem", "Cho thịt xay, tôm, mộc nhĩ, miến, cà rốt bào sợi và trứng gà vào tô lớn, nêm chút hạt tiêu, bột canh rồi trộn đều tay.", 15),
                    ("Gói nem", "Trải bánh đa nem ra mặt phẳng, múc lượng nhân vừa phải, gấp hai bên mép lại rồi cuộn tròn đều tay.", 15),
                    ("Rán nem 2 lửa", "Rán nem lần 1 ở lửa nhỏ cho chín đều, trước khi ăn rán lại lần 2 lửa to để vỏ nem vàng giòn lâu.", 20),
                ]
            }
        ]

        for r_data in recipes_data:
            stmt = select(Recipe).where(Recipe.slug == r_data["slug"])
            res = await db.execute(stmt)
            if not res.scalar_one_or_none():
                cat = created_categories[r_data["category_slug"]]
                nut = r_data["nutrition"]
                rec = Recipe(
                    title=r_data["title"],
                    slug=r_data["slug"],
                    description=r_data["description"],
                    instructions=r_data["instructions"],
                    prep_time=r_data["prep_time"],
                    cook_time=r_data["cook_time"],
                    servings=r_data["servings"],
                    difficulty=r_data["difficulty"],
                    status=r_data["status"],
                    category_id=cat.id,
                    author_id=author.id,
                    published_at=datetime.now(timezone.utc),
                    nutrition_calories=nut["calories"],
                    nutrition_protein=nut["protein"],
                    nutrition_carbohydrates=nut["carbohydrates"],
                    nutrition_fat=nut["fat"],
                    nutrition_fiber=nut["fiber"],
                    nutrition_sodium=nut["sodium"],
                )
                db.add(rec)
                await db.flush()

                for idx, (title, desc, duration) in enumerate(r_data["steps"], 1):
                    step = RecipeStep(
                        recipe_id=rec.id,
                        step_number=idx,
                        title=title,
                        description=desc,
                        timer_minutes=duration,
                    )
                    db.add(step)

                for idx, (name, qty, unit, notes) in enumerate(r_data["ingredients"]):
                    ing = RecipeIngredient(
                        recipe_id=rec.id,
                        name=name,
                        quantity=qty,
                        unit=unit,
                        notes=notes,
                        order_index=idx,
                    )
                    db.add(ing)

                print(f"  Created Recipe: {r_data['title']}")

        await db.commit()
    print("✅ Seeding completed successfully!")


if __name__ == "__main__":
    asyncio.run(seed_data())
