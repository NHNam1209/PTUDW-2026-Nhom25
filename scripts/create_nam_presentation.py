# -*- coding: utf-8 -*-
"""
Script to generate Slide_Bao_Cao_Ca_Nhan_Nguyen_Hoai_Nam.pptx
PowerPoint presentation specifically tailored for Nguyen Hoai Nam's defense (6-7 mins).
Focuses strictly on: DevOps, Backend Core, Auth & Security, Recipe Management & OCC, Health Checks.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

WORKSPACE_DIR = r"D:\PTUDWNC\PTUDW-2026-Nhom25"
SCREENSHOTS_DIR = os.path.join(WORKSPACE_DIR, "screenshots")
OUTPUT_PPTX = os.path.join(WORKSPACE_DIR, "Slide_Bao_Cao_Ca_Nhan_Nguyen_Hoai_Nam.pptx")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

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

blank_layout = prs.slide_layouts[6]

def add_header(slide, title_text, category_text="BÁO CÁO CÁ NHÂN: NGUYỄN HOÀI NAM (LEAD) • CULINARY BLOG"):
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p_cat = tf.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.name = "Segoe UI"
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = ACCENT_BLUE
    p_cat.space_after = Pt(2)
    
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
# SLIDE 1: TIÊU ĐỀ BÁO CÁO CÁ NHÂN (30s)
# ==============================================================================
slide1 = prs.slides.add_slide(blank_layout)
bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
bg1.fill.solid()
bg1.fill.fore_color.rgb = DARK_NAVY
bg1.line.fill.background()

tb1 = slide1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(4.5))
tf1 = tb1.text_frame
tf1.word_wrap = True

p_sub = tf1.paragraphs[0]
p_sub.text = "BÁO CÁO BẢO VỆ ĐỒ ÁN CUỐI KỲ • PHẦN TRÌNH BÀY CÁ NHÂN"
p_sub.font.name = "Segoe UI"
p_sub.font.size = Pt(13)
p_sub.font.bold = True
p_sub.font.color.rgb = AMBER_GOLD
p_sub.space_after = Pt(10)

p_title = tf1.add_paragraph()
p_title.text = "NGUYỄN HOÀI NAM (TRƯỞNG NHÓM)"
p_title.font.name = "Segoe UI"
p_title.font.size = Pt(36)
p_title.font.bold = True
p_title.font.color.rgb = WHITE
p_title.space_after = Pt(8)

p_desc = tf1.add_paragraph()
p_desc.text = "Trách nhiệm: Kiến trúc Hệ thống, Backend Core, Xác thực & Bảo mật, Recipe Core, DevOps"
p_desc.font.name = "Segoe UI"
p_desc.font.size = Pt(17)
p_desc.font.color.rgb = RGBColor(203, 213, 225)
p_desc.space_after = Pt(25)

# Info Card
info_card = add_card(slide1, Inches(1.0), Inches(4.6), Inches(11.3), Inches(2.1), bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
tb_info = slide1.shapes.add_textbox(Inches(1.2), Inches(4.8), Inches(10.9), Inches(1.7))
tf_info = tb_info.text_frame
tf_info.word_wrap = True

p1 = tf_info.paragraphs[0]
p1.text = "Đề tài: Hệ thống Culinary Blog (Nhóm 25) • GVHD: TS. Nguyễn Thị Lương"
p1.font.name = "Segoe UI"
p1.font.size = Pt(14)
p1.font.bold = True
p1.font.color.rgb = WHITE
p1.space_after = Pt(4)

p2 = tf_info.add_paragraph()
p2.text = "Sinh viên thực hiện: Nguyễn Hoài Nam — MSSV: 2312607 / 2312694 (Lớp: CTK47-PM)"
p2.font.name = "Segoe UI"
p2.font.size = Pt(13)
p2.font.color.rgb = RGBColor(226, 232, 240)
p2.space_after = Pt(4)

p3 = tf_info.add_paragraph()
p3.text = "Phạm vi báo cáo: Toàn bộ các Issues từ #1 đến #19 (SETUP, DEVOPS, FR-AUTH, FR-RCP, FR-OBS-001)"
p3.font.name = "Segoe UI"
p3.font.size = Pt(12)
p3.font.italic = True
p3.font.color.rgb = AMBER_GOLD

add_speaker_note(slide1,
    "KỊCH BẢN NÓI (30 giây):\n"
    "Kính thưa Cô và các bạn! Em tên là Nguyễn Hoài Nam, Trưởng nhóm 25. "
    "Hôm nay, em xin phép đại diện nhóm báo cáo phần công việc mà bản thân em trực tiếp thiết kế và cài đặt trong dự án Culinary Blog. "
    "Phần việc của em bao gồm: Thiết kế kiến trúc tổng thể, hạ tầng DevOps & Docker, xây dựng toàn bộ Module Xác thực và Bảo mật tài khoản, "
    "Module Quản lý Công thức cốt lõi, kiểm soát Concurrency và bộ Health Check Probes theo chuẩn Cloud-Native."
)

# ==============================================================================
# SLIDE 2: TỔNG HỢP KHỐI LƯỢNG CÔNG VIỆC CÁ NHÂN (35s)
# ==============================================================================
slide2 = prs.slides.add_slide(blank_layout)
add_header(slide2, "Tổng Hợp Trách Nhiệm & Khối Lượng Công Việc Đã Thực Hiện")

cols = [
    ("DEVOPS & HẠ TẦNG", "Khởi tạo & Điều phối", [
        "Docker Compose 6 dịch vụ",
        "Nginx Reverse Proxy & Routing",
        "PostgreSQL 16 DB init & Seeding",
        "Kiến trúc Clean Architecture"
    ], PRIMARY_BLUE),
    ("AUTH & BẢO MẬT (FR-AUTH)", "7 Chức năng hoàn chỉnh", [
        "FR-AUTH-001: User Registration",
        "FR-AUTH-002: Login & Lockout",
        "FR-AUTH-003: Google OAuth 2.0",
        "FR-AUTH-004: Token Rotation",
        "FR-AUTH-005: Logout & Blacklist",
        "FR-AUTH-006/007: User Profile"
    ], AMBER_GOLD),
    ("RECIPE CORE (FR-RCP)", "10 Chức năng nghiệp vụ", [
        "FR-RCP-001: Listing & Pagination",
        "FR-RCP-002: Recipe Detail View",
        "FR-RCP-003: Create Recipe Draft",
        "FR-RCP-004: Concurrency (row_version)",
        "FR-RCP-005/006: Publish & Archive",
        "FR-RCP-007/008: Delete & Media",
        "FR-RCP-009/010: Steps & Ingredients"
    ], GREEN_SUCCESS),
    ("OBSERVABILITY (FR-OBS)", "Giám sát Cloud-Native", [
        "FR-OBS-001: Health Check Probes",
        "Tách bạch /health/live (Process)",
        "Tách bạch /health/ready (DB/Redis)",
        "X-Correlation-ID tracing log"
    ], ACCENT_BLUE)
]

for idx, (title, sub, bullets, color) in enumerate(cols):
    left = Inches(0.8 + idx * 3.0)
    add_card(slide2, left, Inches(1.8), Inches(2.8), Inches(5.1))
    
    tb = slide2.shapes.add_textbox(left + Inches(0.15), Inches(2.0), Inches(2.5), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = color
    p.space_after = Pt(2)
    
    ps = tf.add_paragraph()
    ps.text = sub
    ps.font.name = "Segoe UI"
    ps.font.size = Pt(9.5)
    ps.font.italic = True
    ps.font.color.rgb = TEXT_MUTED
    ps.space_after = Pt(10)
    
    for b in bullets:
        pb = tf.add_paragraph()
        pb.text = "• " + b
        pb.font.name = "Segoe UI"
        pb.font.size = Pt(9.5)
        pb.font.color.rgb = TEXT_DARK
        pb.space_after = Pt(4)

add_speaker_note(slide2,
    "KỊCH BẢN NÓI (35 giây):\n"
    "Cụ thể, trong đồ án này, em trực tiếp đảm nhiệm và hoàn thành 19 issues cốt lõi theo đặc tả SRS:\n"
    "- Về DevOps: Em thiết lập toàn bộ Docker Compose 6 dịch vụ, Nginx proxy và khởi tạo database seeding.\n"
    "- Về Module Auth: Em lập trình đầy đủ từ Đăng ký, Đăng nhập với cơ chế khóa tài khoản, Google OAuth 2.0 đến Token Rotation.\n"
    "- Về Recipe Core: Em cài đặt toàn bộ vòng đời công thức món ăn, kiểm soát concurrency bằng row_version, quản lý nguyên liệu và các bước nấu.\n"
    "- Về Vận hành: Em xây dựng bộ 3 endpoint Health Check phục vụ liveness và readiness probes."
)

# ==============================================================================
# SLIDE 3: KIẾN TRÚC DEVOPS & DOCKER COMPOSE (45s)
# ==============================================================================
slide3 = prs.slides.add_slide(blank_layout)
add_header(slide3, "Hạ Tầng DevOps & Kiến Trúc Container Hóa")

# Left: Text
add_card(slide3, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_d = slide3.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_d = tb_d.text_frame
tf_d.word_wrap = True

pd1 = tf_d.paragraphs[0]
pd1.text = "THIẾT KẾ ĐIỀU PHỐI DOCKER & NGINX"
pd1.font.name = "Segoe UI"
pd1.font.size = Pt(13)
pd1.font.bold = True
pd1.font.color.rgb = PRIMARY_BLUE
pd1.space_after = Pt(8)

devops_items = [
    ("Nginx Reverse Proxy (Port 80)", "Tiếp nhận toàn bộ request từ người dùng; định tuyến /api/v1 sang Backend container và các request còn lại sang Frontend Vite container."),
    ("FastAPI Backend Container (Port 8000)", "Môi trường Python 3.12, chạy qua Uvicorn worker. Giao tiếp bất đồng bộ qua asyncpg và SQLAlchemy 2.0."),
    ("PostgreSQL 16 Alpine (Port 5433:5432)", "Kèm script init.sql tự động kích hoạt extension unaccent, pg_trgm và seed dữ liệu 41 công thức mẫu."),
    ("Redis 7 Alpine (Port 6381:6379)", "Phân tán cache, lưu trữ Blacklist Token khi logout và bộ đếm Rate Limiting theo IP."),
    ("MinIO & MailHog Sandbox", "Object Storage chuẩn S3 lưu trữ tệp ảnh; MailHog bắt trọn email SMTP trên cổng 8025 để demo an toàn.")
]

for title, desc in devops_items:
    p = tf_d.add_paragraph()
    p.text = "► " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pdesc = tf_d.add_paragraph()
    pdesc.text = desc
    pdesc.font.name = "Segoe UI"
    pdesc.font.size = Pt(9.5)
    pdesc.font.color.rgb = TEXT_DARK
    pdesc.space_after = Pt(6)

# Right: Screenshot Mailhog or Console
img_path_m = os.path.join(SCREENSHOTS_DIR, "demo_16_mailhog_ui.png")
if os.path.exists(img_path_m):
    slide3.shapes.add_picture(img_path_m, Inches(6.8), Inches(1.8), width=Inches(5.7))
else:
    add_card(slide3, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))

add_speaker_note(slide3,
    "KỊCH BẢN NÓI (45 giây):\n"
    "Bắt đầu với phần Hạ tầng DevOps: Em đã xây dựng giải pháp container hóa hoàn chỉnh qua Docker Compose gồm 6 dịch vụ độc lập.\n"
    "Ở tầng biên, Nginx lắng nghe cổng 80, giải quyết bài toán định tuyến và CORS cho toàn hệ thống.\n"
    "Cơ sở dữ liệu PostgreSQL 16 được tích hợp health check tự động khởi chạy và nạp sẵn 41 công thức mẫu.\n"
    "Hệ thống còn có Redis quản lý token blacklist và MailHog làm SMTP server ảo bắt trọn email chào mừng gửi từ background job."
)

# ==============================================================================
# SLIDE 4: MODULE XÁC THỰC & BẢO MẬT NÂNG CAO (50s)
# ==============================================================================
slide4 = prs.slides.add_slide(blank_layout)
add_header(slide4, "Module Xác Thực & Bảo Mật Nâng Cao (FR-AUTH-001 -> 007)")

add_card(slide4, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_a1 = slide4.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_a1 = tb_a1.text_frame
tf_a1.word_wrap = True

pa1 = tf_a1.paragraphs[0]
pa1.text = "1. BẢO MẬT ĐĂNG NHẬP & CHỐNG TẤN CÔNG"
pa1.font.name = "Segoe UI"
pa1.font.size = Pt(13)
pa1.font.bold = True
pa1.font.color.rgb = PRIMARY_BLUE
pa1.space_after = Pt(8)

auth_items_1 = [
    ("Mã hóa mật khẩu Bcrypt an toàn", "Mật khẩu được băm bằng Passlib Bcrypt với salt ngẫu nhiên. Validation mật khẩu yêu cầu tối thiểu 8 ký tự, có chữ hoa, chữ thường và số."),
    ("Khóa tài khoản chống Brute-force", "Hàm login() theo dõi số lần thất bại (access_failed_count). Khi sai 5 lần liên tiếp, trường lockout_end kích hoạt khóa tài khoản trong 15 phút."),
    ("Google OAuth 2.0 Identity Provider", "Verify ID Token từ Google, tự động sinh username không trùng lặp và cấp cặp token JWT phiên làm việc.")
]

for title, desc in auth_items_1:
    p = tf_a1.add_paragraph()
    p.text = "✔ " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_a1.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

add_card(slide4, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_a2 = slide4.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_a2 = tb_a2.text_frame
tf_a2.word_wrap = True

pa2 = tf_a2.paragraphs[0]
pa2.text = "2. TOKEN ROTATION & PHÁT HIỆN TÁI SỬ DỤNG"
pa2.font.name = "Segoe UI"
pa2.font.size = Pt(13)
pa2.font.bold = True
pa2.font.color.rgb = AMBER_GOLD
pa2.space_after = Pt(8)

auth_items_2 = [
    ("Mô hình Cặp Token (Hybrid Model)", "Access Token có hạn ngắn (15 phút) mang tính stateless. Refresh Token có hạn 7 ngày, lưu mã băm SHA-256 trong bảng refresh_tokens."),
    ("Token Rotation (Xoay vòng token)", "Mỗi lần client gửi Refresh Token, hệ thống lập tức thu hồi (revoke) token cũ và phát hành cặp token hoàn toàn mới."),
    ("Phát hiện tấn công phát lại (Reuse Attack)", "Nếu một Refresh Token đã bị revoke được gửi lại, hệ thống lập tức thu hồi toàn bộ phiên của người dùng đó (revoked_at = now) để ngăn chặn kẻ gian chiếm đoạt tài khoản.")
]

for title, desc in auth_items_2:
    p = tf_a2.add_paragraph()
    p.text = "★ " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_a2.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

add_speaker_note(slide4,
    "KỊCH BẢN NÓI (50 giây):\n"
    "Về Module Xác thực và Bảo mật: Em thiết kế bảo mật đa lớp theo tiêu chuẩn công nghiệp:\n"
    "Thứ nhất, đối với đăng nhập, em lập trình cơ chế theo dõi access_failed_count; nếu nhập sai 5 lần, hệ thống kích hoạt lockout_end khóa 15 phút.\n"
    "Thứ hai, điểm đặc biệt nhất là kỹ thuật Refresh Token Rotation: Mỗi lần cấp mới access token, refresh token cũ bị đánh dấu thu hồi ngay lập tức. "
    "Nếu kẻ tấn công đánh cắp được token cũ và gửi lên, hệ thống sẽ phát hiện hành vi Token Reuse và tự động vô hiệu hóa toàn bộ token của tài khoản đó. "
    "Em cũng đã tích hợp xác thực SSO qua Google OAuth 2.0."
)

# ==============================================================================
# SLIDE 5: MODULE CÔNG THỨC & VÒNG ĐỜI RECIPE (45s)
# ==============================================================================
slide5 = prs.slides.add_slide(blank_layout)
add_header(slide5, "Module Công Thức Cốt Lõi (FR-RCP-001 -> FR-RCP-010)")

add_card(slide5, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_r1 = slide5.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_r1 = tb_r1.text_frame
tf_r1.word_wrap = True

pr1 = tf_r1.paragraphs[0]
pr1.text = "1. VÒNG ĐỜI CÔNG THỨC & QUY TẮC NGHIỆP VỤ"
pr1.font.name = "Segoe UI"
pr1.font.size = Pt(13)
pr1.font.bold = True
pr1.font.color.rgb = PRIMARY_BLUE
pr1.space_after = Pt(8)

rcp_items_1 = [
    ("Trạng thái Bản nháp (Draft)", "Cho phép tác giả lưu trữ công thức chưa hoàn thiện, không hiển thị ra trang công khai."),
    ("Điều kiện Xuất bản (Publish)", "Hàm publish_recipe() kiểm tra chặt chẽ: công thức bắt buộc phải có ít nhất 1 bước nấu và 1 nguyên liệu mới cho phép xuất bản."),
    ("Lưu trữ (Archive) & Xóa mềm", "Cho phép tác giả ẩn công thức tạm thời. Khi xóa, thực hiện Soft Delete (is_deleted = True) để bảo toàn dữ liệu liên quan."),
    ("Tự động Renumbering các bước nấu", "Khi thêm, sửa, xóa bước nấu (RecipeStep), hệ thống tự động sắp xếp và đánh số lại từ 1 đến N liên tục.")
]

for title, desc in rcp_items_1:
    p = tf_r1.add_paragraph()
    p.text = "• " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_r1.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

add_card(slide5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_r2 = slide5.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_r2 = tb_r2.text_frame
tf_r2.word_wrap = True

pr2 = tf_r2.paragraphs[0]
pr2.text = "2. PHÂN TRANG & TỐI ƯU HÓA TRUY VẤN ORM"
pr2.font.name = "Segoe UI"
pr2.font.size = Pt(13)
pr2.font.bold = True
pr2.font.color.rgb = GREEN_SUCCESS
pr2.space_after = Pt(8)

rcp_items_2 = [
    ("Phân trang Offset-based (page, pageSize)", "Hỗ trợ duyệt theo số trang, tính toán tổng số trang totalPages. Kết hợp lọc theo danh mục, độ khó, thời gian nấu."),
    ("Giải quyết Cartesian Explosion", "Trong hàm get_recipes(), em sử dụng selectinload(Recipe.category), selectinload(Recipe.author), selectinload(Recipe.images) thay vì joinedload."),
    ("Tối ưu hóa băng thông mạng", "Thay vì sinh câu lệnh JOIN nhân chéo hàng trăm dòng (Cartesian Explosion), selectinload tách thành các query độc lập, giảm lượng dữ liệu truyền qua network từ 150 dòng xuống còn 26 dòng!")
]

for title, desc in rcp_items_2:
    p = tf_r2.add_paragraph()
    p.text = "• " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_r2.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

add_speaker_note(slide5,
    "KỊCH BẢN NÓI (45 giây):\n"
    "Chuyển sang Module Recipe Core: Em chịu trách nhiệm thiết kế toàn bộ vòng đời của công thức từ Draft, Publish tới Archive.\n"
    "Khi xuất bản, em cài đặt điều kiện ràng buộc bắt buộc phải có tối thiểu 1 bước và 1 nguyên liệu.\n"
    "Các bước nấu khi bị xóa hoặc chèn thêm sẽ được tự động đánh số lại liên tục.\n"
    "Đặc biệt, về mặt hiệu năng CSDL, khi query danh sách công thức, em sử dụng kỹ thuật selectinload của SQLAlchemy để tránh hiện tượng "
    "Cartesian Explosion - tức bùng nổ tích Descartes khi nạp nhiều collection quan hệ, giúp giảm đáng kể thời gian phản hồi."
)

# ==============================================================================
# SLIDE 6: OPTIMISTIC CONCURRENCY & SOFT DELETE (50s)
# ==============================================================================
slide6 = prs.slides.add_slide(blank_layout)
add_header(slide6, "Kiểm Soát Concurrency (OCC) & Ràng Buộc Toàn Vẹn")

# Left Column: Code OCC
add_card(slide6, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_c1 = slide6.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_c1 = tb_c1.text_frame
tf_c1.word_wrap = True

pc1 = tf_c1.paragraphs[0]
pc1.text = "KIỂM SOÁT ĐỒNG THỜI (ROW_VERSION)"
pc1.font.name = "Segoe UI"
pc1.font.size = Pt(13)
pc1.font.bold = True
pc1.font.color.rgb = PRIMARY_BLUE
pc1.space_after = Pt(6)

c1_desc = [
    ("Vấn đề Lost Update", "Xảy ra khi 2 phiên cùng mở 1 bài viết để chỉnh sửa. Người lưu sau sẽ ghi đè và làm mất dữ liệu của người lưu trước."),
    ("Cài đặt Optimistic Concurrency Control", "Trong BaseEntity, em định nghĩa cột row_version = Column(Integer, default=1)."),
    ("Xử lý tại API update_recipe()", "Em kiểm tra: if recipe.row_version != payload.row_version thì lập tức raise ConcurrencyConflictException trả về mã lỗi 409 Conflict."),
    ("Tăng phiên bản nguyên tử", "Nếu khớp phiên bản, hệ thống cập nhật dữ liệu và tăng recipe.row_version += 1.")
]

for title, desc in c1_desc:
    p = tf_c1.add_paragraph()
    p.text = "► " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_c1.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(5)

# Right Column: Soft Delete & Partial Index
add_card(slide6, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_c2 = slide6.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_c2 = tb_c2.text_frame
tf_c2.word_wrap = True

pc2 = tf_c2.paragraphs[0]
pc2.text = "XỬ LÝ MÂU THUẪN SOFT DELETE & UNIQUE SLUG"
pc2.font.name = "Segoe UI"
pc2.font.size = Pt(13)
pc2.font.bold = True
pc2.font.color.rgb = AMBER_GOLD
pc2.space_after = Pt(6)

c2_desc = [
    ("Mâu thuẫn trong file SRS gốc", "SRS yêu cầu slug phải là UNIQUE, nhưng đồng thời yêu cầu áp dụng Soft Delete (is_deleted = True). Khi xóa bài cũ, bản ghi vẫn còn trong DB nên không thể tạo bài mới trùng slug."),
    ("Giải pháp của em", "Em giải quyết bằng 2 kỹ thuật phối hợp:\n1. Tự động sinh slug độc nhất bằng hàm get_unique_slug() nối thêm hậu tố ngẫu nhiên khi bị trùng.\n2. Cấu hình Partial Unique Index trong CSDL: CREATE UNIQUE INDEX uq_slug ON recipes (slug) WHERE is_deleted = false."),
    ("Hiệu quả đạt được", "Bảo toàn 100% dữ liệu lịch sử bài viết mà không bao giờ bị lỗi vi phạm ràng buộc toàn vẹn.")
]

for title, desc in c2_desc:
    p = tf_c2.add_paragraph()
    p.text = "★ " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_c2.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(5)

add_speaker_note(slide6,
    "KỊCH BẢN NÓI (50 giây):\n"
    "Một trong những phần em đầu tư nhiều kỹ thuật chuyên sâu nhất là Kiểm soát Concurrency và Xử lý mâu thuẫn SRS:\n"
    "Để giải quyết bài toán Lost Update khi 2 tác giả cùng chỉnh sửa một công thức, em áp dụng Optimistic Concurrency Control qua cột row_version. "
    "Nếu phát hiện phiên bản dữ liệu gửi lên bị cũ, API lập tức từ chối và trả về HTTP 409 Conflict, yêu cầu tải lại dữ liệu mới nhất.\n"
    "Ngoài ra, em đã chỉ ra và xử lý mâu thuẫn trong SRS giữa việc Soft Delete và Ràng buộc duy nhất trên Slug bằng cách sử dụng "
    "Partial Unique Index trong PostgreSQL, đảm bảo bài viết bị xóa mềm không làm nghẽn việc tạo bài mới."
)

# ==============================================================================
# SLIDE 7: RESOURCE-BASED AUTHORIZATION & DTO PATTERN (40s)
# ==============================================================================
slide7 = prs.slides.add_slide(blank_layout)
add_header(slide7, "Resource-Based Authorization & DTO Pattern")

add_card(slide7, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_auth_r = slide7.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_ar = tb_auth_r.text_frame
tf_ar.word_wrap = True

par1 = tf_ar.paragraphs[0]
par1.text = "1. RESOURCE-BASED AUTHORIZATION"
par1.font.name = "Segoe UI"
par1.font.size = Pt(13)
par1.font.bold = True
par1.font.color.rgb = PRIMARY_BLUE
par1.space_after = Pt(8)

res_items = [
    ("Định nghĩa", "Phân quyền không chỉ dựa vào Role (Admin/Author), mà căn cứ vào quyền sở hữu trên chính thực thể dữ liệu cụ thể."),
    ("Hàm kiểm tra trong mã nguồn", "def _check_recipe_ownership(recipe: Recipe, user: User):\n  if user.role != 'Admin' and str(recipe.author_id) != str(user.id):\n    raise ForbiddenException(detail='Bạn không có quyền chỉnh sửa công thức này.')"),
    ("Áp dụng", "Toàn bộ API Sửa, Xóa, Đổi ảnh, Quản lý bước nấu đều bắt buộc qua hàm này để bảo vệ dữ liệu tác giả.")
]

for title, desc in res_items:
    p = tf_ar.add_paragraph()
    p.text = "• " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_ar.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

add_card(slide7, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_dto = slide7.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_dto = tb_dto.text_frame
tf_dto.word_wrap = True

pdto1 = tf_dto.paragraphs[0]
pdto1.text = "2. THIẾT KẾ DTO & INPUT VALIDATION"
pdto1.font.name = "Segoe UI"
pdto1.font.size = Pt(13)
pdto1.font.bold = True
pdto1.font.color.rgb = GREEN_SUCCESS
pdto1.space_after = Pt(8)

dto_items = [
    ("Tách rời Entity khỏi API Contract", "Sử dụng Pydantic v2 schemas: RecipeSummaryDto, RecipeDetailDto, RecipeCreateDto."),
    ("Ẩn giấu thông tin nhạy cảm", "User entity chứa password_hash, access_failed_count; UserProfileDto chỉ chọn lọc trả về id, fullName, email, avatarUrl, bio."),
    ("Chống tấn công Mass Assignment", "DTO kiểm soát chặt chẽ các trường được phép nhập, ngăn chặn người dùng tự gửi role='Admin' trong payload."),
    ("Ngăn chặn Circular Reference", "Tránh lỗi vòng lặp tuần hoàn vô hạn giữa Recipe và User khi serialize JSON.")
]

for title, desc in dto_items:
    p = tf_dto.add_paragraph()
    p.text = "• " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_dto.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

add_speaker_note(slide7,
    "KỊCH BẢN NÓI (40 giây):\n"
    "Về kiểm soát truy cập và chuẩn hóa dữ liệu:\n"
    "Em cài đặt hàm _check_recipe_ownership thực hiện Resource-based authorization: Người dùng dù đã đăng nhập nhưng nếu không phải tác giả sở hữu "
    "công thức đó và không phải Admin thì tuyệt đối không thể can thiệp, trả về lỗi 403 Forbidden.\n"
    "Song song đó, em thiết kế toàn bộ hệ thống DTO qua Pydantic v2 để bảo vệ dữ liệu nhạy cảm như mật khẩu hash, ngăn chặn triệt để tấn công Mass Assignment "
    "và loại bỏ lỗi vòng lặp tuần hoàn khi tuần tự hóa JSON."
)

# ==============================================================================
# SLIDE 8: HEALTH CHECK PROBES CHUẨN CLOUD-NATIVE (45s)
# ==============================================================================
slide8 = prs.slides.add_slide(blank_layout)
add_header(slide8, "Hệ Thống Giám Sát Cloud-Native: Health Check Probes")

# Left Column: Probes Logic
add_card(slide8, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
tb_h1 = slide8.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.7))
tf_h1 = tb_h1.text_frame
tf_h1.word_wrap = True

ph1 = tf_h1.paragraphs[0]
ph1.text = "TÁCH BẠCH LIVENESS & READINESS (FR-OBS-001)"
ph1.font.name = "Segoe UI"
ph1.font.size = Pt(13)
ph1.font.bold = True
ph1.font.color.rgb = PRIMARY_BLUE
ph1.space_after = Pt(6)

health_points = [
    ("Liveness Probe (/health/live)", "Chỉ kiểm tra tiến trình Python FastAPI có còn sống hay không. Không kiểm tra DB. Trả về 200 OK. Nếu endpoint này chết, Docker/Kubernetes mới restart container."),
    ("Readiness Probe (/health/ready)", "Kiểm tra xem ứng dụng đã sẵn sàng nhận traffic chưa: Thực hiện SELECT 1 kiểm tra PostgreSQL và ping Redis. Nếu DB/Redis lỗi, trả về 503 Service Unavailable để load balancer tạm ngưng gửi traffic."),
    ("Aggregated Health Check (/health)", "Kiểm tra toàn diện cả PostgreSQL, Redis và MinIO Storage, phân loại trạng thái Healthy / Degraded / Unhealthy."),
    ("Ý nghĩa thực tế", "Tránh hiện tượng CrashLoopBackOff và 'bão kết nối' (Thundering Herd) khi Database bị quá tải tạm thời.")
]

for title, desc in health_points:
    p = tf_h1.add_paragraph()
    p.text = "► " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_h1.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(5)

# Right: Screenshot Health Check
img_path_h = os.path.join(SCREENSHOTS_DIR, "demo_15_health_probe.png")
if os.path.exists(img_path_h):
    slide8.shapes.add_picture(img_path_h, Inches(6.8), Inches(1.8), width=Inches(5.7))
else:
    add_card(slide8, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.1))

add_speaker_note(slide8,
    "KỊCH BẢN NÓI (45 giây):\n"
    "Đối với yêu cầu giám sát hệ thống (FR-OBS-001), em đã thiết kế riêng biệt 3 endpoints chuẩn Cloud-Native:\n"
    "Endpoint /health/live đóng vai trò Liveness probe, chỉ kiểm tra process Python để bộ điều phối biết có cần restart hay không.\n"
    "Endpoint /health/ready đóng vai trò Readiness probe, kiểm tra trực tiếp kết nối tới PostgreSQL và Redis. "
    "Nếu database bị nghẽn, endpoint này trả về 503 để Nginx tạm ngưng chuyển request tới, nhưng KHÔNG restart container. "
    "Điều này giúp hệ thống tránh được lỗi dây chuyền CrashLoopBackOff rất thường gặp trong môi trường microservices."
)

# ==============================================================================
# SLIDE 9: MINH CHỨNG TRIỂN KHAI & TÀI LIỆU SWAGGER (40s)
# ==============================================================================
slide9 = prs.slides.add_slide(blank_layout)
add_header(slide9, "Minh Chứng Triển Khai & Kiểm Thử Tự Động")

# Left Column: Points
add_card(slide9, Inches(0.8), Inches(1.8), Inches(5.2), Inches(5.1))
tb_sw = slide9.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(4.8), Inches(4.7))
tf_sw = tb_sw.text_frame
tf_sw.word_wrap = True

psw = tf_sw.paragraphs[0]
psw.text = "TÀI LIỆU HÓA & KIỂM THỬ TỰ ĐỘNG"
psw.font.name = "Segoe UI"
psw.font.size = Pt(13)
psw.font.bold = True
psw.font.color.rgb = PRIMARY_BLUE
psw.space_after = Pt(8)

test_points = [
    ("Tài liệu OpenAPI / Swagger UI", "Toàn bộ 19 endpoints em phụ trách đều được document chi tiết tại /docs và /redoc với đầy đủ schema request/response."),
    ("CORS & Rate Limiting Middleware", "Tích hợp sẵn middleware giới hạn số lượt request chống spam và bảo vệ CORS theo NFR-SEC-005."),
    ("Bộ kiểm thử tự động Pytest", "Viết các bài test trong tests/test_auth_unit.py và test_health.py đảm bảo logic xác thực và health check luôn chạy đúng."),
    ("Tự động Seeding CSDL", "Script seed.py nạp đầy đủ tài khoản Admin, Author và 41 công thức mẫu khi khởi chạy lần đầu.")
]

for title, desc in test_points:
    p = tf_sw.add_paragraph()
    p.text = "✔ " + title
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_after = Pt(1)
    
    pd = tf_sw.add_paragraph()
    pd.text = desc
    pd.font.name = "Segoe UI"
    pd.font.size = Pt(10)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

# Right: Screenshot Swagger
img_path_s = os.path.join(SCREENSHOTS_DIR, "demo_14_swagger_docs.png")
if os.path.exists(img_path_s):
    slide9.shapes.add_picture(img_path_s, Inches(6.3), Inches(1.8), width=Inches(6.2))
else:
    add_card(slide9, Inches(6.3), Inches(1.8), Inches(6.2), Inches(5.1))

add_speaker_note(slide9,
    "KỊCH BẢN NÓI (40 giây):\n"
    "Để chứng minh kết quả cài đặt: Toàn bộ các API em xây dựng đều được tích hợp tài liệu hóa Swagger UI tự động tại /docs.\n"
    "Em đã thiết lập bộ test tự động Pytest kiểm tra tính toàn vẹn của logic băm mật khẩu, token expiration và các probes.\n"
    "Dữ liệu mẫu 41 món ăn cùng tài khoản thử nghiệm cũng được em viết sẵn trong kịch bản seed.py, giúp hệ thống sẵn sàng hoạt động ngay sau khi khởi chạy."
)

# ==============================================================================
# SLIDE 10: TỔNG KẾT & SẴN SÀNG TRẢ LỜI PHẢN BIỆN (20s)
# ==============================================================================
slide10 = prs.slides.add_slide(blank_layout)
bg10 = slide10.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
bg10.fill.solid()
bg10.fill.fore_color.rgb = DARK_NAVY
bg10.line.fill.background()

tb10 = slide10.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.3), Inches(3.5))
tf10 = tb10.text_frame
tf10.word_wrap = True

pt1 = tf10.paragraphs[0]
pt1.alignment = PP_ALIGN.CENTER
pt1.text = "EM ĐÃ HOÀN THÀNH TOÀN BỘ 19/19 CHỨC NĂNG ĐƯỢC PHÂN CÔNG"
pt1.font.name = "Segoe UI"
pt1.font.size = Pt(28)
pt1.font.bold = True
pt1.font.color.rgb = WHITE
pt1.space_after = Pt(14)

pt2 = tf10.add_paragraph()
pt2.alignment = PP_ALIGN.CENTER
pt2.text = "NGUYỄN HOÀI NAM SẴN SÀNG GIẢI THÍCH MÃ NGUỒN VÀ TRẢ LỜI CÂU HỎI CỦA CÔ!"
pt2.font.name = "Segoe UI"
pt2.font.size = Pt(16)
pt2.font.bold = True
pt2.font.color.rgb = AMBER_GOLD
pt2.space_after = Pt(20)

pt3 = tf10.add_paragraph()
pt3.alignment = PP_ALIGN.CENTER
pt3.text = "Cảm ơn Cô đã chú ý lắng nghe phần báo cáo cá nhân của em."
pt3.font.name = "Segoe UI"
pt3.font.size = Pt(14)
pt3.font.italic = True
pt3.font.color.rgb = RGBColor(148, 163, 184)

add_speaker_note(slide10,
    "KỊCH BẢN NÓI (20 giây):\n"
    "Tóm lại, em đã hoàn thành 100% tất cả 19 đầu việc được giao từ DevOps, Auth, Recipe Core đến Health Checks, đảm bảo đúng chuẩn SRS và tối ưu hiệu năng. "
    "Em xin chân thành cảm ơn Cô. Bây giờ em đã sẵn sàng giải thích chi tiết bất kỳ đoạn code nào hoặc trả lời các câu hỏi phản biện từ Cô!"
)

prs.save(OUTPUT_PPTX)
print("Saved PPTX successfully:", OUTPUT_PPTX)
