# -*- coding: utf-8 -*-
"""
Script to generate Tai_Lieu_On_Tap_Thi_Cuoi_Ky_Culinary_Blog.docx
Comprehensive, professionally formatted Word document for exam defense.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

WORKSPACE_DIR = r"D:\PTUDWNC\PTUDW-2026-Nhom25"
OUTPUT_DOCX = os.path.join(WORKSPACE_DIR, "Tai_Lieu_On_Tap_Thi_Cuoi_Ky_Culinary_Blog.docx")

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
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(20)
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
    run.font.size = Pt(13)
    run.italic = True
    run.font.color.rgb = GRAY
    return p

def add_h1(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(15)
    run.bold = True
    run.font.color.rgb = NAVY
    return p

def add_h2(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12.5)
    run.bold = True
    run.font.color.rgb = BLUE_ACCENT
    return p

def add_p(text, bold_prefix="", indent=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.25
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.25)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(11.5)
        r_pre.bold = True
        r_pre.font.color.rgb = DARK_SLATE
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11.5)
    run.font.color.rgb = DARK_SLATE
    return p

def add_bullet(text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.2
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(11.5)
        r_pre.bold = True
        r_pre.font.color.rgb = DARK_SLATE
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11.5)
    run.font.color.rgb = DARK_SLATE
    return p

def add_callout(text, title="LƯU Ý QUAN TRỌNG:"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    set_cell_shading(cell, "EFF6FF")
    
    # Left border blue
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
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

# ----------------- BUILD CONTENT -----------------

add_title("BỘ TÀI LIỆU ÔN TẬP VÀ ĐÁP ÁN BẢO VỆ CUỐI KỲ")
add_subtitle("Đồ án: Hệ thống Blog Ẩm thực và Nấu ăn (Culinary Blog) — Nhóm 25\n"
             "Môn học: Phát triển ứng dụng web nâng cao — GVHD: TS. Nguyễn Thị Lương\n"
             "Thành viên: Nguyễn Hoài Nam (Lead), Đỗ Duy Biên, Hoàng Thăng Long, Trần Chánh Phát")

add_callout(
    "Tài liệu này được biên soạn bám sát 100% mã nguồn thực tế của dự án Nhóm 25, tài liệu đặc tả SRS v1.0.0 "
    "và bộ câu hỏi ôn tập thi cuối kỳ gồm 3 phần: Phần I - 20 câu hỏi Lý thuyết, Phần II - Báo cáo & Giải thích mã nguồn, "
    "Phần III - 9 bài toán Mở rộng giải quyết vấn đề.",
    "HƯỚNG DẪN ÔN TẬP:"
)

# Read markdown content from TAI_LIEU_ON_TAP_THI_CUOI_KY.md
md_path = os.path.join(WORKSPACE_DIR, "TAI_LIEU_ON_TAP_THI_CUOI_KY.md")
with open(md_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

in_code_block = False
code_lines = []

for line in lines:
    s = line.strip()
    if not s and not in_code_block:
        continue
    
    if s.startswith("```"):
        if in_code_block:
            in_code_block = False
            # write code box
            code_text = "\n".join(code_lines)
            code_lines = []
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
            run.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
            doc.add_paragraph().paragraph_format.space_after = Pt(3)
        else:
            in_code_block = True
            code_lines = []
        continue

    if in_code_block:
        code_lines.append(line.rstrip("\n\r"))
        continue

    if s.startswith("# "):
        add_h1(s[2:].upper())
    elif s.startswith("## "):
        add_h1(s[3:])
    elif s.startswith("### "):
        add_h2(s[4:])
    elif s.startswith("#### "):
        add_p(s[5:], bold_prefix="▶ ")
    elif s.startswith("* ") or s.startswith("- "):
        content = s[2:]
        if "**" in content:
            parts = content.split("**")
            if len(parts) >= 3 and content.startswith("**"):
                add_bullet(parts[2].lstrip(": "), bold_prefix=parts[1] + ": ")
            else:
                add_bullet(content.replace("**", ""))
        else:
            add_bullet(content)
    elif s.startswith("1. ") or s.startswith("2. ") or s.startswith("3. ") or s.startswith("4. ") or s.startswith("5. ") or s.startswith("6. ") or s.startswith("7. ") or s.startswith("8. ") or s.startswith("9. "):
        num_prefix = s[:3]
        content = s[3:]
        if "**" in content:
            parts = content.split("**")
            if len(parts) >= 3 and content.startswith("**"):
                add_p(parts[2].lstrip(": "), bold_prefix=num_prefix + parts[1] + ": ")
            else:
                add_p(content.replace("**", ""), bold_prefix=num_prefix)
        else:
            add_p(content, bold_prefix=num_prefix)
    elif s.startswith("|"):
        # simple table row, skip markdown separators
        if "---" in s:
            continue
        # regular text
        add_p(s.replace("|", "  ").strip())
    else:
        # plain paragraph
        if s.startswith("**") and "**" in s[2:]:
            parts = s.split("**")
            add_p(parts[2].lstrip(": "), bold_prefix=parts[1] + ": ")
        else:
            add_p(s.replace("**", ""))

doc.save(OUTPUT_DOCX)
print("Saved DOCX successfully:", OUTPUT_DOCX)
