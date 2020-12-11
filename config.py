FROM_WORKSPACE_ROOT = r'C:\Users\inz\Desktop\winDev\qcEast\boBang\bobang-client'  # from
TO_WORKSPACE_ROOT = r'C:\Users\inz\Desktop\winDev\qcEast\boBang\bobang-mer-test'  # to destination (for test)
# to_workspace = r'C:\Users\inz\Desktop\winDev\qcEast\boBang\bobang-merhcant'  # to destination

to_reverse = False  # is to copy from to_workspace to to from_workspace

''' list of paths from root to dir
    sort alphabetically asc
'''
to_sync_dirs_list = [
    r'pages/chatting',
    r'pages/displayDetails',
    r'pages/launch',
    r'pages/location',
    r'util/rongCloud',
    r'util/reuse',
    r'util/newSDK'
]

to_sync_files_list = [
    r'.gitignore',
    r'PROJECT.md',
    r'components/myHouseCard.vue',
    r'components/sHouseCard.vue',
    r'pages/textDetails.vue',
    r'util/commonFuncs.js',
    r'util/misc.js',
    r'util/network.js',
]


# sync every ? second
sync_frequency = 60

import functools
import sched, time

s = sched.scheduler(time.time, time.sleep)

def setInterval(sec):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*argv, **kw):
            setInterval(sec)(func)
            func(*argv, **kw)

        s.enter(sec, 1, wrapper, ())
        return wrapper

    s.run()
    return decorator
