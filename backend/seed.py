"""
Database Seeding Script for Culinary Blog (Clean Architecture)
Real Data according to Dien May Xanh 'Vao Bep' standards:
- 12 Real Categories
- 60 Real Recipes with authentic ingredients, steps, timers, and images
- Admin and Author accounts
- Clears all random/mock test data
"""

import asyncio
from datetime import datetime, timezone
from sqlalchemy import select, func, delete
from app.core.database import async_engine, AsyncSessionLocal, Base
from app.core.security import get_password_hash
from app.domain.models import User, Category, Recipe, RecipeStep, RecipeIngredient, RecipeImage
from app.domain.enums import RecipeDifficulty, RecipeStatus
from app.core.real_recipes_data import REAL_CATEGORIES, REAL_RECIPES


async def seed_database():
    print("🌱 Starting Clean Architecture database seeding with REAL DATA (Vào Bếp - Điện Máy Xanh)...")
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

        # 2. Xóa sạch dữ liệu ngẫu nhiên cũ để test
        print("  🧹 Purging old mock/random test recipes, ingredients, steps, images and categories...")
        await db.execute(delete(RecipeImage))
        await db.execute(delete(RecipeStep))
        await db.execute(delete(RecipeIngredient))
        await db.execute(delete(Recipe))
        await db.execute(delete(Category))
        await db.commit()

        # 3. Seed 12 Categories thật
        cat_map = {}
        for cat_data in REAL_CATEGORIES:
            cat = Category(
                name=cat_data["name"],
                slug=cat_data["slug"],
                description=cat_data["description"],
                image_url=cat_data.get("image_url"),
                order_index=cat_data["order_index"],
            )
            db.add(cat)
            await db.flush()
            cat_map[cat_data["slug"]] = cat

        total_cats = (await db.execute(select(func.count(Category.id)))).scalar()
        print(f"  ✓ Categories seeded: {total_cats} categories (Requirement: >= 10)")

        # 4. Seed 60 Recipes thật
        print(f"  🍳 Seeding {len(REAL_RECIPES)} authentic recipes with full ingredients, steps, and images...")
        for idx, r_data in enumerate(REAL_RECIPES):
            cat = cat_map.get(r_data["category_slug"])
            if not cat:
                cat = list(cat_map.values())[0]

            # 90% published, 10% draft for realistic CMS workflow
            status = RecipeStatus.Published if (idx % 10 != 0) else RecipeStatus.Draft
            diff_enum = RecipeDifficulty(r_data.get("difficulty", 2))

            nutr = r_data.get("nutrition", {})
            recipe = Recipe(
                title=r_data["title"],
                slug=r_data["slug"],
                description=r_data["description"],
                instructions="Thực hiện theo các bước tuần tự được hướng dẫn chi tiết, căn chuẩn thời gian hẹn giờ nấu.",
                prep_time=r_data.get("prep_time", 20),
                cook_time=r_data.get("cook_time", 30),
                servings=r_data.get("servings", 4),
                difficulty=diff_enum.value,
                status=status.value,
                category_id=cat.id,
                author_id=author.id,
                published_at=datetime.now(timezone.utc) if status == RecipeStatus.Published else None,
                nutrition_calories=nutr.get("calories", 400),
                nutrition_protein=nutr.get("protein", 25),
                nutrition_carbohydrates=nutr.get("carbohydrates", 30),
                nutrition_fat=nutr.get("fat", 18),
                nutrition_fiber=nutr.get("fiber", 2),
                nutrition_sodium=nutr.get("sodium", 600),
            )
            db.add(recipe)
            await db.flush()

            # Ingredients thật
            for ing_idx, ing_data in enumerate(r_data.get("ingredients", [])):
                ing = RecipeIngredient(
                    recipe_id=recipe.id,
                    name=ing_data["name"],
                    quantity=float(ing_data.get("quantity", 1)),
                    unit=ing_data.get("unit", "phần"),
                    notes=ing_data.get("notes", ""),
                    order_index=ing_idx + 1,
                )
                db.add(ing)

            # Steps thật
            for step_data in r_data.get("steps", []):
                step = RecipeStep(
                    recipe_id=recipe.id,
                    step_number=step_data["step_number"],
                    title=step_data["title"],
                    description=step_data["description"],
                    timer_minutes=step_data.get("timer_minutes", 10),
                )
                db.add(step)

            # Image thật
            img_url = r_data.get("image_url", "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&auto=format&fit=crop")
            img = RecipeImage(
                recipe_id=recipe.id,
                original_url=img_url,
                medium_url=img_url.replace("w=1200", "w=800"),
                thumbnail_url=img_url.replace("w=1200", "w=400"),
                alt_text=r_data["title"],
                is_primary=True,
                order_index=1,
            )
            db.add(img)

        await db.commit()

        final_recipes = (await db.execute(select(func.count(Recipe.id)))).scalar()
        final_ings = (await db.execute(select(func.count(RecipeIngredient.id)))).scalar()
        final_steps = (await db.execute(select(func.count(RecipeStep.id)))).scalar()
        final_images = (await db.execute(select(func.count(RecipeImage.id)))).scalar()

        print(f"  ✓ Total Categories: {total_cats}")
        print(f"  ✓ Total Authentic Recipes: {final_recipes} (Requirement: >= 50)")
        print(f"  ✓ Total Authentic Ingredients: {final_ings}")
        print(f"  ✓ Total Step-by-Step Cooking Instructions: {final_steps}")
        print(f"  ✓ Total Recipe Images: {final_images}")
        print(f"  ✓ Real database seeding completed successfully!")


if __name__ == "__main__":
    asyncio.run(seed_database())
