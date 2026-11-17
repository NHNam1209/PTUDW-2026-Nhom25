import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.config import settings

logger = logging.getLogger("culinary_blog.services.email")


async def send_welcome_email(user_email: str, full_name: str) -> bool:
    """FR-JOB-001: Background task to send a welcome email to newly registered users."""
    logger.info(f"[JOB-EMAIL] Initiating welcome email dispatch to: {user_email}")

    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f7fafc; margin: 0; padding: 20px; }}
            .container {{ max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); }}
            .header {{ background-color: #ea580c; color: white; padding: 24px; text-align: center; }}
            .content {{ padding: 32px 24px; color: #2d3748; line-height: 1.6; }}
            .btn {{ display: inline-block; background-color: #ea580c; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 16px; }}
            .footer {{ background-color: #edf2f7; padding: 16px; text-align: center; font-size: 12px; color: #718096; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Chào Mừng Đến Với Culinary Blog! 🍳</h1>
            </div>
            <div class="content">
                <p>Xin chào <strong>{full_name}</strong>,</p>
                <p>Cảm ơn bạn đã đăng ký tài khoản tại nền tảng chia sẻ công thức ẩm thực của chúng tôi.</p>
                <p>Giờ đây, bạn có thể tự do khám phá hàng trăm công thức tuyệt hảo, lưu lại món yêu thích, và chia sẻ các tác phẩm nấu nướng do chính tay mình tạo ra.</p>
                <p style="text-align: center;">
                    <a href="https://culinaryblog.com/recipes" class="btn">Khám Phá Công Thức Ngay</a>
                </p>
                <br>
                <p>Trân trọng,<br><strong>Đội ngũ Phát triển Culinary Blog</strong></p>
            </div>
            <div class="footer">
                &copy; 2026 Culinary Blog. All rights reserved.
            </div>
        </div>
    </body>
    </html>
    """

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Chào mừng bạn đến với Culinary Blog! 🍳"
        msg["From"] = f"{settings.EMAILS_FROM_NAME} <{settings.EMAILS_FROM_EMAIL}>"
        msg["To"] = user_email
        msg.attach(MIMEText(html_content, "html", "utf-8"))

        # Attempt to deliver via SMTP / MailHog
        try:
            with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT, timeout=5) as server:
                if settings.SMTP_TLS:
                    server.starttls()
                if settings.SMTP_USER and settings.SMTP_PASSWORD:
                    server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
                server.send_message(msg)
            logger.info(f"[JOB-EMAIL] Welcome email successfully delivered to {user_email} via SMTP ({settings.SMTP_SERVER}:{settings.SMTP_PORT})")
            return True
        except (smtplib.SMTPException, OSError) as smtp_err:
            logger.warning(
                f"[JOB-EMAIL] SMTP delivery unready ({smtp_err}). Email logged in development mode for {user_email}."
            )
            return False

    except Exception as e:
        logger.error(f"[JOB-EMAIL] Unexpected error delivering email to {user_email}: {e}", exc_info=True)
        return False
