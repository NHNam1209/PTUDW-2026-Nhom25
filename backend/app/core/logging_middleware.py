import uuid
import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Cấu hình log cơ bản
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger("api_tracker")

class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 1. Lấy X-Correlation-ID từ client gửi lên hoặc tự sinh mới
        correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
        request.state.correlation_id = correlation_id
        
        start_time = time.time()
        
        # 2. Xử lý request
        response = await call_next(request)
        
        # 3. Tính thời gian phản hồi
        duration = (time.time() - start_time) * 1000
        
        # 4. Trả Correlation-ID về lại cho Response Header
        response.headers["X-Correlation-ID"] = correlation_id
        
        # 5. Ghi Structured Log dạng rõ ràng
        logger.info(
            f"method={request.method} path={request.url.path} "
            f"status={response.status_code} duration={duration:.2f}ms "
            f"correlation_id={correlation_id}"
        )
        return response