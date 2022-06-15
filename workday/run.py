import os

import sys

from read_ini import INIParser

if getattr(sys, 'frozen', False):  # -170929 打包exe之后，os.path.dirname(__file__)不是exe所在文件夹
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(__file__)
path = os.path.normpath('%s\%s' % (application_path, '日历'))
for r in os.listdir(path):
    if r.endswith('ini'):
        cfg = INIParser()
        cfg.read(os.path.normpath('%s\%s' % (path, r)))

        data_attribs = cfg.as_dict()
        datas = cfg.get_options()
        break

def fun_1(start_day, days, data_attribs, datas):

    ind = datas.index(start_day)

    day_total = 0
    for i in range(int(days)):
        try:

            while data_attribs[datas[ind + day_total]][0] != '0':
                # 节假日
                day_total += 1
            else:
                day_total += 1
        except IndexError:
            print('%s %s天后的日期,不在日期列表内' % (start_day, days))
            break
    return datas[ind+day_total-1]


def fun_2(in_day_1, in_day_2, data_attribs, datas):

    ind_1 = datas.index(in_day_1)
    ind_2 = datas.index(in_day_2)
    workdays = 0
    for i in range(ind_1, ind_2+1):
        if data_attribs[datas[i]][0] == '0':
            workdays += 1
    return workdays





def run():
    print('=============================================================')
    print('功能1：输入一个日期X，天数Y，计算日期X后Y个工作日后日期')
    print('功能2：输入一个日期X，日期Z，计算日期X与日期Z之间的工作日个数')
    print('=============================================================\n')
    fun = input('输入功能（1或者2）后按回车键：')
    while not(fun == '1'or fun == '2'):
        print('无法识别,请重新输入')
        fun = input('输入功能（1或者2）后按回车键：')
    if fun == '1':
        start_day = input('输入第1个日期X(如20180101)：')
        while not ((start_day.isdigit() and len(start_day) == 8) and start_day in datas):
            if not (start_day.isdigit() and len(start_day) == 8):
                start_day = input('输入应为数字且长度为8，请重新输入第1个日期X：')

            if start_day not in datas:
                print('%s 不在日期列表内' % start_day)
                start_day = input('请重新输入第1个日期X：')

        days = input('输入天数Y：')

        while not ((days.isdigit() and int(days) > 0) and
                               datas.index(start_day)+int(days) < len(datas)):
            if not (days.isdigit() and int(days) > 0):
                days = input('天数应为大于0的数字，请重新输入天数Y：')

            if datas.index(start_day)+int(days)> len(datas):
                days = input('%s 后%s天已超过日期列表,请重新输入天数Y：'%(start_day,days))

        out = fun_1(start_day, days, data_attribs, datas)
        print('------------------------------------------------\n')
        print('%s 后%s个工作日为%s' % (start_day, days, out))

        input('\nPress ENTER to exit...\n')
    elif fun == '2':
        start_day = input('输入第1个日期X(如20180101)：')
        while not (start_day.isdigit() and len(start_day) == 8):
            start_day = input('请重新输入第1个日期X：')

        end_day = input('输入第2个日期Z(如20180101)：')
        while not (end_day.isdigit() and len(end_day) >= 4):
            end_day = input('请重新输入第2个日期Z：')

        out = fun_2(start_day, end_day, data_attribs, datas)
        print('------------------------------------------------\n')
        print('%s 到%s之间共有%s个工作日' % (start_day, end_day, out))

        input('\nPress ENTER to exit...\n')
if __name__ == '__main__':
    run()
    #print(fun_1('20181232', '3', data_attribs, datas))
    #print(fun_1('20180508', '5', data_attribs, datas))
    #print(fun_1('20180508', '10', data_attribs, datas))

