# -*- coding: utf-8 -*-
"""
Script tạo báo cáo chuẩn theo mẫu Nhom_1_BC_v4.docx cho Đồ án Culinary Blog (Nhóm 25)
Môn học: Phát triển ứng dụng web nâng cao
Giảng viên hướng dẫn: TS. Nguyễn Thị Lương
Thành viên:
  - Nguyễn Hoài Nam (Trưởng nhóm) - 2312694 - CTK47-PM
  - Đỗ Duy Biên - 2312584 - CTK47-PM
  - Hoàng Thăng Long - 2312676 - CTK47-PM
  - Trần Chánh Phát - 2212437 - CTK46-PM
Độ dài kỳ vọng: 20 - 25 trang Word
"""

import os
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

WORKSPACE_DIR = r"d:\PTUDWNC\PTUDW-2026-Nhom25"
SCREENSHOTS_DIR = os.path.join(WORKSPACE_DIR, "screenshots")
TEMPLATE_PATH = os.path.join(WORKSPACE_DIR, "Nhom_1_BC_v4.docx")
BACKUP_TEMPLATE_PATH = os.path.join(WORKSPACE_DIR, "Nhom_1_BC_v4_original.docx")

OUTPUT_PATH_1 = os.path.join(WORKSPACE_DIR, "Bao_Cao_Do_An_Nhom_25_Culinary_Blog.docx")
OUTPUT_PATH_2 = r"d:\PTUDWNC\Bao_Cao_Do_An_Nhom_25_Culinary_Blog.docx"
OUTPUT_PATH_V4 = TEMPLATE_PATH

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex="F1F5F9"):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)

def set_table_borders(table, color="CCCCCC", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'<w:tblBorders {nsdecls("w")}>'
                        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                        f'</w:tblBorders>')
    tblPr.append(borders)

def add_chapter_heading(doc, text):
    p = doc.add_paragraph()
    p.style = doc.styles['Heading 1']
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.line_spacing = 1.3
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(15)
    run.bold = True
    run.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A) # Deep Navy Blue
    return p

def add_sec_heading(doc, text):
    p = doc.add_paragraph()
    p.style = doc.styles['List Paragraph']
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.3
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12.5)
    run.bold = True
    run.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    return p

def add_body_paragraph(doc, text):
    p = doc.add_paragraph()
    p.style = doc.styles['Normal']
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Inches(0.3)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.3
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    return p

def add_bullet(doc, text, bold_prefix=""):
    p = doc.add_paragraph()
    p.style = doc.styles['Normal']
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.35)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.line_spacing = 1.25
    
    r_bullet = p.add_run("•  ")
    r_bullet.font.name = "Times New Roman"
    r_bullet.font.size = Pt(11.5)
    r_bullet.bold = True
    r_bullet.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    
    if bold_prefix:
        r_lead = p.add_run(bold_prefix + ": ")
        r_lead.font.name = "Times New Roman"
        r_lead.font.size = Pt(11.5)
        r_lead.bold = True
        
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11.5)
    return p

def add_figure(doc, img_rel_path, caption_text, width_in=5.6):
    img_path = os.path.join(SCREENSHOTS_DIR, img_rel_path)
    if not os.path.exists(img_path):
        return None
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(6)
    p_img.paragraph_format.space_after = Pt(3)
    r_img = p_img.add_run()
    r_img.add_picture(img_path, width=Inches(width_in))
    
    p_cap = doc.add_paragraph()
    p_cap.style = doc.styles['Caption']
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(6)
    r_cap = p_cap.add_run(caption_text)
    r_cap.font.name = "Times New Roman"
    r_cap.font.size = Pt(10)
    r_cap.italic = True
    return p_cap

def main():
    print(f"Loading template from {TEMPLATE_PATH}...")
    if not os.path.exists(BACKUP_TEMPLATE_PATH):
        shutil.copy2(TEMPLATE_PATH, BACKUP_TEMPLATE_PATH)
        print("Backed up original template to Nhom_1_BC_v4_original.docx")
        
    doc = docx.Document(TEMPLATE_PATH)
    
    # =========================================================================
    # 1. CẬP NHẬT TRANG BÌA (TABLE 0)
    # =========================================================================
    print("Updating Cover Page (Table 0)...")
    t0 = doc.tables[0]
    cell = t0.rows[0].cells[0]
    
    for p in cell.paragraphs:
        if "Phát triển ứng dụng di động" in p.text:
            p.text = "Môn: Phát triển ứng dụng web nâng cao"
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.bold = True
                r.font.name = "Times New Roman"
                r.font.size = Pt(14)
        elif "Phát triển ứng dụng hỗ trợ quản lý và đặt lịch sân cầu lông" in p.text:
            p.text = "Đề tài: Hệ thống ứng dụng web chia sẻ, khám phá và quản lý công thức ẩm thực (Culinary Blog)"
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.bold = True
                r.italic = True
                r.font.name = "Times New Roman"
                r.font.size = Pt(15)
                r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        elif "Nhóm: 01" in p.text or "Nhóm: 1" in p.text:
            p.text = "Nhóm: 25"
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.bold = True
                r.font.name = "Times New Roman"
                r.font.size = Pt(13)
        elif "Giảng viên hướng dẫn:" in p.text:
            p.text = "Giảng viên hướng dẫn:\tTS. Nguyễn Thị Lương"
            for r in p.runs:
                r.bold = True
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)
        elif "tháng 5 năm 2026" in p.text:
            p.text = "Lâm Đồng, tháng 11 năm 2026"
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.bold = True
                r.italic = True
                r.font.name = "Times New Roman"
                r.font.size = Pt(13)

    # Cập nhật bảng sinh viên thực hiện trên trang bìa
    sub_table = cell.tables[0]
    members = [
        ("2312694", "Nguyễn Hoài Nam (Trưởng nhóm)", "CTK47-PM"),
        ("2312584", "Đỗ Duy Biên", "CTK47-PM"),
        ("2312676", "Hoàng Thăng Long", "CTK47-PM"),
        ("2212437", "Trần Chánh Phát", "CTK46-PM")
    ]
    while len(sub_table.rows) > 1:
        tr = sub_table.rows[-1]._tr
        tr.getparent().remove(tr)
        
    for mssv, name, lop in members:
        row = sub_table.add_row()
        row.cells[0].text = mssv
        row.cells[1].text = name
        row.cells[2].text = lop
        for idx, c in enumerate(row.cells):
            set_cell_margins(c, top=60, bottom=60, left=100, right=100)
            for p in c.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                if idx in [0, 2]:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(11)
                    if "Trưởng nhóm" in name and idx == 1:
                        r.bold = True

    # =========================================================================
    # 2. CẬP NHẬT MỤC LỤC & DANH MỤC TỪ VIẾT TẮT & DANH MỤC HÌNH ẢNH
    # =========================================================================
    print("Updating Table of Contents and Abbreviations Table...")
    
    # Cập nhật Mục lục trong Section 1
    # Tìm đoạn văn Mục lục
    toc_items = [
        ("DANH MỤC TỪ VIẾT TẮT", "ii", 1),
        ("DANH MỤC HÌNH ẢNH", "iii", 1),
        ("NỘI DUNG BÁO CÁO", "1", 1),
        ("CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI VÀ CÔNG NGHỆ SỬ DỤNG", "1", 1),
        ("1.1. Ý nghĩa đề tài", "1", 2),
        ("1.2. Mục tiêu đề tài", "1", 2),
        ("1.3. Công nghệ và ngôn ngữ lập trình sử dụng", "2", 2),
        ("CHƯƠNG 2. PHÂN TÍCH CHỨC NĂNG VÀ THIẾT KẾ HỆ THỐNG", "4", 1),
        ("2.1. Phân hệ Độc giả (Reader)", "4", 2),
        ("2.2. Phân hệ Tác giả ẩm thực (Creator / Author)", "4", 2),
        ("2.3. Phân hệ Quản trị viên (Admin)", "5", 2),
        ("2.4. Sơ đồ Use Case & Luồng nghiệp vụ tổng quan", "5", 2),
        ("2.5. Thiết kế Cơ sở dữ liệu quan hệ (PostgreSQL 16)", "6", 2),
        ("2.6. Kiến trúc hệ thống Clean Architecture 4 tầng", "7", 2),
        ("CHƯƠNG 3. CÁC ĐẶC TẢ KỸ THUẬT VÀ GIẢI PHÁP CỐT LÕI", "9", 1),
        ("3.1. Kiểm soát xung đột đồng thời (Optimistic Concurrency Control)", "9", 2),
        ("3.2. Bảo mật xác thực JWT kép & Chống phát lại Refresh Token", "10", 2),
        ("3.3. Tối ưu tìm kiếm toàn văn tiếng Việt (Full-Text Search unaccent)", "10", 2),
        ("3.4. Kiến trúc xử lý tác vụ ngầm & Lập lịch định kỳ (Background Jobs)", "11", 2),
        ("3.5. Kiểm soát tần suất truy cập (Rate Limiting) & Chuẩn hóa lỗi RFC 7807", "12", 2),
        ("3.6. Truy vết luồng dữ liệu & Giám sát hệ thống (Structured Logging & Probes)", "12", 2),
        ("CHƯƠNG 4. HƯỚNG DẪN CÀI ĐẶT VÀ SỬ DỤNG ỨNG DỤNG (DEMO SẢN PHẨM)", "13", 1),
        ("4.1. Hướng dẫn cài đặt và vận hành hệ thống qua Docker Compose", "13", 2),
        ("4.2. Hướng dẫn sử dụng cho Độc giả", "14", 2),
        ("4.3. Hướng dẫn sử dụng cho Tác giả ẩm thực", "16", 2),
        ("4.4. Hướng dẫn sử dụng cho Quản trị viên", "18", 2),
        ("4.5. Giám sát hạ tầng kỹ thuật và Tài liệu API", "20", 2),
        ("KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", "21", 1),
        ("1. Kết luận", "21", 2),
        ("2. Hướng phát triển", "21", 2),
        ("PHÂN CÔNG CÔNG VIỆC", "22", 1),
        ("DANH MỤC TÀI LIỆU THAM KHẢO", "23", 1)
    ]
    
    # Cập nhật các dòng toc hiện có hoặc gán lại text
    # Các dòng paragraph từ index 1 đến 22 trong template ban đầu
    p_idx = 1
    for title, pg, level in toc_items:
        if p_idx < len(doc.paragraphs) and doc.paragraphs[p_idx].style.name.startswith('toc'):
            p_toc = doc.paragraphs[p_idx]
            p_toc.text = f"{title}\t{pg}"
            p_idx += 1
            
    # Cập nhật Bảng từ viết tắt (Table 1)
    t1 = doc.tables[1]
    abbreviations = [
        ("API", "Application Programming Interface", "Giao diện lập trình ứng dụng cho phép các dịch vụ giao tiếp qua giao thức HTTP"),
        ("CSDL", "Cơ sở dữ liệu", "Hệ thống lưu trữ và quản lý dữ liệu quan hệ (PostgreSQL 16)"),
        ("HTTP / HTTPS", "HyperText Transfer Protocol / Secure", "Giao thức truyền tải siêu văn bản có chứng chỉ mã hóa an toàn SSL/TLS"),
        ("REST / RESTful", "Representational State Transfer", "Phong cách kiến trúc API chuẩn hóa các phương thức HTTP (GET, POST, PUT, DELETE)"),
        ("JWT", "JSON Web Token", "Chuẩn mã hóa token xác thực người dùng stateless (gồm Access Token và Refresh Token)"),
        ("FTS", "Full-Text Search", "Cơ chế tìm kiếm toàn văn tối ưu với tsvector và unaccent trong PostgreSQL"),
        ("S3", "Simple Storage Service", "Dịch vụ lưu trữ đối tượng đám mây tương thích AWS S3 (MinIO Object Storage)"),
        ("OCC", "Optimistic Concurrency Control", "Kiểm soát truy cập đồng thời lạc quan ngăn ngừa ghi đè dữ liệu bằng rowVersion"),
        ("RFC 7807", "Problem Details for HTTP APIs", "Chuẩn đặc tả quốc tế cấu trúc thông báo lỗi API dạng application/problem+json"),
        ("ORM", "Object-Relational Mapping", "Kỹ thuật ánh xạ bảng CSDL thành các đối tượng Python qua SQLAlchemy 2.0"),
        ("CORS", "Cross-Origin Resource Sharing", "Cơ chế bảo mật trình duyệt cho phép frontend và backend chia sẻ tài nguyên"),
        ("SPA", "Single Page Application", "Ứng dụng web trang đơn xây dựng bằng React 19 và Vite"),
        ("DTO", "Data Transfer Object", "Lớp mô hình truyền tải và kiểm thực dữ liệu đầu vào/ra (Pydantic Schemas v2)"),
        ("SRS", "Software Requirements Specification", "Tài liệu đặc tả yêu cầu phần mềm chuẩn quốc tế IEEE 830 / ISO 29148")
    ]
    while len(t1.rows) > 1:
        tr = t1.rows[-1]._tr
        tr.getparent().remove(tr)
    for abbr, full, note in abbreviations:
        row = t1.add_row()
        row.cells[0].text = abbr
        row.cells[1].text = full
        row.cells[2].text = note
        for idx, c in enumerate(row.cells):
            set_cell_margins(c, top=60, bottom=60, left=100, right=100)
            for p in c.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                if idx == 0:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for r in p.runs:
                        r.bold = True
                        r.font.name = "Times New Roman"
                        r.font.size = Pt(11)
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    for r in p.runs:
                        r.font.name = "Times New Roman"
                        r.font.size = Pt(11)

    # Cập nhật Danh mục hình ảnh
    figures_list = [
        ("Hình 4.1. Giao diện Trang chủ hệ thống ẩm thực Culinary Blog", "14"),
        ("Hình 4.2. Màn hình duyệt danh sách công thức nấu ăn & bộ lọc đa tiêu chí", "14"),
        ("Hình 4.3. Màn hình chi tiết công thức, định lượng nguyên liệu & bộ đếm hẹn giờ nấu", "15"),
        ("Hình 4.4. Danh mục khám phá món ăn ẩm thực phong phú (22 danh mục)", "15"),
        ("Hình 4.5. Chi tiết danh mục và danh sách công thức thuộc danh mục", "16"),
        ("Hình 4.6. Kết quả tìm kiếm toàn văn tiếng Việt không dấu (PostgreSQL FTS unaccent)", "16"),
        ("Hình 4.7. Màn hình Đăng nhập hệ thống & Tích hợp đăng nhập nhanh Google OAuth 2.0", "17"),
        ("Hình 4.8. Màn hình Đăng ký tài khoản tác giả ẩm thực kèm kiểm tra mật khẩu", "17"),
        ("Hình 4.9. Creator Dashboard - Bảng điều khiển tác giả & thống kê số liệu bài viết", "18"),
        ("Hình 4.10. Bảng quản lý công thức và vòng đời trạng thái (Draft / Publish / Archived)", "18"),
        ("Hình 4.11. Bộ biên tập công thức nấu ăn chuyên sâu đa bước (Recipe Editor Wizard)", "19"),
        ("Hình 4.12. Màn hình Quản trị viên quản lý danh mục món ăn (Category Admin)", "19"),
        ("Hình 4.13. Màn hình Quản trị viên quản lý danh sách người dùng (Users Management)", "20"),
        ("Hình 4.14. Tài liệu đặc tả API tương tác trực quan Swagger UI (FastAPI OpenAPI)", "20"),
        ("Hình 4.15. Kiểm tra tình trạng sức khỏe hệ thống (Health Check Probe)", "21"),
        ("Hình 4.16. Hộp thư MailHog kiểm thử gửi email ngầm chào mừng người dùng", "21"),
        ("Hình 4.17. Giao diện quản lý lưu trữ đối tượng MinIO Object Storage Console", "21")
    ]
    # Cập nhật các dòng table of figures hiện có
    tof_idx = 0
    for p in doc.paragraphs:
        if p.style.name == 'table of figures':
            if tof_idx < len(figures_list):
                p.text = f"{figures_list[tof_idx][0]}\t{figures_list[tof_idx][1]}"
                tof_idx += 1

    # =========================================================================
    # 3. XÓA BỎ NỘI DUNG CŨ CỦA ĐỒ ÁN CẦU LÔNG (TỪ ELEM 39 ĐẾN SÁT SECTPR CUỐI)
    # =========================================================================
    print("Clearing old badminton report body elements...")
    body = doc._body._element
    children = list(body)
    # Xóa từ element index 39 tới element kế cuối (giữ sectPr cuối cùng)
    for el in children[39:-1]:
        body.remove(el)

    # =========================================================================
    # 4. THÊM NỘI DUNG BÁO CÁO MỚI (CHƯƠNG 1 -> 4, KẾT LUẬN, PHÂN CÔNG, TÀI LIỆU)
    # =========================================================================
    print("Generating comprehensive Culinary Blog chapters...")

    # Tiêu đề chung phần nội dung
    p_title = doc.add_paragraph()
    p_title.style = doc.styles['Heading 1']
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(12)
    r_t = p_title.add_run("NỘI DUNG BÁO CÁO")
    r_t.font.name = "Times New Roman"
    r_t.font.size = Pt(16)
    r_t.bold = True
    r_t.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    # -------------------------------------------------------------------------
    # CHƯƠNG 1
    # -------------------------------------------------------------------------
    add_chapter_heading(doc, "CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI VÀ CÔNG NGHỆ SỬ DỤNG")
    
    add_sec_heading(doc, "1.1. Ý nghĩa đề tài")
    add_body_paragraph(doc, "Trong kỷ nguyên số hóa hiện nay, văn hóa ẩm thực và nhu cầu tự nấu ăn tại gia đình ngày càng trở thành một xu hướng phổ biến trong đời sống xã hội. Người dùng không chỉ tìm kiếm công thức nấu ăn đơn thuần trên các mạng xã hội mà còn có nhu cầu tiếp cận những hướng dẫn ẩm thực chi tiết, chuẩn xác về định lượng nguyên liệu, bảng phân tích giá trị dinh dưỡng, cùng các tiện ích hỗ trợ người nấu trực tiếp theo thời gian thực (như bộ đếm giờ từng công đoạn nấu ăn).")
    add_body_paragraph(doc, "Tuy nhiên, hầu hết các nền tảng chia sẻ công thức ẩm thực hiện nay còn bộc lộ nhiều điểm hạn chế: nội dung phân tán, thiếu quy chuẩn định lượng, giao diện phức tạp và thiếu khả năng hỗ trợ quy trình nấu ăn tương tác. Hơn nữa, việc thiếu cơ chế đồng bộ đồng thời khiến nội dung công thức dễ bị ghi đè dữ liệu khi nhiều tác giả cùng chỉnh sửa. Nhằm giải quyết triệt để những bất cập trên, đề tài \"Hệ thống ứng dụng web chia sẻ, khám phá và quản lý công thức ẩm thực (Culinary Blog System)\" được nghiên cứu và phát triển nhằm mang lại một nền tảng toàn diện, hiện đại, bảo mật cao và tối ưu trải nghiệm cho cả độc giả, tác giả ẩm thực và quản trị viên.")

    add_sec_heading(doc, "1.2. Mục tiêu đề tài")
    add_body_paragraph(doc, "Đề tài được định hướng triển khai đáp ứng trọn vẹn các mục tiêu kỹ thuật và nghiệp vụ thực tiễn sau:")
    add_bullet(doc, "Xây dựng hệ thống web Single Page Application (SPA) trên nền React 19 kết hợp kiến trúc Clean Architecture 4 tầng tại Backend FastAPI, đảm bảo tính phân tách trách nhiệm (Separation of Concerns) và khả năng mở rộng quy mô lớn.", "Kiến trúc chuẩn mực")
    add_bullet(doc, "Cung cấp đầy đủ các tính năng duyệt công thức, tìm kiếm toàn văn tiếng Việt không dấu (Full-Text Search unaccent), xem định lượng nguyên liệu tự động điều chỉnh theo số khẩu phần, và bộ hẹn giờ thông minh (Cooking Timer) theo từng bước.", "Trải nghiệm người dùng vượt trội")
    add_bullet(doc, "Trang bị bộ công cụ soạn thảo đa bước (Wizard) cho tác giả, hỗ trợ tải ảnh trực tiếp lên MinIO S3 Object Storage, quản lý vòng đời trạng thái món ăn khép kín (Draft -> Publish -> Archived).", "Công cụ sáng tạo nội dung")
    add_bullet(doc, "Hiện thực cơ chế kiểm soát xung đột dữ liệu đồng thời (Optimistic Concurrency Control), bảo mật xác thực kép JWT (Access Token & Refresh Token) chống Replay Attack, đăng nhập Google OAuth 2.0 và kiểm soát tần suất truy cập Rate Limiting.", "Bảo mật & Hiệu năng cao")
    add_bullet(doc, "Đóng gói toàn bộ hệ sinh thái vi dịch vụ (Web, API, DB, Cache, S3 Storage, SMTP) trong Docker Compose, triển khai Reverse Proxy Nginx, sẵn sàng cho môi trường Production thực tế.", "Tự động hóa DevOps")

    add_sec_heading(doc, "1.3. Công nghệ và ngôn ngữ lập trình sử dụng")
    add_body_paragraph(doc, "Hệ thống Culinary Blog được xây dựng bằng cách kết hợp các công nghệ phần mềm tiên tiến nhất hiện nay:")
    
    # Bảng công nghệ
    tbl_tech = doc.add_table(rows=1, cols=3)
    tbl_tech.style = 'Table Grid'
    set_table_borders(tbl_tech)
    hdr_cells = tbl_tech.rows[0].cells
    hdr_cells[0].text = "Thành phần"
    hdr_cells[1].text = "Công nghệ sử dụng"
    hdr_cells[2].text = "Vai trò & Đặc tả kỹ thuật"
    for c in hdr_cells:
        set_cell_margins(c, 80, 80, 120, 120)
        set_cell_shading(c, "E2E8F0")
        for p in c.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.bold = True
                r.font.name = "Times New Roman"
                r.font.size = Pt(11)

    tech_data = [
        ("Backend Framework", "Python 3.12 / FastAPI", "Xây dựng RESTful API bất đồng bộ (asyncio), hiệu năng cao, tự động sinh OpenAPI Swagger."),
        ("ORM & Migration", "SQLAlchemy 2.0 & Alembic", "Mô hình hóa thực thể CSDL quan hệ, hỗ trợ AsyncSession Local và điều phối migration CSDL."),
        ("Frontend Web", "React 19 / Vite / Tailwind", "Xây dựng giao diện tương tác cao (SPA), tải trang tức thì, thiết kế responsive đa nền tảng."),
        ("Cơ sở dữ liệu", "PostgreSQL 16", "Lưu trữ dữ liệu quan hệ, đánh chỉ mục GIN, hỗ trợ tìm kiếm toàn văn unaccent và tsvector."),
        ("Bộ nhớ đệm & Limiter", "Redis 7 Alpine", "Lưu trữ phiên làm việc, Blacklist refresh token và thực thi thuật toán Sliding-Window Rate Limiting."),
        ("Lưu trữ tệp tin", "MinIO (S3-Compatible)", "Dịch vụ Object Storage lưu trữ ảnh đại diện và ảnh minh họa công thức, tương thích AWS S3 SDK."),
        ("Dịch vụ Thư điện tử", "MailHog / SMTP Service", "Môi trường giả lập gửi nhận email MIME HTML kiểm thử tác vụ ngầm gửi email chào mừng."),
        ("Web Server & Proxy", "Nginx Alpine Reverse Proxy", "Điều hướng tải (Port 80), phục vụ tài nguyên tĩnh, thiết lập CORS và đệm kết nối an toàn."),
        ("Đóng gói triển khai", "Docker & Docker Compose", "Đóng gói toàn bộ các dịch vụ thành các container độc lập, triển khai đồng bộ bằng 1 lệnh.")
    ]
    for comp, tech, role in tech_data:
        row = tbl_tech.add_row()
        row.cells[0].text = comp
        row.cells[1].text = tech
        row.cells[2].text = role
        for idx, c in enumerate(row.cells):
            set_cell_margins(c, 60, 60, 100, 100)
            for p in c.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                if idx == 0:
                    for r in p.runs:
                        r.bold = True
                        r.font.name = "Times New Roman"
                        r.font.size = Pt(10.5)
                else:
                    for r in p.runs:
                        r.font.name = "Times New Roman"
                        r.font.size = Pt(10.5)

    # -------------------------------------------------------------------------
    # CHƯƠNG 2
    # -------------------------------------------------------------------------
    add_chapter_heading(doc, "CHƯƠNG 2. PHÂN TÍCH CHỨC NĂNG VÀ THIẾT KẾ HỆ THỐNG")
    
    add_sec_heading(doc, "2.1. Phân hệ Độc giả (Reader / Public User)")
    add_body_paragraph(doc, "Phân hệ Độc giả cung cấp giao diện công khai, hướng tới trải nghiệm khám phá ẩm thực nhanh chóng, sinh động và trực quan mà không yêu cầu bắt buộc đăng nhập:")
    add_bullet(doc, "Hiển thị các công thức nấu ăn mới nhất, nổi bật nhất theo từng tuần, kèm danh mục các món ăn thịnh hành và thanh tìm kiếm tức thì.", "Trang chủ tương tác (Homepage)")
    add_bullet(doc, "Hỗ trợ duyệt danh sách món ăn phân trang linh hoạt, lọc kết hợp đa tiêu chí: độ khó (Dễ, Trung bình, Khó), danh mục món, thời gian chuẩn bị và số lượng calo.", "Duyệt công thức & Bộ lọc")
    add_bullet(doc, "Tìm kiếm công thức thông minh hỗ trợ gõ tiếng Việt có dấu hoặc không dấu, tự động chuẩn hóa chuỗi và xếp hạng độ liên quan.", "Tìm kiếm toàn văn bản (FTS)")
    add_bullet(doc, "Hiển thị đầy đủ nguyên liệu có khả năng tính toán lại định lượng khi người xem đổi số khẩu phần, danh sách các bước nấu có bộ đếm ngược thời gian nấu ăn thực tế (Cooking Timer).", "Trang chi tiết công thức")

    add_sec_heading(doc, "2.2. Phân hệ Tác giả ẩm thực (Creator / Author)")
    add_body_paragraph(doc, "Tác giả ẩm thực là trung tâm sáng tạo nội dung của hệ sinh thái Culinary Blog. Sau khi đăng ký hoặc đăng nhập thông qua tài khoản cục bộ hoặc Google OAuth 2.0, tác giả được cấp các quyền hạn chuyên sâu:")
    add_bullet(doc, "Giao diện tổng quan thể hiện số lượng bài viết đã tạo, số công thức đã xuất bản, số bài nháp và lượt xem tương tác.", "Creator Dashboard")
    add_bullet(doc, "Quản lý toàn bộ danh sách bài viết cá nhân theo các tab trạng thái: Tạo nháp (Draft) -> Xuất bản (Published) -> Lưu trữ (Archived) -> Xóa mềm.", "Quản lý công thức cá nhân")
    add_bullet(doc, "Giao diện soạn thảo đa bước hướng dẫn tác giả nhập thông tin tổng quan, bảng nguyên liệu động, các bước thực hiện tuần tự kèm thời gian đếm ngược, và bảng dinh dưỡng.", "Bộ biên tập công thức (Wizard)")
    add_bullet(doc, "Tải ảnh trực tiếp lên MinIO Object Storage, hỗ trợ chọn ảnh đại diện chính (Primary Image), xem trước ảnh và xóa ảnh an toàn.", "Quản lý đa phương tiện")

    add_sec_heading(doc, "2.3. Phân hệ Quản trị viên (Admin)")
    add_body_paragraph(doc, "Quản trị viên là phân hệ có thẩm quyền cao nhất trong hệ thống, chịu trách nhiệm bảo đảm chất lượng nội dung và an ninh vận hành:")
    add_bullet(doc, "Tạo mới, chỉnh sửa thông tin, cập nhật ảnh biểu trưng và xóa các danh mục ẩm thực (có kiểm tra ràng buộc toàn vẹn dữ liệu).", "Quản trị danh mục ẩm thực")
    add_bullet(doc, "Tra cứu danh sách thành viên, chuyển đổi phân quyền giữa các vai trò (Admin, Author, Reader) và kích hoạt tính năng khóa/mở khóa tài khoản khi phát hiện vi phạm.", "Quản lý người dùng hệ thống")
    add_bullet(doc, "Theo dõi các probe kiểm tra sức khỏe (/health), nhật ký kiểm toán hệ thống (Audit Logs) và số liệu lưu trữ MinIO.", "Giám sát & Quản trị hạ tầng")

    add_sec_heading(doc, "2.4. Sơ đồ Use Case & Luồng nghiệp vụ tổng quan")
    add_body_paragraph(doc, "Hệ thống phân định ranh giới chức năng rõ ràng giữa 3 nhóm tác nhân chính (Độc giả, Tác giả và Quản trị viên). Các Use Case được thiết kế khép kín, đảm bảo tính bảo mật và kiểm soát truy cập dựa trên vai trò (RBAC - Role-Based Access Control):")
    add_bullet(doc, "Độc giả có quyền truy cập các Use Case: Xem trang chủ, Xem danh mục, Xem công thức, Tìm kiếm món ăn, Đăng ký, Đăng nhập.", "Nhóm Use Case Công khai")
    add_bullet(doc, "Tác giả có quyền thực hiện các Use Case: Quản lý Dashboard cá nhân, Tạo bản nháp công thức, Chỉnh sửa công thức (kèm OCC), Xuất bản công thức, Upload ảnh lên MinIO, Cập nhật hồ sơ cá nhân.", "Nhóm Use Case Sáng tạo nội dung")
    add_bullet(doc, "Quản trị viên quản lý toàn bộ các Use Case: Quản lý danh mục ẩm thực, Quản lý tài khoản người dùng, Khóa tài khoản, Xem tài liệu kỹ thuật Swagger và probe sức khỏe hệ thống.", "Nhóm Use Case Quản trị")

    add_sec_heading(doc, "2.5. Thiết kế Cơ sở dữ liệu quan hệ (PostgreSQL 16)")
    add_body_paragraph(doc, "Cơ sở dữ liệu được thiết kế theo chuẩn dạng chuẩn 3NF, bảo đảm tính toàn vẹn tham chiếu, tối ưu hóa hiệu năng truy vấn cho các nghiệp vụ đọc dữ liệu quy mô lớn:")
    add_bullet(doc, "Lưu trữ thông tin định danh, email (duy nhất), mật khẩu băm Bcrypt, vai trò (Admin, Author, User), trạng thái khóa, số lần đăng nhập thất bại và thời điểm khóa tài khoản.", "Bảng users")
    add_bullet(doc, "Lưu trữ các phân loại món ăn (22 danh mục chuẩn), tên, slug SEO duy nhất, mô tả và đường dẫn ảnh biểu trưng.", "Bảng categories")
    add_bullet(doc, "Bảng trung tâm lưu trữ tiêu đề, slug, mô tả, khẩu phần, thời gian chuẩn bị & nấu ăn, độ khó, trạng thái vòng đời (Draft=0, Published=1, Archived=2), trường kiểm soát xung đột đồng thời rowVersion (UUID), và các chỉ số dinh dưỡng (Calories, Protein, Carbs, Fat, Fiber, Sodium).", "Bảng recipes")
    add_bullet(doc, "Lưu trữ chi tiết các thành phần món ăn: tên nguyên liệu, định lượng số học (amount), đơn vị đo (unit) và ghi chú chế biến.", "Bảng recipe_ingredients")
    add_bullet(doc, "Lưu trữ tuần tự các bước nấu: số thứ tự bước (step_number), hướng dẫn chi tiết, và thời gian thực hiện tính bằng phút (timer_minutes).", "Bảng recipe_steps")
    add_bullet(doc, "Lưu trữ đường dẫn URL tệp ảnh trên MinIO S3, cờ đánh dấu ảnh chính (is_primary), thứ tự hiển thị và kích thước tệp.", "Bảng recipe_images")
    add_bullet(doc, "Quản lý token làm mới: chuỗi token băm SHA-256, thời gian hết hạn, thời điểm thu hồi (revoked_at), địa chỉ IP và User-Agent nhằm ngăn chặn tấn công Replay Attack.", "Bảng refresh_tokens")

    add_sec_heading(doc, "2.6. Kiến trúc hệ thống Clean Architecture 4 tầng")
    add_body_paragraph(doc, "Nhằm đáp ứng các tiêu chuẩn kiến trúc phần mềm quốc tế, mã nguồn Backend được cấu trúc chặt chẽ theo nguyên lý Clean Architecture 4 tầng phân tách độc lập:")
    add_bullet(doc, "Chứa các Business Entities thuần túy, định nghĩa các ngoại lệ nghiệp vụ độc lập framework (Domain Exceptions: EntityNotFoundException, RecipeConcurrencyException, TokenReuseDetectedException...) và các Value Objects.", "1. Domain Layer (app/domain)")
    add_bullet(doc, "Chứa các giao diện trừu tượng (Interfaces / Protocols), Generic Base Repository, RecipeRepository, UserRepository và mẫu thiết kế Unit of Work điều phối giao dịch ACID bảo đảm tính nhất quán dữ liệu.", "2. Application Layer (app/repositories & app/services)")
    add_bullet(doc, "Hiện thực chi tiết công nghệ kết nối ngoại vi: SQLAlchemy ORM mapping, AsyncPG driver, dịch vụ lưu trữ đám mây MinIO S3 Storage, dịch vụ gửi thư SMTP/MailHog, và cấu hình xoay vòng nhật ký RotatingFileHandler.", "3. Infrastructure Layer (app/core & app/services)")
    add_bullet(doc, "Điểm tiếp nhận yêu cầu từ client: RESTful API routers (v1), kiểm thực và chuẩn hóa dữ liệu đầu vào/ra qua Pydantic DTO Schemas v2, Middleware xử lý ngoại lệ tập trung RFC 7807, Rate Limiting và Correlation-ID.", "4. Presentation Layer (app/api/v1)")

    # -------------------------------------------------------------------------
    # CHƯƠNG 3
    # -------------------------------------------------------------------------
    add_chapter_heading(doc, "CHƯƠNG 3. CÁC ĐẶC TẢ KỸ THUẬT VÀ GIẢI PHÁP CỐT LÕI")
    
    add_sec_heading(doc, "3.1. Kiểm soát xung đột đồng thời (Optimistic Concurrency Control)")
    add_body_paragraph(doc, "Trong hệ thống chia sẻ công thức ẩm thực, tình huống hai người dùng hoặc tác giả cùng truy cập và cập nhật một bài viết tại cùng một thời điểm rất dễ xảy ra, dẫn đến hiện tượng \"mất mát cập nhật\" (Lost Update). Để giải quyết triệt để vấn đề này mà không cần khóa cứng CSDL (Pessimistic Locking gây suy giảm hiệu năng), hệ thống áp dụng kỹ thuật Optimistic Concurrency Control (OCC) dựa trên trường rowVersion dạng UUID.")
    add_body_paragraph(doc, "Mỗi khi công thức được tạo mới hoặc chỉnh sửa thành công, hệ thống tự động sinh một mã UUID ngẫu nhiên mới gán vào rowVersion. Khi client gửi yêu cầu PATCH/PUT, bắt buộc phải đính kèm giá trị rowVersion mà client đang nắm giữ. Tại tầng Repository, câu lệnh UPDATE được thực thi với điều kiện WHERE id = :id AND row_version = :expected_version. Nếu câu lệnh trả về số hàng ảnh hưởng bằng 0, hệ thống ngay lập tức ném ra ngoại lệ RecipeConcurrencyException và trả về mã lỗi HTTP 409 Conflict chuẩn RFC 7807, ngăn chặn hoàn toàn việc vô tình ghi đè dữ liệu của người khác.")

    add_sec_heading(doc, "3.2. Bảo mật xác thực JWT kép & Chống phát lại Refresh Token")
    add_body_paragraph(doc, "Hệ thống triển khai cơ chế xác thực kép kết hợp giữa Access Token (thời gian sống ngắn, 15 phút, lưu tại bộ nhớ RAM) và Refresh Token (thời gian sống dài, 7 ngày, bảo vệ chống giả mạo):")
    add_bullet(doc, "Mỗi khi client gọi API làm mới phiên (/auth/refresh), hệ thống thu hồi ngay lập tức Refresh Token cũ và phát hành một cặp token hoàn toàn mới.", "Cơ chế xoay vòng Token (Token Rotation)")
    add_bullet(doc, "Nếu một Refresh Token đã từng bị thu hồi lại được gửi lên máy chủ (dấu hiệu kẻ tấn công đã đánh cắp token và cố gắng sử dụng lại), hệ thống sẽ kích hoạt ngoại lệ TokenReuseDetectedException, lập tức thu hồi toàn bộ các Refresh Token của người dùng đó và buộc đăng nhập lại từ đầu.", "Phát hiện tấn công phát lại (Replay Attack Detection)")
    add_bullet(doc, "Hỗ trợ đăng nhập nhanh qua Google OAuth 2.0 Identity Provider, xác thực tính hợp lệ của Google ID Token phía máy chủ và tự động đồng bộ tài khoản người dùng.", "Xác thực xã hội Google OAuth 2.0")

    add_sec_heading(doc, "3.3. Tối ưu tìm kiếm toàn văn tiếng Việt (Full-Text Search unaccent)")
    add_body_paragraph(doc, "Tìm kiếm công thức nấu ăn bằng tiếng Việt thường gặp trở ngại lớn do tính đa dạng của dấu thanh và cách gõ bàn phím (VNI, Telex, không dấu). Việc dùng mệnh đề LIKE hoặc ILIKE truyền thống sẽ gây quét toàn bộ bảng (Table Scan), làm nghẽn hệ thống khi dữ liệu tăng cao.")
    add_body_paragraph(doc, "Hệ thống kích hoạt tiện ích mở rộng unaccent và pg_trgm trên PostgreSQL 16. Cột dữ liệu tìm kiếm được kết hợp từ tiêu đề, mô tả và tên nguyên liệu, chuyển đổi thành véc-tơ văn bản tsvector không dấu. Kết hợp với chỉ mục GIN (Generalized Inverted Index), tốc độ phản hồi tìm kiếm đạt mức < 15ms cho hơn hàng trăm nghìn bản ghi, hỗ trợ chính xác cả truy vấn có dấu (\"phở bò\") lẫn không dấu (\"pho bo\").")

    add_sec_heading(doc, "3.4. Kiến trúc xử lý tác vụ ngầm & Lập lịch định kỳ (Background Jobs)")
    add_body_paragraph(doc, "Để đảm bảo API luôn phản hồi nhanh chóng (dưới 100ms) mà không bị nghẽn bởi các tác vụ nặng, hệ thống tách rời các xử lý tốn tài nguyên sang luồng tác vụ ngầm (Background Tasks & APScheduler):")
    add_bullet(doc, "Khi người dùng đăng ký tài khoản thành công, tác vụ ngầm được khởi tạo để soạn thảo email định dạng MIME HTML kèm lời chào mừng cá nhân hóa và gửi qua máy chủ SMTP mà không chặn phản hồi đăng ký của người dùng.", "Gửi Email Chào mừng (FR-JOB-001)")
    add_bullet(doc, "Sau khi ảnh gốc được tải lên MinIO, thư viện Pillow sẽ tự động xử lý cắt, nén và sinh phiên bản ảnh thu nhỏ (thumbnail 300x300 pixels), tối ưu hóa băng thông tải trang cho client.", "Tự động sinh ảnh Thumbnail (FR-JOB-002)")
    add_bullet(doc, "Lập trình viên tích hợp thư viện APScheduler với CronTrigger chạy định kỳ mỗi đêm lúc 00:00 (hoặc kích hoạt tức thì), tự động truy vấn CSDL và kết xuất tệp sitemap.xml chuẩn phục vụ tối ưu hóa công cụ tìm kiếm Google.", "Tạo Sitemap.xml định kỳ (FR-JOB-003)")

    add_sec_heading(doc, "3.5. Kiểm soát tần suất truy cập (Rate Limiting) & Chuẩn hóa lỗi RFC 7807")
    add_body_paragraph(doc, "Để bảo vệ hệ thống khỏi các đợt tấn công từ chối dịch vụ (DoS) và vét cạn mật khẩu (Brute-Force), Middleware kiểm soát tần suất truy cập được cấu hình theo thuật toán Sliding-Window dựa trên Redis:")
    add_bullet(doc, "Tối đa 10 lượt yêu cầu/phút cho phân hệ Auth, 5 lượt yêu cầu/phút cho chức năng upload ảnh, và 100 lượt yêu cầu/phút cho các API chung. Khi vượt quá ngưỡng, hệ thống trả về mã lỗi HTTP 429 Too Many Requests kèm tiêu đề Retry-After.", "Phân ngưỡng Rate Limiting")
    add_bullet(doc, "Mọi lỗi phát sinh trong hệ thống (Validation Error, Domain Exception, HTTP Exception) đều được bắt tập trung và định dạng theo chuẩn quốc tế RFC 7807 Problem Details (Content-Type: application/problem+json) gồm: type, title, status, detail, instance và correlation_id.", "Chuẩn hóa lỗi RFC 7807")

    add_sec_heading(doc, "3.6. Truy vết luồng dữ liệu & Giám sát hệ thống (Structured Logging & Probes)")
    add_body_paragraph(doc, "Hệ thống tích hợp Middleware tự động sinh mã định danh duy nhất (Correlation ID) cho mỗi yêu cầu HTTP đến, lưu trữ vào ContextVar và gắn vào tiêu đề X-Correlation-ID của phản hồi. Mọi bản ghi nhật ký (logs) đều được ghi có cấu trúc với thời gian, cấp độ lỗi, Correlation ID và thông điệp.")
    add_body_paragraph(doc, "Đồng thời, hệ thống cung cấp các endpoint probe chuẩn Kubernetes: /health (kiểm tra trạng thái chung), /health/live (Liveness Probe kiểm tra tiến trình sống), và /health/ready (Readiness Probe kiểm tra kết nối CSDL PostgreSQL và Redis), đảm bảo khả năng tự phục hồi khi triển khai trên cụm container.")

    # -------------------------------------------------------------------------
    # CHƯƠNG 4
    # -------------------------------------------------------------------------
    add_chapter_heading(doc, "CHƯƠNG 4. HƯỚNG DẪN CÀI ĐẶT VÀ SỬ DỤNG ỨNG DỤNG (DEMO SẢN PHẨM)")
    
    add_sec_heading(doc, "4.1. Hướng dẫn cài đặt và vận hành hệ thống qua Docker Compose")
    add_body_paragraph(doc, "Hệ thống Culinary Blog được container hóa toàn diện, cho phép khởi động toàn bộ môi trường từ cơ sở dữ liệu đến giao diện người dùng chỉ với vài thao tác cơ bản:")
    
    # Bảng phân phối cổng
    tbl_ports = doc.add_table(rows=1, cols=4)
    tbl_ports.style = 'Table Grid'
    set_table_borders(tbl_ports)
    p_hdr = tbl_ports.rows[0].cells
    p_hdr[0].text = "Dịch vụ"
    p_hdr[1].text = "Cổng máy chủ (Host)"
    p_hdr[2].text = "Cổng container"
    p_hdr[3].text = "Mục đích sử dụng"
    for c in p_hdr:
        set_cell_margins(c, 80, 80, 100, 100)
        set_cell_shading(c, "E2E8F0")
        for p in c.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.bold = True
                r.font.name = "Times New Roman"
                r.font.size = Pt(10.5)

    port_data = [
        ("Nginx Gateway", "80", "80", "Điểm đón tiếp lưu lượng chính của toàn hệ thống"),
        ("Frontend Web", "3000", "80", "Giao diện người dùng React 19 SPA"),
        ("FastAPI Backend", "8000", "8000", "Máy chủ RESTful API & Swagger UI Docs"),
        ("PostgreSQL 16", "5433", "5432", "Cơ sở dữ liệu quan hệ chính của ứng dụng"),
        ("Redis 7 Alpine", "6381", "6379", "Bộ nhớ đệm Cache & Rate Limiting Storage"),
        ("MinIO Storage", "9000", "9000", "API lưu trữ tệp tin tương thích AWS S3"),
        ("MinIO Console", "9001", "9001", "Giao diện web quản trị bucket lưu trữ"),
        ("MailHog Web UI", "8026", "8025", "Giao diện duyệt hộp thư kiểm thử email ngầm")
    ]
    for srv, hp, cp, desc in port_data:
        row = tbl_ports.add_row()
        row.cells[0].text = srv
        row.cells[1].text = hp
        row.cells[2].text = cp
        row.cells[3].text = desc
        for idx, c in enumerate(row.cells):
            set_cell_margins(c, 50, 50, 80, 80)
            for p in c.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                if idx in [1, 2]:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(10)

    add_body_paragraph(doc, "Quy trình khởi động hệ thống từng bước:")
    add_bullet(doc, "Sao chép mã nguồn từ repository: git clone https://github.com/NHNam1209/PTUDW-2026-Nhom25.git && cd PTUDW-2026-Nhom25", "Bước 1. Clone mã nguồn")
    add_bullet(doc, "Cấu hình biến môi trường: Sao chép tệp .env.example thành .env và giữ nguyên cấu hình cổng chuẩn.", "Bước 2. Cấu hình môi trường")
    add_bullet(doc, "Khởi động toàn bộ container: docker compose up -d --build", "Bước 3. Xây dựng & Chạy Docker")
    add_bullet(doc, "Nạp dữ liệu mẫu hoàn chỉnh (22 danh mục, 105 công thức mẫu kèm nguyên liệu và hẹn giờ): docker exec -it culinary_api python seed.py", "Bước 4. Seed dữ liệu")
    add_bullet(doc, "Chạy bộ kiểm thử tự động xác minh: docker exec -it culinary_api pytest (kết quả 11/11 bài test PASS 100%).", "Bước 5. Kiểm thử hệ thống")

    add_sec_heading(doc, "4.2. Hướng dẫn sử dụng cho Độc giả")
    add_body_paragraph(doc, "Độc giả truy cập vào địa chỉ http://localhost:3000 hoặc http://localhost (thông qua cổng Nginx). Giao diện trang chủ chào đón người dùng bằng biểu ngữ hiện đại, danh sách danh mục nổi bật và các công thức nấu ăn mới nhất.")
    
    add_figure(doc, "demo_01_homepage.png", "Hình 4.1. Giao diện Trang chủ hệ thống ẩm thực Culinary Blog")
    add_figure(doc, "demo_02_recipes_list.png", "Hình 4.2. Màn hình duyệt danh sách công thức nấu ăn & bộ lọc đa tiêu chí")
    
    add_body_paragraph(doc, "Khi nhấp vào một món ăn bất kỳ, độc giả được dẫn tới trang chi tiết. Tại đây, độc giả có thể tùy chỉnh số khẩu phần ăn để hệ thống tự động tính toán lại khối lượng nguyên liệu tương ứng. Người dùng có thể nhấn nút \"Bắt đầu hẹn giờ\" tại từng bước nấu để đồng hồ đếm ngược kích hoạt, có âm thanh thông báo khi hoàn thành.")
    
    add_figure(doc, "demo_03_recipe_detail.png", "Hình 4.3. Màn hình chi tiết công thức, định lượng nguyên liệu & bộ đếm hẹn giờ nấu")
    add_figure(doc, "demo_04_categories_overview.png", "Hình 4.4. Danh mục khám phá món ăn ẩm thực phong phú (22 danh mục)")
    add_figure(doc, "demo_05_category_detail.png", "Hình 4.5. Chi tiết danh mục và danh sách công thức thuộc danh mục")
    add_figure(doc, "demo_06_search_results.png", "Hình 4.6. Kết quả tìm kiếm toàn văn tiếng Việt không dấu (PostgreSQL FTS unaccent)")

    add_sec_heading(doc, "4.3. Hướng dẫn sử dụng cho Tác giả ẩm thực")
    add_body_paragraph(doc, "Để bắt đầu sáng tạo nội dung, người dùng nhấn nút \"Đăng nhập\" hoặc \"Đăng ký\" trên thanh điều hướng. Hệ thống hỗ trợ đăng nhập nhanh bằng tài khoản Google chỉ với 1 cú nhấp chuột, hoặc đăng ký tài khoản cục bộ với cơ chế kiểm tra độ mạnh mật khẩu theo thời gian thực.")
    
    add_figure(doc, "demo_07_login_page.png", "Hình 4.7. Màn hình Đăng nhập hệ thống & Tích hợp đăng nhập nhanh Google OAuth 2.0")
    add_figure(doc, "demo_08_register_page.png", "Hình 4.8. Màn hình Đăng ký tài khoản tác giả ẩm thực kèm kiểm tra mật khẩu")
    
    add_body_paragraph(doc, "Sau khi đăng nhập thành công với vai trò Tác giả, người dùng có quyền truy cập vào Creator Dashboard. Bảng điều khiển tổng hợp thống kê số lượng công thức cá nhân, số lượt xem và biểu đồ tương tác.")
    
    add_figure(doc, "demo_09_creator_dashboard.png", "Hình 4.9. Creator Dashboard - Bảng điều khiển tác giả & thống kê số liệu bài viết")
    add_figure(doc, "demo_10_recipe_management.png", "Hình 4.10. Bảng quản lý công thức và vòng đời trạng thái (Draft / Publish / Archived)")
    add_figure(doc, "demo_11_recipe_editor.png", "Hình 4.11. Bộ biên tập công thức nấu ăn chuyên sâu đa bước (Recipe Editor Wizard)")

    add_sec_heading(doc, "4.4. Hướng dẫn sử dụng cho Quản trị viên")
    add_body_paragraph(doc, "Tài khoản Quản trị viên (admin@culinaryblog.com) sở hữu quyền quản trị cao nhất trên toàn hệ thống. Quản trị viên có thể trực tiếp thêm mới, đổi tên hoặc xóa các danh mục ẩm thực, đồng thời theo dõi toàn bộ danh sách thành viên trong hệ thống.")
    
    add_figure(doc, "demo_12_category_admin.png", "Hình 4.12. Màn hình Quản trị viên quản lý danh mục món ăn (Category Admin)")
    add_figure(doc, "demo_13_users_management.png", "Hình 4.13. Màn hình Quản trị viên quản lý danh sách người dùng (Users Management)")

    add_sec_heading(doc, "4.5. Giám sát hạ tầng kỹ thuật và Tài liệu API")
    add_body_paragraph(doc, "Hệ thống cung cấp đầy đủ các cổng giao tiếp dành cho kỹ sư vận hành và lập trình viên tích hợp:")
    add_bullet(doc, "Địa chỉ http://localhost:8000/docs hiển thị toàn bộ 45+ API endpoints được nhóm theo phân hệ chuẩn OpenAPI, cho phép gửi yêu cầu thử nghiệm trực tiếp.", "Tài liệu Swagger UI")
    add_bullet(doc, "Địa chỉ http://localhost:8000/health cung cấp thông tin kiểm tra sức khỏe của PostgreSQL, Redis và MinIO theo thời gian thực.", "Health Check Probes")
    add_bullet(doc, "Địa chỉ http://localhost:8026 cho phép duyệt các email HTML chào mừng được gửi ngầm tự động khi có thành viên mới đăng ký.", "MailHog SMTP Dashboard")
    add_bullet(doc, "Địa chỉ http://localhost:9001 cung cấp bảng điều khiển quản trị các bucket tệp tin hình ảnh đã tải lên.", "MinIO S3 Console")

    add_figure(doc, "demo_14_swagger_docs.png", "Hình 4.14. Tài liệu đặc tả API tương tác trực quan Swagger UI (FastAPI OpenAPI)")
    add_figure(doc, "demo_15_health_probe.png", "Hình 4.15. Kiểm tra tình trạng sức khỏe hệ thống (Health Check Probe)")
    add_figure(doc, "demo_16_mailhog_ui.png", "Hình 4.16. Hộp thư MailHog kiểm thử gửi email ngầm chào mừng người dùng")
    add_figure(doc, "demo_17_minio_console.png", "Hình 4.17. Giao diện quản lý lưu trữ đối tượng MinIO Object Storage Console")

    # -------------------------------------------------------------------------
    # KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
    # -------------------------------------------------------------------------
    add_chapter_heading(doc, "KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN")
    
    add_sec_heading(doc, "1. Kết luận")
    add_body_paragraph(doc, "Trải qua quá trình nghiên cứu, phân tích đặc tả yêu cầu chuẩn quốc tế (IEEE 830 / ISO 29148) và triển khai thực tế, Nhóm 25 đã hoàn thành xuất sắc toàn bộ các mục tiêu đặt ra cho đồ án \"Hệ thống ứng dụng web chia sẻ, khám phá và quản lý công thức ẩm thực (Culinary Blog System)\".")
    add_body_paragraph(doc, "Các kết quả nổi bật đạt được bao gồm:")
    add_bullet(doc, "Hoàn thành 100% các yêu cầu chức năng (45 Functional Requirements từ FR-AUTH, FR-RCP, FR-CAT, FR-SRCH, FR-FILE, FR-JOB đến FR-OBS) và các yêu cầu phi chức năng về hiệu năng và bảo mật.", "Mức độ hoàn thiện chức năng")
    add_bullet(doc, "Hiện thực chuẩn mực mô hình Clean Architecture 4 tầng tại Backend, áp dụng các mẫu thiết kế hướng đối tượng Repository và Unit of Work, phân tách ranh giới nghiệp vụ rõ ràng và dễ bảo trì.", "Chất lượng kiến trúc phần mềm")
    add_bullet(doc, "Giải quyết triệt để các bài toán kỹ thuật phức tạp: Kiểm soát xung đột ghi đè đồng thời (OCC rowVersion), Bảo mật JWT kép chống Replay Attack, Tìm kiếm toàn văn PostgreSQL unaccent, Xử lý tác vụ ngầm APScheduler & Pillow, và Sliding-Window Rate Limiting.", "Giải pháp kỹ thuật chuyên sâu")
    add_bullet(doc, "Giao diện React 19 hiện đại, thân thiện, tương thích đa thiết bị, đạt chuẩn trải nghiệm người dùng với các tiện ích thiết thực (đổi khẩu phần động, bấm giờ nấu ăn).", "Trải nghiệm người dùng")
    add_bullet(doc, "Tự động hóa hoàn toàn quy trình đóng gói và triển khai qua Docker Compose, tích hợp bộ kiểm thử tự động với tỷ lệ pass 100%.", "Sẵn sàng vận hành thực tế")

    add_sec_heading(doc, "2. Hướng phát triển")
    add_body_paragraph(doc, "Nhằm tiếp tục nâng cao giá trị ứng dụng và hướng tới việc thương mại hóa trên diện rộng, hệ thống có thể tiếp tục mở rộng theo các hướng nghiên cứu sau:")
    add_bullet(doc, "Tích hợp mô hình ngôn ngữ lớn (LLM như Gemini API) để tự động gợi ý món ăn dựa trên nguyên liệu sẵn có trong tủ lạnh của người dùng và tính toán kế hoạch thực đơn tuần.", "Tích hợp Trí tuệ Nhân tạo (AI)")
    add_bullet(doc, "Bổ sung chức năng bình luận nhiều cấp, đánh giá sao, chấm điểm độ ngon và người dùng tải ảnh thành phẩm món ăn thực tế đã nấu.", "Tính năng Mạng xã hội ẩm thực")
    add_bullet(doc, "Phát triển phiên bản ứng dụng di động đa nền tảng (React Native / Flutter) sử dụng chung hệ thống RESTful API hiện tại để tối ưu trải nghiệm người dùng trên thiết bị cầm tay.", "Mở rộng Ứng dụng Di động")
    add_bullet(doc, "Kết nối với các sàn thương mại điện tử hoặc dịch vụ giao hàng thực phẩm để người dùng có thể mua nhanh toàn bộ giỏ nguyên liệu của món ăn chỉ với một cú nhấp chuột.", "Tích hợp Thương mại điện tử")

    # -------------------------------------------------------------------------
    # PHÂN CÔNG CÔNG VIỆC
    # -------------------------------------------------------------------------
    add_chapter_heading(doc, "PHÂN CÔNG CÔNG VIỆC")
    
    add_body_paragraph(doc, "Bảng tổng hợp phân công trách nhiệm, danh mục chức năng chi tiết và tỷ lệ hoàn thành công việc của tất cả các thành viên trong Nhóm 25 đối với Đồ án Culinary Blog:")
    
    # Bảng phân công chi tiết
    tbl_assign = doc.add_table(rows=1, cols=6)
    tbl_assign.style = 'Table Grid'
    set_table_borders(tbl_assign)
    a_hdr = tbl_assign.rows[0].cells
    a_hdr[0].text = "STT"
    a_hdr[1].text = "MSSV"
    a_hdr[2].text = "Họ và tên"
    a_hdr[3].text = "Vai trò"
    a_hdr[4].text = "Hạng mục công việc được giao"
    a_hdr[5].text = "Tiến độ"
    for c in a_hdr:
        set_cell_margins(c, 80, 80, 100, 100)
        set_cell_shading(c, "E2E8F0")
        for p in c.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.bold = True
                r.font.name = "Times New Roman"
                r.font.size = Pt(10.5)

    assignments = [
        ("1", "2312694", "Nguyễn Hoài Nam", "Trưởng nhóm / Backend Lead / DevOps",
         "• Thiết kế kiến trúc tổng thể Clean Architecture 4 tầng cho Backend FastAPI.\n"
         "• Hiện thực phân hệ Xác thực bảo mật: Đăng ký, Đăng nhập local, Google OAuth 2.0, JWT Rotation, chống Replay Attack.\n"
         "• Xây dựng phân hệ Công thức (Recipe Module): CRUD, phân trang, lọc đa tiêu chí, chuyển trạng thái vòng đời.\n"
         "• Cài đặt cơ chế kiểm soát xung đột đồng thời Optimistic Concurrency Control (rowVersion UUID).\n"
         "• Thiết lập hạ tầng Docker Compose, Nginx Gateway, mạng nội bộ và script Seeding 105 công thức mẫu.\n"
         "• Xây dựng bộ Unit & Integration Tests (11 bài test pass 100%).", "100%"),
        
        ("2", "2312584", "Đỗ Duy Biên", "Backend Developer / Data Specialist",
         "• Xây dựng phân hệ Danh mục ẩm thực (Category Module): CRUD API, thống kê số lượng công thức, quản lý danh mục cha-con.\n"
         "• Tối ưu hóa công cụ tìm kiếm toàn văn tiếng Việt PostgreSQL Full-Text Search với unaccent và tsvector.\n"
         "• Phát triển dịch vụ lưu trữ tệp tin MinIO S3 Object Storage Service (xác thực MIME, magic bytes, giới hạn 5MB).\n"
         "• Hiện thực các Background Jobs: Gửi email chào mừng (FR-JOB-001), sinh ảnh thumbnail tự động (FR-JOB-002), Cron job sitemap.xml (FR-JOB-003).\n"
         "• Xây dựng hệ thống Structured Logging với Correlation ID và ContextVar.", "100%"),
        
        ("3", "2312676", "Hoàng Thăng Long", "Frontend Lead / UI-UX Developer",
         "• Xây dựng giao diện Trang chủ công khai (Homepage): Banner ẩm thực, công thức thịnh hành, danh mục nổi bật.\n"
         "• Phát triển Màn hình duyệt danh sách công thức (Recipe Catalog) kèm bộ lọc đa tiêu chí và phân trang động.\n"
         "• Hiện thực Màn hình chi tiết món ăn (Recipe Detail View): Tính toán định lượng nguyên liệu theo số khẩu phần, tích hợp đồng hồ bấm giờ nấu ăn theo từng bước (Cooking Timer).\n"
         "• Xây dựng Màn hình xem bài viết theo Danh mục ẩm thực (Category Pages) và Màn hình kết quả tìm kiếm (Search Results).\n"
         "• Phát triển Giao diện Đăng nhập (tích hợp nút Google OAuth), Đăng ký tài khoản và Trang hồ sơ cá nhân tác giả.", "100%"),
        
        ("4", "2212437", "Trần Chánh Phát", "Frontend Developer / Dashboard Specialist",
         "• Xây dựng Màn hình Creator Dashboard: Tổng quan thống kê bài viết, lượt xem và biểu đồ tương tác của tác giả.\n"
         "• Phát triển Bảng quản lý công thức cá nhân (Recipe Management Table) với các tab trạng thái Draft/Publish/Archived.\n"
         "• Hiện thực Bộ soạn thảo công thức nấu ăn đa bước chuyên sâu (Recipe Creation & Edit Wizard) kèm bộ đếm thời gian.\n"
         "• Xây dựng Component tải ảnh kéo thả ImageUploader kết nối trực tiếp MinIO S3, gán ảnh đại diện chính.\n"
         "• Phát triển Màn hình Quản trị viên: Quản trị danh mục ẩm thực (Category Admin) và Quản lý danh sách người dùng (Users Management).", "100%")
    ]

    for stt, mssv, name, role, tasks, progress in assignments:
        row = tbl_assign.add_row()
        row.cells[0].text = stt
        row.cells[1].text = mssv
        row.cells[2].text = name
        row.cells[3].text = role
        row.cells[4].text = tasks
        row.cells[5].text = progress
        for idx, c in enumerate(row.cells):
            set_cell_margins(c, 50, 50, 80, 80)
            for p in c.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                if idx in [0, 1, 5]:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(10)
                    if idx == 5:
                        r.bold = True
                        r.font.color.rgb = RGBColor(0x16, 0x65, 0x34) # Green color

    add_body_paragraph(doc, "Liên kết Repository chứa toàn bộ mã nguồn, tài liệu và lịch sử commit của Đồ án:")
    p_link = doc.add_paragraph()
    p_link.paragraph_format.left_indent = Inches(0.3)
    r_l1 = p_link.add_run("GitHub Repository: ")
    r_l1.bold = True
    r_l1.font.name = "Times New Roman"
    r_l2 = p_link.add_run("https://github.com/NHNam1209/PTUDW-2026-Nhom25.git")
    r_l2.font.name = "Times New Roman"
    r_l2.underline = True
    r_l2.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)

    # -------------------------------------------------------------------------
    # DANH MỤC TÀI LIỆU THAM KHẢO
    # -------------------------------------------------------------------------
    add_chapter_heading(doc, "DANH MỤC TÀI LIỆU THAM KHẢO")
    
    refs = [
        "IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements Specifications, IEEE Computer Society, 1998.",
        "ISO/IEC/IEEE 29148:2018, Systems and software engineering - Life cycle processes - Requirements engineering, 2018.",
        "Robert C. Martin, Clean Architecture: A Craftsman's Guide to Software Structure and Design, Prentice Hall, 2017.",
        "Martin Fowler, Patterns of Enterprise Application Architecture, Addison-Wesley Professional, 2002.",
        "Tiangolo, FastAPI Documentation - Modern, High-Performance Web Framework for Python, https://fastapi.tiangolo.com/.",
        "React Official Documentation, The Library for Web and Native User Interfaces (React 19), https://react.dev/.",
        "PostgreSQL Global Development Group, PostgreSQL 16 Documentation: Full Text Search & Extensions, https://www.postgresql.org/docs/16/.",
        "IETF RFC 7807, Problem Details for HTTP APIs, Internet Engineering Task Force, 2016, https://tools.ietf.org/html/rfc7807.",
        "IETF RFC 6749, The OAuth 2.0 Authorization Framework, Internet Engineering Task Force, 2012, https://tools.ietf.org/html/rfc6749.",
        "MinIO Object Storage Documentation, High Performance Object Storage for AI & Cloud Native, https://min.io/docs/minio/linux/index.html."
    ]
    for r in refs:
        p_ref = doc.add_paragraph()
        p_ref.style = doc.styles['Normal']
        p_ref.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_ref.paragraph_format.left_indent = Inches(0.35)
        p_ref.paragraph_format.space_before = Pt(0)
        p_ref.paragraph_format.space_after = Pt(3)
        p_ref.paragraph_format.line_spacing = 1.2
        r_num = p_ref.add_run(f"[{refs.index(r)+1}]  ")
        r_num.bold = True
        r_num.font.name = "Times New Roman"
        r_num.font.size = Pt(11)
        r_txt = p_ref.add_run(r)
        r_txt.font.name = "Times New Roman"
        r_txt.font.size = Pt(11)

    # Lưu tài liệu ra các đường dẫn mong muốn
    print(f"Saving report to {OUTPUT_PATH_1}...")
    doc.save(OUTPUT_PATH_1)
    
    print(f"Saving report to {OUTPUT_PATH_2}...")
    doc.save(OUTPUT_PATH_2)
    
    print(f"Saving report to {OUTPUT_PATH_V4}...")
    doc.save(OUTPUT_PATH_V4)
    
    print("ALL REPORTS GENERATED AND SAVED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
