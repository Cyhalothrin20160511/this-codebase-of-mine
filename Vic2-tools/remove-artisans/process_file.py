import os
import re

def process_file(file_path):
    try:
        # Open the file in read mode with 'gbk' encoding
        with open(file_path, 'r', encoding='gbk') as file:
            content = file.read()
            
        # Read the file content again
        with open(file_path, 'r', encoding='gbk') as file:
            content = file.read()

        # Use regex to remove the matched part
        content = re.sub(r'artisans\s*=\s*{[^}]*}\n', '', content)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(content)
            
    except UnicodeDecodeError as e:
        print(f"Error decoding file {file_path}: {e}")
        # Handle or ignore the error

def process_directory(directory_path):
    # Get the current script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the relative directory path
    relative_directory_path = os.path.join(script_directory, directory_path)

    # Recursively walk through the directory
    for root, dirs, files in os.walk(relative_directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Process each file
            process_file(file_path)

# Start processing the directory
process_directory('1861.4.14')
