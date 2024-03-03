import os

def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    
    print("Directories:")
    print(directories)
    
    print("\nFiles:")
    print(files)
    
    print("\nAll Directories and Files:")
    print(os.listdir(path))

# Example usage:
path = "/your/specified/path"
list_directories_files(path)
