from numpy import *


# pu为级别为hi的数据，level_t为目标级别,s为定义域
# 本函数将级别为hi的数据扰动成级别为t的数据
def data_redisturbance(level_t_epsilon, pu, level_hi_epsilon, s):
    ru = []
    h = len(s)
    p_t = exp(level_t_epsilon) / (exp(level_t_epsilon) + h - 1)
    p_hi = exp(level_hi_epsilon) / (exp(level_hi_epsilon) + h - 1)
    alpha = (h * p_t - p_t + p_hi - 1) / (h * p_hi - 1)
    for x in pu:
        # 以alpha的概率保持自身
        if random.uniform(0,1) <= alpha:
            ru.append(x)
        else:
            tempnum = random.randint(0,h)
            while x == s[tempnum]:
                tempnum = random.randint(0,h)
            ru.append(s[tempnum])
    # print('ru len',ru.__len__())
    return ru
