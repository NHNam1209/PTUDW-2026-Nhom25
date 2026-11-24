# -*- coding: utf-8 -*-
"""
Script to generate Slide_Bao_Cao_Cuoi_Ky_Culinary_Blog.pptx
Professional 16:9 PowerPoint Presentation for 6-7 minute final defense.
Includes embedded screenshots and speaker notes.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

WORKSPACE_DIR = r"D:\PTUDWNC\PTUDW-2026-Nhom25"
SCREENSHOTS_DIR = os.path.join(WORKSPACE_DIR, "screenshots")
OUTPUT_PPTX = os.path.join(WORKSPACE_DIR, "Slide_Bao_Cao_Cuoi_Ky_Culinary_Blog.pptx")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color Palette
DARK_NAVY = RGBColor(15, 23, 42)      # #0F172A
PRIMARY_BLUE = RGBColor(30, 58, 138)  # #1E3A8A
ACCENT_BLUE = RGBColor(37, 99, 235)   # #2563EB
AMBER_GOLD = RGBColor(245, 158, 11)   # #F59E0B
WHITE = RGBColor(255, 255, 255)
CARD_BG = RGBColor(248, 250, 252)     # #F8FAFC
CARD_BORDER = RGBColor(226, 232, 240) # #E2E8F0
TEXT_DARK = RGBColor(30, 41, 59)      # #1E293B
TEXT_MUTED = RGBColor(100, 116, 139)  # #64748B
GREEN_SUCCESS = RGBColor(22, 163, 74) # #16A34A

blank_slide_layout = prs.slide_layouts[6]

def add_header(slide, title_text, category_text="ĐỒ ÁN PHÁT TRIỂN ỨNG DỤNG WEB NÂNG CAO • NHÓM 25"):
    # Header container
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    # Category tag
    p_cat = tf.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.name = "Segoe UI"
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = ACCENT_BLUE
    p_cat.space_after = Pt(2)
    
    # Title
    p_title = tf.add_paragraph()
    p_title.text = title_text
    p_title.font.name = "Segoe UI"
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = DARK_NAVY

def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.2)
    return shape

def add_speaker_note(slide, note_text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = note_text

# ==============================================================================
# SLIDE 1: TITLE SLIDE (35s)
# ==============================================================================
slide1 = prs.slides.add_slide(blank_slide_layout)

# Background deep navy
bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
bg1.fill.solid()
bg1.fill.fore_color.rgb = DARK_NAVY
bg1.line.fill.background()

# Title Card / Content
tb1 = slide1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(4.5))
tf1 = tb1.text_frame
tf1.word_wrap = True

p_sub = tf1.paragraphs[0]
p_sub.text = "BÁO CÁO ĐỒ ÁN MÔN HỌC • PHÁT TRIỂN ỨNG DỤNG WEB NÂNG CAO"
p_sub.font.name = "Segoe UI"
p_sub.font.size = Pt(13)
p_sub.font.bold = True
p_sub.font.color.rgb = AMBER_GOLD
p_sub.space_after = Pt(10)

p_title = tf1.add_paragraph()
p_title.text = "HỆ THỐNG CULINARY BLOG"
p_title.font.name = "Segoe UI"
p_title.font.size = Pt(36)
p_title.font.bold = True
p_title.font.color.rgb = WHITE
p_title.space_after = Pt(8)

p_desc = tf1.add_paragraph()
p_desc.text = "Nền tảng Chia sẻ và Quản lý Công thức Ẩm thực chuẩn IEEE 830 / ISO 29148"
p_desc.font.name = "Segoe UI"
p_desc.font.size = Pt(18)
p_desc.font.color.rgb = RGBColor(203, 213, 225)
p_desc.space_after = Pt(30)

# Info Card at bottom
info_card = add_card(slide1, Inches(1.0), Inches(4.6), Inches(11.3), Inches(2.1), bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
tb_info = slide1.shapes.add_textbox(Inches(1.2), Inches(4.8), Inches(10.9), Inches(1.7))
tf_info = tb_info.text_frame
tf_info.word_wrap = True

p1 = tf_info.paragraphs[0]
p1.text = "Giảng viên hướng dẫn: TS. Nguyễn Thị Lương"
p1.font.name = "Segoe UI"
p1.font.size = Pt(14)
p1.font.bold = True
p1.font.color.rgb = WHITE
p1.space_after = Pt(6)

p2 = tf_info.add_paragraph()
p2.text = "Nhóm thực hiện (Nhóm 25): Nguyễn Hoài Nam (Trưởng nhóm), Đỗ Duy Biên, Hoàng Thăng Long, Trần Chánh Phát"
p2.font.name = "Segoe UI"
p2.font.size = Pt(13)
p2.font.color.rgb = RGBColor(226, 232, 240)
p2.space_after = Pt(4)

p3 = tf_info.add_paragraph()
p3.text = "Kiến trúc: FastAPI • React 19 • PostgreSQL 16 (FTS) • Redis 7 • MinIO S3 • Docker Compose"
p3.font.name = "Segoe UI"
p3.font.size = Pt(12)
p3.font.italic = True
p3.font.color.rgb = AMBER_GOLD

add_speaker_note(slide1, 
    "KỊCH BẢN THUYẾT TRÌNH (30 giây):\n"
    "Kính chào Cô và các bạn! Hôm nay, Nhóm 25 xin đại diện trình bày báo cáo đồ án cuối kỳ môn Phát triển ứng dụng web nâng cao "
    "với đề tài: 'Hệ thống Culinary Blog - Nền tảng chia sẻ và quản lý công thức ẩm thực'. "
    "Dự án được xây dựng bám sát theo tài liệu đặc tả chuẩn IEEE 830, áp dụng các kỹ thuật công nghệ hiện đại như FastAPI, React 19, "
    "PostgreSQL Full-Text Search, Redis, MinIO S3 và Docker. Sau đây em xin bắt đầu phần trình bày."
)

# ==============================================================================
# SLIDE 2: MỤC TIÊU DỰ ÁN & ĐỐI TƯỢNG NGƯỜI DÙNG (35s)
# ==============================================================================
slide2 = prs.slides.add_slide(blank_slide_layout)
add_header(slide2, "Mục Tiêu Dự Án & Phân Hệ Người Dùng")

# 3 User Role Cards
roles = [
    ("ĐỘC GIẢ (PUBLIC GUEST)", "Khám phá & Trải nghiệm", [
        "Xem danh mục và công thức món ăn chuẩn SEO",
        "Tìm kiếm Full-Text Search tiếng Việt không dấu",
        "Lọc đa tiêu chí: danh mục, độ khó, thời gian nấu",
        "Xem nguyên liệu, hướng dẫn từng bước và dinh dưỡng"
    ], ACCENT_BLUE),
    ("TÁC GIẢ (CREATOR / AUTHOR)", "Sáng tạo & Quản lý nội dung", [
        "Đăng ký, Đăng nhập (Local & Google OAuth 2.0)",
        "Bảng điều khiển tác giả (Dashboard Overview)",
        "Trình biên soạn công thức đa bước kéo thả (Drag & Drop)",
        "Quản lý trạng thái: Bản nháp (Draft), Xuất bản, Lưu trữ"
    ], AMBER_GOLD),
    ("QUẢN TRỊ VIÊN (ADMINISTRATOR)", "Vận hành & Giám sát hệ thống", [
        "Quản lý danh mục món ăn (CRUD Categories)",
        "Quản lý và kiểm soát tài khoản người dùng (Users Page)",
        "Giám sát sức khỏe hạ tầng qua Health Check Probes",
        "Bảo vệ tính toàn vẹn dữ liệu hệ thống"
    ], GREEN_SUCCESS),
]

for idx, (title, sub, bullets, color) in enumerate(roles):
    left = Inches(0.8 + idx * 4.0)
    add_card(slide2, left, Inches(1.8), Inches(3.7), Inches(5.1))
    
    tb = slide2.shapes.add_textbox(left + Inches(0.2), Inches(2.0), Inches(3.3), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = "Segoe UI"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = color
    p.space_after = Pt(2)
    
    p_s = tf.add_paragraph()
    p_s.text = sub
    p_s.font.name = "Segoe UI"
    p_s.font.size = Pt(11)
    p_s.font.italic = True
    p_s.font.color.rgb = TEXT_MUTED
    p_s.space_after = Pt(14)
    
    for b in bullets:
        pb = tf.add_paragraph()
        pb.text = "• " + b
        pb.font.name = "Segoe UI"
        pb.font.size = Pt(11)
        pb.font.color.rgb = TEXT_DARK
        pb.space_after = Pt(8)

add_speaker_note(slide2,
    "KỊCH BẢN THUYẾT TRÌNH (35 giây):\n"
    "Hệ thống Culinary Blog giải quyết bài toán quản lý và chia sẻ công thức ẩm thực một cách có cấu trúc cho 3 đối tượng người dùng:\n"
    "Thứ nhất là Độc giả vãng lai, được tối ưu hóa SEO với dữ liệu cấu trúc Schema.org, tìm kiếm tiếng Việt không dấu siêu tốc.\n"
    "Thứ hai là Tác giả sáng tạo nội dung, được trang bị công cụ Creator Dashboard và bộ soạn thảo công thức kéo thả chuyên nghiệp.\n"
    "Thứ ba là Quản trị viên, toàn quyền kiểm soát danh mục, quản lý người dùng và theo dõi trạng thái hệ thống theo thời gian thực."
)

# ==============================================================================
# SLIDE 3: TỔNG QUAN KIẾN TRÚC HỆ THỐNG (40s)
# ==============================================================================
slide3 = prs.slides.add_slide(blank_slide_layout)
add_header(slide3, "Kiến Trúc Hệ Thống (Decoupled & Clean Architecture)")

# Left Card: Infrastructure & Data Flow
add_card(slide3, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_arch = slide3.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_a = tb_arch.text_frame
tf_a.word_wrap = True

pa1 = tf_a.paragraphs[0]
pa1.text = "1. MÔ HÌNH HẠ TẦNG (CONTAINERIZED)"
pa1.font.name = "Segoe UI"
pa1.font.size = Pt(13)
pa1.font.bold = True
pa1.font.color.rgb = PRIMARY_BLUE
pa1.space_after = Pt(6)

arch_points = [
    ("Reverse Proxy (Nginx)", "Cổng 80 tiếp nhận toàn bộ traffic, định tuyến /api sang Backend và root sang Frontend."),
    ("Frontend (React 19 / Vite)", "Single Page Application (SPA), render giao diện nhanh, tương tác mượt mà qua REST API."),
    ("Backend API (FastAPI)", "Xây dựng theo Clean Architecture (Domain -> Schema -> Service -> API Router)."),
    ("Database (PostgreSQL 16)", "Lưu trữ dữ liệu quan hệ, tích hợp unaccent và pg_trgm cho Full-Text Search."),
    ("Caching & Tokens (Redis 7)", "Quản lý token blacklist, rate limit request, distributed caching."),
    ("Object Storage (MinIO S3)", "Tương thích AWS S3, quản lý và phân phối tệp ảnh công thức nấu ăn an toàn.")
]

for title, desc in arch_points:
    p = tf_a.add_paragraph()
    p.text = "• " + title + ": "
    p.font.name = "Segoe UI"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    
    r = p.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK
    p.space_after = Pt(5)

# Right Card: Clean Architecture Layers Diagram
add_card(slide3, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_clean = slide3.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_c = tb_clean.text_frame
tf_c.word_wrap = True

pc1 = tf_c.paragraphs[0]
pc1.text = "2. NGUYÊN LÝ THIẾT KẾ CLEAN ARCHITECTURE"
pc1.font.name = "Segoe UI"
pc1.font.size = Pt(13)
pc1.font.bold = True
pc1.font.color.rgb = PRIMARY_BLUE
pc1.space_after = Pt(10)

clean_layers = [
    ("Presentation Layer (API Routers)", "FastAPI endpoints, dependency injection, middleware correlation-id & rate-limit."),
    ("Schemas & DTOs (Pydantic v2)", "Chuyển giao dữ liệu, validate payload chặt chẽ, loại bỏ thông tin nhạy cảm (passwords)."),
    ("Service & Business Logic", "Xử lý nghiệp vụ: Sinh slug tiếng Việt, tương tác MinIO S3 SDK, cron sitemap generator."),
    ("Domain Core (Entities & Enums)", "Chứa BaseEntity, Recipe Aggregate Root, quan hệ chặt chẽ, hoàn toàn độc lập framework."),
    ("Unit of Work & Soft Delete", "Đảm bảo tính toàn vẹn giao dịch ACID, chống mất dữ liệu với cờ is_deleted.")
]

for title, desc in clean_layers:
    p = tf_c.add_paragraph()
    p.text = "► " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(1)
    
    pd = tf_c.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(10.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(8)

add_speaker_note(slide3,
    "KỊCH BẢN THUYẾT TRÌNH (40 giây):\n"
    "Về mặt kiến trúc, dự án áp dụng mô hình Decoupled Architecture đóng gói hoàn chỉnh bằng Docker Compose gồm 6 dịch vụ:\n"
    "Nginx đứng đầu làm Reverse Proxy điều phối traffic. Tầng Backend viết bằng FastAPI theo tư tưởng Clean Architecture: "
    "Domain là trung tâm chứa các Entity nghiệp vụ thuần túy, bao bọc bởi Schemas Pydantic v2, độc lập hoàn toàn với hạ tầng.\n"
    "Hệ thống lưu trữ ảnh qua MinIO S3, cache bằng Redis và CSDL PostgreSQL 16 hỗ trợ Full-Text Search."
)

# ==============================================================================
# SLIDE 4: PHÂN CÔNG VAI TRÒ NHÓM 25 (35s)
# ==============================================================================
slide4 = prs.slides.add_slide(blank_slide_layout)
add_header(slide4, "Phân Công Trách Nhiệm Thành Viên (Nhóm 25)")

members = [
    ("1. NGUYỄN HOÀI NAM (LEAD)", "Backend Core, Auth, Recipe & DevOps", [
        "Kiến trúc Docker, Nginx, DB Init & Seeding",
        "Auth: JWT Token Rotation, OAuth2, Lockout",
        "Recipe Core: CRUD, Concurrency (row_version)",
        "Bộ 3 Health Check Probes (/live, /ready, /health)"
    ]),
    ("2. ĐỖ DUY BIÊN", "Backend Categories, Search & Jobs", [
        "Categories CRUD & Ràng buộc toàn vẹn",
        "Full-Text Search PostgreSQL (unaccent, simple)",
        "MinIO S3 Service (kiểm tra MIME, Magic Bytes)",
        "Background Jobs: Resize ảnh, Cron sinh sitemap.xml"
    ]),
    ("3. HOÀNG THĂNG LONG", "Frontend Public & Catalog UI", [
        "Trang chủ (Home Page) & Bố cục chung",
        "Recipe Catalog (Lọc đa tiêu chí, phân trang)",
        "Trang chi tiết công thức & Bảng dinh dưỡng",
        "Auth UI: Form Đăng nhập, Đăng ký, Profile tác giả"
    ]),
    ("4. TRẦN CHÁNH PHÁT", "Frontend Dashboard & Recipe Editor", [
        "Creator Dashboard: Thống kê & Quản lý bài viết",
        "Recipe Editor Wizard: Form đa bước",
        "Step & Ingredient Editor kéo thả (useDragReorder)",
        "Admin Category & Users Management UI, Schema.org SEO"
    ]),
]

for idx, (name, role, tasks) in enumerate(members):
    row = idx // 2
    col = idx % 2
    left = Inches(0.8 + col * 6.0)
    top = Inches(1.8 + row * 2.6)
    
    add_card(slide4, left, top, Inches(5.7), Inches(2.4))
    tb = slide4.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), Inches(5.3), Inches(2.1))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = name
    p.font.name = "Segoe UI"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    
    p_r = tf.add_paragraph()
    p_r.text = role
    p_r.font.name = "Segoe UI"
    p_r.font.size = Pt(10.5)
    p_r.font.bold = True
    p_r.font.color.rgb = ACCENT_BLUE
    p_r.space_after = Pt(4)
    
    for t in tasks:
        pt = tf.add_paragraph()
        pt.text = "• " + t
        pt.font.name = "Segoe UI"
        pt.font.size = Pt(10)
        pt.font.color.rgb = TEXT_DARK
        pt.space_after = Pt(2)

add_speaker_note(slide4,
    "KỊCH BẢN THUYẾT TRÌNH (35 giây):\n"
    "Nhóm 25 gồm 4 thành viên với phân công công việc cụ thể theo đúng mã chức năng SRS:\n"
    "- Bạn Nguyễn Hoài Nam làm Trưởng nhóm phụ trách toàn bộ hạ tầng DevOps, module Xác thực nâng cao và Recipe Core.\n"
    "- Bạn Đỗ Duy Biên phụ trách Module Categories, tìm kiếm Full-Text Search, lưu trữ MinIO S3 và các background jobs.\n"
    "- Bạn Hoàng Thăng Long xây dựng giao diện web công khai, duyệt danh sách món ăn và trang chi tiết.\n"
    "- Bạn Trần Chánh Phát hoàn thiện bảng điều khiển Creator Dashboard, bộ soạn thảo công thức kéo thả và giao diện Admin."
)

# ==============================================================================
# SLIDE 5: BACKEND CORE - XÁC THỰC & QUẢN LÝ CÔNG THỨC (40s)
# ==============================================================================
slide5 = prs.slides.add_slide(blank_slide_layout)
add_header(slide5, "Backend Core: Bảo Mật Xác Thực & Quản Lý Công Thức")

# Left Column: Auth Details
add_card(slide5, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_auth = slide5.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_au = tb_auth.text_frame
tf_au.word_wrap = True

pau1 = tf_au.paragraphs[0]
pau1.text = "1. BẢO MẬT & XÁC THỰC TOÀN DIỆN (FR-AUTH)"
pau1.font.name = "Segoe UI"
pau1.font.size = Pt(13)
pau1.font.bold = True
pau1.font.color.rgb = PRIMARY_BLUE
pau1.space_after = Pt(8)

auth_features = [
    ("JWT Token Rotation & Reuse Detection", "Access token (15p) + Refresh token (7 ngày). Mỗi lần refresh sinh ra cặp token mới và thu hồi token cũ, phát hiện tấn công phát lại."),
    ("Khóa tài khoản chống Brute-force", "Sau 5 lần đăng nhập thất bại liên tiếp, tài khoản tự động bị khóa tạm thời (Lockout) trong 15 phút."),
    ("Google OAuth 2.0 Integration", "Hỗ trợ đăng nhập nhanh bằng tài khoản Google, tự động liên kết hoặc tạo tài khoản mới."),
    ("Resource-based Authorization", "Kiểm tra quyền sở hữu công thức: chỉ tác giả hoặc Admin mới có quyền cập nhật, xuất bản hoặc xóa.")
]

for title, desc in auth_features:
    p = tf_au.add_paragraph()
    p.text = "✓ " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_au.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(10)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

# Right Column: Recipe Core & Concurrency
add_card(slide5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_rcp = slide5.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_rc = tb_rcp.text_frame
tf_rc.word_wrap = True

prc1 = tf_rc.paragraphs[0]
prc1.text = "2. QUẢN LÝ CÔNG THỨC & CONCURRENCY (FR-RCP)"
prc1.font.name = "Segoe UI"
prc1.font.size = Pt(13)
prc1.font.bold = True
prc1.font.color.rgb = PRIMARY_BLUE
prc1.space_after = Pt(8)

rcp_features = [
    ("Optimistic Concurrency Control (OCC)", "Quản lý bằng cột row_version. Khi cập nhật, nếu phiên bản client khác server sẽ ném lỗi 409 Conflict, chống Lost Update."),
    ("Aggregate Root & Cascade Lifecycle", "Recipe quản lý vòng đời Steps, Ingredients, Images. Cập nhật các bước tự động đánh số lại (renumbering)."),
    ("Soft Delete An Toàn", "Xóa mềm thông qua cờ is_deleted = True, bảo toàn lịch sử dữ liệu và quan hệ cơ sở dữ liệu."),
    ("Tự động sinh SEO Slug Tiếng Việt", "Tích hợp unidecode biến đổi tiêu đề thành slug URL chuẩn hóa (banh-canh-cua-gio-heo).")
]

for title, desc in rcp_features:
    p = tf_rc.add_paragraph()
    p.text = "✓ " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.space_after = Pt(1)
    
    pd = tf_rc.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(10)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

add_speaker_note(slide5,
    "KỊCH BẢN THUYẾT TRÌNH (40 giây):\n"
    "Đi sâu vào Backend Core, hệ thống sở hữu 2 điểm sáng kỹ thuật:\n"
    "Thứ nhất là cơ chế Xác thực bảo mật: nhóm cài đặt Token Rotation với tính năng phát hiện tái sử dụng token, khóa tài khoản chống dò pass "
    "và phân quyền Resource-based authorization.\n"
    "Thứ hai là Quản lý công thức: nhóm triển khai Optimistic Concurrency Control thông qua row_version để chống mất dữ liệu khi nhiều người sửa cùng lúc, "
    "kết hợp Soft Delete bảo vệ dữ liệu và tự động sinh slug chuẩn SEO."
)

# ==============================================================================
# SLIDE 6: BACKEND - SEARCH FTS, STORAGE & BACKGROUND JOBS (40s)
# ==============================================================================
slide6 = prs.slides.add_slide(blank_slide_layout)
add_header(slide6, "Tìm Kiếm FTS Tiếng Việt, MinIO S3 & Background Jobs")

col_w = Inches(3.7)
h_val = Inches(5.1)

# Card 1: FTS
add_card(slide6, Inches(0.8), Inches(1.8), col_w, h_val)
tb1 = slide6.shapes.add_textbox(Inches(1.0), Inches(2.0), col_w - Inches(0.4), h_val - Inches(0.4))
tf1 = tb1.text_frame
tf1.word_wrap = True
p = tf1.paragraphs[0]
p.text = "FULL-TEXT SEARCH TIẾNG VIỆT"
p.font.name = "Segoe UI"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = PRIMARY_BLUE
p.space_after = Pt(8)

p_fts = [
    "Cấu hình 'simple' trong PostgreSQL giúp không bị mất từ dừng tiếng Anh.",
    "Tích hợp extension unaccent loại bỏ dấu tiếng Việt chuẩn xác.",
    "Đánh chỉ mục tsvector @@ plainto_tsquery trên Title và Description.",
    "Người dùng gõ 'pho bo' hay 'Phở Bò' đều trả về kết quả chính xác trong mili-giây."
]
for item in p_fts:
    pi = tf1.add_paragraph()
    pi.text = "• " + item
    pi.font.name = "Segoe UI"
    pi.font.size = Pt(10.5)
    pi.font.color.rgb = TEXT_DARK
    pi.space_after = Pt(8)

# Card 2: MinIO Storage
add_card(slide6, Inches(4.8), Inches(1.8), col_w, h_val)
tb2 = slide6.shapes.add_textbox(Inches(5.0), Inches(2.0), col_w - Inches(0.4), h_val - Inches(0.4))
tf2 = tb2.text_frame
tf2.word_wrap = True
p2 = tf2.paragraphs[0]
p2.text = "MINIO S3 STORAGE SERVICE"
p2.font.name = "Segoe UI"
p2.font.size = Pt(12)
p2.font.bold = True
p2.font.color.rgb = AMBER_GOLD
p2.space_after = Pt(8)

p_s3 = [
    "Lưu trữ đối tượng chuẩn AWS S3 tương thích cao.",
    "Kiểm tra MIME type và Magic Bytes thực tế của file ảnh trước khi lưu.",
    "Giới hạn dung lượng tối đa 5MB / ảnh, ngăn chặn tấn công tệp độc hại.",
    "Tự động tạo ảnh Thumbnail kích thước nhỏ bằng thư viện Pillow phục vụ Catalog."
]
for item in p_s3:
    pi = tf2.add_paragraph()
    pi.text = "• " + item
    pi.font.name = "Segoe UI"
    pi.font.size = Pt(10.5)
    pi.font.color.rgb = TEXT_DARK
    pi.space_after = Pt(8)

# Card 3: Background Jobs & Cron
add_card(slide6, Inches(8.8), Inches(1.8), col_w, h_val)
tb3 = slide6.shapes.add_textbox(Inches(9.0), Inches(2.0), col_w - Inches(0.4), h_val - Inches(0.4))
tf3 = tb3.text_frame
tf3.word_wrap = True
p3 = tf3.paragraphs[0]
p3.text = "BACKGROUND JOBS & CRON"
p3.font.name = "Segoe UI"
p3.font.size = Pt(12)
p3.font.bold = True
p3.font.color.rgb = GREEN_SUCCESS
p3.space_after = Pt(8)

p_jobs = [
    "APScheduler chạy ngầm định kỳ 24 giờ một lần.",
    "Tự động quét toàn bộ công thức Published để tạo file sitemap.xml phục vụ Google.",
    "Tích hợp MailHog SMTP sandbox gửi email chào mừng người dùng mới.",
    "Structured Logging kèm Correlation-ID truy vết từng bước xử lý của hệ thống."
]
for item in p_jobs:
    pi = tf3.add_paragraph()
    pi.text = "• " + item
    pi.font.name = "Segoe UI"
    pi.font.size = Pt(10.5)
    pi.font.color.rgb = TEXT_DARK
    pi.space_after = Pt(8)

add_speaker_note(slide6,
    "KỊCH BẢN THUYẾT TRÌNH (40 giây):\n"
    "Tiếp theo, về tìm kiếm và hạ tầng nền:\n"
    "Nhóm sử dụng Full-Text Search PostgreSQL với cấu hình 'simple' kết hợp hàm unaccent, giải quyết triệt để vấn đề tìm kiếm tiếng Việt không dấu.\n"
    "Dịch vụ lưu trữ MinIO S3 SDK kiểm tra Magic Bytes chống file giả mạo và tự động sinh thumbnail qua Pillow.\n"
    "Ngoài ra, hệ thống có Background Cron Job tự động cập nhật file sitemap.xml mỗi 24h và ghi log có cấu trúc với Correlation-ID."
)

# ==============================================================================
# SLIDE 7: FRONTEND - TRẢI NGHIỆM ĐỘC GIẢ & SEO (40s)
# ==============================================================================
slide7 = prs.slides.add_slide(blank_slide_layout)
add_header(slide7, "Frontend Public Web: Tối Ưu Trải Nghiệm & SEO")

# Left: Text features
add_card(slide7, Inches(0.8), Inches(1.8), Inches(5.2), Inches(5.1))
tb_fe = slide7.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(4.8), Inches(4.7))
tf_fe = tb_fe.text_frame
tf_fe.word_wrap = True

pfe = tf_fe.paragraphs[0]
pfe.text = "TÍNH NĂNG DÀNH CHO ĐỘC GIẢ"
pfe.font.name = "Segoe UI"
pfe.font.size = Pt(13)
pfe.font.bold = True
pfe.font.color.rgb = PRIMARY_BLUE
pfe.space_after = Pt(8)

fe_points = [
    ("Giao diện Trang chủ (Home Page)", "Banner nổi bật, hiển thị danh mục món ăn trực quan và các công thức mới xuất bản."),
    ("Bộ lọc Catalog thông minh", "Kết hợp lọc theo Danh mục, Độ khó (Dễ/TB/Khó), Thời gian nấu và Phân trang mượt mà."),
    ("Trang Chi tiết món ăn (Recipe Detail)", "Hiển thị ảnh bìa sắc nét, danh sách nguyên liệu, các bước thực hiện và chỉ số dinh dưỡng rõ ràng."),
    ("Tối ưu SEO & Schema.org JSON-LD", "Nhúng dữ liệu có cấu trúc Recipe Schema giúp Google hiển thị Rich Snippets trực tiếp trên kết quả tìm kiếm.")
]

for title, desc in fe_points:
    p = tf_fe.add_paragraph()
    p.text = "• " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_fe.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(10)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

# Right: Screenshot Demo
img_path1 = os.path.join(SCREENSHOTS_DIR, "demo_03_recipe_detail.png")
if os.path.exists(img_path1):
    slide7.shapes.add_picture(img_path1, Inches(6.3), Inches(1.8), width=Inches(6.2))
else:
    add_card(slide7, Inches(6.3), Inches(1.8), Inches(6.2), Inches(5.1))

add_speaker_note(slide7,
    "KỊCH BẢN THUYẾT TRÌNH (40 giây):\n"
    "Ở phía người dùng cuối, Frontend được xây dựng bằng React 19 và Tailwind CSS hiện đại:\n"
    "Giao diện phân trang kết hợp bộ lọc thời gian thực. Trang chi tiết món ăn hiển thị trực quan từ nguyên liệu đến các bước nấu ăn.\n"
    "Đặc biệt, nhóm đã nhúng cấu trúc JSON-LD chuẩn Schema.org Recipe, giúp công cụ tìm kiếm của Google dễ dàng lập chỉ mục "
    "và hiển thị đầy đủ thông tin calo, thời gian nấu ngay ngoài kết quả tìm kiếm."
)

# ==============================================================================
# SLIDE 8: FRONTEND - DASHBOARD TÁC GIẢ & BỘ SOẠN THẢO (40s)
# ==============================================================================
slide8 = prs.slides.add_slide(blank_slide_layout)
add_header(slide8, "Creator Dashboard & Bộ Soạn Thảo Công Thức Đa Bước")

# Left: Text features
add_card(slide8, Inches(0.8), Inches(1.8), Inches(5.2), Inches(5.1))
tb_dash = slide8.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(4.8), Inches(4.7))
tf_d = tb_dash.text_frame
tf_d.word_wrap = True

pd1 = tf_d.paragraphs[0]
pd1.text = "CÔNG CỤ QUẢN TRỊ NỘI DUNG"
pd1.font.name = "Segoe UI"
pd1.font.size = Pt(13)
pd1.font.bold = True
pd1.font.color.rgb = PRIMARY_BLUE
pd1.space_after = Pt(8)

dash_points = [
    ("Bảng điều khiển tác giả (Dashboard)", "Theo dõi số lượng công thức theo trạng thái (Bản nháp / Xuất bản / Lưu trữ) và lượt xem."),
    ("Quản lý Recipe cá nhân (FR-DASH-002)", "Bảng quản lý công thức có hỗ trợ tìm kiếm nhanh, chuyển trạng thái và xóa an toàn."),
    ("Trình biên soạn Wizard đa bước", "Form tạo công thức chia làm các bước logic: Thông tin cơ bản -> Dinh dưỡng -> Nguyên liệu -> Các bước nấu -> Tải ảnh."),
    ("Kéo thả bước nấu (useDragReorder)", "Hỗ trợ kéo thả đổi vị trí các bước nấu trực quan, tự động renumbering trên giao diện và backend.")
]

for title, desc in dash_points:
    p = tf_d.add_paragraph()
    p.text = "• " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pdesc = tf_d.add_paragraph()
    pdesc.text = desc
    pdesc.font.name = "Segoe UI"
    pdesc.font.size = Pt(10)
    pdesc.font.color.rgb = TEXT_DARK
    pdesc.space_after = Pt(6)

# Right: Screenshot Demo
img_path2 = os.path.join(SCREENSHOTS_DIR, "demo_09_creator_dashboard.png")
if os.path.exists(img_path2):
    slide8.shapes.add_picture(img_path2, Inches(6.3), Inches(1.8), width=Inches(6.2))
else:
    add_card(slide8, Inches(6.3), Inches(1.8), Inches(6.2), Inches(5.1))

add_speaker_note(slide8,
    "KỊCH BẢN THUYẾT TRÌNH (40 giây):\n"
    "Dành cho các tác giả nấu ăn, nhóm đã thiết kế Creator Dashboard trực quan:\n"
    "Tác giả quản lý toàn bộ các công thức ở trạng thái Draft, Published và Archived. "
    "Bộ công cụ Recipe Editor Wizard cho phép nhập liệu từng bước, hỗ trợ thêm ảnh bìa MinIO với thanh tiến trình tải lên, "
    "và tích hợp kéo thả thay đổi thứ tự các bước nấu ăn vô cùng mượt mà qua custom hook useDragReorder."
)

# ==============================================================================
# SLIDE 9: GIẢI QUYẾT MÂU THUẪN SRS & ĐIỂM SÁNG DỰ ÁN (40s)
# ==============================================================================
slide9 = prs.slides.add_slide(blank_slide_layout)
add_header(slide9, "Giải Quyết Mâu Thuẫn Trong SRS & Điểm Sáng Dự Án")

# Card Left: Mâu thuẫn & Giải pháp
add_card(slide9, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_m = slide9.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_m = tb_m.text_frame
tf_m.word_wrap = True

pm = tf_m.paragraphs[0]
pm.text = "1. MÂU THUẪN SRS & HƯỚNG GIẢI QUYẾT"
pm.font.name = "Segoe UI"
pm.font.size = Pt(13)
pm.font.bold = True
pm.font.color.rgb = PRIMARY_BLUE
pm.space_after = Pt(8)

conflicts = [
    ("Soft Delete vs Unique Constraint trên Slug", "Vấn đề: Xóa mềm thì bài cũ vẫn còn trong DB, tạo bài mới cùng slug bị lỗi.\nGiải pháp: Sử dụng Partial Unique Index (WHERE is_deleted = false) trong PostgreSQL."),
    ("JWT Stateless vs Thu hồi Token (Revocation)", "Vấn đề: Token stateless không thể thu hồi trước hạn hết hạn.\nGiải pháp: Áp dụng mô hình Hybrid: Access Token ngắn hạn (15p) + Refresh Token whitelist lưu DB/Redis, hỗ trợ đưa token vào Blacklist tức thì."),
    ("Sự pha trộn công nghệ (.NET vs Python/React)", "Giải pháp: Ánh xạ chuẩn mực kiến trúc từ SRS sang hệ sinh thái FastAPI, SQLAlchemy Async và React SPA.")
]

for title, desc in conflicts:
    p = tf_m.add_paragraph()
    p.text = "► " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_m.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

# Card Right: Điểm mới
add_card(slide9, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_new = slide9.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_n = tb_new.text_frame
tf_n.word_wrap = True

pn = tf_n.paragraphs[0]
pn.text = "2. NHỮNG TÍNH NĂNG MỚI NỔI BẬT"
pn.font.name = "Segoe UI"
pn.font.size = Pt(13)
pn.font.bold = True
pn.font.color.rgb = GREEN_SUCCESS
pn.space_after = Pt(8)

new_feats = [
    ("Tự động sinh Slug tiếng Việt chuẩn SEO", "Chuyển đổi tiêu đề có dấu thành URL slug thân thiện tự động, xử lý chống trùng lặp bằng hậu tố ngẫu nhiên."),
    ("Cron Job tự động sinh Sitemap XML", "APScheduler chạy ngầm định kỳ 24h quét toàn bộ bài viết Published phục vụ Google Search Console."),
    ("Bộ 3 Probe Health Check Cloud-Native", "Tách bạch /health/live (process) và /health/ready (kết nối DB, Redis) theo chuẩn Kubernetes/Docker."),
    ("Trang Quản trị Người Dùng (Users Page)", "Bổ sung màn hình Admin cho phép kích hoạt, khóa tài khoản và phân quyền tác giả trực quan.")
]

for title, desc in new_feats:
    p = tf_n.add_paragraph()
    p.text = "★ " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_n.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

add_speaker_note(slide9,
    "KỊCH BẢN THUYẾT TRÌNH (40 giây):\n"
    "Trong quá trình thực hiện, nhóm đã phát hiện và xử lý thành công 2 mâu thuẫn lớn trong file SRS:\n"
    "Mâu thuẫn thứ nhất giữa Soft Delete và ràng buộc Unique slug, được nhóm giải quyết bằng Partial Index trong PostgreSQL.\n"
    "Mâu thuẫn thứ hai giữa JWT Stateless và yêu cầu thu hồi tức thì, được nhóm giải quyết bằng mô hình Hybrid kết hợp Redis Blacklist.\n"
    "Đồng thời, nhóm đã bổ sung các tính năng giá trị như sinh slug tiếng Việt tự động, cron sitemap.xml và hệ thống Health Check 3 mức."
)

# ==============================================================================
# SLIDE 10: DEVOPS, KIỂM THỬ & GIÁM SÁT HỆ THỐNG (35s)
# ==============================================================================
slide10 = prs.slides.add_slide(blank_slide_layout)
add_header(slide10, "DevOps, Đóng Gói Docker & Giám Sát Vận Hành")

# Left Column: Docker Compose & Probes
add_card(slide10, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_dev = slide10.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_dv = tb_dev.text_frame
tf_dv.word_wrap = True

pdv = tf_dv.paragraphs[0]
pdv.text = "HẠ TẦNG DOCKER & OBSERVABILITY"
pdv.font.name = "Segoe UI"
pdv.font.size = Pt(13)
pdv.font.bold = True
pdv.font.color.rgb = PRIMARY_BLUE
pdv.space_after = Pt(8)

dev_points = [
    ("Đóng gói Docker Compose 1-Click", "Chạy trọn gói 6 containers: Nginx, Backend API, Frontend Vite, PostgreSQL, Redis, MinIO và MailHog."),
    ("Tách bạch Liveness & Readiness Probes", "Endpoint /health/live kiểm tra process, /health/ready kiểm tra kết nối DB và Redis, tránh lỗi CrashLoopBackOff khi DB chậm."),
    ("Truy vết với X-Correlation-ID", "Gắn định danh UUID duy nhất cho từng HTTP request xuyên suốt từ Nginx đến DB logs."),
    ("Kiểm thử tự động với Pytest", "Bộ test case Unit & Integration test kiểm tra tính đúng đắn của Auth, Categories, Recipes và Health Checks.")
]

for title, desc in dev_points:
    p = tf_dv.add_paragraph()
    p.text = "✔ " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_dv.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(10)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

# Right: Screenshot Swagger / Health Probe
img_path3 = os.path.join(SCREENSHOTS_DIR, "demo_14_swagger_docs.png")
if os.path.exists(img_path3):
    slide10.shapes.add_picture(img_path3, Inches(6.8), Inches(1.8), width=Inches(5.7))
else:
    add_card(slide10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))

add_speaker_note(slide10,
    "KỊCH BẢN THUYẾT TRÌNH (35 giây):\n"
    "Về khía cạnh vận hành, toàn bộ dự án được triển khai chỉ với 1 câu lệnh docker compose up.\n"
    "Tài liệu API Swagger và Redoc được sinh tự động 100%. "
    "Hệ thống trang bị bộ probe giám sát sức khỏe chuẩn Cloud-Native giúp phát hiện sự cố sớm, "
    "kèm theo bộ kiểm thử tự động Pytest đảm bảo độ tin cậy cao nhất cho mã nguồn."
)

# ==============================================================================
# SLIDE 11: TỔNG KẾT KẾT QUẢ ĐẠT ĐƯỢC (30s)
# ==============================================================================
slide11 = prs.slides.add_slide(blank_slide_layout)
add_header(slide11, "Tổng Kết Đồ Án & Kết Quả Đạt Được")

# 4 Metric Cards
metrics = [
    ("100%", "HOÀN THÀNH SRS", "Toàn bộ chức năng trong tài liệu đặc tả SRS v1.0.0 đều được hiện thực và kiểm thử."),
    ("6+", "DỊCH VỤ DOCKER", "Hạ tầng container hóa chuẩn mực: Nginx, FastAPI, React 19, Postgres, Redis, MinIO."),
    ("100/100", "BẢO MẬT & SEO", "Tích hợp Token Rotation, Brute-force Lockout, FTS tiếng Việt và Schema.org JSON-LD."),
    ("01", "BỘ MÃ NGUỒN CHUẨN", "Cấu trúc Clean Architecture dễ bảo trì, sẵn sàng mở rộng và đóng gói lên Cloud.")
]

for idx, (stat, title, desc) in enumerate(metrics):
    row = idx // 2
    col = idx % 2
    left = Inches(0.8 + col * 6.0)
    top = Inches(1.8 + row * 2.6)
    
    add_card(slide11, left, top, Inches(5.7), Inches(2.4))
    tb = slide11.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), Inches(5.3), Inches(2.0))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = stat
    p.font.name = "Segoe UI"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    
    pt = tf.add_paragraph()
    pt.text = title
    pt.font.name = "Segoe UI"
    pt.font.size = Pt(12)
    pt.font.bold = True
    pt.font.color.rgb = DARK_NAVY
    pt.space_after = Pt(4)
    
    pd = tf.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(10.5)
    pd.font.color.rgb = TEXT_MUTED

add_speaker_note(slide11,
    "KỊCH BẢN THUYẾT TRÌNH (30 giây):\n"
    "Tổng kết lại, Nhóm 25 đã hoàn thành trọn vẹn 100% các yêu cầu chức năng và phi chức năng theo đặc tả SRS v1.0.0. "
    "Hệ thống đạt chuẩn cao về mặt kiến trúc, bảo mật và trải nghiệm người dùng, "
    "sẵn sàng đóng gói và triển khai trên các nền tảng đám mây thực tế."
)

# ==============================================================================
# SLIDE 12: CẢM ƠN & Q&A (20s)
# ==============================================================================
slide12 = prs.slides.add_slide(blank_slide_layout)
bg12 = slide12.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
bg12.fill.solid()
bg12.fill.fore_color.rgb = DARK_NAVY
bg12.line.fill.background()

tb12 = slide12.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.3), Inches(3.5))
tf12 = tb12.text_frame
tf12.word_wrap = True

p_thx = tf12.paragraphs[0]
p_thx.alignment = PP_ALIGN.CENTER
p_thx.text = "XIN CHÂN THÀNH CẢM ƠN CÔ VÀ CÁC BẠN!"
p_thx.font.name = "Segoe UI"
p_thx.font.size = Pt(32)
p_thx.font.bold = True
p_thx.font.color.rgb = WHITE
p_thx.space_after = Pt(14)

p_qa = tf12.add_paragraph()
p_qa.alignment = PP_ALIGN.CENTER
p_qa.text = "HỆ THỐNG CULINARY BLOG • NHÓM 25 SẴN SÀNG CHO PHẦN Q&A VÀ DEMO"
p_qa.font.name = "Segoe UI"
p_qa.font.size = Pt(16)
p_qa.font.bold = True
p_qa.font.color.rgb = AMBER_GOLD
p_qa.space_after = Pt(20)

p_src = tf12.add_paragraph()
p_src.alignment = PP_ALIGN.CENTER
p_src.text = "GitHub: https://github.com/NHNam1209/PTUDW-2026-Nhom25"
p_src.font.name = "Segoe UI"
p_src.font.size = Pt(13)
p_src.font.color.rgb = RGBColor(148, 163, 184)

add_speaker_note(slide12,
    "KỊCH BẢN THUYẾT TRÌNH (20 giây):\n"
    "Trên đây là toàn bộ phần trình bày về kiến trúc và các giải pháp kỹ thuật của Hệ thống Culinary Blog. "
    "Em xin chân thành cảm ơn Cô và các bạn đã chú ý lắng nghe. Sau đây, Nhóm 25 rất mong nhận được những góp ý, câu hỏi phản biện từ Cô "
    "và xin phép chuyển sang phần Demo trực tiếp sản phẩm!"
)

prs.save(OUTPUT_PPTX)
print("Saved PPTX successfully:", OUTPUT_PPTX)
