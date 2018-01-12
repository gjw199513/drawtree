# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/12 0012 上午 10:45'

# 加入循环操作
import turtle


def draw_pentagram(size):
    """
    绘制五角星
    :param size:
    :return:
    """
    # 计数器
    count = 1
    while count <= 5:
        # 第一条边
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main():
    """
    主函数
    :return:
    """
    turtle.speed(1)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50
    while size <= 100:
        draw_pentagram(size)
        size += 10

    turtle.exitonclick()


# 五角星的绘制
if __name__ == '__main__':
    main()
