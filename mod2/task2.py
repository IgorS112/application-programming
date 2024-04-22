import sys

def get_mean_size():
    lines = sys.stdin.readlines()[1:]
    total_size = 0
    num_files = 0
    for line in lines:
        columns = line.split()
        if len(columns) > 4:
            size = int(columns[4])
            total_size += size
            num_files += 1
    if num_files == 0:
        return "No files found or unable to get file sizes."
    mean_size = total_size / num_files
    return mean_size

if __name__ == "__main__":
    mean_size = get_mean_size()
    print(f"Mean size of files: {mean_size}")
