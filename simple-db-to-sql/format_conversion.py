import os

# 定义替换和删除操作
def replace_in_file(input_file, output_file, db_name):
    # 获取脚本所在的目录路径
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # 构建输入和输出文件的绝对路径
    input_file_path = os.path.join(script_directory, input_file)
    output_file_path = os.path.join(script_directory, output_file)

    # 检查输入文件是否存在
    if not os.path.exists(input_file_path):
        print(f"文件 {input_file_path} 不存在！")
        return

    # 读取文件内容
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 执行替换操作
    content = content.replace('INTEGER', 'INT')
    content = content.replace('VARCHAR', 'TEXT')
    content = content.replace('"', '`')

    # 替换 BEGIN TRANSACTION 为 CREATE DATABASE IF NOT EXISTS db_name; USE db_name;
    content = content.replace('BEGIN TRANSACTION;', f'CREATE DATABASE IF NOT EXISTS {db_name};\nUSE {db_name};')

    # 删除 COMMIT;
    content = content.replace('COMMIT;', '')

    # 保存修改后的内容到输出文件
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"替换和删除操作完成！修改后的文件保存在 {output_file_path}")

# 获取用户输入的数据库名称
db_name = input("请输入数据库名称：")

# 获取相对路径的输入输出文件
input_file = 'lexiko.sql'
output_file = db_name + '.sql'

# 调用函数进行替换
replace_in_file(input_file, output_file, db_name)
