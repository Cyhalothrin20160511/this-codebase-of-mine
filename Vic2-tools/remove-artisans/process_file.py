import os
import re

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='gbk') as file:
            content = file.read()
            
        # 读取文件内容
        with open(file_path, 'r', encoding='gbk') as file:
            content = file.read()

        # 使用正则表达式删除匹配的部分
        content = re.sub(r'artisans\s*=\s*{[^}]*}\n', '', content)

        # 将修改后的内容写回文件
        with open(file_path, 'w') as file:
            file.write(content)
            
    except UnicodeDecodeError as e:
        print(f"Error decoding file {file_path}: {e}")
        # 处理错误或者忽略错误


def process_directory(directory_path):
    # 获取当前脚本所在的目录
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # 构建相对路径
    relative_directory_path = os.path.join(script_directory, directory_path)

    # 递归遍历文件夹
    for root, dirs, files in os.walk(relative_directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            # 处理每个文件
            process_file(file_path)


# 替换 'your_directory' 为你要处理的文件夹的实际路径
# process_directory('your_directory')
process_directory('1861.4.14')
