import os

def rename_files(directory_path):
    # 获取当前脚本所在的目录
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # 构建相对路径
    relative_directory_path = os.path.join(script_directory, directory_path)

    # 遍历目录中的文件
    for filename in os.listdir(relative_directory_path):
        # 检查文件名是否以 _republic 结尾
        if filename.endswith('_republic.tga'):
            # 构建新文件名
            new_filename = filename.replace('_republic.tga', '_nationalist.tga')
            # 获取文件的完整路径
            old_file = os.path.join(relative_directory_path, filename)
            new_file = os.path.join(relative_directory_path, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} -> {new_file}')

# 指定要操作的目录
directory_path = 'flags'
rename_files(directory_path)