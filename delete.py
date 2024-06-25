import os
import fnmatch


def delete_files(file_patterns, root_dir='.'):
    """
    删除指定目录及其子目录中所有匹配文件模式的文件。

    :param file_patterns: 需要删除的文件模式列表（例如 ['*.html', '*.csv']）
    :param root_dir: 根目录，默认为当前目录
    """
    for root, dirs, files in os.walk(root_dir):
        for pattern in file_patterns:
            for filename in fnmatch.filter(files, pattern):
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")


if __name__ == '__main__':
    # 定义要删除的文件模式
    patterns_to_delete = ['*.html', '*.csv']
    # 开始删除文件
    delete_files(patterns_to_delete)
