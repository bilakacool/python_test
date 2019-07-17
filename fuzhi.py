# coding=utf-8


# 递归删除文件夹
def shanchu(wenjianjia):
    """递归删除一个文件夹"""
    import os

    # 遍历文件夹中的文件，是文件则直接删除，是文件夹则继续遍历
    for wenjian in os.listdir(wenjianjia):
        a = wenjianjia+'/'+wenjian
        if os.path.isfile(a):
            os.remove(a)
        elif os.path.isdir(a):
            shanchu(a)
    os.rmdir(wenjianjia)


# 复制文件old到new中
def fuzhi(old, new):
    """复制文件old或文件夹old到文件夹new中"""

    import os
    from pathlib import Path

    # 调整old和new的格式
    old, new = old.replace('\\', '/'), new.replace('\\', '/')
    if new[-1] == '/':
        new = new[:-1]
    if old[-1] == '/':
        old = old[:-1]

    # 检查old和new是否存在
    if (not os.path.isfile(old) and not os.path.isdir(old)) or (not os.path.isdir(new) and not os.path.isfile(new)):
        print('该文件不存在')
        return

    # 文件名字被占用时的名字
    fuben = '-副本'

    # 如果old是文件则直接复制到new
    if Path(old).is_file():
        wenjian = old.split('/')[-1]
        oldwenjian = open(old, 'rb')
        newwenjian = open(new + '/%s' % wenjian, 'wb')
        newwenjian.writelines(oldwenjian)
        oldwenjian.close()
        newwenjian.close()
        print('%s文件复制成功' % wenjian)
        return

    # 如果new在old目录中会造成死循环
    if old in new or new == old:

        # 将old中文件复制到old同目录中
        newnew = old[:-(old[::-1].find('/')+1)]
        newold = fuzhi(old, newnew)

        # 将复制的old文件复制到new中
        oldnew = fuzhi(newold, new)

        # 名字重复则建立副本
        oldname = old.split('/')[-1]
        while oldname in os.listdir(new):
            oldname = oldname + fuben

        # 将new中的文件名修改为old同名，如果old在new中存在则修改为副本名字
        os.rename(oldnew, new+'/'+oldname)

        # 删除中间文件
        shanchu(newold)
        return

    # 如果old文件夹已存在则创建新名字的文件夹
    oldname = old.split('/')[-1]
    while oldname in os.listdir(new):
        oldname = oldname + fuben
    os.mkdir(new+'/'+oldname)

    # 如果old是文件夹则遍历路径中所有文件并复制
    for wenjian in os.listdir(old+'/'):

        # 如果遍历对象是文件则拷贝文件
        if Path(old+'/'+wenjian).is_file():
            oldwenjian = open('%s/%s' % (old, wenjian), 'rb')
            newwenjian = open(new+'/%s/%s' % (oldname, wenjian), 'wb')
            newwenjian.writelines(oldwenjian)
            oldwenjian.close()
            newwenjian.close()
            print('%s文件复制成功' % wenjian)

        # 如果遍历对象是文件夹则递归执行遍历
        if Path(old+'/'+wenjian).is_dir():
            oldlujing, newlujing = old+'/'+wenjian, new+'/'+oldname
            fuzhi(oldlujing, newlujing)
    return new+'/'+oldname


old = input('请输入要复制的文件：')
new = input('请输入要复制的位置：')
fuzhi(old, new)

