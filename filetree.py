import os

def print_directory_tree(root_path, indent=""):
    """
    Recursively prints the directory tree starting from the given root path.
    """
    print(f"{indent} {os.path.basename(root_path)}/")

    for entry in os.listdir(root_path):
        entry_path = os.path.join(root_path, entry)
        if os.path.isdir(entry_path):
            print_directory_tree(entry_path, indent + "  ")
        else:
            print(f"{indent}  {entry}")

base_directory = os.path.dirname(os.path.abspath(__file__))

print_directory_tree(base_directory)