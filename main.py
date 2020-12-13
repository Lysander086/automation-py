import os, shutil, stat
from pathlib import Path

from config import sync_frequency, to_reverse, to_sync_files_list, to_sync_again, to_thorough_copy
from decorator import setInterval

# files and dirs to sync
from config import to_sync_dirs_list, FROM_WORKSPACE_ROOT, TO_WORKSPACE_ROOT


def judge_to_swap(left, right):
    if not to_reverse:
        return left, right
    else:
        return right, left


def remove_readonly(func, path, _):
    """Clear the readonly bit and reattempt the removal"""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise


def sync_dirs():
    for directory in to_sync_dirs_list:
        from_path = Path(FROM_WORKSPACE_ROOT + '\\' + directory)
        to_path = Path(TO_WORKSPACE_ROOT + '\\' + directory)
        from_path, to_path = judge_to_swap(from_path, to_path)

        if to_thorough_copy and to_path.exists():
            # shutil.rmtree(to_path, onerror=onerror) # would raise Permission Error
            # os.system('rmdir /S /Q "{}"'.format(to_path))
            os.system('rimraf "{}"'.format(to_path))

        shutil.copytree(from_path, to_path, dirs_exist_ok=True)


def sync_files():
    for file_name in to_sync_files_list:
        file_from = Path(FROM_WORKSPACE_ROOT + '\\' + file_name)
        file_to = Path(TO_WORKSPACE_ROOT + '\\' + file_name)
        file_from, file_to = judge_to_swap(file_from, file_to)
        # if the file does not exist, create it
        if not os.path.exists(file_to):
            file_to.parents[0].mkdir(parents=True, exist_ok=True)
        shutil.copy(file_from, file_to)


times = 0


def show_times():
    global times
    times += 1
    print('synced ' + times.__str__() + ' times')


@setInterval(sec=sync_frequency)
def sync_again():
    sync_files()
    sync_dirs()
    show_times()


def entry():
    sync_files()
    sync_dirs()
    show_times()
    if to_sync_again:
        sync_again()


# read input from terminal: https://blog.csdn.net/PPLLO_o/article/details/99057765

if __name__ == '__main__':
    entry()
