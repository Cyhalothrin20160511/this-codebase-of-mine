import os

def rename_files(directory_path):
    # Get the current script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the relative directory path
    relative_directory_path = os.path.join(script_directory, directory_path)

    # Iterate through the files in the directory
    for filename in os.listdir(relative_directory_path):
        # Check if the filename ends with '_republic.tga'
        if filename.endswith('_republic.tga'):
            # Construct the new filename
            new_filename = filename.replace('_republic.tga', '_nationalist.tga')
            # Get the full path of the old file and the new file
            old_file = os.path.join(relative_directory_path, filename)
            new_file = os.path.join(relative_directory_path, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} -> {new_file}')

# Specify the directory to operate on
directory_path = 'flags'
rename_files(directory_path)
