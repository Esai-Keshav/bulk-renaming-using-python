import os

def bulk_rename(folder_path, file_extension='.jpeg'):
    folder_path = os.path.abspath(folder_path)

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Get all files with the specified extension in the folder
    files_to_rename = [f for f in os.listdir(folder_path) if f.endswith(file_extension)]

    for index, old_file_name in enumerate(files_to_rename, start=1):
        # Decode the file name to handle Unicode characters (not necessary for ASCII characters)
        old_file_name = os.fsdecode(old_file_name)

        # Split the file name and extension
        file_name, file_ext = os.path.splitext(old_file_name)

        # Generate the new file name by appending an incremental number
        new_file_name = f"{index}{file_extension}"
        
        # Create the full paths for the old and new files
        old_file_path = os.path.join(folder_path, old_file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)

        # Print the renaming details
        print(f"Renamed: {old_file_name} -> {new_file_name}")

if __name__ == "__main__":
    folder_path = r'C:/Users/user/Desktop/Create_Images_Using_Video/Task 3'
    bulk_rename(folder_path)
