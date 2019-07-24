# coding=utf-8


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


def fuben(old, new, fuben='副本'):
    """如果new文件夹中有old文件，则将文件名返回old-fuben"""
    import os

    # oldname = old.split('/')[-1]
    oldname = os.path.basename(old)
    while oldname in os.listdir(new):
        oldname = oldname+'-'+fuben
    return oldname


def geshi(wenjian):
    """将文件名调整为统一格式"""
    wenjian = wenjian.replace('\\', '/')
    if wenjian[-1] == '/':
        wenjian = wenjian[:-1]
    return wenjian


def fuzhiwenjian(old, new):
    """将文件old复制到new中"""
    import os

    # wenjian = old.split('/')[-1]
    wenjian = os.path.basename(old)
    if wenjian in os.listdir(new):
        print('%s文件已存在' % wenjian)
        return
    oldwenjian = open(old, 'rb')
    newwenjian = open(new + '/%s' % wenjian, 'xb')
    newwenjian.writelines(oldwenjian)
    oldwenjian.close()
    newwenjian.close()
    print('%s文件复制成功' % wenjian)


def fuzhi(old, new):
    """复制文件old或文件夹old到文件夹new中"""
    import os
    from pathlib import Path

    # 检查old和new是否存在
    if (not os.path.isfile(old) and not os.path.isdir(old)) or (not os.path.isdir(new)):
        print('复制的文件或复制的位置不存在')
        return

    # 调整old和new的格式
    old = geshi(old)
    new = geshi(new)

    # 如果old是文件则直接复制到new
    if Path(old).is_file():
        fuzhiwenjian(old, new)
        return

    # 如果new在old目录中会造成死循环
    if old in new or new == old:

        # 将old中文件复制到old同目录中,再将复制的文件复制到new中，再删除中间文件
        # newnew = old[:-(old.reverse.find('/')+1)]
        newnew = os.path.dirname(old)
        newold = fuzhi(old, newnew)
        oldnew = fuzhi(newold, new)
        shanchu(newold)

        # 将new中的文件名修改为old同名，如果old在new中存在则修改为副本名字
        oldname = fuben(old, new)
        os.rename(oldnew, new+'/'+oldname)
        return

    else:
        # 在new中创建old文件夹，如果old文件夹已存在则创建副本文件夹
        oldname = fuben(old, new)
        os.mkdir(new+'/'+oldname)

        # 如果old是文件夹则遍历路径中所有文件并复制
        for wenjian in os.listdir(old+'/'):

            # 如果遍历对象是文件则拷贝文件
            if Path(old+'/'+wenjian).is_file():
                fuzhiwenjian(old+'/'+wenjian, new+'/'+oldname)

            # 如果遍历对象是文件夹则递归执行遍历
            if Path(old+'/'+wenjian).is_dir():
                oldlujing, newlujing = old+'/'+wenjian, new+'/'+oldname
                fuzhi(oldlujing, newlujing)

        # 返回新的文件new文件路径以便递归使用
        return new+'/'+oldname


old = input('请输入要复制的文件：')
new = input('请输入要复制的位置：')
fuzhi(old, new)
