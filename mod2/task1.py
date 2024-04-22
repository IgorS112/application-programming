def get_summary_rss(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        total_rss_bytes = 0
        for line in lines:
            columns = line.split()
            rss_bytes = int(columns[5])
            total_rss_bytes += rss_bytes
    summary_rss = convert_bytes(total_rss_bytes)
    return summary_rss

def convert_bytes(size, precision=2):
    suffixes = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    index = 0
    while size > 1024 and index < len(suffixes)-1:
        size /= 1024.0
        index += 1
    return f'{size:.{precision}f} {suffixes[index]}'

if __name__ == "__main__":
    file_path = 'output_file.txt'
    summary_rss = get_summary_rss(file_path)
    print(f'Summary RSS: {summary_rss}')
