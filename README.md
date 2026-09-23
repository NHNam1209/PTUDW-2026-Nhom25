# 🍳 CULINARY BLOG – DỰ ÁN BLOG ẨM THỰC VÀ NẤU ĂN (NHÓM 25)

> Hệ thống ứng dụng web chia sẻ, khám phá và quản lý công thức ẩm thực theo chuẩn đặc tả phần mềm **IEEE 830 / ISO/IEC/IEEE 29148:2018 (SRS v1.0.0)**.

---

## 👥 THÀNH VIÊN NHÓM VÀ PHÂN CÔNG VAI TRÒ

| STT | MSSV | Họ và tên | Email | GitHub | Vai trò |
|:---:|:---:|:---|:---|:---|:---|
| **1** | **2312607** | **Nguyễn Hoài Nam (Trưởng nhóm)** | **namnh.tandt@gmail.com** | [NHNam1209](https://github.com/NHNam1209) | **Team Lead, Backend Core, Auth & Recipe Modules, DevOps & Docker** |
| 2 | 2312584 | Đỗ Duy Biên | 2312584@dlu.edu.vn | [2312584](https://github.com/2312584) | Backend Categories, Search FTS, Storage & Background Jobs |
| 3 | 2312676 | Hoàng Thăng Long | 2312676@gmail.com | [2312676-sys](https://github.com/2312676-sys) | Frontend Public Web, Recipe Catalog, SEO & Auth UI |
| 4 | 2212437 | Trần Chánh Phát | 2212437@dlu.edu.vn | [2212437](https://github.com/2212437) | Frontend Creator Dashboard, Recipe Editor & Admin Management |

---

## 🛠️ KIẾN TRÚC VÀ CÔNG NGHỆ

- **Backend:** Python 3.12, FastAPI, SQLAlchemy 2.0 (Async/Sync), Alembic, Pydantic v2
- **Frontend:** React 19 / Vite, React Router, Axios, Zustand State Management, Tailwind CSS
- **Cơ sở dữ liệu:** PostgreSQL 16 (Full-Text Search với `unaccent` và `pg_trgm`)
- **Cache & Message Broker:** Redis 7 Alpine
- **Object Storage (File Upload):** MinIO (S3-Compatible Storage)
- **Reverse Proxy & Web Server:** Nginx Alpine
- **Đóng gói & Điều phối:** Docker & Docker Compose

---

## 🌿 QUY TẮC PHÂN NHÁNH GITHUB (BRANCH STRATEGY)

Tất cả các nhánh chức năng được đặt tên chính xác theo format đặc tả SRS:
```
<Mã_FR>/<Tên chức năng bằng tiếng Anh>
```
Ví dụ: `FR-AUTH-001/User Registration`, `FR-RCP-001/Recipe Listing`, `FR-CAT-001/Category Listing`.

### 1. Nhánh cố định (Core Branches)
- `main`: Nhánh production ổn định cao nhất, chỉ merge qua Pull Request được review.
- `develop`: Nhánh tích hợp chính dành cho toàn đội dự án.

### 2. Danh sách phân nhánh chi tiết theo thành viên

#### 👤 Nguyễn Hoài Nam (Lead)
| Mã Đặc Tả | Tên Nhánh Git | Nội dung & Chức năng |
|---|---|---|
| `DEVOPS` | `setup/project-infrastructure` | Khởi tạo cấu trúc dự án, Dockerfile, Docker Compose, Nginx, Database Seeding |
| `FR-AUTH-001` | `FR-AUTH-001/User Registration` | Đăng ký tài khoản mới, mã hóa PBKDF2/Bcrypt, role "Author" mặc định |
| `FR-AUTH-002` | `FR-AUTH-002/Email Password Login` | Đăng nhập local, chống brute-force lockout, cấp Access & Refresh Token |
| `FR-AUTH-003` | `FR-AUTH-003/Google OAuth2 Login` | Đăng nhập / đăng ký qua Google OAuth 2.0 Identity Provider |
| `FR-AUTH-004` | `FR-AUTH-004/Token Refresh Rotation` | Token Rotation, kiểm soát Reuse Attack Detection, cấp cặp token mới |
| `FR-AUTH-005` | `FR-AUTH-005/User Logout` | Thu hồi refresh token, kết thúc phiên đăng nhập |
| `FR-AUTH-006` | `FR-AUTH-006/View User Profile` | Endpoint GET /auth/me xem hồ sơ cá nhân |
| `FR-AUTH-007` | `FR-AUTH-007/Update User Profile` | Endpoint PATCH /auth/me cập nhật display name, avatar, bio |
| `FR-RCP-001` | `FR-RCP-001/Recipe Listing Pagination` | Danh sách công thức phân trang, lọc theo danh mục/độ khó, sắp xếp linh hoạt |
| `FR-RCP-002` | `FR-RCP-002/Recipe Detail View` | Chi tiết công thức kèm steps, ingredients, nutrition, images |
| `FR-RCP-003` | `FR-RCP-003/Create Recipe Draft` | Tạo công thức mới trạng thái Draft, sinh SEO slug tự động |
| `FR-RCP-004` | `FR-RCP-004/Update Recipe Concurrency` | Cập nhật công thức, Resource-Based Auth & Optimistic Concurrency |
| `FR-RCP-005` | `FR-RCP-005/Publish Unpublish Recipe` | Xuất bản / Hủy xuất bản (yêu cầu tối thiểu 1 bước và 1 nguyên liệu) |
| `FR-RCP-006` | `FR-RCP-006/Archive Recipe` | Chuyển công thức sang trạng thái lưu trữ Archived |
| `FR-RCP-007` | `FR-RCP-007/Delete Recipe Cascade` | Xóa công thức vĩnh viễn, dọn dẹp các tệp ảnh trên MinIO |
| `FR-RCP-008` | `FR-RCP-008/Recipe Image Management` | Upload ảnh (kiểm tra MIME, magic bytes, 5MB), đặt ảnh chính, xóa ảnh |
| `FR-RCP-009` | `FR-RCP-009/Recipe Ingredients CRUD` | Thêm, sửa, xóa nguyên liệu của công thức |
| `FR-RCP-010` | `FR-RCP-010/Recipe Steps CRUD` | Thêm, sửa, xóa và tự động đánh số lại (renumber) các bước thực hiện |
| `FR-OBS-001` | `FR-OBS-001/Health Check Probes` | Bộ probe /health, /health/live, /health/ready |

#### 👤 Đỗ Duy Biên
| Mã Đặc Tả | Tên Nhánh Git | Nội dung & Chức năng |
|---|---|---|
| `FR-CAT-001` | `FR-CAT-001/Category Listing` | API danh sách danh mục kèm thống kê số lượng recipe |
| `FR-CAT-002` | `FR-CAT-002/Category Detail Recipes` | Chi tiết danh mục và danh sách công thức thuộc danh mục |
| `FR-CAT-003` | `FR-CAT-003/Admin Create Category` | Tạo danh mục mới dành cho Admin, tự động sinh slug tiếng Việt |
| `FR-CAT-004` | `FR-CAT-004/Admin Update Category` | Cập nhật thông tin danh mục |
| `FR-CAT-005` | `FR-CAT-005/Admin Delete Category` | Xóa danh mục (ràng buộc không xóa khi đang có recipes) |
| `FR-SRCH-001`| `FR-SRCH-001/Full Text Search` | Tìm kiếm toàn văn bản tiếng Việt với `tsvector`, `tsquery` & `unaccent` |
| `FR-SRCH-002`| `FR-SRCH-002/Filter And Sorting` | Bộ lọc kết hợp đa tiêu chí (độ khó, thời gian, khẩu phần) |
| `FR-FILE-001`| `FR-FILE-001/MinIO Storage Service` | Module giao tiếp MinIO S3 Object Storage |
| `FR-JOB-001` | `FR-JOB-001/Welcome Email Job` | Background job gửi email chào mừng người dùng mới |
| `FR-JOB-002` | `FR-JOB-002/Image Resize Thumbnail` | Tự động tạo ảnh thumbnail và ảnh vừa |
| `FR-JOB-003` | `FR-JOB-003/Sitemap XML Generation` | Job định kỳ tạo `sitemap.xml` phục vụ SEO |
| `FR-OBS-002` | `FR-OBS-002/Structured Logging` | Cấu hình structured log với Correlation-ID và log request |

#### 👤 Hoàng Thăng Long
| Mã Đặc Tả | Tên Nhánh Git | Nội dung & Chức năng |
|---|---|---|
| `FR-UI-001` | `FR-UI-001/Public Home Page` | Giao diện Trang chủ: banner, danh mục nổi bật, recipes mới nhất |
| `FR-UI-002` | `FR-UI-002/Recipe Catalog Page` | Giao diện duyệt danh sách công thức, phân trang, lọc theo tiêu chí |
| `FR-UI-003` | `FR-UI-003/Recipe Detail View` | Giao diện chi tiết món ăn: nguyên liệu, hướng dẫn từng bước, dinh dưỡng |
| `FR-UI-004` | `FR-UI-004/Category Pages` | Trang xem công thức theo từng danh mục cụ thể |
| `FR-UI-005` | `FR-UI-005/Search Results Page` | Giao diện tìm kiếm trực quan có gợi ý và highlight từ khóa |
| `FR-AUTH-UI-001` | `FR-AUTH-UI-001/Login Page` | Form đăng nhập (Email/Password & Đăng nhập bằng Google) |
| `FR-AUTH-UI-002` | `FR-AUTH-UI-002/Register Page` | Form đăng ký tài khoản với validation độ mạnh mật khẩu realtime |
| `FR-AUTH-UI-003` | `FR-AUTH-UI-003/User Profile Page` | Trang xem và cập nhật thông tin tác giả cá nhân |

#### 👤 Trần Chánh Phát
| Mã Đặc Tả | Tên Nhánh Git | Nội dung & Chức năng |
|---|---|---|
| `FR-DASH-001`| `FR-DASH-001/Creator Dashboard Overview` | Màn hình bảng điều khiển tác giả, thống kê công thức |
| `FR-DASH-002`| `FR-DASH-002/Recipe Management Table` | Bảng quản lý recipes cá nhân: trạng thái Draft/Published/Archived |
| `FR-DASH-003`| `FR-DASH-003/Recipe Creation Wizard` | Form tạo mới & cập nhật công thức đa bước (Multi-step Form) |
| `FR-DASH-004`| `FR-DASH-004/Step And Ingredient Editor`| Bộ công cụ thêm/sửa/xóa nguyên liệu và các bước thực hiện kéo thả |
| `FR-DASH-005`| `FR-DASH-005/Image Uploader Component` | Component tải ảnh lên MinIO có preview, đặt ảnh bìa và thanh tiến trình |
| `FR-ADMIN-001`| `FR-ADMIN-001/Admin Category Management` | Màn hình quản lý danh mục dành cho Admin (CRUD modal) |
| `FR-SEO-001` | `FR-SEO-001/JSON-LD Recipe Schema` | Nhúng dữ liệu có cấu trúc Schema.org Recipe và thẻ Open Graph |

---

## 📋 DANH SÁCH ISSUES CÔNG VIỆC DỰ ÁN

| Issue ID | Mã SRS | Tên công việc | Người phụ trách | Phạm vi | Trạng thái |
|:---:|:---:|:---|:---:|:---:|:---:|
| **#1** | `SETUP` | Khởi tạo khung dự án, Docker Compose, Nginx, DB init | **Nguyễn Hoài Nam** | DevOps | ✅ Hoàn thành |
| **#2** | `FR-AUTH-001` | Xây dựng API Đăng ký tài khoản (User Registration) | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#3** | `FR-AUTH-002` | Xây dựng API Đăng nhập Email/Password & Lockout | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#4** | `FR-AUTH-003` | Tích hợp xác thực Google OAuth 2.0 | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#5** | `FR-AUTH-004` | Xây dựng cơ chế Token Refresh & Token Rotation | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#6** | `FR-AUTH-005` | Xây dựng API Đăng xuất (Token Revocation) | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#7** | `FR-AUTH-006` | Xây dựng API Xem thông tin tài khoản hiện tại | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#8** | `FR-AUTH-007` | Xây dựng API Cập nhật hồ sơ tác giả | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#9** | `FR-RCP-001` | Xây dựng API Danh sách công thức (Phân trang, Lọc, Sắp xếp) | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#10** | `FR-RCP-002` | Xây dựng API Chi tiết công thức nấu ăn | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#11** | `FR-RCP-003` | Xây dựng API Tạo công thức nấu ăn mới (Draft) | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#12** | `FR-RCP-004` | Xây dựng API Cập nhật công thức & Optimistic Concurrency | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#13** | `FR-RCP-005` | Xây dựng API Xuất bản / Hủy xuất bản công thức | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#14** | `FR-RCP-006` | Xây dựng API Lưu trữ công thức (Archive) | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#15** | `FR-RCP-007` | Xây dựng API Xóa vĩnh viễn công thức & tệp ảnh | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#16** | `FR-RCP-008` | Xây dựng API Quản lý ảnh (Upload MinIO, Set Primary, Delete) | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#17** | `FR-RCP-009` | Xây dựng API Quản lý nguyên liệu (CRUD) | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#18** | `FR-RCP-010` | Xây dựng API Quản lý các bước nấu (CRUD & Renumbering) | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#19** | `FR-OBS-001` | Xây dựng Health Check Endpoints (/health, /live, /ready) | **Nguyễn Hoài Nam** | Backend | ✅ Hoàn thành |
| **#20** | `FR-CAT-001` | API Lấy danh sách danh mục kèm số lượng recipe | Đỗ Duy Biên | Backend | 🔄 Đang triển khai |
| **#21** | `FR-CAT-002` | API Lấy chi tiết danh mục và recipes liên quan | Đỗ Duy Biên | Backend | 🔄 Đang triển khai |
| **#22** | `FR-CAT-003` | API Tạo mới danh mục (Admin) | Đỗ Duy Biên | Backend | 🔄 Đang triển khai |
| **#23** | `FR-CAT-004` | API Cập nhật danh mục (Admin) | Đỗ Duy Biên | Backend | 🔄 Đang triển khai |
| **#24** | `FR-CAT-005` | API Xóa danh mục và ràng buộc toàn vẹn | Đỗ Duy Biên | Backend | 🔄 Đang triển khai |
| **#25** | `FR-SRCH-001`| Tích hợp Full-Text Search PostgreSQL (tsvector/unaccent) | Đỗ Duy Biên | Backend | 🔄 Đang triển khai |
| **#26** | `FR-FILE-001`| Xây dựng dịch vụ lưu trữ đối tượng MinIO S3 SDK | Đỗ Duy Biên | Backend | 🔄 Đang triển khai |
| **#27** | `FR-JOB-001` | Xây dựng Background Job gửi email chào mừng | Đỗ Duy Biên | Backend | 🔄 Đang triển khai |
| **#28** | `FR-JOB-002` | Xây dựng Background Job resize ảnh thumbnails | Đỗ Duy Biên | Backend | 🔄 Đang triển khai |
| **#29** | `FR-JOB-003` | Xây dựng Cron Job tạo `sitemap.xml` tự động | Đỗ Duy Biên | Backend | 🔄 Đang triển khai |
| **#30** | `FR-OBS-002` | Cấu hình Structured Logging & Correlation-ID | Đỗ Duy Biên | Backend | 🔄 Đang triển khai |
| **#31** | `FR-UI-001` | Xây dựng Trang chủ (Home Page) | Hoàng Thăng Long | Frontend | 🔄 Đang triển khai |
| **#32** | `FR-UI-002` | Xây dựng Trang danh sách công thức kèm bộ lọc & phân trang | Hoàng Thăng Long | Frontend | 🔄 Đang triển khai |
| **#33** | `FR-UI-003` | Xây dựng Trang chi tiết công thức nấu ăn | Hoàng Thăng Long | Frontend | 🔄 Đang triển khai |
| **#34** | `FR-UI-004` | Xây dựng Trang danh mục món ăn | Hoàng Thăng Long | Frontend | 🔄 Đang triển khai |
| **#35** | `FR-UI-005` | Xây dựng Trang kết quả tìm kiếm | Hoàng Thăng Long | Frontend | 🔄 Đang triển khai |
| **#36** | `FR-AUTH-UI-001` | Giao diện Đăng nhập & nút đăng nhập Google | Hoàng Thăng Long | Frontend | 🔄 Đang triển khai |
| **#37** | `FR-AUTH-UI-002` | Giao diện Đăng ký tài khoản mới | Hoàng Thăng Long | Frontend | 🔄 Đang triển khai |
| **#38** | `FR-AUTH-UI-003` | Giao diện Trang hồ sơ cá nhân tác giả | Hoàng Thăng Long | Frontend | 🔄 Đang triển khai |
| **#39** | `FR-DASH-001`| Xây dựng Bảng điều khiển tác giả (Dashboard Overview) | Trần Chánh Phát | Frontend | 🔄 Đang triển khai |
| **#40** | `FR-DASH-002`| Xây dựng Màn hình quản lý danh sách công thức cá nhân | Trần Chánh Phát | Frontend | 🔄 Đang triển khai |
| **#41** | `FR-DASH-003`| Xây dựng Form tạo & chỉnh sửa công thức nấu ăn | Trần Chánh Phát | Frontend | 🔄 Đang triển khai |
| **#42** | `FR-DASH-004`| Xây dựng Bộ nhập danh sách nguyên liệu và các bước làm | Trần Chánh Phát | Frontend | 🔄 Đang triển khai |
| **#43** | `FR-DASH-005`| Xây dựng Component upload hình ảnh lên MinIO | Trần Chánh Phát | Frontend | 🔄 Đang triển khai |
| **#44** | `FR-ADMIN-001`| Xây dựng Giao diện quản lý danh mục (Dành cho Admin) | Trần Chánh Phát | Frontend | 🔄 Đang triển khai |
| **#45** | `FR-SEO-001` | Tối ưu SEO với Schema.org Recipe Structured Data & OG | Trần Chánh Phát | Frontend | 🔄 Đang triển khai |

---

## 🚀 HƯỚNG DẪN CÀI ĐẶT VÀ KHỞI CHẠY (DOCKER)

### 1. Yêu cầu tiên quyết
- Cài đặt **Docker** và **Docker Compose**.
- Đã cài đặt **Git**.

### 2. Khởi chạy toàn bộ hệ thống bằng 1 lệnh
```bash
# Clone repository
git clone https://github.com/NHNam1209/PTUDW-2026-Nhom25.git
cd PTUDW-2026-Nhom25

# Khởi chạy Docker Compose
docker compose up -d --build
```

### 3. Cổng truy cập các dịch vụ
| Dịch vụ | URL | Ghi chú |
|---|---|---|
| **Cổng vào chính (Nginx)** | `http://localhost` | Điều hướng frontend & API |
| **Frontend Web (React)** | `http://localhost:3000` | Trực tiếp giao diện người dùng |
| **Backend API (FastAPI)** | `http://localhost:8000` | REST API Server |
| **Tài liệu Swagger UI** | `http://localhost:8000/docs` | Thử nghiệm các endpoints trực tiếp |
| **Tài liệu ReDoc** | `http://localhost:8000/redoc` | Tài liệu API tiêu chuẩn |
| **MinIO Console** | `http://localhost:9001` | Quản trị Object Storage (`minioadmin` / `minioadminpassword`) |
| **MailHog Web UI** | `http://localhost:8025` | Hộp thư test email local |

### 4. Nạp dữ liệu mẫu ban đầu (Database Seeding)
```bash
docker compose exec api python seed.py
```
Tài khoản thử nghiệm được nạp sẵn:
- **Admin:** `admin@culinaryblog.com` / `Admin@123456`
- **Tác giả (Author):** `namnh.tandt@gmail.com` / `Nam@123456`

---

## 🧪 KIỂM THỬ TỰ ĐỘNG (AUTOMATED TESTING)

Chạy bộ kiểm thử unit test & integration test của phần Backend:
```bash
cd backend
python -m pytest tests/ -v
```