# KỊCH BẢN THUYẾT TRÌNH BÁO CÁO ĐỒ ÁN (6 - 7 PHÚT)
## ĐỒ ÁN: HỆ THỐNG CULINARY BLOG — NHÓM 25
**Môn học:** Phát triển Ứng dụng Web Nâng cao (PTUDWNC)  
**Giảng viên hướng dẫn:** TS. Nguyễn Thị Lương  
**Thời lượng chuẩn:** 6 phút 30 giây (khoảng 380 - 410 giây)  
**Tốc độ nói:** Vừa phải, tự tin, nhấn mạnh từ khóa kỹ thuật.

---

### SLIDE 1: MỞ ĐẦU & GIỚI THIỆU NHÓM (Thời gian: 30 giây)
> *"Kính chào Cô và các bạn! Em xin đại diện cho Nhóm 25 trình bày báo cáo đồ án môn Phát triển ứng dụng web nâng cao với đề tài: **'Hệ thống Culinary Blog - Nền tảng Chia sẻ và Quản lý Công thức Ẩm thực'**.*  
> *Đồ án được thực hiện bởi 4 thành viên gồm bạn Nguyễn Hoài Nam làm Trưởng nhóm, bạn Đỗ Duy Biên, bạn Hoàng Thăng Long và bạn Trần Chánh Phát.*  
> *Hệ thống được xây dựng bám sát theo chuẩn đặc tả phần mềm IEEE 830, ứng dụng các công nghệ hiện đại như FastAPI, React 19, PostgreSQL Full-Text Search, Redis, MinIO S3 và đóng gói bằng Docker."*

---

### SLIDE 2: MỤC TIÊU DỰ ÁN & ĐỐI TƯỢNG NGƯỜI DÙNG (Thời gian: 35 giây)
> *"Về bài toán nghiệp vụ, Culinary Blog được thiết kế chuyên biệt phục vụ 3 nhóm đối tượng:*  
> 1. *Thứ nhất là **Độc giả vãng lai**: Được tối ưu hóa trải nghiệm tìm kiếm món ăn siêu tốc bằng tiếng Việt không dấu, bộ lọc đa tiêu chí và trang chi tiết tối ưu SEO với cấu trúc Schema.org.*  
> 2. *Thứ hai là **Tác giả ẩm thực**: Cung cấp Creator Dashboard quản lý bài viết và bộ soạn thảo công thức kéo thả chuyên nghiệp.*  
> 3. *Thứ ba là **Quản trị viên**: Toàn quyền kiểm soát danh mục, quản lý người dùng và giám sát sức khỏe hạ tầng thời gian thực."*

---

### SLIDE 3: KIẾN TRÚC HỆ THỐNG TỔNG THỂ (Thời gian: 40 giây)
> *"Về kiến trúc tổng thể, nhóm triển khai mô hình **Decoupled Architecture** tách biệt hoàn toàn Frontend và Backend, đóng gói gồm 6 dịch vụ Docker Compose:*  
> *Ở vòng ngoài, **Nginx** làm Reverse Proxy tiếp nhận cổng 80 và điều phối traffic.*  
> *Phía Backend, nhóm áp dụng **Clean Architecture** với FastAPI: Tầng Domain giữ các Entity nghiệp vụ thuần túy, bọc ngoài bởi Schemas Pydantic v2 và Services. Dữ liệu được lưu trữ quan hệ trên **PostgreSQL 16**, phân tán cache và quản lý token bằng **Redis 7**, lưu trữ tệp ảnh trên **MinIO S3** và bắt email bằng **MailHog**."*

---

### SLIDE 4: PHÂN CÔNG VAI TRÒ NHÓM 25 (Thời gian: 35 giây)
> *"Khối lượng công việc được chia đều và gắn chặt với từng mã chức năng trong SRS:*  
> - *Bạn **Nguyễn Hoài Nam** phụ trách hạ tầng DevOps, Docker, module Xác thực nâng cao và Recipe Core.*  
> - *Bạn **Đỗ Duy Biên** phụ trách Module Categories, tìm kiếm Full-Text Search PostgreSQL, MinIO Storage và Background Jobs.*  
> - *Bạn **Hoàng Thăng Long** phụ trách giao diện người dùng công khai, trang danh mục, catalog món ăn và trang chi tiết.*  
> - *Bạn **Trần Chánh Phát** phụ trách bảng điều khiển tác giả Creator Dashboard, bộ soạn thảo kéo thả và trang quản trị Admin."*

---

### SLIDE 5: BACKEND CORE - BẢO MẬT & QUẢN LÝ CÔNG THỨC (Thời gian: 40 giây)
> *"Đi sâu vào Backend Core, nhóm đã hiện thực những giải pháp bảo mật và quản lý dữ liệu nâng cao:*  
> *Về bảo mật: Hệ thống sử dụng cặp **JWT Token Rotation** với cơ chế phát hiện tấn công tái sử dụng (Reuse Attack Detection), cơ chế khóa tài khoản tạm thời khi đăng nhập sai 5 lần, và tích hợp đăng nhập Google OAuth 2.0.*  
> *Về quản lý công thức: Nhóm áp dụng **Optimistic Concurrency Control** qua cột `row_version` để giải quyết triệt để lỗi Lost Update khi nhiều người cùng sửa bài, kết hợp kỹ thuật **Soft Delete** bảo vệ dữ liệu và tự động sinh slug tiếng Việt chuẩn SEO."*

---

### SLIDE 6: BACKEND - SEARCH FTS, MINIO STORAGE & JOBS (Thời gian: 40 giây)
> *"Tại tầng dữ liệu và background jobs:*  
> *Tính năng tìm kiếm sử dụng **PostgreSQL Full-Text Search** cấu hình `'simple'` kết hợp hàm `unaccent`. Lý do chọn `'simple'` thay vì `'english'` là để tránh việc bộ phân tích tiếng Anh tự ý cắt đuôi từ hoặc xóa nhầm các từ tiếng Việt.*  
> *Tệp ảnh tải lên được kiểm tra MIME type và Magic Bytes chặt chẽ qua MinIO S3 SDK, tự động tạo ảnh thumbnail.*  
> *Hệ thống còn tích hợp **APScheduler** chạy nền định kỳ mỗi 24h quét và tự động sinh file `sitemap.xml` phục vụ SEO Google."*

---

### SLIDE 7: FRONTEND - TRẢI NGHIỆM ĐỘC GIẢ & SEO (Thời gian: 40 giây)
> *"Ở phía giao diện người dùng, Frontend được xây dựng bằng **React 19** và Tailwind CSS:*  
> *Trang Catalog hỗ trợ bộ lọc kết hợp đa tiêu chí theo độ khó, thời gian nấu và phân trang linh hoạt.*  
> *Trang chi tiết món ăn trình bày sinh động từ ảnh bìa, nguyên liệu, hướng dẫn từng bước đến bảng dinh dưỡng.*  
> *Đặc biệt, nhóm đã nhúng cấu trúc dữ liệu **Schema.org Recipe** dạng JSON-LD, giúp công cụ tìm kiếm của Google hiển thị trực tiếp đánh giá sao, thời gian nấu và calo ngoài trang tìm kiếm."*

---

### SLIDE 8: FRONTEND - CREATOR DASHBOARD & BỘ SOẠN THẢO (Thời gian: 40 giây)
> *"Dành cho tác giả, hệ thống mang đến **Creator Dashboard** trực quan theo dõi số lượng bài viết:*  
> *Điểm nhấn là **Recipe Editor Wizard** - bộ công cụ tạo công thức đa bước. Tác giả có thể tải ảnh có thanh tiến trình preview và đặc biệt là tính năng kéo thả (**Drag and Drop**) thay đổi thứ tự các bước nấu ăn qua custom hook `useDragReorder`, hệ thống sẽ tự động đánh số lại các bước một cách đồng bộ."*

---

### SLIDE 9: GIẢI QUYẾT MÂU THUẪN SRS & ĐIỂM SÁNG DỰ ÁN (Thời gian: 40 giây)
> *"Trong quá trình phát triển, nhóm đã phát hiện và xử lý thỏa đáng 2 mâu thuẫn lớn trong file đặc tả SRS:*  
> 1. *Mâu thuẫn giữa Soft Delete và ràng buộc Unique Slug: Được giải quyết bằng **Partial Unique Index** trong PostgreSQL chỉ áp dụng trên các bản ghi chưa bị xóa mềm.*  
> 2. *Mâu thuẫn giữa JWT Stateless và yêu cầu Thu hồi token lập tức: Được giải quyết bằng mô hình **Hybrid Token**, đưa token thu hồi vào Redis Blacklist.*  
> *Ngoài ra, nhóm đã phát triển thêm các tính năng ngoài SRS như sinh slug tiếng Việt tự động, cron sitemap và trang quản lý người dùng."*

---

### SLIDE 10: DEVOPS & GIÁM SÁT SỨC KHỎE HỆ THỐNG (Thời gian: 35 giây)
> *"Về khía cạnh vận hành và kiểm thử:*  
> *Toàn bộ hệ thống được triển khai nhất quán qua **Docker Compose** chỉ với 1 câu lệnh.*  
> *Nhóm thiết kế tách bạch bộ 3 probes: `/health/live` kiểm tra process và `/health/ready` kiểm tra database/redis theo chuẩn Kubernetes, tránh tình trạng container bị restart hàng loạt khi CSDL bị chậm.*  
> *Mỗi request đều được gắn **Correlation-ID** để truy vết log từ Nginx qua FastAPI đến database."*

---

### SLIDE 11: TỔNG KẾT & KẾT QUẢ ĐẠT ĐƯỢC (Thời gian: 30 giây)
> *"Tóm lại, Nhóm 25 đã hoàn thành **100% các yêu cầu chức năng và phi chức năng** trong tài liệu đặc tả SRS v1.0.0. "  
> *Hệ thống sở hữu mã nguồn chuẩn mực theo Clean Architecture, giao diện hiện đại, bảo mật đa lớp và sẵn sàng mở rộng quy mô."*

---

### SLIDE 12: LỜI CẢM ƠN & CHUYỂN SANG DEMO (Thời gian: 15 - 20 giây)
> *"Trên đây là toàn bộ nội dung báo cáo của Nhóm 25. Em xin chân thành cảm ơn Cô và các bạn đã chú ý theo dõi!*  
> *Sau đây, nhóm em xin phép được tiếp nhận các câu hỏi phản biện từ Cô và bắt đầu phần Demo trực tiếp ứng dụng!"*
