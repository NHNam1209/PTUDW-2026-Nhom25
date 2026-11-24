# KỊCH BẢN THUYẾT TRÌNH BÁO CÁO CÁ NHÂN (6 - 7 PHÚT)
## SINH VIÊN: NGUYỄN HOÀI NAM (TRƯỞNG NHÓM 25)
**Môn học:** Phát triển Ứng dụng Web Nâng cao (PTUDWNC)  
**Giảng viên hướng dẫn:** TS. Nguyễn Thị Lương  
**Phạm vi:** 19 Chức năng (SETUP, DEVOPS, FR-AUTH-001 -> 007, FR-RCP-001 -> 010, FR-OBS-001)  
**Thời lượng chuẩn:** 6 phút 30 giây (khoảng 380 - 410 giây)  
**Tệp Slide trình chiếu đi kèm:** `Slide_Bao_Cao_Ca_Nhan_Nguyen_Hoai_Nam.pptx`

---

### SLIDE 1: MỞ ĐẦU & GIỚI THIỆU PHẦN BÁO CÁO CÁ NHÂN (Thời gian: 30 giây)
> *"Kính thưa Cô và các bạn! Em tên là **Nguyễn Hoài Nam**, Trưởng nhóm 25. "  
> "Trong buổi bảo vệ đồ án hôm nay, theo đúng phân công 'ai làm gì sẽ báo cáo phần đó', em xin phép trình bày chi tiết phần công việc mà bản thân em trực tiếp thiết kế, cài đặt và phụ trách trong dự án Culinary Blog. "  
> "Phần việc của em bao gồm: Thiết kế kiến trúc hệ thống, xây dựng hạ tầng DevOps & Docker, toàn bộ Module Xác thực và Bảo mật tài khoản, Module Quản lý Công thức cốt lõi, cơ chế kiểm soát Concurrency và hệ thống Health Check Probes chuẩn Cloud-Native."*

---

### SLIDE 2: TỔNG HỢP 19 ĐẦU VIỆC ĐÃ HOÀN THÀNH (Thời gian: 35 giây)
> *"Về khối lượng công việc thực tế, em trực tiếp đảm nhiệm và đã hoàn thành 100% tất cả **19 đầu việc** theo tài liệu đặc tả SRS v1.0.0: "  
> "- Thứ nhất là gói **Hạ tầng DevOps**: Khởi tạo cấu trúc dự án, Docker Compose 6 dịch vụ và Nginx reverse proxy. "  
> "- Thứ hai là trọn bộ **7 chức năng Xác thực nâng cao** từ `FR-AUTH-001` đến `007`: Đăng ký, Đăng nhập với cơ chế khóa tài khoản, Google OAuth 2.0, Token Rotation và quản lý hồ sơ tác giả. "  
> "- Thứ ba là trọn bộ **10 chức năng Quản lý công thức cốt lõi** từ `FR-RCP-001` đến `010`: Vòng đời công thức, kiểm soát xung đột bằng `row_version`, phân trang và quản lý nguyên liệu, các bước nấu. "  
> "- Thứ tư là gói **Giám sát hệ thống** `FR-OBS-001` với bộ 3 endpoint health checks."*

---

### SLIDE 3: HẠ TẦNG DEVOPS & ĐIỀU PHỐI DOCKER COMPOSE (Thời gian: 45 giây)
> *"Bắt đầu với phần Hạ tầng DevOps: Em đã xây dựng giải pháp container hóa hoàn chỉnh qua **Docker Compose** gồm 6 dịch vụ độc lập: "  
> "- Ở tầng biên, **Nginx** lắng nghe cổng 80, giải quyết triệt để bài toán định tuyến Reverse Proxy và xử lý CORS: các request `/api/v1` được chuyển mượt mà về Backend, các request còn lại về Frontend. "  
> "- Backend chạy **FastAPI Python 3.12** theo chuẩn Clean Architecture, giao tiếp bất đồng bộ qua SQLAlchemy Async và `asyncpg` với CSDL **PostgreSQL 16**. "  
> "- Hệ thống có **Redis 7** quản lý token blacklist và rate limiting, **MinIO** lưu trữ tệp ảnh S3 và **MailHog** làm SMTP ảo bắt trọn email chào mừng gửi từ background job."*

---

### SLIDE 4: MODULE XÁC THỰC & REFRESH TOKEN ROTATION (Thời gian: 50 giây)
> *"Điểm sáng đầu tiên trong phần code của em là Module Xác thực bảo mật đa lớp: "  
> "- Mật khẩu người dùng được băm bằng thuật toán **Bcrypt** kèm salt ngẫu nhiên. Trong hàm `login()`, em cài đặt thuật toán theo dõi `access_failed_count`; nếu nhập sai 5 lần liên tiếp, hệ thống kích hoạt `lockout_end` tự động khóa tài khoản trong 15 phút để chống dò pass Brute-force. "  
> "- Đặc biệt, em hiện thực cơ chế **Refresh Token Rotation** theo chuẩn RFC 6819: Access Token chỉ có hạn ngắn 15 phút, mỗi lần lấy Access Token mới thì Refresh Token cũ bị đánh dấu thu hồi (revoked) ngay lập tức. "  
> "- Nếu kẻ tấn công đánh cắp được token cũ và gửi lên, hệ thống sẽ phát hiện hành vi **Token Reuse Attack** và tự động vô hiệu hóa toàn bộ token của tài khoản đó, buộc đăng nhập lại để bảo vệ phiên. Em cũng đã tích hợp đăng nhập nhanh qua Google OAuth 2.0."*

---

### SLIDE 5: MODULE CÔNG THỨC & TỐI ƯU HÓA TRUY VẤN ORM (Thời gian: 45 giây)
> *"Chuyển sang Module Recipe Core: Em chịu trách nhiệm thiết kế toàn bộ vòng đời của công thức từ Draft, Publish tới Archive: "  
> "- Khi tác giả bấm xuất bản, hàm `publish_recipe()` của em kiểm tra ràng buộc nghiêm ngặt: công thức bắt buộc phải có tối thiểu 1 bước và 1 nguyên liệu thì mới được xuất bản. "  
> "- Các bước nấu khi thêm, sửa hoặc xóa được tự động đánh số lại liên tục (renumbering). "  
> "- Đặc biệt, về mặt hiệu năng CSDL, khi query danh sách công thức, em sử dụng kỹ thuật `selectinload()` của SQLAlchemy thay vì `joinedload`. Giải pháp này triệt tiêu hoàn toàn lỗi **Cartesian Explosion** (bùng nổ tích Descartes) khi nạp nhiều collection quan hệ (ảnh, nguyên liệu, bước nấu), giúp giảm lượng dữ liệu truyền qua network từ 150 dòng xuống còn 26 dòng, tăng tốc độ phản hồi đáng kể."*

---

### SLIDE 6: OPTIMISTIC CONCURRENCY & XỬ LÝ MÂU THUẪN SRS (Thời gian: 50 giây)
> *"Về mặt kỹ thuật chuyên sâu, em đầu tư giải quyết 2 bài toán lớn: "  
> "- Thứ nhất là cơ chế **Optimistic Concurrency Control** thông qua cột `row_version`: Khi 2 người cùng sửa một công thức, hàm `update_recipe()` đối chiếu `row_version` từ client gửi lên; nếu phiên bản bị cũ, API lập tức từ chối và trả về lỗi **HTTP 409 Conflict** để chống lỗi Lost Update (ghi đè dữ liệu của nhau). "  
> "- Thứ hai, em đã phát hiện và xử lý mâu thuẫn lớn trong file SRS giữa việc **Soft Delete** (`is_deleted = True`) và **Ràng buộc duy nhất trên Slug**: Khi xóa mềm thì bài cũ vẫn còn trong database, nếu tác giả tạo bài mới cùng tiêu đề sẽ bị lỗi trùng slug. Em đã giải quyết bằng cách cấu hình **Partial Unique Index** trong PostgreSQL chỉ áp dụng ràng buộc duy nhất trên các bài chưa bị xóa mềm (`WHERE is_deleted = false`), bảo toàn 100% dữ liệu lịch sử mà không gây lỗi toàn vẹn."*

---

### SLIDE 7: RESOURCE-BASED AUTHORIZATION & DTO PATTERN (Thời gian: 40 giây)
> *"Về kiểm soát truy cập và chuẩn hóa dữ liệu: "  
> "- Em cài đặt hàm `_check_recipe_ownership()` thực hiện **Resource-based authorization**: Người dùng dù đã đăng nhập hợp lệ nhưng nếu không phải tác giả sở hữu công thức đó và không phải Admin thì tuyệt đối không thể sửa hoặc xóa bài của người khác, trả về lỗi **HTTP 403 Forbidden**. "  
> "- Toàn bộ dữ liệu vào ra API đều được em đóng gói qua hệ thống DTO Pydantic v2: Entity `User` chứa các thông tin nhạy cảm như `password_hash`, `lockout_end` được giấu kín hoàn toàn; chỉ trả về `UserProfileDto`. Kỹ thuật này cũng ngăn chặn triệt để tấn công Mass Assignment và tránh lỗi lặp tuần hoàn khi serialize JSON."*

---

### SLIDE 8: GIÁM SÁT SỨC KHỎE HỆ THỐNG: HEALTH CHECK PROBES (Thời gian: 45 giây)
> *"Đối với yêu cầu giám sát hệ thống theo mã `FR-OBS-001`, em đã thiết kế riêng biệt 3 endpoints chuẩn Cloud-Native: "  
> "- Endpoint `/health/live` đóng vai trò **Liveness probe**, chỉ kiểm tra tiến trình Python FastAPI có còn sống hay không để Docker/Kubernetes biết có cần restart hay không. "  
> "- Endpoint `/health/ready` đóng vai trò **Readiness probe**, kiểm tra trực tiếp kết nối tới CSDL PostgreSQL và Redis. Nếu database bị nghẽn, endpoint này trả về 503 để load balancer tạm ngưng điều phối traffic đến nhưng KHÔNG restart container. "  
> "- Việc tách bạch đúng 2 probe này giúp hệ thống của em tránh được hiện tượng **CrashLoopBackOff** và cơn bão kết nối (Thundering Herd) khi CSDL bị chậm tạm thời."*

---

### SLIDE 9: MINH CHỨNG TRIỂN KHAI & KIỂM THỬ TỰ ĐỘNG (Thời gian: 40 giây)
> *"Để chứng minh kết quả cài đặt thực tế: "  
> "- Toàn bộ 19 endpoints em xây dựng đều được tích hợp tài liệu hóa Swagger UI tự động tại đường dẫn `/docs` với đầy đủ schema và mã lỗi chuẩn hóa. "  
> "- Em đã thiết lập bộ test tự động Pytest trong `tests/test_auth_unit.py` và `test_health.py` kiểm tra độ phức tạp mật khẩu, cơ chế token expiration và tính đúng đắn của các probes. "  
> "- Kịch bản `seed.py` do em viết cũng nạp sẵn 41 món ăn mẫu và tài khoản thử nghiệm giúp hệ thống sẵn sàng hoạt động ngay sau khi khởi chạy."*

---

### SLIDE 10: TỔNG KẾT & SẴN SÀNG TRẢ LỜI PHẢN BIỆN (Thời gian: 20 giây)
> *"Tóm lại, em đã hoàn thành 100% tất cả 19 đầu việc được giao từ DevOps, Auth, Recipe Core đến Health Checks, đảm bảo đúng chuẩn SRS, bảo mật cao và tối ưu hiệu năng CSDL. "  
> "Em xin chân thành cảm ơn Cô đã chú ý lắng nghe phần báo cáo cá nhân của em. "  
> "Bây giờ em đã sẵn sàng giải thích chi tiết bất kỳ đoạn code nào hoặc trả lời các câu hỏi phản biện từ Cô!"*
