# coding=utf-8


# 小星星
def xing():
    """显示星星"""

    print('*' * 30)


# 游戏流程
def caiquan():
    """返回游戏的结果，0为平局，1为胜利，-1为失败,2为退回，-2为输入错误"""
    import random

    # 得到电脑和玩家的出拳内容
    jiqiren = random.randint(1, 3)
    xing()
    wanjia = input('布为1 * 剪刀为2 * 拳头为3 * 回到首页为0\n请输入：')
    xing()
    if wanjia == '0':
        return 2

    # 打印玩家出拳结果
    elif wanjia == '3':
        print('玩家是拳头')
    elif wanjia == '1':
        print('玩家是布')
    elif wanjia == '2':
        print('玩家是剪刀')

    # 输入错误判断
    else:
        return -2

    # 打印电脑出拳结果
    if jiqiren == 3:
        print('电脑是拳头')
    elif jiqiren == 1:
        print('电脑是布')
    elif jiqiren == 2:
        print('电脑是剪刀')

    # 胜利判断
    if (wanjia == '3' and jiqiren == 2) or \
            (wanjia == '1' and jiqiren == 3) or \
            (wanjia == '2' and jiqiren == 1):
        return 1
    # 平局判断
    elif wanjia == str(jiqiren):
        return 0
    # 失败判断
    else:
        return -1


# 游戏首页
def shouye():
    """游戏首页，返回0为退出游戏，返回1为开始游戏，返回2为查看榜单，返回0为输入错误"""
    xing()
    kaishi = input("开始游戏请按1\n查看榜单请按2\n结束游戏请按0\n请输入：")

    if kaishi == '1':
        return 1
    elif kaishi == '0':
        return 0
    elif kaishi == '2':
        return 2
    else:
        return -1


# 写入游戏结果
def bangdan(mingzi, gaofen, gaolian):
    """根据名字，得分，连胜制作榜单"""
    import os

    # 创建本场游戏榜单列表
    bangdan = []
    bangdan.append(mingzi)
    bangdan.append(gaofen)
    bangdan.append(gaolian)

    # 首次创建榜单文件
    if 'bangdan.txt' not in os.listdir(os.getcwd()):
        bang = open('./bangdan.txt', 'a')
        bang.write('名次排行\t玩家名字\t最高得分\t最高连胜\n')
        bang.close()

    # 将榜单数据写入榜单文件
    bang = open('./bangdan.txt', 'a')
    bang.write('无\t\t' + bangdan[0] + '\t\t' + bangdan[1] + '\t\t' + bangdan[2] + '\n')
    bang.close()


# 对榜单中的数据进行排序
def paixu():
    """将榜单中数据按照得分情况进行排序"""

    # 将排行榜数据存入列表中
    bang = open('./bangdan.txt', 'r')
    id = 0
    bang2 = []
    bang3 = []
    for i in bang.readlines():

        # 将排行榜数据列表再存入大列表中
        if id != 0:
            bang2.append(i.split('\t'))

        # 将榜单的首行字段列表保存
        else:
            bang3 = i.split('\t')
        id += 1

    # 将玩家数据列表按照分数从高到低排序
    for j in range(len(bang2)):
        for k in range(len(bang2)):
            if int(bang2[j][4][:-1]) > int(bang2[k][4][:-1]):
                bang2[j], bang2[k] = bang2[k], bang2[j]
    bang.close()

    # 将排序后的玩家数据写入游戏结果
    bang = open('./bangdan.txt', 'w')

    # 写入首行字段
    bang.write(bang3[0]+'\t'+bang3[1]+'\t'+bang3[2]+'\t'+bang3[3])

    # 写入玩家数据和名次
    for i in range(len(bang2)):
        n = str(i+1)
        bang.write('第'+n+'名'+'\t\t'+bang2[i][2]+'\t\t'+bang2[i][4]+'\t\t'+bang2[i][6])
    bang.close()


# 将榜单数据进行备份
def beifen():
    """将榜单中的历史数据进行备份"""
    import os
    import time

    # 创建备份文件夹
    if 'beifen' not in os.listdir(os.getcwd()):
        os.mkdir('beifen')

    # 创建以当前时间命名备份文件
    beifen = open('./bangdan.txt', 'rb')
    a = time.strftime('%Y-%m-%d %H.%M.%S')
    beifen1 = open('./beifen/bangdan%s.txt' % a, 'wb')

    # 将数据备份
    beifen1.writelines(beifen)
    beifen.close()
    beifen1.close()


# 读取游戏结果
def bang(shuliang=10):
    """输入显示榜单的数量，读取游戏榜单到屏幕上"""
    import os

    # 榜单为空判断
    if 'bangdan.txt' not in os.listdir(os.getcwd()):
        print('榜单目前为空')
        return

    # 展示榜单
    print('排行榜仅展示前%d名成绩' % shuliang)
    bang = open('bangdan.txt', 'r')

    # 展示排行榜前几名
    j = 0
    for i in bang.readlines():
        if j <= shuliang:
            j += 1
            # 去掉末尾的换行符
            print(i[:-1])


# 游戏开始
def kaishi(mingzi='游客', defen=3, changci=10, liansheng=0, gaolian=0):
    """输入玩家用户名，开始猜拳游戏"""

    # 初始分判断
    if defen <= 0:
        print('\n初始分数太低了。。。\n\n游戏结束')
        return

    # 最高积分定义
    gaofen = defen

    # 定义场次
    changci1 = changci
    xing()
    print('游戏规则：进行%d场游戏后结束\n本场游戏的初始分为：%d分' % (changci, defen))

    # 进入游戏判断
    while defen > 0:

        # 进入游戏判断
        xuanze = shouye()
        if xuanze == 0:
            break
        if xuanze == -1:
            xing()
            print('输入有误，请重新输入')
            continue
        if xuanze == 2:
            xing()
            bang()
            continue

        # 游戏正式开始
        while changci1 > 0:
            jieguo = caiquan()

            # 异常游戏判断
            if jieguo == 2:
                print('回到首页，\n您当前得分为：%d分' % defen)
                break
            if jieguo == -2:
                print('输入有误，请重新输入')
                continue

            # 平局结果
            if jieguo == 0:
                print('打平了！！！')
                liansheng = 0
                changci1 -= 1

            # 胜利结果
            if jieguo == 1:
                print('胜利了！！！')
                liansheng += 1
                defen = defen + liansheng

                # 最高分和最高连胜判断
                if liansheng > gaolian:
                    gaolian = liansheng
                if defen > gaofen:
                    gaofen = defen

                # 当前连胜
                if liansheng > 1:
                    print('恭喜获得%d连胜' % liansheng)
                print('本场得分加%d分' % liansheng)
                changci1 -= 1

            # 失败结果
            if jieguo == -1:
                print('失败了！！！')
                defen -= 1
                liansheng = 0
                changci1 -= 1

            # 游戏后统计积分
            print('您当前得分为：%d分' % defen)

            # 胜利后超过10分判断
            if jieguo == 1 and defen >= 10:
                print('你是真的好牛逼啊！！！')

            # 分数为0，游戏结束
            if defen <= 0:
                xing()
                print('好菜啊，分数用光了。。。')
                break
            if changci1 == 0:
                xing()
                print('%d场游戏进行完毕' % changci)
        if changci1 == 0:
            break

    # 进行游戏后输出游戏结果
    if changci1 != changci:
        xing()
        print('本场最高得分为%d分' % gaofen)
        if gaolian > 0:
            print('最高连胜为%d连胜' % gaolian)
        else:
            print('未取得连胜')

        # 保存游戏记录
        mingzi = str(mingzi)
        gaofen = str(gaofen)
        gaolian = str(gaolian)
        bangdan(mingzi, gaofen+'分', gaolian + '连胜')
        xing()
        paixu()
        beifen()
        print('游戏记录已保存')

    # 游戏结束
    xing()
    print('\n游戏结束')


# 主页界面
def zhuye():
    """输入主页操作，返回3为游客模式，返回1为登陆账号，返回2为注册账号，返回4登录最近的账号，返回0退出游戏,返回-1输入错误"""

    xing()
    # 输入登陆操作
    zhuye = input('登录账号请按1\n注册账号请按2\n游客模式请按3\n快速登录请按4\n退出游戏请按0\n请输入：')
    if zhuye == '3':
        return 3
    if zhuye == '1':
        return 1
    if zhuye == '2':
        return 2
    if zhuye == '0':
        return 0
    if zhuye == '4':
        return 4
    else:
        return -1


# 进入游戏
def denglu():
    """登录并进入游戏"""
    # 进入游戏首页
    print('*' * 10 + '猜拳小游戏' + '*' * 10, end="\n\n")

    zhanghao = 0
    while 1:
        denglu = zhuye()
        if denglu == -1:
            print('输入错误，请重新输入')
            continue
        if denglu == 0:
            xing()
            print('\n退出游戏')
            break
        if denglu == 2:
            while zhuce(6) == 0:
                continue
            continue
        if denglu == 1:
            zhanghao = yonghu()
            if zhanghao == 0:
                xing()
                print('用户名或密码不正确 ')
                continue
            xing()
            print('用户%s登录成功，开始游戏' % zhanghao)
            kaishi(zhanghao)
            continue
        if denglu == 3:
            xing()
            print('进入游客模式，开始游戏')
            kaishi()
            continue
        if denglu == 4:
            if zhanghao == 0:
                xing()
                print('最近没有登录账号')
                continue
            xing()
            print('用户%s登录成功，开始游戏' % zhanghao)
            kaishi(zhanghao)
            continue


# 账号注册
def zhuce(long):
    """输入用户名最大长度，注册账号，并将账号存储在文本中"""
    import os
    xing()

    # 输入用户名
    zhanghao = input('请输入注册用户名：')

    # 账号存储文档不存在时创建文档
    if 'yonghu.txt' not in os.listdir(os.getcwd()):
        yonghu = open('yonghu.txt', 'w')
        yonghu.close()

    # 将文档中的用户名集中到一个列表中
    yonghu = open('yonghu.txt', 'r')
    a = []
    for i in yonghu.readlines():
        a.extend(i.split('\t'))
        a = a[::2]
    yonghu.close()

    # 如果用户名存在则需要重新输入
    if zhanghao in a:
        xing()
        print('此账号已存在,请重新输入')
        return 0

    # 用户名为空则需要重新输入
    if zhanghao == ''
        xing()
        print('账号不可为空')
        return 0

    # 用户名过长时需要重新输入
    if len(zhanghao) > long:
        xing()
        print('用户名过长，请重新输入')
        return 0

    # 输入注册账号的密码
    mima = input('请输入注册密码：')

    # 确认用户名和密码
    queren = input('注册的用户为%s,密码为%s,确认请按1：' % (zhanghao, mima))
    if queren == '1':
        yonghu = open('yonghu.txt', 'a')
        yonghu.write('%s\t%s\n' % (zhanghao, mima))
        yonghu.close()
    else:
        xing()
        print('注册已取消')
    return


# 账号登录
def yonghu():
    """登陆账号"""

    # 输入用户名和密码
    xing()
    zhanghao = input('请输入用户名：')
    mima = input('请输入密码：')

    # 将用户名和密码组合成指定格式的字符串
    a = zhanghao+'\t'+mima+'\n'

    # 用户名或密码不正确判断
    if a not in open('yonghu.txt', 'r').readlines():
        return 0
    return zhanghao










denglu()

