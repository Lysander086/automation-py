FROM_WORKSPACE_ROOT = r'C:\Users\inz\Desktop\winDev\qcEast\boBang\bobang-client'  # from
# TO_WORKSPACE_ROOT = r'C:\Users\inz\Desktop\winDev\qcEast\boBang\bobang-mer-test'  # to destination (for test)
TO_WORKSPACE_ROOT = r'C:\Users\inz\Desktop\winDev\qcEast\boBang\bobang-merhcant'  # to destination

to_reverse = False  # is to copy from to_workspace to to from_workspace


# directories to synchronize, sort alphabetically asc
to_sync_dirs_list = [
    r'utilPy',
    r'pages/chatting',
    r'pages/displayDetails',
    r'pages/launch',
    r'pages/location',
    r'util/rongCloud',
    r'util/reuse',
    # r'util/newSDK' # would raise Permission Denied, it's ok to ignore this dir
]

# files to synchronize, sort alphabetically asc
to_sync_files_list = [
    r'App.vue',
    r'.gitignore',
    r'双端共用代码(双端一致).md',
    r'PROJECT.md',
    r'components/myHouseCard.vue',
    r'components/sHouseCard.vue',
    r'pages/textDetails.vue',
    r'util/commonFuncs.js',
    r'util/misc.js',
    r'util/network.js',
]


to_sync_again = False # 实时更新代码
# sync every ? second
sync_frequency = 30

to_thorough_copy = False #  to_thorough_copy作用: 会把文件夹下多余的文件删除