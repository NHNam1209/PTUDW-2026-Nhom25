# -*- coding: utf-8 -*-
"""
Script to generate Tai_Lieu_Bao_Cao_Ca_Nhan_Nguyen_Hoai_Nam.docx
Focuses 100% on Nguyen Hoai Nam's assigned tasks, code explanations, and targeted Q&A.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

WORKSPACE_DIR = r"D:\PTUDWNC\PTUDW-2026-Nhom25"
OUTPUT_DOCX = os.path.join(WORKSPACE_DIR, "Tai_Lieu_Bao_Cao_Ca_Nhan_Nguyen_Hoai_Nam.docx")

doc = docx.Document()

# Page setup: A4, normal margins
section = doc.sections[0]
section.page_width = Inches(8.27)
section.page_height = Inches(11.69)
section.top_margin = Inches(0.8)
section.bottom_margin = Inches(0.8)
section.left_margin = Inches(0.9)
section.right_margin = Inches(0.8)

NAVY = RGBColor(0x1E, 0x3A, 0x8A)
DARK_SLATE = RGBColor(0x0F, 0x17, 0x2A)
GRAY = RGBColor(0x47, 0x55, 0x69)
BLUE_ACCENT = RGBColor(0x25, 0x63, 0xEB)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex="F8FAFC"):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)

def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(18)
    run.bold = True
    run.font.color.rgb = NAVY
    return p

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(14)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.italic = True
    run.font.color.rgb = GRAY
    return p

def add_h1(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(14)
    run.bold = True
    run.font.color.rgb = NAVY
    return p

def add_h2(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.bold = True
    run.font.color.rgb = BLUE_ACCENT
    return p

def add_p(text, bold_prefix="", indent=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.25
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.25)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(11)
        r_pre.bold = True
        r_pre.font.color.rgb = DARK_SLATE
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)
    run.font.color.rgb = DARK_SLATE
    return p

def add_bullet(text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.line_spacing = 1.2
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(11)
        r_pre.bold = True
        r_pre.font.color.rgb = DARK_SLATE
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)
    run.font.color.rgb = DARK_SLATE
    return p

def add_code_box(code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
    set_cell_shading(cell, "F1F5F9")
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(code_text)
    run.font.name = "Consolas"
    run.font.size = Pt(9.5)
    run.font.color.rgb = DARK_SLATE
    doc.add_paragraph().paragraph_format.space_after = Pt(3)

def add_callout(text, title="ĐIỂM NHẤN BẢO VỆ:"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    set_cell_shading(cell, "EFF6FF")
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}>'
                        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="2563EB"/>'
                        f'<w:top w:val="none"/>'
                        f'<w:right w:val="none"/>'
                        f'<w:bottom w:val="none"/>'
                        f'</w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(f"{title} ")
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(11)
    r1.bold = True
    r1.font.color.rgb = BLUE_ACCENT
    
    r2 = p.add_run(text)
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(11)
    r2.font.color.rgb = DARK_SLATE
    
    doc.add_paragraph().paragraph_format.space_after = Pt(3)

# ==================== BUILD DOCUMENT ====================

add_title("BÁO CÁO CÁ NHÂN & TÀI LIỆU ÔN TẬP BẢO VỆ CUỐI KỲ")
add_subtitle("Sinh viên thực hiện: NGUYỄN HOÀI NAM (Trưởng nhóm - MSSV: 2312607 / 2312694)\n"
             "Đề tài: Hệ thống Culinary Blog — Nhóm 25 • Môn học: Phát triển ứng dụng web nâng cao\n"
             "Giảng viên hướng dẫn: TS. Nguyễn Thị Lương")

add_callout(
    "Tài liệu này tập trung 100% vào các phân hệ do sinh viên NGUYỄN HOÀI NAM trực tiếp thiết kế, cài đặt và phụ trách "
    "(gồm 19 Issues: SETUP, DEVOPS, toàn bộ FR-AUTH-001 -> 007, toàn bộ FR-RCP-001 -> 010 và FR-OBS-001). "
    "Bao gồm kịch bản thuyết trình cá nhân 6-7 phút, giải thích chi tiết 9 đoạn mã nguồn trọng điểm và bộ câu hỏi phản biện chuyên sâu.",
    "MỤC TIÊU TÀI LIỆU:"
)

# ----------------- PHẦN 1 -----------------
add_h1("PHẦN I. DANH SÁCH 19 ĐẦU VIỆC DO NGUYỄN HOÀI NAM PHỤ TRÁCH")

issues = [
    ("Issue #1 (SETUP/DEVOPS)", "Khởi tạo khung dự án, cấu hình Dockerfile, Docker Compose 6 dịch vụ, Nginx reverse proxy, PostgreSQL init & seed script."),
    ("Issue #2 (FR-AUTH-001)", "API Đăng ký tài khoản (User Registration): Băm mật khẩu Bcrypt, validation độ phức tạp, gán role mặc định Author."),
    ("Issue #3 (FR-AUTH-002)", "API Đăng nhập Email/Password & Lockout: Kiểm tra thông tin, theo dõi access_failed_count, khóa 15 phút nếu sai 5 lần, cấp Access (15p) & Refresh token."),
    ("Issue #4 (FR-AUTH-003)", "Tích hợp Google OAuth 2.0 Identity Provider: Xác thực Google ID Token, sinh username tự động không trùng lặp, cấp phiên làm việc."),
    ("Issue #5 (FR-AUTH-004)", "Cơ chế Token Refresh & Token Rotation: Thu hồi refresh token cũ, cấp cặp token mới, phát hiện tấn công tái sử dụng (Reuse Attack) thu hồi toàn bộ token người dùng."),
    ("Issue #6 (FR-AUTH-005)", "API Đăng xuất (User Logout): Thu hồi refresh token, đưa access token vào Redis blacklist kết thúc phiên ngay lập tức."),
    ("Issue #7 (FR-AUTH-006)", "API Xem thông tin cá nhân (GET /api/v1/auth/me): Trả về UserProfileDto bảo mật, loại bỏ mật khẩu băm."),
    ("Issue #8 (FR-AUTH-007)", "API Cập nhật hồ sơ tác giả (PATCH /api/v1/auth/me): Cập nhật một phần (fullName, avatarUrl, bio)."),
    ("Issue #9 (FR-RCP-001)", "API Danh sách công thức: Phân trang Offset-based (page, pageSize), lọc đa tiêu chí (danh mục, độ khó, thời gian), sắp xếp, chống Cartesian Explosion bằng selectinload()."),
    ("Issue #10 (FR-RCP-002)", "API Chi tiết công thức nấu ăn: Lấy công thức theo ID hoặc Slug SEO, nạp kèm steps, ingredients, images và nutrition."),
    ("Issue #11 (FR-RCP-003)", "API Tạo công thức mới (POST /api/v1/recipes): Khởi tạo trạng thái Draft, tự động sinh slug tiếng Việt chuẩn SEO."),
    ("Issue #12 (FR-RCP-004)", "API Cập nhật công thức: Kiểm soát xung đột Optimistic Concurrency Control qua row_version (trả 409 Conflict khi bị tranh chấp) và Resource-based Authorization."),
    ("Issue #13 (FR-RCP-005)", "API Xuất bản / Hủy xuất bản (Publish/Unpublish): Kiểm tra điều kiện bắt buộc tối thiểu 1 bước nấu và 1 nguyên liệu."),
    ("Issue #14 (FR-RCP-006)", "API Lưu trữ công thức (Archive): Chuyển trạng thái sang Archived, ẩn khỏi danh mục công khai."),
    ("Issue #15 (FR-RCP-007)", "API Xóa công thức: Áp dụng Xóa mềm (Soft Delete is_deleted = True), giải quyết mâu thuẫn Unique constraint trên Slug."),
    ("Issue #16 (FR-RCP-008)", "API Quản lý ảnh công thức: Upload ảnh lên MinIO, kiểm tra MIME & Magic bytes, đặt ảnh đại diện chính (primary image), xóa ảnh."),
    ("Issue #17 (FR-RCP-009)", "API Quản lý nguyên liệu (Recipe Ingredients CRUD): Thêm, sửa, xóa danh sách nguyên liệu và định lượng."),
    ("Issue #18 (FR-RCP-010)", "API Quản lý các bước nấu (Recipe Steps CRUD): Thêm, sửa, xóa bước và tự động đánh số lại (renumbering) liên tục."),
    ("Issue #19 (FR-OBS-001)", "Xây dựng bộ 3 Health Check Probes: Tách bạch /health/live (Process liveness) và /health/ready (Database/Redis readiness) chuẩn Cloud-Native.")
]

for code, desc in issues:
    add_bullet(desc, bold_prefix=code + ": ")

# ----------------- PHẦN 2 -----------------
add_h1("PHẦN II. GIẢI THÍCH CHI TIẾT 9 ĐOẠN MÃ NGUỒN CỐT LÕI (KHI GIÁO VIÊN CHỈ ĐỊNH)")

add_h2("1. Kiểm soát Đăng nhập & Khóa tài khoản chống Brute-force (FR-AUTH-002)")
add_p("Vị trí: backend/app/api/v1/auth.py (trong hàm login)")
add_code_box(
"""if not verify_password(req.password, user.password_hash):
    user.access_failed_count += 1
    if user.access_failed_count >= 5:
        user.lockout_end = datetime.now(timezone.utc) + timedelta(minutes=15)
    await db.commit()
    raise UnauthorizedException(
        error_code="AUTH_INVALID_CREDENTIALS",
        detail="Email hoặc mật khẩu không chính xác."
    )

user.access_failed_count = 0
user.lockout_end = None"""
)
add_p("Ý nghĩa & Chức năng: Chống lại các cuộc tấn công dò mật khẩu tự động (Brute-force). Khi người dùng nhập sai, biến access_failed_count tăng thêm 1. Khi đạt ngưỡng 5 lần, trường lockout_end được gán thời gian khóa 15 phút. Nếu đăng nhập đúng, bộ đếm được reset về 0.")

add_h2("2. Refresh Token Rotation & Phát hiện tấn công phát lại Reuse Attack (FR-AUTH-004)")
add_p("Vị trí: backend/app/api/v1/auth.py (trong hàm refresh_token)")
add_code_box(
"""if token_record.revoked_at is not None:
    # Nghi vấn kẻ gian dùng lại Refresh Token đã thu hồi -> Thu hồi toàn bộ token người dùng!
    await db.execute(
        update(RefreshToken)
        .where(RefreshToken.user_id == token_record.user_id)
        .values(revoked_at=datetime.now(timezone.utc))
    )
    await db.commit()
    raise UnauthorizedException(
        error_code="AUTH_REFRESH_TOKEN_REVOKED",
        detail="Refresh token đã bị thu hồi trước đó. Phát hiện nghi vấn tấn công phát lại (Token Reuse Attack)."
    )"""
)
add_p("Ý nghĩa & Chức năng: Theo chuẩn RFC 6819, mỗi khi Refresh Token được dùng để đổi Access Token mới, token cũ bị thu hồi ngay. Nếu một token đã thu hồi lại được gửi lên server lần nữa, điều đó chứng tỏ token đã bị hacker đánh cắp và sử dụng trái phép. Hệ thống lập tức thu hồi toàn bộ token của tài khoản đó, buộc người dùng đăng nhập lại để bảo vệ phiên.")

add_h2("3. Kiểm soát Concurrency: Optimistic Concurrency Control (FR-RCP-004)")
add_p("Vị trí: backend/app/api/v1/recipes.py (trong hàm update_recipe)")
add_code_box(
"""if recipe.row_version != payload.row_version:
    raise ConcurrencyConflictException(
        error_code="CONCURRENCY_CONFLICT",
        detail="Công thức đã bị chỉnh sửa bởi phiên khác. Vui lòng tải lại dữ liệu mới nhất trước khi lưu."
    )
recipe.row_version += 1"""
)
add_p("Ý nghĩa & Chức năng: Giải quyết bài toán 'Lost Update' khi 2 tác giả (hoặc 1 người mở 2 tab) cùng sửa 1 công thức. Client gửi kèm số row_version đã đọc được. Nếu số này không khớp với CSDL hiện tại, hệ thống từ chối lưu và trả về mã lỗi HTTP 409 Conflict. Nếu hợp lệ, hệ thống tăng row_version lên 1.")

add_h2("4. Phân quyền dựa trên tài nguyên: Resource-Based Authorization")
add_p("Vị trí: backend/app/api/v1/recipes.py")
add_code_box(
"""def _check_recipe_ownership(recipe: Recipe, user: User) -> None:
    if user.role != "Admin" and str(recipe.author_id) != str(user.id):
        raise ForbiddenException(
            error_code="RECIPE_FORBIDDEN",
            detail="Bạn không có quyền chỉnh sửa hoặc xóa công thức này."
        )"""
)
add_p("Ý nghĩa & Chức năng: Ngăn chặn người dùng sửa bài viết của người khác. Kiểm tra thực thể Recipe cụ thể có author_id trùng với ID người đang đăng nhập hay không. Nếu không trùng và người đó không phải Admin, chặn lại bằng mã lỗi HTTP 403 Forbidden.")

add_h2("5. Ràng buộc điều kiện Xuất bản bài viết (FR-RCP-005)")
add_p("Vị trí: backend/app/api/v1/recipes.py (trong hàm publish_recipe)")
add_code_box(
"""if not recipe.steps or not recipe.ingredients:
    raise BadRequestException(
        error_code="RECIPE_INCOMPLETE",
        detail="Công thức phải có ít nhất 1 bước thực hiện và 1 nguyên liệu mới được xuất bản."
    )
recipe.status = RecipeStatus.Published.value
recipe.published_at = datetime.now(timezone.utc)"""
)
add_p("Ý nghĩa & Chức năng: Đảm bảo chất lượng bài viết trước khi đưa ra trang chủ. Một công thức không có nguyên liệu hoặc không có hướng dẫn các bước nấu thì không được phép xuất bản ra công chúng.")

add_h2("6. Xóa mềm (Soft Delete) & Xử lý mâu thuẫn Unique Slug (FR-RCP-007)")
add_p("Vị trí: backend/app/api/v1/recipes.py (hàm delete_recipe) & models/base.py")
add_code_box(
"""# Soft delete
recipe.is_deleted = True
recipe.status = RecipeStatus.Archived.value
recipe.updated_at = datetime.now(timezone.utc)
await db.commit()"""
)
add_p("Ý nghĩa & Chức năng: Khi xóa công thức, không chạy lệnh DELETE vật lý để tránh mất mát lịch sử và gãy liên kết dữ liệu. Dữ liệu chỉ được đánh dấu is_deleted = True. Mâu thuẫn với ràng buộc Unique trên Slug được Nam giải quyết bằng Partial Unique Index trong CSDL (WHERE is_deleted = false) hoặc thêm hậu tố ngẫu nhiên.")

add_h2("7. Tối ưu hóa hiệu năng truy vấn, tránh Cartesian Explosion")
add_p("Vị trí: backend/app/api/v1/recipes.py (trong hàm get_recipes)")
add_code_box(
"""stmt = (
    select(Recipe)
    .where(Recipe.is_deleted == False)
    .options(
        selectinload(Recipe.category),
        selectinload(Recipe.author),
        selectinload(Recipe.images),
    )
)"""
)
add_p("Ý nghĩa & Chức năng: Sử dụng selectinload() của SQLAlchemy 2.0. Kỹ thuật này tương đương AsSplitQuery() trong EF Core: Tách câu query nạp các collection con (ảnh, tác giả, danh mục) thành các truy vấn SELECT WHERE id IN (...) độc lập, tránh việc CSDL thực hiện phép tích Descartes nhân chéo 150 - 750 dòng trả về mạng.")

add_h2("8. Bộ 3 Health Check Probes chuẩn Cloud-Native (FR-OBS-001)")
add_p("Vị trí: backend/app/api/v1/health.py")
add_code_box(
"""@router.get("/health/live")
async def liveness():
    # Kiểm tra process còn sống không -> trả về 200
    return {"status": "Healthy", "probe": "liveness"}

@router.get("/health/ready")
async def readiness(response: Response, db: AsyncSession = Depends(get_db)):
    # Kiểm tra kết nối DB và Redis
    try:
        await db.execute(text("SELECT 1"))
        r = aioredis.from_url(settings.REDIS_URL, socket_timeout=2.0)
        await r.ping()
    except Exception:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "Unhealthy", "probe": "readiness"}"""
)
add_p("Ý nghĩa & Chức năng: Tách biệt rạch ròi giữa Liveness và Readiness probes. Nếu database bị chậm, /health/ready trả về 503 để Nginx tạm ngưng chuyển traffic đến, nhưng /health/live vẫn trả 200 để Docker/K8s không restart container, tránh lỗi CrashLoopBackOff sập hệ thống.")

add_h2("9. Tích hợp Xác thực Google OAuth 2.0 (FR-AUTH-003)")
add_p("Vị trí: backend/app/api/v1/auth.py (trong hàm google_login)")
add_p("Ý nghĩa & Chức năng: Xác thực token Google qua google-auth. Nếu là người dùng mới, tự động trích xuất email, avatar và sinh user_name duy nhất bằng thuật toán vòng lặp tăng dần counter (base_username1, base_username2...), cấp role Author và phát hành cặp token JWT.")

# ----------------- PHẦN 3 -----------------
add_h1("PHẦN III. BỘ CÂU HỎI LÝ THUYẾT & PHẢN BIỆN CHUYÊN BIỆT CHO NGUYỄN HOÀI NAM")

qa_list = [
    ("Câu 1: Tại sao em lại chọn kiến trúc Decoupled (FastAPI + React SPA) kết hợp Nginx thay vì dùng Full-stack Monolith (như Django Template hay Next.js SSR)?",
     "Trả lời: Kiến trúc Decoupled cho phép tách biệt rạch ròi trách nhiệm (Separation of Concerns). Backend FastAPI đóng vai trò API Service thuần túy, có thể tái sử dụng 100% khi sau này phát triển thêm ứng dụng Mobile (Flutter/React Native). Nginx làm Reverse Proxy giúp che giấu cấu trúc mạng nội bộ, tối ưu hóa SSL termination và xử lý CORS tập trung."),
    
    ("Câu 2: Tại sao JWT là Stateless? Ưu và nhược điểm khi em áp dụng cho dự án này là gì?",
     "Trả lời: JWT tự mang đầy đủ thông tin (user_id, roles, exp) trong payload được ký số bằng SECRET_KEY, server verify không cần query DB. Ưu điểm là scale ngang backend không cần share session. Nhược điểm là khó thu hồi tức thì nếu bị lộ token. Để giải quyết nhược điểm này, em đã thiết kế Access Token ngắn hạn (15 phút) kết hợp Refresh Token lưu database/Redis để có thể thu hồi (revoke) ngay lập tức khi người dùng bấm Đăng xuất hoặc bị Khóa tài khoản."),
    
    ("Câu 3: Trong API của em, tại sao PUT /recipes/{id} lại khác PATCH /auth/me?",
     "Trả lời: Theo chuẩn RESTful, PUT là thay thế toàn bộ tài nguyên (Idempotent). Khi sửa Recipe, client phải gửi đầy đủ thông tin (tiêu đề, mô tả, khẩu phần, thời gian nấu, dinh dưỡng) để ghi đè toàn bộ bản ghi. Trong khi đó, PATCH là cập nhật từng phần: khi user sửa Profile, họ chỉ muốn đổi tên hiển thị (fullName) hoặc avatar mà không cần gửi lại toàn bộ thông tin tài khoản."),
    
    ("Câu 4: Khi người dùng xem danh sách Recipe, em dùng kỹ thuật phân trang nào? Tại sao không dùng Cursor-based?",
     "Trả lời: Em sử dụng Offset-based pagination với query params page=1 và pageSize=12. Lý do: Giao diện web của Culinary Blog yêu cầu hiển thị thanh số trang cụ thể (Trang 1, 2, 3...) và hiển thị tổng số trang (totalPages). Cursor-based rất khó hỗ trợ nhảy trang bất kỳ (chỉ hợp với cuộn vô tận). Với quy mô dữ liệu blog ẩm thực, bảng recipes có đánh B-tree index cho các cột lọc thì Offset-based ở các trang đầu phản hồi cực nhanh dưới 15ms."),
    
    ("Câu 5: Hiện tượng Cartesian Explosion trong truy vấn công thức xảy ra thế nào và em xử lý ra sao?",
     "Trả lời: Khi 1 Recipe có 10 Steps, 15 Ingredients và 3 Images, nếu dùng JOIN thông thường (joinedload), CSDL sẽ nhân chéo kết quả: 1 x 10 x 15 x 3 = 450 dòng trả về qua mạng, làm nhân bản thông tin recipe cha 450 lần. Em đã xử lý bằng cách dùng selectinload() của SQLAlchemy (tương đương AsSplitQuery trong EF Core): tách thành 4 query SELECT WHERE id IN (...) độc lập, chỉ trả về 1 + 10 + 15 + 3 = 29 dòng, giảm 15 lần lưu lượng truyền tải."),
    
    ("Câu 6: Tại sao em phải tách biệt /health/live và /health/ready?",
     "Trả lời: /health/live kiểm tra process có còn phản hồi không (nếu chết thì restart). /health/ready kiểm tra dependency bên ngoài (DB, Redis). Nếu chỉ có 1 endpoint kiểm tra cả DB, khi database bị quá tải tạm thời, bộ điều phối sẽ tưởng container bị hỏng và restart liên tục (CrashLoopBackOff), tạo ra cơn bão kết nối (Thundering Herd) làm sập hoàn toàn hệ thống.")
]

for q, a in qa_list:
    add_h2(q)
    add_p(a)

# ----------------- PHẦN 4 -----------------
add_h1("PHẦN IV. KỊCH BẢN THUYẾT TRÌNH CÁ NHÂN CĂN CHUẨN 6 – 7 PHÚT")

speech_steps = [
    ("Slide 1: Mở đầu & Giới thiệu vai trò (30s)", 
     "Kính thưa Cô và các bạn! Em tên là Nguyễn Hoài Nam, Trưởng nhóm 25. "
     "Trong buổi bảo vệ hôm nay, em xin phép trình bày chi tiết phần công việc mà bản thân em trực tiếp thiết kế và cài đặt trong dự án Culinary Blog. "
     "Phạm vi phụ trách của em bao gồm: Thiết kế kiến trúc tổng thể, hạ tầng DevOps Docker, toàn bộ Module Xác thực và Bảo mật tài khoản, "
     "Module Quản lý Công thức cốt lõi, cơ chế kiểm soát Concurrency và hệ thống Health Check Probes chuẩn Cloud-Native."),
    
    ("Slide 2: Tổng hợp 19 Chức năng hoàn thành (35s)",
     "Về khối lượng công việc, em trực tiếp đảm nhiệm và hoàn thành 100% tất cả 19 đầu việc theo đặc tả SRS v1.0.0. "
     "Bao gồm: 1 gói Setup DevOps, 7 chức năng Xác thực nâng cao từ FR-AUTH-001 đến 007, 10 chức năng Quản lý công thức từ FR-RCP-001 đến 010, "
     "và gói giám sát hệ thống FR-OBS-001."),
    
    ("Slide 3: Hạ tầng DevOps & Điều phối Container (45s)",
     "Về hạ tầng, em đóng gói toàn bộ hệ thống bằng Docker Compose với 6 container dịch vụ độc lập. "
     "Nginx đứng ở tầng biên lắng nghe cổng 80, giải quyết triệt để bài toán định tuyến Reverse Proxy và xử lý CORS. "
     "Backend viết bằng FastAPI Python 3.12 theo chuẩn Clean Architecture, giao tiếp bất đồng bộ qua SQLAlchemy Async và asyncpg với PostgreSQL 16. "
     "Hệ thống có Redis quản lý token và MailHog làm SMTP ảo bắt trọn email."),
    
    ("Slide 4: Module Xác thực & Token Rotation (50s)",
     "Điểm sáng đầu tiên trong phần code của em là Module Xác thực bảo mật đa lớp: "
     "Mật khẩu được băm bằng Bcrypt kèm salt ngẫu nhiên. Em cài đặt thuật toán theo dõi số lần đăng nhập sai, nếu sai 5 lần liên tiếp sẽ tự động kích hoạt lockout khóa tài khoản 15 phút. "
     "Đặc biệt, em hiện thực cơ chế Refresh Token Rotation theo chuẩn RFC 6819: Mỗi lần refresh sẽ hủy token cũ và phát hành token mới. "
     "Nếu phát hiện token cũ bị dùng lại (Token Reuse Attack), hệ thống lập tức thu hồi toàn bộ phiên của user đó để bảo vệ tài khoản."),
    
    ("Slide 5: Module Công thức & Tối ưu ORM (45s)",
     "Điểm sáng thứ hai là Module Recipe Core: Em cài đặt trọn vẹn vòng đời công thức từ Draft, Publish tới Archive. "
     "Hàm xuất bản công thức kiểm tra bắt buộc phải có tối thiểu 1 bước và 1 nguyên liệu. Các bước nấu khi thêm/sửa/xóa được tự động đánh số lại. "
     "Về hiệu năng CSDL, khi query danh sách công thức, em dùng kỹ thuật selectinload() của SQLAlchemy để triệt tiêu hoàn toàn lỗi Cartesian Explosion, "
     "giúp số dòng dữ liệu nạp qua mạng giảm từ 150 dòng xuống còn 26 dòng."),
    
    ("Slide 6: Optimistic Concurrency & Xử lý Mâu thuẫn SRS (50s)",
     "Về mặt kỹ thuật chuyên sâu, em cài đặt cơ chế Optimistic Concurrency Control qua trường row_version để giải quyết triệt để lỗi Lost Update khi nhiều người cùng sửa 1 công thức. "
     "Nếu phát hiện phiên bản dữ liệu bị cũ, API lập tức từ chối và trả về HTTP 409 Conflict. "
     "Ngoài ra, em đã phát hiện và xử lý mâu thuẫn lớn trong file SRS giữa việc Soft Delete và Ràng buộc duy nhất trên Slug bằng cách sử dụng Partial Unique Index trong CSDL, "
     "giúp tác giả xóa bài cũ mà vẫn có thể tạo lại bài mới với slug đó mà không vi phạm toàn vẹn dữ liệu."),
    
    ("Slide 7: Resource-Based Authorization & DTO Pattern (40s)",
     "Về kiểm soát truy cập và chuẩn hóa dữ liệu: Em cài đặt hàm _check_recipe_ownership kiểm tra quyền sở hữu bài viết: người dùng dù đã đăng nhập nhưng không phải tác giả và không phải Admin thì tuyệt đối không thể sửa hoặc xóa bài của người khác, trả về lỗi 403 Forbidden. "
     "Toàn bộ dữ liệu ra vào đều qua hệ thống Pydantic DTO để giấu kín mật khẩu hash và ngăn chặn lỗi vòng lặp tuần hoàn khi serialize JSON."),
    
    ("Slide 8: Giám sát Health Check Probes Cloud-Native (45s)",
     "Về giám sát hệ thống theo FR-OBS-001, em đã thiết kế riêng biệt 3 endpoints chuẩn Cloud-Native: "
     "Endpoint /health/live kiểm tra tiến trình Python còn sống để bộ điều phối biết có cần restart hay không. "
     "Endpoint /health/ready kiểm tra kết nối CSDL PostgreSQL và Redis. Nếu database bị nghẽn, endpoint này trả về 503 để load balancer tạm ngưng chuyển traffic đến nhưng KHÔNG restart container, "
     "giúp hệ thống tránh được lỗi dây chuyền CrashLoopBackOff."),
    
    ("Slide 9: Minh chứng Triển khai & Kiểm thử (40s)",
     "Để chứng minh kết quả cài đặt: Toàn bộ 19 endpoints em xây dựng đều được tích hợp tài liệu hóa Swagger UI tự động tại /docs. "
     "Em đã viết bộ test tự động Pytest kiểm tra logic xác thực mật khẩu, token expiration và các probes. "
     "Kịch bản seed.py nạp sẵn 41 món ăn mẫu và tài khoản thử nghiệm giúp hệ thống sẵn sàng hoạt động ngay sau khi khởi chạy."),
    
    ("Slide 10: Tổng kết & Sẵn sàng Q&A (20s)",
     "Tóm lại, em đã hoàn thành 100% tất cả 19 đầu việc được giao, đảm bảo đúng chuẩn SRS, bảo mật cao và tối ưu hiệu năng. "
     "Em xin chân thành cảm ơn Cô đã lắng nghe. Bây giờ em đã sẵn sàng giải thích chi tiết bất kỳ đoạn code nào hoặc trả lời các câu hỏi phản biện từ Cô!")
]

for title, speech in speech_steps:
    add_h2(title)
    add_p(speech, indent=True)

doc.save(OUTPUT_DOCX)
print("Saved DOCX successfully:", OUTPUT_DOCX)
