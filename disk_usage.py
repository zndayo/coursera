import shutil
import os

def check_disk_usage(path):
    """Check disk usage for a given path."""
    total, used, free = shutil.disk_usage(path)
    print(f"Disk usage for {path}:")
    print(f"  Total: {total // (2**30)} GB")
    print(f"  Used:  {used // (2**30)} GB")
    print(f"  Free:  {free // (2**30)} GB")

if __name__ == "__main__":
    # Check disk usage for the current directory
    current_dir = os.getcwd()
    check_disk_usage(current_dir)
    home_dir = os.path.expanduser("~")
    check_multiple_paths([current_dir, home_dir])


