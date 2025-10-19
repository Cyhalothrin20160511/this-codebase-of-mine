import os

def clean_and_rename_tga(directory_path):
    # Get the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the target directory path
    target_directory = os.path.join(script_directory, directory_path)

    # Iterate over files in the directory
    for filename in os.listdir(target_directory):
        if filename.endswith(".tga"):
            file_path = os.path.join(target_directory, filename)

            # 1. Delete .tga files without an underscore (e.g., ENG.tga)
            if "_" not in filename.replace(".tga", ""):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
                continue

            # 2. Rename *_republic.tga to *.tga
            if filename.endswith("_republic.tga"):
                new_filename = filename.replace("_republic.tga", ".tga")
                new_file_path = os.path.join(target_directory, new_filename)

                # If the target file already exists, remove it to avoid conflicts
                if os.path.exists(new_file_path):
                    os.remove(new_file_path)
                    print(f"Removed existing: {new_file_path}")

                os.rename(file_path, new_file_path)
                print(f"Renamed: {file_path} -> {new_file_path}")


# Specify the directory to operate on (e.g., "flags" folder)
directory_path = "flags"
clean_and_rename_tga(directory_path)
