from pdf2image import convert_from_path
import pytesseract
import os

# 获取当前文件所在目录（即子文件夹的路径）
current_dir = os.path.dirname(os.path.abspath(__file__))

# 配置 Tesseract 的路径（Windows 用户需指定路径）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

poppler_path = os.path.join(current_dir, r'poppler-24.08.0\Library\bin')

def extract_text_from_image_pdf(pdf_path, output_file, lang="rus"):
    try:
        # Step 1: 将 PDF 转换为图片
        images = convert_from_path(pdf_path, poppler_path=poppler_path)
        
        # Step 2: 使用 OCR 处理每张图片
        text = ""
        for i, image in enumerate(images):
            print(f"正在处理第 {i + 1} 页...")
            text += pytesseract.image_to_string(image, lang=lang) + "\n"
        
        # Step 3: 将提取的文本保存到文件
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)
        
        print(f"提取的文本已保存到: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# 示例用法
pdf_path = os.path.join(current_dir, "Winnie the Pooh.pdf")  # 替换为你的 PDF 文件路径
output_file = os.path.join(current_dir, "Winnie the Pooh.txt")  # 保存结果的文件名
extract_text_from_image_pdf(pdf_path, output_file)
