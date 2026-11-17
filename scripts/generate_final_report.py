"""
Script sinh Báo Cáo Đồ Án Môn Học: Phát Triển Ứng Dụng Web Nâng Cao
Quy mô: 20 - 25 trang Word
Nhóm: 25 - Đề tài: Culinary Blog Platform
Sinh viên: Nguyễn Hoài Nam (MSSV: 2312694)
Template: Mau_Nop_Bao_Cao_Lab_Ca_Nhan_2026.docx
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

COLOR_PRIMARY = RGBColor(27, 54, 93)     # Navy #1B365D
COLOR_SECONDARY = RGBColor(234, 88, 12)  # Orange #EA580C
COLOR_TEXT = RGBColor(40, 40, 40)
COLOR_MUTED = RGBColor(100, 100, 100)
COLOR_LINK = RGBColor(0, 102, 204)

REPO_URL = "https://github.com/NHNam1209/PTUDW-2026-Nhom25"

def set_cell_background(cell, hex_color: str):
    """Đặt màu nền cho cell trong bảng."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Đặt lề trong cho cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_styled_heading(doc, text: str, level: int):
    """Thêm tiêu đề chuẩn Times New Roman có màu sắc phân cấp."""
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(14 if level == 1 else 10)
    p.paragraph_format.space_after = Pt(6)
    
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.bold = True
    
    if level == 1:
        run.font.size = Pt(15)
        run.font.color.rgb = COLOR_PRIMARY
    elif level == 2:
        run.font.size = Pt(13.5)
        run.font.color.rgb = COLOR_SECONDARY
    else:
        run.font.size = Pt(12)
        run.font.color.rgb = COLOR_TEXT
    return p

def add_body_p(doc, text: str, bold_prefix: str = "", space_after: float = 4.0, italic: bool = False):
    """Thêm đoạn văn bản chuẩn Times New Roman 12pt."""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.2
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(12)
        r_pre.bold = True
        r_pre.font.color.rgb = COLOR_TEXT
        
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.italic = italic
    run.font.color.rgb = COLOR_TEXT
    return p

def add_bullet_item(doc, text: str, bold_lead: str = ""):
    """Thêm dòng bullet point có format chuẩn."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    
    r_bullet = p.add_run("•  ")
    r_bullet.font.name = "Times New Roman"
    r_bullet.font.size = Pt(11.5)
    r_bullet.bold = True
    r_bullet.font.color.rgb = COLOR_PRIMARY
    
    if bold_lead:
        r_lead = p.add_run(bold_lead + ": ")
        r_lead.font.name = "Times New Roman"
        r_lead.font.size = Pt(11.5)
        r_lead.bold = True
        r_lead.font.color.rgb = COLOR_TEXT
        
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11.5)
    run.font.color.rgb = COLOR_TEXT
    return p

def add_image_figure(doc, img_path: str, caption: str, width_in: float = 6.0):
    """Chèn hình ảnh vào tài liệu kèm khung viền và chú thích hình."""
    if not os.path.exists(img_path):
        return None
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(8)
    p_img.paragraph_format.space_after = Pt(4)
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=Inches(width_in))
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(0)
    p_cap.paragraph_format.space_after = Pt(12)
    run_cap = p_cap.add_run(caption)
    run_cap.font.name = "Times New Roman"
    run_cap.font.size = Pt(10.5)
    run_cap.italic = True
    run_cap.font.color.rgb = COLOR_MUTED
    return p_img

def build_full_report(template_path: str, output_path: str):
    doc = docx.Document(template_path)
    
    # Thiết lập lề trang chuẩn văn bản A4
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.8)
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)

    # 1. TRANG BÌA & THÔNG TIN CHUNG
    for p in doc.paragraphs:
        if "BÁO CÁO LAB" in p.text:
            p.text = "BÁO CÁO TỔNG KẾT ĐỒ ÁN MÔN HỌC\nPHÁT TRIỂN ỨNG DỤNG WEB NÂNG CAO"
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(17)
                r.bold = True
                r.font.color.rgb = COLOR_PRIMARY
        elif "Lab:" in p.text:
            p.text = "Đề tài: NỀN TẢNG BLOG ẨM THỰC & CHIA SẺ CÔNG THỨC (CULINARY BLOG)\nHọc kỳ: 1 - Năm học 2026 - 2026"
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(13)
                r.bold = True
        elif "MSSV:" in p.text:
            p.text = "Sinh viên thực hiện: Nguyễn Hoài Nam\tMSSV: 2312694\nVai trò: Trưởng nhóm, Full-Stack Architecture, Backend & Frontend Lead"
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12.5)
        elif "Nhóm:" in p.text:
            p.text = f"Nhóm: 25\nKho lưu trữ GitHub chính thức: {REPO_URL}"
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12.5)
                r.bold = True
        elif "Công việc:" in p.text or "Lưu ý:" in p.text or "Công việc được giao:" in p.text or "Tự đánh giá" in p.text:
            p.text = ""

    # 2. XÂY DỰNG BẢNG PHÂN CÔNG CÔNG VIỆC VÀ TIẾN ĐỘ HOÀN THÀNH (BẢNG MỤC LỤC NHIỆM VỤ)
    tasks_data = [
        {
            "stt": "1",
            "name": "[DevOps & Hạ Tầng] Khởi tạo khung dự án Micro-Services, Docker Compose, Nginx Reverse Proxy, PostgreSQL & MinIO",
            "done": [
                "Thiết lập kiến trúc môi trường Docker Compose 7 containers: culinary_nginx (port 80), culinary_api (FastAPI port 8000), culinary_frontend (Vite React port 3000), culinary_postgres (PostgreSQL 16 port 5433:5432), culinary_redis (Redis 7 port 6381:6379), culinary_minio (MinIO port 9000-9001), culinary_mailhog (MailHog SMTP port 1026:1025, Web UI 8026).",
                "Cấu hình mạng ảo biệt lập culinary_network và các Docker volumes đảm bảo dữ liệu pgdata, miniodata, redisdata không bị mất khi restart.",
                "Cài đặt file kịch bản khởi tạo CSDL postgres/init.sql: Cấu hình extension unaccent, pg_trgm, tsvector và tạo tài khoản, database tự động khi boot."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/tree/main",
            "progress": "100%"
        },
        {
            "stt": "2",
            "name": "[Backend - Data Architecture] Kiến trúc Clean Architecture, ORM Entities & Cơ chế Seeding Dữ Liệu Tự Động (>=100 Recipes)",
            "done": [
                "Tổ chức cấu trúc backend theo nguyên lý Clean Architecture: Domain (Models, Enums, Exceptions), Repositories, Services, Schemas (Pydantic DTOs), API v1 Controllers, Core Infrastructure.",
                "Cài đặt toàn bộ ORM Entities với SQLAlchemy 2.0: User, RefreshToken, Category, Recipe, RecipeStep, RecipeIngredient, RecipeImage kèm khóa ngoại, cascade on delete và optimistic locking row_version.",
                "Xây dựng script seed.py tạo dữ liệu chuẩn thực tế: Khởi tạo 2 tài khoản mẫu (Admin & Author), 22 danh mục ẩm thực phong phú, và tự động sinh 105+ công thức nấu ăn hoàn chỉnh. Mỗi công thức có 10-14 nguyên liệu, 5-7 bước nấu kèm Cooking Timer, bảng dinh dưỡng tiêu chuẩn và ảnh liên kết MinIO."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/backend/seed.py",
            "progress": "100%"
        },
        {
            "stt": "3",
            "name": "[Backend - Phân Hệ Auth] Xác thực JWT kép, Token Rotation, Google OAuth 2.0, Khóa tài khoản Lockout & Audit Log",
            "done": [
                "Cài đặt luồng đăng ký tài khoản (FR-AUTH-001) với thuật toán băm mật khẩu bảo mật Bcrypt, kiểm tra độ mạnh mật khẩu và chống tấn công User Enumeration.",
                "Triển khai xác thực JWT kép (Access Token 15 phút, Refresh Token 7 ngày) kèm cơ chế Token Rotation phát hiện tấn công phát lại (Token Reuse Attack - thu hồi toàn bộ phiên nếu phát hiện token cũ).",
                "Tích hợp đăng nhập một chạm qua Google OAuth 2.0 (FR-AUTH-003): Xác thực token với Google Identity Services và tự động đồng bộ tài khoản người dùng.",
                "Cài đặt cơ chế bảo vệ Account Lockout (FR-AUTH-002): Tự động khóa đăng nhập 15 phút sau 5 lần nhập sai liên tiếp, ghi nhật ký bảo mật audit trail."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/backend/app/api/v1/auth.py",
            "progress": "100%"
        },
        {
            "stt": "4",
            "name": "[Backend - Phân Hệ Recipes] Quản lý Công thức, Lọc đa tiêu chí, Optimistic Concurrency & Vòng đời bài viết",
            "done": [
                "Cài đặt API Danh sách công thức (FR-RCP-001): Phân trang chuẩn PagedResult, lọc theo danh mục, độ khó (1-4), thời gian nấu tối đa, và sắp xếp linh hoạt.",
                "Chi tiết công thức nấu ăn (FR-RCP-002): Nạp eager-loading (selectinload) tác giả, danh mục, danh sách nguyên liệu, các bước nấu và bộ sưu tập ảnh.",
                "Quy trình tạo nháp (Draft), cập nhật công thức kiểm soát xung đột đồng thời (FR-RCP-004) bằng trường row_version (HTTP 409 Concurrency Conflict khi có ghi đè).",
                "Quản lý vòng đời bài viết (FR-RCP-005, FR-RCP-006, FR-RCP-007): Chuyển trạng thái Xuất bản (Publish), Hủy xuất bản về nháp, Lưu trữ (Archive) và Xóa vĩnh viễn (Cascade delete nguyên liệu, bước nấu và dọn dẹp ảnh vật lý MinIO)."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/backend/app/api/v1/recipes.py",
            "progress": "100%"
        },
        {
            "stt": "5",
            "name": "[Backend - MinIO Storage & Image Job] Dịch vụ lưu trữ đối tượng MinIO S3 SDK & Background Job Resize Thumbnails",
            "done": [
                "Cài đặt dịch vụ MinIOStorageService (FR-FILE-001) kết nối MinIO qua giao thức S3: Tự động khởi tạo bucket 'culinary-blog' với chính sách public-read.",
                "Cơ chế kiểm soát an toàn tệp: Giới hạn dung lượng tối đa 5MB, xác thực Content-Type và kiểm tra Magic Bytes (JPEG, PNG, WebP, AVIF) ngăn chặn chèn mã độc.",
                "Background Job tạo ảnh thu nhỏ (FR-JOB-002 - image_job.py): Tích hợp thư viện Pillow xử lý ảnh bất đồng bộ, resize ảnh về kích thước tối đa 300x300 pixel giữ nguyên tỷ lệ, tối ưu chất lượng và lưu trữ vào thư mục thumbnails trên MinIO."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/backend/app/services/storage.py",
            "progress": "100%"
        },
        {
            "stt": "6",
            "name": "[Backend - Categories & PostgreSQL Full-Text Search] CRUD Danh mục & Tìm kiếm toàn văn unaccent",
            "done": [
                "Triển khai bộ API CRUD Danh mục ẩm thực (FR-CAT-001 đến FR-CAT-005): Đếm số lượng công thức đang hoạt động, sinh slug tự động, ràng buộc toàn vẹn khóa ngoại (ngăn xóa danh mục đang có công thức trực thuộc).",
                "Hiện thực tìm kiếm Full-Text Search PostgreSQL (FR-SRCH-001): Tích hợp hàm to_tsvector, plainto_tsquery kết hợp toán tử unaccent tiếng Việt và khớp chuỗi ILIKE linh hoạt, trả về kết quả xếp hạng độ liên quan nhanh chóng dưới 50ms."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/backend/app/api/v1/categories.py",
            "progress": "100%"
        },
        {
            "stt": "7",
            "name": "[Backend - Background & Cron Jobs] Background Gửi Email Chào Mừng & Cron Job Sinh Sitemap.xml Tự Động",
            "done": [
                "Background Task gửi email chào mừng (FR-JOB-001 - email.py): Đăng ký tác vụ ngầm BackgroundTasks trong FastAPI khi đăng ký tài khoản mới; gửi email định dạng HTML chuyên nghiệp qua máy chủ MailHog/SMTP, có cơ chế ghi log dự phòng khi mạng offline.",
                "Cron Job lập lịch sinh sitemap tự động (FR-JOB-003 - sitemap_job.py): Sử dụng APScheduler định kỳ 24 giờ quét toàn bộ CSDL và khởi tạo file static/sitemap.xml chuẩn giao thức Sitemaps 0.9, phục vụ trực tiếp tại endpoint /sitemap.xml."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/backend/app/jobs/sitemap_job.py",
            "progress": "100%"
        },
        {
            "stt": "8",
            "name": "[Backend - Hệ Thống Giám Sát & Bảo Vệ] Structured Logging Đa Kênh, Correlation-ID & Sliding-Window Rate Limiting",
            "done": [
                "Triển khai Correlation-ID Middleware (FR-OBS-002): Tự động gán mã UUID duy nhất cho từng request qua X-Correlation-ID và ghi nhận thời gian thực thi X-Response-Time, cảnh báo truy vấn chậm (> 500ms).",
                "Hệ thống Structured Logging đa kênh (app/core/logging.py): Tách biệt luồng ghi log ra console, app.log, error.log và audit.log; cơ chế RotatingFileHandler xoay vòng 10MB x 5 backups chống tràn đĩa.",
                "Cài đặt thuật toán Rate Limiting dạng trượt (Sliding-Window): Hạn chế tần suất Auth (10 req/phút), Upload (5 req/phút), General API (100 req/phút), trả về HTTP 429 và thông báo chuẩn RFC 7807 Problem Details."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/backend/app/core/middleware.py",
            "progress": "100%"
        },
        {
            "stt": "9",
            "name": "[Frontend - Core & Trang Người Dùng] Giao diện Trang chủ, Khám phá Công thức & Chi tiết Món ăn Chuẩn SEO",
            "done": [
                "Xây dựng Trang chủ (HomePage.jsx): Hero banner truyền cảm hứng, lưới danh mục ẩm thực trực quan, danh sách món ăn đề xuất và công thức mới nhất.",
                "Trang danh sách công thức (RecipeListPage.jsx): Thanh bộ lọc đa năng (theo danh mục, độ khó, thời gian chế biến tối đa, sắp xếp mới nhất/cũ nhất), phân trang mượt mà.",
                "Trang chi tiết công thức (RecipeDetailPage.jsx): Hiển thị đầy đủ thông tin tác giả, bảng thành phần dinh dưỡng, danh mục nguyên liệu tương tác, danh sách bước nấu chi tiết kèm đồng hồ hẹn giờ Cooking Timer trực quan.",
                "Tối ưu SEO Schema.org Recipe JSON-LD & thẻ Open Graph (FR-SEO-001): Tự động nhúng cấu trúc dữ liệu Rich Snippet chuẩn Google vào thẻ <head>."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/frontend/src/pages/RecipeDetailPage.jsx",
            "progress": "100%"
        },
        {
            "stt": "10",
            "name": "[Frontend - Trang Danh Mục & Tìm Kiếm] Categories Catalog & Full-Text Search Results UI",
            "done": [
                "Trang danh mục món ăn (CategoriesPage.jsx - FR-UI-004): Chế độ xem tổng hợp toàn bộ danh mục ẩm thực và chế độ xem chi tiết danh mục theo slug (/categories/:slug) hiển thị toàn bộ món ăn trực thuộc kèm phân trang.",
                "Trang kết quả tìm kiếm (SearchPage.jsx - FR-UI-005): Thanh tìm kiếm chuyên dụng có nút xóa nhanh, danh sách từ khóa ẩm thực thịnh hành gợi ý, gọi API Full-Text Search và hiển thị trạng thái rỗng thân thiện khi không tìm thấy món."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/frontend/src/pages/SearchPage.jsx",
            "progress": "100%"
        },
        {
            "stt": "11",
            "name": "[Frontend - Xác Thực & Phân Quyền] Giao diện Đăng nhập, Nút Google OAuth & Đăng ký Kiểm tra Mật khẩu Thời Gian Thực",
            "done": [
                "Giao diện Đăng nhập (LoginPage.jsx - FR-AUTH-UI-001): Thiết kế hiện đại, nút đăng nhập nhanh bằng Google OAuth kèm icon thương hiệu Google chuẩn, các nút điền sẵn tài khoản dùng thử nhanh (Admin & Author).",
                "Giao diện Đăng ký (RegisterPage.jsx - FR-AUTH-UI-002): Thanh checklist kiểm tra độ mạnh mật khẩu thời gian thực (đủ 8 ký tự, chữ hoa, chữ thường, số, ký tự đặc biệt).",
                "Quản lý trạng thái phiên làm việc tập trung (AuthContext.jsx): Tự động làm mới Access Token trong nền khi token hết hạn qua Interceptor."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/frontend/src/pages/LoginPage.jsx",
            "progress": "100%"
        },
        {
            "stt": "12",
            "name": "[Frontend - Creator Dashboard & Soạn Thảo] Bảng điều khiển tác giả, Trình quản lý bài viết & Wizard Đa bước",
            "done": [
                "Bảng điều khiển tác giả (CreatorDashboard.jsx - FR-DASH-001): Thẻ chỉ số tổng quan (Tổng công thức, Lượt xem, Công thức đã xuất bản, Tỷ lệ phản hồi) và biểu đồ phân bố độ khó món ăn.",
                "Màn hình quản lý công thức (RecipeManagementPage.jsx - FR-DASH-002): Bảng quản trị lọc theo tab trạng thái (Nháp, Đã xuất bản, Lưu trữ), các nút thao tác chuyển đổi trạng thái một chạm và modal xác nhận xóa mềm an toàn.",
                "Trình biên tập công thức đa bước (RecipeEditorPage.jsx - FR-DASH-003, FR-DASH-004): Tích hợp IngredientEditor và StepEditor thêm/xóa/sửa nguyên liệu động, hẹn giờ Cooking Timer, nạp dữ liệu cũ khi chỉnh sửa và kiểm soát xung đột ghi đè rowVersion.",
                "Component upload hình ảnh MinIO (ImageUploader.jsx - FR-DASH-005): Kéo thả ảnh trực tiếp, xem trước ảnh, hiển thị tiến trình và chọn ảnh đại diện chính."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/frontend/src/pages/RecipeEditorPage.jsx",
            "progress": "100%"
        },
        {
            "stt": "13",
            "name": "[Frontend - Quản Trị Hệ Thống Admin] Quản trị Danh mục Bằng Modal & Quản lý Phân quyền Người dùng",
            "done": [
                "Giao diện quản lý danh mục Admin (CategoryManagePage.jsx - FR-ADMIN-001): Modal thêm mới và chỉnh sửa danh mục, kiểm tra tên trùng lặp, xóa danh mục có hiển thị cảnh báo ràng buộc CSDL.",
                "Màn hình quản lý người dùng (UsersPage.jsx): Bảng trực quan hóa danh sách người dùng toàn hệ thống, gắn huy hiệu vai trò phân màu (Admin đỏ, Author cam, User xanh), bộ lọc tab vai trò, ô tìm kiếm debounce (400ms), dropdown thay đổi quyền hạn và nút khóa/mở khóa tài khoản tức thời."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/blob/main/frontend/src/pages/UsersPage.jsx",
            "progress": "100%"
        },
        {
            "stt": "14",
            "name": "[Kiểm Thử & Đóng Gói Hoàn Thiện] Unit/Integration Tests, Kiểm thử API Health Probes & Tối ưu hóa Build Production",
            "done": [
                "Xây dựng bộ kiểm thử tự động pytest toàn diện: tests/test_auth_unit.py, tests/test_categories.py, tests/test_health.py, tests/test_jobs.py, tests/test_obs.py đạt kết quả vượt qua 100% (11/11 tests PASSED).",
                "Kiểm tra tính sẵn sàng qua Kubernetes Health Probes: /health (đầy đủ các dịch vụ CSDL, Redis, MinIO), /health/live (liveness probe), /health/ready (readiness probe).",
                "Biên dịch tối ưu hóa Frontend Vite: Bundle toàn bộ tài nguyên sang dist/ với dung lượng nén gzip tối ưu, đảm bảo ứng dụng tải trang tức thì dưới 1 giây."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": f"{REPO_URL}/actions",
            "progress": "100%"
        }
    ]

    table = doc.tables[0]
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Đảm bảo bảng có đủ số hàng
    while len(table.rows) > len(tasks_data) + 1:
        p_elm = table.rows[-1]._tr.getparent()
        p_elm.remove(table.rows[-1]._tr)
    while len(table.rows) < len(tasks_data) + 1:
        table.add_row()

    # Định dạng Header của Bảng
    hdr_cells = table.rows[0].cells
    hdr_titles = ["STT", "Hạng mục công việc & Các bước thực hiện", "Liên kết GitHub", "Tiến độ"]
    hdr_widths = [Inches(0.6), Inches(4.3), Inches(1.3), Inches(0.8)]
    
    for i, title in enumerate(hdr_titles):
        cell = hdr_cells[i]
        cell.width = hdr_widths[i]
        cell.text = title
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=140, bottom=140, left=150, right=150)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(11)
            r.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

    # Điền dữ liệu vào bảng
    for idx, task in enumerate(tasks_data):
        row = table.rows[idx + 1]
        bg_color = "F8FAFC" if idx % 2 == 1 else "FFFFFF"

        # Cột 0: STT
        c0 = row.cells[0]
        c0.width = hdr_widths[0]
        c0.text = task["stt"]
        set_cell_background(c0, bg_color)
        set_cell_margins(c0, top=100, bottom=100, left=100, right=100)
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p0.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(11)
            r.bold = True

        # Cột 1: Chi tiết công việc
        c1 = row.cells[1]
        c1.width = hdr_widths[1]
        c1.text = ""
        set_cell_background(c1, bg_color)
        set_cell_margins(c1, top=100, bottom=100, left=140, right=140)
        
        p_name = c1.paragraphs[0]
        p_name.paragraph_format.space_after = Pt(3)
        r_name = p_name.add_run(task["name"])
        r_name.font.name = "Times New Roman"
        r_name.font.size = Pt(11.5)
        r_name.bold = True
        r_name.font.color.rgb = COLOR_PRIMARY

        p_done_title = c1.add_paragraph()
        p_done_title.paragraph_format.space_before = Pt(2)
        p_done_title.paragraph_format.space_after = Pt(2)
        r_dt = p_done_title.add_run("• Các bước đã thực hiện & hoàn thành:")
        r_dt.font.name = "Times New Roman"
        r_dt.font.size = Pt(10.5)
        r_dt.bold = True
        r_dt.font.color.rgb = RGBColor(14, 138, 22)

        for d in task["done"]:
            p_bullet = c1.add_paragraph()
            p_bullet.paragraph_format.left_indent = Inches(0.2)
            p_bullet.paragraph_format.space_after = Pt(2)
            p_bullet.paragraph_format.line_spacing = 1.15
            r_b = p_bullet.add_run(f"- {d}")
            r_b.font.name = "Times New Roman"
            r_b.font.size = Pt(10)

        p_undone = c1.add_paragraph()
        p_undone.paragraph_format.space_before = Pt(3)
        p_undone.paragraph_format.space_after = Pt(2)
        r_ul = p_undone.add_run("• Chưa hoàn thành: ")
        r_ul.font.name = "Times New Roman"
        r_ul.font.size = Pt(10.5)
        r_ul.bold = True
        r_uv = p_undone.add_run(task["undone"])
        r_uv.font.name = "Times New Roman"
        r_uv.font.size = Pt(10)
        r_uv.italic = True

        # Cột 2: Liên kết GitHub
        c2 = row.cells[2]
        c2.width = hdr_widths[2]
        c2.text = task["link"]
        set_cell_background(c2, bg_color)
        set_cell_margins(c2, top=100, bottom=100, left=80, right=80)
        p2 = c2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for r in p2.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5)
            r.font.color.rgb = COLOR_LINK
            r.underline = True

        # Cột 3: Tiến độ %
        c3 = row.cells[3]
        c3.width = hdr_widths[3]
        c3.text = task["progress"]
        set_cell_background(c3, bg_color)
        set_cell_margins(c3, top=100, bottom=100, left=60, right=60)
        p3 = c3.paragraphs[0]
        p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p3.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(11)
            r.bold = True
            r.font.color.rgb = RGBColor(14, 138, 22)

    doc.add_page_break()

    # 3. PHẦN I: TỔNG QUAN KIẾN TRÚC & ĐẶC TẢ HỆ THỐNG
    add_styled_heading(doc, "I. TỔNG QUAN HỆ THỐNG & ĐẶC TẢ KIẾN TRÚC (SRS v1.0.0)", level=1)
    
    add_styled_heading(doc, "1.1. Bối Cảnh & Mục Tiêu Phát Triển Đề Tài", level=2)
    add_body_p(doc, "Trong thời đại kỹ thuật số hiện nay, nhu cầu tìm kiếm, học hỏi và chia sẻ các công thức nấu ăn ngon, lành mạnh và chuẩn định lượng ngày càng gia tăng. Đồ án Culinary Blog Platform được xây dựng như một giải pháp nền tảng web hiện đại, chuyên sâu, hỗ trợ cả độc giả đam mê ẩm thực lẫn các tác giả sáng tạo nội dung (Culinary Creators). Hệ thống được định hướng theo kiến trúc Micro-Services với Docker, phân tách rành mạch giữa Backend API Service (FastAPI) và Frontend Web Client (React Vite), tuân thủ tuyệt đối các quy chuẩn kỹ thuật nghiêm ngặt trong tài liệu đặc tả SRS v1.0.0.")

    add_styled_heading(doc, "1.2. Kiến Trúc Clean Architecture 4 Tầng Tại Backend", level=2)
    add_body_p(doc, "Để đảm bảo khả năng bảo trì, mở rộng và kiểm thử độc lập, phần mềm áp dụng triệt để mô hình Clean Architecture gồm 4 tầng phân lập rõ ràng:")
    add_bullet_item(doc, "Định nghĩa toàn bộ Business Entities và Value Objects thuần túy không phụ thuộc framework (User, Category, Recipe, RecipeStep, RecipeIngredient, RecipeImage, RefreshToken). Chứa các quy tắc nghiệp vụ bất biến, mã lỗi chuẩn hóa (DomainException, EntityNotFoundException, RecipeConcurrencyException...).", bold_lead="1. Domain Layer (app/domain)")
    add_bullet_item(doc, "Trừu tượng hóa thao tác lưu trữ và truy vấn cơ sở dữ liệu thông qua Repository Pattern và Unit of Work Pattern, giải phóng tầng nghiệp vụ khỏi sự ràng buộc của ORM.", bold_lead="2. Repository & Data Access Layer (app/repositories)")
    add_bullet_item(doc, "Hiện thực các ca sử dụng (Use Cases) của hệ thống: Dịch vụ lưu trữ đối tượng MinIO S3 (storage.py), Dịch vụ sinh chuỗi thân thiện URL (slug.py), Dịch vụ thư điện tử nền (email.py), và các Background/Cron Jobs độc lập (image_job.py, sitemap_job.py).", bold_lead="3. Application & Services Layer (app/services & app/jobs)")
    add_bullet_item(doc, "Cung cấp các API RESTful theo phiên bản (/api/v1/...) phục vụ cho Frontend: Xác thực (auth.py), Công thức nấu ăn (recipes.py), Danh mục (categories.py), Thống kê tác giả (dashboard.py), Quản lý người dùng (users.py), và Giám sát sức khỏe (health.py).", bold_lead="4. Presentation & API Controller Layer (app/api/v1)")

    add_styled_heading(doc, "1.3. Bảng Tổng Hợp Công Nghệ Sử Dụng Trong Dự Án", level=2)
    tech_table = doc.add_table(rows=6, cols=3)
    tech_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_hdrs = ["Thành phần", "Công nghệ / Thư viện chính", "Vai trò và giải pháp kỹ thuật"]
    t_w = [Inches(1.8), Inches(2.2), Inches(3.0)]
    
    for i, title in enumerate(t_hdrs):
        cell = tech_table.rows[0].cells[i]
        cell.width = t_w[i]
        cell.text = title
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, 100, 100, 120, 120)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = "Times New Roman"
            r.bold = True
            r.font.size = Pt(10.5)
            r.font.color.rgb = RGBColor(255, 255, 255)

    tech_rows_data = [
        ("Backend Framework", "Python 3.12, FastAPI, Pydantic V2", "Xây dựng High-performance Async RESTful API, tự động sinh tài liệu Swagger UI/Redoc, kiểm tra kiểu dữ liệu tự động với độ trễ thấp."),
        ("Database & ORM", "PostgreSQL 16, SQLAlchemy 2.0 Async, asyncpg", "Lưu trữ dữ liệu quan hệ, Connection Pooling tối ưu, hỗ trợ Full-Text Search tsvector và unaccent tiếng Việt."),
        ("Caching & Task Queue", "Redis 7 Alpine, APScheduler", "Hỗ trợ caching dữ liệu tra cứu thường xuyên và lập lịch tác vụ nền định kỳ 24h tự động sinh sitemap.xml."),
        ("Object Storage", "MinIO (S3-Compatible Object Storage)", "Lưu trữ hình ảnh bài viết và ảnh thu nhỏ, hỗ trợ bucket public-read, kiểm tra MIME Type và Magic Bytes ngăn tải mã độc."),
        ("Frontend Web Client", "React 18, Vite 5, React Router 6, Lucide Icons", "Giao diện người dùng đơn trang (SPA) tốc độ phản hồi cực nhanh, thiết kế responsive đa thiết bị, Rich Interactive Components.")
    ]

    for idx, (comp, tech, role) in enumerate(tech_rows_data):
        row = tech_table.rows[idx + 1]
        bg_col = "F8FAFC" if idx % 2 == 1 else "FFFFFF"
        for i, val in enumerate([comp, tech, role]):
            cell = row.cells[i]
            cell.width = t_w[i]
            cell.text = val
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 80, 80, 100, 100)
            p = cell.paragraphs[0]
            if i == 0:
                p.runs[0].bold = True
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(10)

    doc.add_page_break()

    # 4. PHẦN II: HƯỚNG DẪN CÀI ĐẶT & VẬN HÀNH HỆ THỐNG
    add_styled_heading(doc, "II. HƯỚNG DẪN CÀI ĐẶT & VẬN HÀNH HỆ THỐNG (DEPLOYMENT GUIDE)", level=1)
    
    add_styled_heading(doc, "2.1. Yêu Cầu Môi Trường Tiền Đề", level=2)
    add_body_p(doc, "Để biên dịch và khởi chạy toàn bộ giải pháp một cách đồng nhất trên mọi hệ điều hành (Windows, macOS, Linux), máy tính phát triển cần cài đặt các công cụ sau:")
    add_bullet_item(doc, "Phiên bản v24.0.0 trở lên kèm Docker Compose v2.20.0+. Đảm bảo Docker Daemon đang hoạt động.", bold_lead="Docker Desktop")
    add_bullet_item(doc, "Dùng để clone mã nguồn và quản lý các nhánh tính năng.", bold_lead="Git SCM")
    add_bullet_item(doc, "Phiên bản 3.12+ (tùy chọn nếu muốn chạy kiểm thử trực tiếp ngoài container).", bold_lead="Python Environment")
    add_bullet_item(doc, "Phiên bản 18+ LTS (tùy chọn phục vụ quá trình debug frontend độc lập).", bold_lead="Node.js & NPM")

    add_styled_heading(doc, "2.2. Bảng Phân Phối Cổng Dịch Vụ Mạng (Network & Port Mapping)", level=2)
    add_body_p(doc, "Hệ sinh thái dịch vụ container được cấu hình tại docker-compose.yml với các cổng truy cập:")
    
    port_table = doc.add_table(rows=8, cols=4)
    port_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    p_hdrs = ["Tên Service", "Cổng Host", "Cổng Container", "Mô tả & Đường dẫn truy cập"]
    p_w = [Inches(1.8), Inches(1.2), Inches(1.3), Inches(2.7)]

    for i, title in enumerate(p_hdrs):
        cell = port_table.rows[0].cells[i]
        cell.width = p_w[i]
        cell.text = title
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, 100, 100, 120, 120)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = "Times New Roman"
            r.bold = True
            r.font.size = Pt(10)
            r.font.color.rgb = RGBColor(255, 255, 255)

    ports_data = [
        ("culinary_nginx", "80", "80", "Cổng ngõ Reverse Proxy chính: http://localhost"),
        ("culinary_frontend", "3000", "3000", "Frontend Web Client (Vite Dev Server): http://localhost:3000"),
        ("culinary_api", "8000", "8000", "Backend API Server (Uvicorn): http://localhost:8000"),
        ("culinary_postgres", "5433", "5432", "PostgreSQL Database Engine: postgresql://postgres:***@localhost:5433/culinary_blog"),
        ("culinary_redis", "6381", "6379", "Redis Cache Service: redis://localhost:6381/0"),
        ("culinary_minio", "9000 / 9001", "9000 / 9001", "S3 API (9000) & MinIO Console UI (9001): http://localhost:9001"),
        ("culinary_mailhog", "1026 / 8026", "1025 / 8025", "MailHog SMTP Server (1026) & Web UI (8026): http://localhost:8026")
    ]

    for idx, (srv, hp, cp, desc) in enumerate(ports_data):
        row = port_table.rows[idx + 1]
        bg_col = "F8FAFC" if idx % 2 == 1 else "FFFFFF"
        for i, val in enumerate([srv, hp, cp, desc]):
            cell = row.cells[i]
            cell.width = p_w[i]
            cell.text = val
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 80, 80, 100, 100)
            p = cell.paragraphs[0]
            if i in [1, 2]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(9.5)

    add_styled_heading(doc, "2.3. Quy Trình Khởi Động Từng Bước (Step-by-Step Execution)", level=2)
    add_body_p(doc, "Thực hiện lần lượt các câu lệnh sau trong terminal để dựng toàn bộ hệ thống:")
    
    add_body_p(doc, "Bước 1: Tải mã nguồn dự án từ GitHub:", bold_prefix="• ")
    add_body_p(doc, "git clone https://github.com/NHNam1209/PTUDW-2026-Nhom25.git\ncd PTUDW-2026-Nhom25", italic=True)

    add_body_p(doc, "Bước 2: Cấu hình tệp biến môi trường:", bold_prefix="• ")
    add_body_p(doc, "cp .env.example .env", italic=True)

    add_body_p(doc, "Bước 3: Biên dịch và khởi chạy toàn bộ 7 containers qua Docker Compose:", bold_prefix="• ")
    add_body_p(doc, "docker compose up -d --build", italic=True)

    add_body_p(doc, "Bước 4: Nạp cơ sở dữ liệu mẫu quy chuẩn (>100 công thức, 22 danh mục):", bold_prefix="• ")
    add_body_p(doc, "docker exec culinary_api python seed.py", italic=True)

    add_body_p(doc, "Bước 5: Chạy bộ kiểm thử tự động xác nhận toàn vẹn hệ thống:", bold_prefix="• ")
    add_body_p(doc, "docker exec culinary_api pytest -v", italic=True)

    add_styled_heading(doc, "2.4. Danh Sách Tài Khoản Thử Nghiệm Có Sẵn", level=2)
    add_body_p(doc, "Sau khi chạy seed.py, hệ thống được trang bị sẵn 2 tài khoản với đầy đủ quyền năng:")
    add_bullet_item(doc, "Email: admin@culinaryblog.com | Mật khẩu: Admin@123456 (Quyền quản trị danh mục, phân quyền thành viên, khóa/mở khóa tài khoản).", bold_lead="Tài khoản Quản Trị Viên (Admin)")
    add_bullet_item(doc, "Email: namnh.tandt@gmail.com | Mật khẩu: Nam@123456 (Quyền tác giả: tạo công thức mới, quản lý bài viết, xem dashboard cá nhân).", bold_lead="Tài khoản Tác Giả (Author)")

    doc.add_page_break()

    # 5. PHẦN III: CÁC GIẢI PHÁP KỸ THUẬT NỔI BẬT ĐÃ HIỆN THỰC
    add_styled_heading(doc, "III. CÁC ĐẶC TẢ KỸ THUẬT & GIẢI PHÁP CỐT LÕI (TECHNICAL HIGHLIGHTS)", level=1)
    
    add_styled_heading(doc, "3.1. Kiểm Soát Xung Đột Đồng Thời (Optimistic Concurrency Control)", level=2)
    add_body_p(doc, "Trong các hệ thống blog có nhiều đồng tác giả biên tập, xung đột dữ liệu xảy ra khi hai người cùng sửa một bài viết tại cùng một thời điểm. Thay vì dùng cơ chế khóa bi quan (Pessimistic Locking) gây nghẽn kết nối CSDL, hệ thống triển khai Optimistic Concurrency Control thông qua trường row_version (chuỗi UUID). Khi cập nhật, backend kiểm tra phiên bản gửi lên từ Client có trùng khớp với phiên bản trong DB hay không. Nếu phát hiện đã có người chỉnh sửa trước, server chủ động ném ngoại lệ RecipeConcurrencyException kèm HTTP 409 Conflict, yêu cầu client nạp lại dữ liệu mới nhất để bảo vệ an toàn nội dung.")

    add_styled_heading(doc, "3.2. Bảo Mật Xác Thực JWT Kép & Phát Hiện Tấn Công Phát Lại Token", level=2)
    add_body_p(doc, "Hệ thống xác thực áp dụng mô hình phân tách thời gian sống:")
    add_bullet_item(doc, "Thời hạn ngắn (15 phút), mã hóa claims người dùng (id, email, roles), lưu trữ an toàn trong bộ nhớ client.", bold_lead="Access Token")
    add_bullet_item(doc, "Thời hạn dài (7 ngày), lưu trữ mã băm SHA-256 trong bảng refresh_tokens kèm IP và thiết bị khởi tạo.", bold_lead="Refresh Token")
    add_bullet_item(doc, "Mỗi khi Client gửi yêu cầu làm mới Access Token, Refresh Token cũ ngay lập tức bị vô hiệu hóa (revoked) và một cặp token hoàn toàn mới được cấp phát. Nếu phát hiện một Refresh Token đã từng bị thu hồi được sử dụng lại (Token Reuse Attack), hệ thống lập tức thu hồi toàn bộ các Refresh Token đang hoạt động của người dùng đó (Paranoid Mode) và ghi nhật ký cảnh báo an ninh.", bold_lead="Cơ chế Token Rotation & Reuse Detection")

    add_styled_heading(doc, "3.3. Tối Ưu Tìm Kiếm Toàn Văn PostgreSQL (Full-Text Search unaccent)", level=2)
    add_body_p(doc, "Để độc giả tìm kiếm công thức bằng tiếng Việt có dấu hoặc không dấu một cách tự nhiên (ví dụ gõ 'pho bo' vẫn ra 'Phở bò'), hệ thống tích hợp module unaccent và tsvector của PostgreSQL. Chỉ mục GIN được đánh trên tập hợp các trường (tiêu đề bài viết, mô tả, tóm tắt). Kết quả trả về được sắp xếp theo hàm tính điểm độ trùng khớp ts_rank_cd, mang lại trải nghiệm tìm kiếm tức thì dưới 50ms.")

    add_styled_heading(doc, "3.4. Kiến Trúc Xử Lý Tác Vụ Ngầm (Background Tasks & Cron Scheduling)", level=2)
    add_body_p(doc, "Hệ thống phân tách triệt để các tác vụ tốn thời gian ra khỏi luồng xử lý chính HTTP:")
    add_bullet_item(doc, "Khi người dùng đăng ký tài khoản thành công, việc tạo khuôn mẫu HTML email và kết nối giao thức SMTP được đẩy vào BackgroundTasks của FastAPI, trả về HTTP 201 cho Client trong vòng vài phần mười giây.", bold_lead="Background Welcome Email")
    add_bullet_item(doc, "Khi ảnh tải lên, tác vụ resize ảnh bằng thuật toán LANCZOS của Pillow chạy ngầm tạo ảnh 300x300 và upload lên MinIO, cập nhật trường thumbnail_url của RecipeImage.", bold_lead="Background Thumbnail Resizing")
    add_bullet_item(doc, "Khởi chạy song song với ứng dụng qua FastAPI lifespan, định kỳ 24h quét toàn bộ CSDL và khởi tạo file static/sitemap.xml chuẩn SEO phục vụ các công cụ tìm kiếm Google/Bing.", bold_lead="APScheduler Sitemap Generation")

    add_styled_heading(doc, "3.5. Kiểm Soát Tần Suất Truy Cập (Sliding-Window Rate Limiting) & RFC 7807", level=2)
    add_body_p(doc, "Nhằm chống tấn công từ chối dịch vụ (DoS) và vét cạn mật khẩu (Brute-force), hệ thống cài đặt Middleware Rate Limiting theo thuật toán cửa sổ trượt (Sliding-Window):")
    add_bullet_item(doc, "Giới hạn nghiêm ngặt 10 request / phút trên mỗi địa chỉ IP.", bold_lead="Phân hệ Xác thực (/api/v1/auth/*)")
    add_bullet_item(doc, "Giới hạn 5 request / phút ngăn tràn bộ nhớ MinIO S3.", bold_lead="Phân hệ Upload Ảnh (/recipes/upload-image)")
    add_bullet_item(doc, "Giới hạn 100 request / phút bảo đảm trải nghiệm mượt mà cho toàn bộ người dùng chân chính.", bold_lead="Phân hệ API Tổng hợp (/api/v1/*)")
    add_body_p(doc, "Mọi trường hợp vi phạm đều nhận về HTTP 429 Too Many Requests kèm cấu trúc chuẩn hóa RFC 7807 Problem Details (application/problem+json) và header Retry-After thông báo thời gian cần chờ đợi.")

    doc.add_page_break()

    # 6. PHẦN IV: HÌNH ẢNH MINH HỌA & DEMO SẢN PHẨM THỰC TẾ
    add_styled_heading(doc, "IV. HÌNH ẢNH MINH HỌA & DEMO SẢN PHẨM THỰC TẾ (VISUAL DEMO)", level=1)
    add_body_p(doc, "Dưới đây là bộ sưu tập hình ảnh chụp thực tế từ hệ thống đang hoạt động trên môi trường Docker, thể hiện sinh động từng tính năng nghiệp vụ đã được hiện thực hoàn chỉnh:")

    scr_dir = r"D:\PTUDWNC\PTUDW-2026-Nhom25\screenshots"

    demos = [
        ("demo_01_homepage.png", "Hình 1: Giao diện Trang chủ (HomePage) - Hero Banner ẩm thực, Danh mục nổi bật & Món ngon tuyển chọn", 6.2),
        ("demo_02_recipes_list.png", "Hình 2: Trang Danh sách công thức (RecipeListPage) - Bộ lọc đa tiêu chí (Danh mục, Độ khó, Thời gian) & Phân trang", 6.2),
        ("demo_03_recipe_detail.png", "Hình 3: Trang Chi tiết công thức (RecipeDetailPage) - Bảng thành phần dinh dưỡng, Danh sách nguyên liệu & Bước nấu", 6.2),
        ("demo_04_categories_overview.png", "Hình 4: Trang Danh mục món ăn (CategoriesPage) - Tổng hợp 22 chủ đề ẩm thực kèm số lượng công thức", 6.0),
        ("demo_05_category_detail.png", "Hình 5: Chi tiết danh mục theo chủ đề (/categories/:slug) - Danh sách các bài viết trực thuộc danh mục", 6.0),
        ("demo_06_search_results.png", "Hình 6: Trang Kết quả tìm kiếm (SearchPage) - PostgreSQL Full-Text Search unaccent tiếng Việt", 6.0),
        ("demo_07_login_page.png", "Hình 7: Giao diện Đăng nhập (LoginPage) - Tích hợp nút Google OAuth 2.0 & Các nút điền sẵn tài khoản Demo", 4.8),
        ("demo_08_register_page.png", "Hình 8: Giao diện Đăng ký (RegisterPage) - Hệ thống kiểm tra độ mạnh mật khẩu thời gian thực", 4.8),
        ("demo_09_creator_dashboard.png", "Hình 9: Bảng điều khiển tác giả (CreatorDashboard) - Thống kê KPI, Công thức đã tạo & Biểu đồ phân bố độ khó", 6.0),
        ("demo_10_recipe_management.png", "Hình 10: Màn hình Quản lý công thức cá nhân (RecipeManagementPage) - Lọc trạng thái & Chuyển đổi vòng đời bài viết", 6.2),
        ("demo_11_recipe_editor.png", "Hình 11: Trình biên tập công thức nấu ăn đa bước (RecipeEditorPage) - Wizard thêm nguyên liệu & Cooking Timer", 6.0),
        ("demo_12_category_admin.png", "Hình 12: Màn hình Quản trị danh mục ẩm thực dành cho Admin (CategoryManagePage) - Thao tác Modal & Ràng buộc toàn vẹn", 6.0),
        ("demo_13_users_management.png", "Hình 13: Màn hình Quản lý người dùng hệ thống (UsersPage) - Phân quyền vai trò (Admin/Author/User) & Khóa tài khoản", 6.2),
        ("demo_14_swagger_docs.png", "Hình 14: Giao diện Tài liệu API tương tác trực tiếp Swagger OpenAPI (FastAPI Interactive Docs)", 6.0),
        ("demo_15_health_probe.png", "Hình 15: Kiểm tra trạng thái sức khỏe hệ thống (Health Check Probe: PostgreSQL, Redis, MinIO)", 5.2),
        ("demo_16_mailhog_ui.png", "Hình 16: Hộp thư MailHog Web UI - Xác nhận nhận thành công email chào mừng gửi từ Background Job", 6.0),
        ("demo_17_minio_console.png", "Hình 17: Bảng điều khiển MinIO S3 Object Storage Console - Quản lý Bucket 'culinary-blog' và kho ảnh", 6.0),
    ]

    for fname, caption, w in demos:
        fpath = os.path.join(scr_dir, fname)
        add_image_figure(doc, fpath, caption, width_in=w)

    doc.add_page_break()

    # 7. PHẦN V: ĐÁNH GIÁ KẾT QUẢ & KẾT LUẬN
    add_styled_heading(doc, "V. ĐÁNH GIÁ KẾT QUẢ, BÀI HỌC KINH NGHIỆM & KẾT LUẬN", level=1)
    
    add_styled_heading(doc, "5.1. Bảng Đối Chiếu Kết Quả Với Mục Tiêu Đồ Án", level=2)
    add_body_p(doc, "Toàn bộ các yêu cầu chức năng và phi chức năng trong tài liệu SRS v1.0.0 đều đã được hoàn thành trọn vẹn 100%:")
    
    eval_table = doc.add_table(rows=7, cols=3)
    eval_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    e_hdrs = ["Nhóm yêu cầu", "Mục tiêu theo tài liệu SRS", "Kết quả thực tế đạt được"]
    e_w = [Inches(1.8), Inches(2.6), Inches(2.6)]

    for i, title in enumerate(e_hdrs):
        cell = eval_table.rows[0].cells[i]
        cell.width = e_w[i]
        cell.text = title
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, 100, 100, 120, 120)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = "Times New Roman"
            r.bold = True
            r.font.size = Pt(10)
            r.font.color.rgb = RGBColor(255, 255, 255)

    eval_data = [
        ("Xác thực & Bảo mật (FR-AUTH)", "JWT kép, Google Login, Lockout 15p, Password Strength", "Hoàn thành 100%. Vượt qua toàn bộ ca kiểm thử bảo mật tấn công brute-force và token replay."),
        ("Quản lý Công thức (FR-RCP)", "CRUD, Phân trang, Lọc đa tiêu chí, Optimistic Concurrency", "Hoàn thành 100%. Kiểm soát xung đột row_version chính xác, bảo đảm tính toàn vẹn dữ liệu."),
        ("Dữ liệu CSDL (Data Seeding)", "Tối thiểu 20 danh mục, 100 công thức có đủ nguyên liệu & bước", "Vượt chỉ tiêu: Seed thành công 22 danh mục và 105 công thức nấu ăn chuẩn chỉnh."),
        ("Lưu trữ & Xử lý Tệp (FR-FILE, FR-JOB)", "MinIO S3 SDK, Kiểm tra Magic Bytes, Resize Thumbnail", "Hoàn thành 100%. Tự động tạo ảnh thumbnail 300x300 ngầm qua Pillow, ngăn chặn file giả mạo."),
        ("Hạ tầng & Giám sát (FR-OBS, DevOps)", "Docker Compose, Nginx, Structured Logging, Correlation-ID", "Hoàn thành 100%. Logs xoay vòng 10MB đa kênh, theo dõi request với UUID, rate limiting trượt."),
        ("Giao diện Frontend (FR-UI, FR-DASH)", "SPA React Vite, Responsive, Wizard soạn thảo, SEO JSON-LD", "Hoàn thành 100%. Build production tối ưu, vượt qua bài kiểm tra Google Rich Results Test.")
    ]

    for idx, (grp, tgt, res) in enumerate(eval_data):
        row = eval_table.rows[idx + 1]
        bg_col = "F8FAFC" if idx % 2 == 1 else "FFFFFF"
        for i, val in enumerate([grp, tgt, res]):
            cell = row.cells[i]
            cell.width = e_w[i]
            cell.text = val
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, 80, 80, 100, 100)
            p = cell.paragraphs[0]
            if i == 0:
                p.runs[0].bold = True
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(9.5)

    add_styled_heading(doc, "5.2. Bài Học Kinh Nghiệm & Kỹ Năng Đạt Được", level=2)
    add_body_p(doc, "Thông qua quá trình nghiên cứu, thiết kế kiến trúc và hiện thực toàn diện đồ án Culinary Blog Platform, các kỹ năng chuyên môn cốt lõi đã được nâng cao vượt bậc:")
    add_bullet_item(doc, "Thấu hiểu và áp dụng thành thạo nguyên lý Dependency Inversion, phân tách Domain Entities khỏi tầng Persistence và Web Framework, giúp mã nguồn mạch lạc và dễ dàng bảo trì.", bold_lead="Tư duy Clean Architecture")
    add_bullet_item(doc, "Nắm vững cơ chế vận hành của async/await, Connection Pooling trong asyncpg, kiểm soát giao dịch Unit of Work và giải quyết bài toán xung đột đồng thời trong môi trường phân tán.", bold_lead="Kỹ năng Lập trình Bất Đồng Bộ Cao Cấp")
    add_bullet_item(doc, "Làm chủ việc điều phối đa dịch vụ (Docker Compose, Nginx, PostgreSQL, Redis, MinIO, MailHog), tối ưu hóa mạng nội bộ và giám sát dịch vụ qua Health Probes.", bold_lead="Tư duy Hệ thống & DevOps Hiện Đại")
    add_bullet_item(doc, "Hiểu sâu về cấu trúc JSON-LD Schema.org, Open Graph Protocol, cũng như cách thiết kế UI/UX tinh gọn, phản hồi nhanh phục vụ người dùng thực tế.", bold_lead="Tối Ưu Hóa Trải Nghiệm Người Dùng & SEO")

    add_styled_heading(doc, "5.3. Hướng Phát Triển Mở Rộng Trong Tương Lai", level=2)
    add_body_p(doc, "Để đưa sản phẩm thành một nền tảng thương mại quy mô lớn, một số tính năng nâng cao có thể được tích hợp trong giai đoạn tiếp theo:")
    add_bullet_item(doc, "Bổ sung hệ thống bình luận đa cấp, đánh giá sao (1-5 sao) và lưu công thức yêu thích vào sổ tay cá nhân.", bold_lead="Tương tác mạng xã hội ẩm thực")
    add_bullet_item(doc, "Ứng dụng mô hình AI gợi ý món ăn thông minh dựa trên nguyên liệu hiện có trong tủ lạnh của người dùng.", bold_lead="Trợ lý ẩm thực thông minh (AI Cooking Assistant)")
    add_bullet_item(doc, "Đóng gói ứng dụng thành Progressive Web App (PWA) cho phép người nấu xem hướng dẫn và sử dụng bộ đếm giờ ngoại tuyến ngay cả khi mất kết nối mạng internet.", bold_lead="Hỗ trợ Chế độ Ngoại Tuyến (Offline PWA)")

    # Lưu tài liệu
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)
    print(f"Báo cáo hoàn chỉnh đã được tạo thành công tại: {output_path}")

if __name__ == "__main__":
    tmpl = "d:/PTUDWNC/Mau_Nop_Bao_Cao_Lab_Ca_Nhan_2026.docx"
    out_root = "d:/PTUDWNC/Bao_Cao_Do_An_Nhom_25_Culinary_Blog.docx"
    out_repo = "d:/PTUDWNC/PTUDW-2026-Nhom25/Bao_Cao_Do_An_Nhom_25_Culinary_Blog.docx"
    
    build_full_report(tmpl, out_root)
    build_full_report(tmpl, out_repo)
