"""
Lab 8 Individual Report Generator (Culinary Blog Platform)
Student: Nguyen Hoai Nam (MSSV: 2312694) - Group: 25
Template: Mau_Nop_Bao_Cao_Lab_Ca_Nhan_2026.docx
"""

import os
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def generate_report(template_path: str, output_path: str):
    doc = docx.Document(template_path)

    # 1. Format Header Metadata
    for p in doc.paragraphs:
        if "Lab:" in p.text:
            p.text = "Lab: 08\tTừ ngày: 29/10/2026\tđến ngày: 04/11/2026"
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(13)
        elif "MSSV:" in p.text:
            p.text = "MSSV: 2312694\tHọ và tên: Nguyễn Hoài Nam"
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(13)
        elif "Nhóm:" in p.text:
            p.text = "Nhóm: 25"
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(13)
        elif "BÁO CÁO LAB" in p.text:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(16)
                r.bold = True
        else:
            for r in p.runs:
                r.font.name = "Times New Roman"

    # 2. Build Structured Tasks (Categorized: Backend & Frontend)
    tasks = [
        # --- BACKEND SERVICES ---
        {
            "stt": "1",
            "name": "[Backend] Kiến trúc Clean Architecture, Khởi tạo ORM Entities & DbContext Configuration",
            "done": [
                "Thiết kế cấu trúc dự án backend tuân thủ nguyên lý Clean Architecture: Domain (models, exceptions, enums), Repositories (data access), Services (business logic & storage), Schemas (Pydantic DTOs), API v1 routers và Core infrastructure.",
                "Cài đặt hoàn chỉnh các ORM Entities với SQLAlchemy: User, Category, Recipe, RecipeStep, RecipeIngredient, RecipeImage, RefreshToken kèm ràng buộc khóa ngoại, quan hệ cascades và chỉ mục tìm kiếm.",
                "Cấu hình DbContext bất đồng bộ (AsyncSessionLocal) trên nền asyncpg và đồng bộ (psycopg2) kết nối PostgreSQL, tối ưu Connection Pooling cho xử lý đa luồng cao."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": "https://github.com/NHNam1209/PTUDW-2026-Nhom25/tree/main",
            "progress": "100%"
        },
        {
            "stt": "2",
            "name": "[Backend] Cơ chế Seeding Dữ Liệu Tự Động (Tối thiểu 20 Categories, 100 Recipes, >=10 Nguyên liệu, >=5 Bước nấu)",
            "done": [
                "Cài đặt script sinh dữ liệu mẫu quy chuẩn (backend/seed.py): Tự động đồng bộ cấu trúc bảng và khởi tạo tài khoản quản trị Admin (admin@culinaryblog.com) cùng Tác giả (namnh.tandt@gmail.com).",
                "Khởi tạo 22 danh mục ẩm thực phong phú (Món khai vị, Món chính, Món tráng miệng, Món chay, Món nướng, Món hấp, Món lẩu, Món xào, Món kho, Canh & Súp, Ẩm thực 3 miền, Eat Clean...).",
                "Sinh tự động 105+ công thức nấu ăn hoàn chỉnh: Mỗi công thức chứa tối thiểu 10-14 nguyên liệu (định lượng, đơn vị, ghi chú), tối thiểu 5-7 bước chế biến chi tiết kèm hẹn giờ nấu (Timer), đầy đủ thông số dinh dưỡng (Calories, Protein, Carbs, Fat, Fiber, Sodium) và gắn ảnh đại diện MinIO."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": "https://github.com/NHNam1209/PTUDW-2026-Nhom25/tree/main",
            "progress": "100%"
        },
        {
            "stt": "3",
            "name": "[Backend] Tầng Domain Exceptions, Triển khai Repository Pattern & Unit of Work",
            "done": [
                "Xây dựng tầng Domain Exceptions độc lập framework (app/domain/exceptions.py): EntityNotFoundException, InvalidRecipeStateException, RecipeConcurrencyException, AccountLockedException, TokenReuseDetectedException, DuplicateEmailException.",
                "Cài đặt Data Access Layer với Generic BaseRepository, RecipeRepository và UserRepository trừu tượng hóa thao tác truy vấn CSDL.",
                "Triển khai Unit of Work pattern (unit_of_work.py) quản lý phiên làm việc tập trung, bảo đảm tính toàn vẹn giao dịch ACID khi thực hiện ghi dữ liệu phức hợp."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": "https://github.com/NHNam1209/PTUDW-2026-Nhom25/tree/main",
            "progress": "100%"
        },
        {
            "stt": "4",
            "name": "[Backend] Middleware Xử Lý Ngoại Lệ Toàn Cục (RFC 7807), Rate Limiting & Structured Logging",
            "done": [
                "Xây dựng Middleware bắt lỗi tập trung (register_exception_handlers) chuẩn hóa phản hồi lỗi theo đặc tả quốc tế RFC 7807 Problem Details (application/problem+json) kèm Correlation ID.",
                "Cài đặt cơ chế kiểm soát tần suất truy cập Rate Limiting (sliding-window): Auth (10 req/phút), Upload (5 req/phút), General API (100 req/phút), trả về HTTP 429 và headers Retry-After.",
                "Thiết lập hệ thống Structured Logging tự động xoay vòng file (RotatingFileHandler 10MB x 5 backups): Tách bạch logs/app.log, logs/error.log và logs/audit.log; tích hợp ContextVar gắn correlation_id truy vết luồng xử lý; log HTTP request/response và cảnh báo truy vấn chậm (> 500ms)."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": "https://github.com/NHNam1209/PTUDW-2026-Nhom25/tree/main",
            "progress": "100%"
        },
        {
            "stt": "5",
            "name": "[Backend] Hệ Thống RESTful API Endpoints & Dịch Vụ Lưu Trữ Tệp MinIO S3",
            "done": [
                "Triển khai đầy đủ RESTful API endpoints phân hệ: Auth (JWT kép, Token Rotation, Google OAuth, Profile), Recipes (CRUD, phân trang, lọc đa tiêu chí, chuyển trạng thái vòng đời), Categories (CRUD và thống kê bài viết), Users (tra cứu, phân quyền Admin/Author, khóa tài khoản), Dashboard KPI và Health Probes.",
                "Cài đặt dịch vụ lưu trữ đám mây MinIO S3 Object Storage (app/services/storage.py): Tự động cấu hình bucket 'culinary-blog' quyền public-read, kiểm tra dung lượng tối đa 5MB, xác thực MIME type và Magic Bytes ngăn chặn file payload độc hại.",
                "Cung cấp các API upload ảnh: POST /recipes/{id}/images, POST /recipes/upload-image, PATCH /images/{id}/primary, DELETE /images/{id} đồng bộ file vật lý trên MinIO."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": "https://github.com/NHNam1209/PTUDW-2026-Nhom25/tree/main",
            "progress": "100%"
        },
        # --- FRONTEND CLIENT ---
        {
            "stt": "6",
            "name": "[Frontend] Xây dựng Màn hình Thêm mới/Cập nhật Công thức & Bộ Soạn Thảo Đa Bước (Wizard)",
            "done": [
                "Xây dựng giao diện biên tập công thức chuyên sâu (RecipeEditorPage.jsx) tích hợp StepEditor.jsx và IngredientEditor.jsx: Nhập tiêu đề, danh mục, độ khó, khẩu phần, thời gian chuẩn bị & nấu, bảng dinh dưỡng tiêu chuẩn.",
                "Bảng quản lý nguyên liệu động: Thêm, xóa, chỉnh sửa tên nguyên liệu, định lượng số học, đơn vị đo lường và ghi chú chuẩn bị.",
                "Bộ soạn thảo các bước nấu ăn tuần tự có tích hợp đồng hồ bấm giờ (Cooking Timer Minutes) hỗ trợ người nấu theo dõi trực tiếp.",
                "Áp dụng cơ chế kiểm soát xung đột ghi đè đồng thời (Optimistic Concurrency Control) thông qua trường rowVersion (UUID)."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": "https://github.com/NHNam1209/PTUDW-2026-Nhom25/tree/main",
            "progress": "100%"
        },
        {
            "stt": "7",
            "name": "[Frontend] Màn hình Quản Lý Công Thức & Vòng Đời Trạng Thái (Draft -> Publish -> Archived/Deleted)",
            "done": [
                "Xây dựng giao diện quản lý bài viết của tác giả và quản trị viên (RecipeManagementPage.jsx): Bảng danh sách công thức, phân trang, bộ lọc tab theo trạng thái món ăn.",
                "Quy trình chuyển đổi trạng thái vòng đời khép kín: Tạo nháp (Draft - 0) -> Xuất bản (Publish - 1) -> Hủy xuất bản về nháp -> Chuyển lưu trữ (Archived - 2) -> Xóa mềm công thức (Soft Delete) kèm modal hộp thoại xác nhận an toàn.",
                "Phân quyền truy cập tài nguyên (Resource-Based Authorization): Tác giả chỉ thao tác trên công thức cá nhân, Quản trị viên quản trị toàn bộ hệ thống."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": "https://github.com/NHNam1209/PTUDW-2026-Nhom25/tree/main",
            "progress": "100%"
        },
        {
            "stt": "8",
            "name": "[Frontend] Màn hình Xem & Quản Lý Danh Sách Người Dùng (Admin & Author User Management)",
            "done": [
                "Xây dựng trang xem và quản trị người dùng (UsersPage.jsx): Bảng trực quan hiển thị Avatar, họ tên, email, huy hiệu vai trò phân màu chuẩn (Admin: Đỏ, Tác giả: Cam, Thành viên: Xanh), số lượng công thức sở hữu, trạng thái hoạt động và ngày đăng ký.",
                "Bộ lọc tab theo vai trò (Tất cả, Quản trị viên, Tác giả, Thành viên), thanh tìm kiếm từ khóa tức thì tích hợp kỹ thuật debounce (400ms) giảm tải truy vấn server, thanh phân trang điều hướng linh hoạt.",
                "Tích hợp quyền quản trị Admin: Thao tác dropdown thay đổi vai trò trực tiếp (Admin/Author/User) và nút khóa/mở khóa tài khoản tức thời có hiển thị thông báo kết quả (Toast notification).",
                "Đăng ký định tuyến /users trong App.jsx và tích hợp menu điều hướng trên Navbar.jsx."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": "https://github.com/NHNam1209/PTUDW-2026-Nhom25/tree/main",
            "progress": "100%"
        },
        {
            "stt": "9",
            "name": "[Frontend] Component Tải Ảnh MinIO & Tối Ưu Hóa SEO (JSON-LD Recipe Schema & Open Graph)",
            "done": [
                "Xây dựng ImageUploader.jsx: Hỗ trợ kéo-thả hoặc chọn tệp tải lên, xem trước hình ảnh (Preview), hiển thị tiến trình upload lên MinIO S3, gán huy hiệu 'Ảnh chính' và nút xóa ảnh.",
                "Tích hợp siêu dữ liệu cấu trúc Schema.org Recipe (useRecipeSeo.js & seo.js): Chuẩn hóa JSON-LD đầy đủ tên món, mô tả, ảnh, thời gian nấu, khẩu phần, danh sách nguyên liệu, các bước HowToStep và bảng dinh dưỡng.",
                "Bổ sung thẻ Meta Open Graph và Twitter Card động cho phép chia sẻ mạng xã hội trực quan, vượt qua kiểm tra Google Rich Results Test."
            ],
            "undone": "Không có (Đã hoàn thành 100%).",
            "link": "https://github.com/NHNam1209/PTUDW-2026-Nhom25/tree/main",
            "progress": "100%"
        }
    ]

    # 3. Populate Document Table
    table = doc.tables[0]

    # Adjust row count to match tasks + header
    while len(table.rows) > len(tasks) + 1:
        p_elm = table.rows[-1]._tr.getparent()
        p_elm.remove(table.rows[-1]._tr)

    while len(table.rows) < len(tasks) + 1:
        table.add_row()

    # Fill content into table rows
    for idx, task in enumerate(tasks):
        row = table.rows[idx + 1]

        # Cell 0: STT
        cell0 = row.cells[0]
        cell0.text = task["stt"]
        cell0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in cell0.paragraphs[0].runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(12)

        # Cell 1: Công việc được giao (Đã hoàn thành & Chưa hoàn thành)
        cell1 = row.cells[1]
        cell1.text = ""
        p_title = cell1.paragraphs[0]
        r_title = p_title.add_run(task["name"])
        r_title.bold = True
        r_title.font.name = "Times New Roman"
        r_title.font.size = Pt(12)

        p_done_label = cell1.add_paragraph()
        r_done_label = p_done_label.add_run("Đã hoàn thành:")
        r_done_label.bold = True
        r_done_label.font.name = "Times New Roman"
        r_done_label.font.size = Pt(12)

        for d in task["done"]:
            p_bullet = cell1.add_paragraph()
            r_bullet = p_bullet.add_run(f"• {d}")
            r_bullet.font.name = "Times New Roman"
            r_bullet.font.size = Pt(11.5)

        p_undone = cell1.add_paragraph()
        r_undone_label = p_undone.add_run("Chưa hoàn thành: ")
        r_undone_label.bold = True
        r_undone_label.font.name = "Times New Roman"
        r_undone_label.font.size = Pt(12)
        r_undone_val = p_undone.add_run(task["undone"])
        r_undone_val.font.name = "Times New Roman"
        r_undone_val.font.size = Pt(11.5)

        # Cell 2: Liên kết GitHub
        cell2 = row.cells[2]
        cell2.text = task["link"]
        cell2.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        for r in cell2.paragraphs[0].runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(11)
            r.font.color.rgb = RGBColor(0, 102, 204)
            r.underline = True

        # Cell 3: Tiến độ %
        cell3 = row.cells[3]
        cell3.text = task["progress"]
        cell3.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in cell3.paragraphs[0].runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(12)
            r.bold = True

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)
    print(f"Generated report successfully: {output_path}")


if __name__ == "__main__":
    template = "d:/PTUDWNC/Mau_Nop_Bao_Cao_Lab_Ca_Nhan_2026.docx"
    output_root = "d:/PTUDWNC/Lab8_2312694_NguyenHoaiNam.docx"
    output_repo = "d:/PTUDWNC/PTUDW-2026-Nhom25/Lab8_2312694_NguyenHoaiNam.docx"

    generate_report(template, output_root)
    generate_report(template, output_repo)

