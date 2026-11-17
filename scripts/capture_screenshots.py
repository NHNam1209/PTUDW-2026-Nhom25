import os
import subprocess
import time

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
OUTPUT_DIR = r"D:\PTUDWNC\PTUDW-2026-Nhom25\screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TARGETS = [
    ("demo_01_homepage.png", "http://localhost:3000/"),
    ("demo_02_recipes_list.png", "http://localhost:3000/recipes"),
    ("demo_03_recipe_detail.png", "http://localhost:3000/recipes/banh-truyen-thong-recipe-10b453c1"),
    ("demo_04_categories_overview.png", "http://localhost:3000/categories"),
    ("demo_05_category_detail.png", "http://localhost:3000/categories/am-thuc-mien-bac"),
    ("demo_06_search_results.png", "http://localhost:3000/search?q=Bun"),
    ("demo_07_login_page.png", "http://localhost:3000/login"),
    ("demo_08_register_page.png", "http://localhost:3000/register"),
    ("demo_09_creator_dashboard.png", "http://localhost:3000/dashboard"),
    ("demo_10_recipe_management.png", "http://localhost:3000/dashboard/recipes"),
    ("demo_11_recipe_editor.png", "http://localhost:3000/dashboard/recipes/new"),
    ("demo_12_category_admin.png", "http://localhost:3000/dashboard/categories"),
    ("demo_13_users_management.png", "http://localhost:3000/users"),
    ("demo_14_swagger_docs.png", "http://localhost:8000/docs"),
    ("demo_15_health_probe.png", "http://localhost:8000/health"),
    ("demo_16_mailhog_ui.png", "http://localhost:8026/"),
    ("demo_17_minio_console.png", "http://localhost:9001/"),
]

for filename, url in TARGETS:
    out_file = os.path.join(OUTPUT_DIR, filename)
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--window-size=1280,820",
        f"--screenshot={out_file}",
        url
    ]
    try:
        subprocess.run(cmd, capture_output=True, timeout=15)
        if os.path.exists(out_file):
            print(f"Captured: {filename} ({os.path.getsize(out_file)} bytes)")
        else:
            print(f"Failed to save: {filename}")
    except Exception as e:
        print(f"Error capturing {filename}: {e}")

print("Screenshot capture sequence finished.")
