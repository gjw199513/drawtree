# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/12 0012 上午 10:45'

# 利用递归绘制分形数
import turtle


def draw_branch(branch_length):
    """
    绘制分形数
    :param branch_length:
    :return:
    """
    if branch_length > 5:
        print(branch_length)
        if branch_length < 40:
            turtle.pensize(2)
            turtle.color('green')
        else:
            turtle.color('brown')
        # 绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length - 15)
        if branch_length < 40:
            turtle.color('green')

        else:
            turtle.color('brown')
        # 返回之前的树枝
        turtle.right(20)
        turtle.backward(branch_length)


def main():
    """
    主函数
    :return:
    """
    turtle.screensize(800, 600, "black")
    turtle.speed(5)
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pensize(3)
    turtle.pendown()
    draw_branch(100)

    turtle.exitonclick()


# 五角星的绘制
if __name__ == '__main__':
    main()
