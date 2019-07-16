# coding=utf-8


def fuzhi(old,new):
    """复制文件old或文件夹old到文件夹new中"""

    import os
    from pathlib import Path

    # 检查old和new是否存在
    while not os.path.isfile(old) and not os.path.isfile(new) and not os.path.isdir(old) and not os.path.isdir(new):
        print('该文件不存在')
        return

    # 调整old和new的格式
    old, new = old.replace('\\', '/'), new.replace('\\', '/')

    # 检查new和old是否在同一目录中
    if new in old or old in new or new == old:
        print('复制的文件和源文件不可以在同一路径中')
        return

    # 如果old是文件则直接复制到new
    if Path(old).is_file():
        # if '.' in old.split('/')[-1]:
        wenjian = old.split('/')[-1]
        oldwenjian = open(old, 'rb')
        newwenjian = open(new + '/%s' % wenjian, 'wb')
        newwenjian.writelines(oldwenjian)
        oldwenjian.close()
        newwenjian.close()
        print('%s文件复制成功' % wenjian)
        return

    # 如果old文件夹已存在则不在new中创建old
    if old.split('/')[-1] not in os.listdir(new+'/'):
        os.mkdir(new+'/'+old.split('/')[-1])

    # 如果old是文件夹则遍历路径中所有文件并复制
    for wenjian in os.listdir(old+'/'):

        # 如果遍历对象是文件则拷贝文件
        if Path(old+'/'+wenjian).is_file():
            # if '.' in wenjian:
            wenjianlujing = old.split('/')[-1]
            oldwenjian = open('%s/%s' % (old, wenjian), 'rb')
            newwenjian = open(new+'/%s/%s' % (wenjianlujing, wenjian), 'wb')
            newwenjian.writelines(oldwenjian)
            oldwenjian.close()
            newwenjian.close()
            print('%s文件复制成功' % wenjian)

        # 如果遍历对象是文件夹则进入此文件夹再次执行遍历
        if Path(old+'/'+wenjian).is_dir():
            # if '.' not in wenjian:
            oldlujing, newlujing = old+'/'+wenjian, new+'/'+old.split('/')[-1]+'/'
            fuzhi(oldlujing, newlujing)


old = input('请输入要复制的文件：')
new = input('请输入要复制的位置：')
fuzhi(old, new)











