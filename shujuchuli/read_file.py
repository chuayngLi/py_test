from docx import Document
import os
import pandas as pd
import xlrd


def read_docx(file_path):
    doc = Document(file_path)
    paragraphs = [p.text for p in doc.paragraphs]
    return '\n'.join(paragraphs)


def read_xls(file_path):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)
    rows = []
    for row_idx in range(sheet.nrows):
        row = [sheet.cell_value(row_idx, col_idx) for col_idx in range(sheet.ncols)]
        rows.append('\t'.join(map(str, row)))
    return '\n'.join(rows)


def traverse_directory(directory, output_file):
    for root, _, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            if name.endswith(".docx"):
                output_file.write(f"File: {file_path}\n")
                output_file.write(read_docx(file_path))
                output_file.write("\n\n")
            elif name.endswith(".xlsx"):
                output_file.write(f"File: {file_path}\n")
                df = pd.read_excel(file_path)
                output_file.write(df.to_string())
                output_file.write("\n\n")
            elif name.endswith(".xls"):
                output_file.write(f"File: {file_path}\n")
                output_file.write(read_xls(file_path))
                output_file.write("\n\n")


read_name = "初中、小学、幼儿园教师资格认定（个人）"
command = '\\教育局（1）\\' + read_name
path = f'D:\\浏览器下载\\ai\\邗江区政务门牌事项梳理（114）\\邗江区政务门牌事项梳理（114）{command}'

output_file_path = './file/' + read_name + '.txt'
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

with open(output_file_path, 'a+', encoding="utf-8") as file:
    traverse_directory(path, file)
