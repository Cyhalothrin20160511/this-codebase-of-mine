import os

# Define the replacement and deletion operations
def replace_in_file(input_file, output_file, db_name):
    # Get the directory path of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute paths for the input and output files
    input_file_path = os.path.join(script_directory, input_file)
    output_file_path = os.path.join(script_directory, output_file)

    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print(f"File {input_file_path} does not exist!")
        return

    # Read the content of the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Perform replacement operations
    content = content.replace('INTEGER', 'INT')
    content = content.replace('VARCHAR', 'TEXT')
    content = content.replace('"', '`')

    # Replace BEGIN TRANSACTION with CREATE DATABASE IF NOT EXISTS db_name; USE db_name;
    content = content.replace('BEGIN TRANSACTION;', f'CREATE DATABASE IF NOT EXISTS {db_name};\nUSE {db_name};')

    # Remove COMMIT;
    content = content.replace('COMMIT;', '')

    # Save the modified content to the output file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Replacement and deletion operations completed! The modified file is saved as {output_file_path}")

# Get the database name from the user
db_name = input("Please enter the database name: ")

# Specify the relative paths for the input and output files
input_file = 'lexiko.sql'
output_file = db_name + '.sql'

# Call the function to perform replacements
replace_in_file(input_file, output_file, db_name)
