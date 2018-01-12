# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/12 0012 上午 10:45'

# 绘制五角星

import turtle


def main():
    """
    主函数
    :return:
    """
    # 计数器
    count = 1
    while count <= 5:
        # 第一条边
        turtle.forward(100)
        turtle.right(144)
        count = count + 1

    turtle.exitonclick()


# 五角星的绘制
if __name__ == '__main__':
    main()
