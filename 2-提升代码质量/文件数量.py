import os

def file_num(folder_path):
    """
    计算指定文件夹下面的文件数量
    :param folder_path: 文件夹路径
    :return: 文件数量
    """
    count = 0
    for root, dirs, files in os.walk(folder_path):
        count += len(dirs)
    return count


folder_path = './'
num_folders = file_num(folder_path)
print('文件数量为：', num_folders)
