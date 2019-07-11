# coding=utf-8

# 游戏流程
def caiquan():
    """返回游戏的结果，0为平局，1为胜利，-1为失败,2为退回，-2为输入错误"""
    import random
    # 得到电脑和玩家的出拳内容
    jiqiren = random.randint(1, 3)
    wanjia = int(input('\n布为1，剪刀为2，拳头为3，回到首页为0\n请输入：'))
    # 删选出不需要的输入
    if wanjia < 0 or wanjia > 3:
        return -2
    if wanjia == 0:
        return 2
    # 打印出双方出拳结果
    if jiqiren == 3:
        print('\n电脑是拳头')
    elif jiqiren == 1:
        print('\n电脑是布')
    elif jiqiren == 2:
        print('\n电脑是剪刀')
    if wanjia == 3:
        print('玩家是拳头')
    elif wanjia == 1:
        print('玩家是布')
    elif wanjia == 2:
        print('玩家是剪刀')
    # 胜利判断
    if (wanjia == 3 and jiqiren == 2) or \
            (wanjia == 1 and jiqiren == 3) or \
            (wanjia == 2 and jiqiren == 1):
        return 1
    # 平局判断
    elif wanjia == jiqiren:
        return 0
    # 失败判断
    else:
        return -1


# 游戏首页
def shouye():
    """游戏首页，返回0为退出游戏，返回1为开始游戏，返回2为输入错误"""
    kaishi = int(input("\n开始游戏请按1\n结束游戏请按0\n请输入："))
    # 输入错误判断
    if (kaishi != 1) and (kaishi != 0):
        return -1
    # 退出游戏
    if kaishi == 0:
        return 0
    return 1


# 游戏开始
def kaishi(defen=3):
    """输入初始得分参数，开始猜拳游戏"""
    # 初始分判断
    if defen <= 0:
        print('\n初试分数太低了。。。\n\n游戏结束')
        return
    # 进入游戏首页
    print('*' * 10 + '猜拳小游戏' + '*' * 10, end="\n\n")
    print('本场游戏的初始分为%d分' % defen)
    # 进入游戏判断
    while defen > 0:
        # 进入游戏判断
        xuanze = shouye()
        if xuanze == 0:
            break
        if xuanze == -1:
            print('\n输入有误，请重新输入')
            continue
        # 进入游戏
        liansheng = 0
        while xuanze == 1:
            jieguo = caiquan()
            # 异常游戏判断
            if jieguo == 2:
                print('\n回到首页，\n您当前得分为：%d分' % defen)
                break
            if jieguo == -2:
                print('\n输入有误，请重新输入')
                continue
            # 正常游戏
            if jieguo == 0:
                print('打平了！！！')
                liansheng = 0
            if jieguo == 1:
                print('胜利了！！！')
                defen += 1
                liansheng += 1
                # 连胜判断
                if liansheng > 1:
                    print('恭喜获得%d连胜' % liansheng)
            if jieguo == -1:
                print('失败了！！！')
                defen -= 1
                liansheng = 0
            # 游戏后统计积分
            print('您当前得分为：%d分' % defen)
            # 胜利后超过10分判断
            if jieguo == 1 and defen >= 10:
                print('你是真的好牛逼啊！！！')
            # 分数为0，游戏结束
            if defen <= 0:
                print('\n好菜啊，分数用光了。。。')
                break
    # 游戏结束
    print('\n游戏结束')


kaishi()

