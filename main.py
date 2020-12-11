import os, shutil
from pathlib import Path

from config import setInterval, sync_frequency, to_reverse, to_sync_files_list

# files and dirs to sync
from config import to_sync_dirs_list, FROM_WORKSPACE_ROOT, TO_WORKSPACE_ROOT


def judge_to_swap(left, right):
    if not to_reverse:
        return left, right
    else:
        return right, left


def sync_dirs():
    for directory in to_sync_dirs_list:
        t_from = Path(FROM_WORKSPACE_ROOT + '\\' + directory)
        t_to = Path(TO_WORKSPACE_ROOT + '\\' + directory)
        t_from, t_to = judge_to_swap(t_from, t_to)
        shutil.copytree(t_from, t_to)


def sync_files():
    for file_name in to_sync_files_list:
        file_from = Path(FROM_WORKSPACE_ROOT + '\\' + file_name)
        file_to = Path(TO_WORKSPACE_ROOT + '\\' + file_name)
        file_from, file_to = judge_to_swap(file_from, file_to)
        # if the file does not exist, create it
        if not os.path.exists(file_to):
            file_to.parents[0].mkdir(parents=True, exist_ok=True)
        shutil.copy(file_from, file_to)


@setInterval(sec=sync_frequency)
def go_sync(times):
    print('complete ' + times.__str__() + ' times')
    times += 1


def entry():
    times = 1
    go_sync(times)
    # sync_dirs()
    # sync_files()


# read input from terminal: https://blog.csdn.net/PPLLO_o/article/details/99057765

if __name__ == '__main__':
    entry()
