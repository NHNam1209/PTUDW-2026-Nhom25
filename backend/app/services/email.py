# app/services/email.py
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.core.config import settings

logger = logging.getLogger("culinary_blog.email")

async def send_welcome_email(user_email: str, full_name: str) -> None:
    """Nhiệm vụ chạy ngầm gửi email chào mừng người dùng mới."""
    try:
        # Nếu chưa cấu hình SMTP trong env thì log để dev/testing
        logger.info(f"[BACKGROUND JOB] Đang gửi email chào mừng tới {user_email}...")
        
        # HTML Template email chào mừng
        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <h2 style="color: #e67e22;">Chào mừng {full_name} đến với Culinary Blog! 🍳</h2>
                <p>Cảm ơn bạn đã đăng ký tài khoản tại nền tảng chia sẻ công thức nấu ăn của chúng tôi.</p>
                <p>Hãy bắt đầu khám phá các công thức hấp dẫn hoặc chia sẻ món ăn ngon do chính bạn nấu nhé!</p>
                <br>
                <p>Trân trọng,</p>
                <p><strong>Đội ngũ Culinary Blog</strong></p>
            </body>
        </html>
        """
        
        # Nếu có cấu hình SMTP Server thật (Ví dụ Gmail, Sendgrid)
        # msg = MIMEMultipart("alternative")
        # msg["Subject"] = "Chào mừng bạn đến với Culinary Blog!"
        # msg["From"] = "no-reply@culinaryblog.com"
        # msg["To"] = user_email
        # msg.attach(MIMEText(html_content, "html"))
        # with smtplib.SMTP("smtp.gmail.com", 587) as server:
        #     server.starttls()
        #     server.login("your_email", "your_password")
        #     server.sendmail("no-reply@culinaryblog.com", user_email, msg.as_string())
        
        logger.info(f"[BACKGROUND JOB] Đã gửi email chào mừng tới thành công cho {user_email}")
    except Exception as e:
        logger.error(f"[BACKGROUND JOB] Lỗi gửi email chào mừng tới {user_email}: {e}")