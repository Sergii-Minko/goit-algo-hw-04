from pathlib import Path

# Creating a Path object for the directory
directory = Path("./picture2/new_folder")

# Check if the directory exists
if directory.exists() and directory.is_dir():
    # Output the list of all files and subdirectories
    for path in directory.iterdir():
        print(path)
else:
    if not directory.exists():
    # Якщо директорія не існує, створюємо її
        directory.mkdir(parents=True, exist_ok=True)
        print("The directory does not exist.")


directory = Path("/my_directory/new_folder")
directory.mkdir(parents=True, exist_ok=True)
