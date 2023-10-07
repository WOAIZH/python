# n=float(input("请付款86.7元："))
# if n<86.7:
#     b=86.7-n
#     a=float(input("付款金额不够，还差%.2f元\n请你付款%.2f元："%(b,b)))
#     if a==b:
#         print('欢迎下次光临！')
#     elif a>b:
#         print('收您%.2f元,找零%.2f元\n老板，发财！'%(a,a-b))
#     else:
#         print('识不识数啊！付两次都没付好')
# else:
#     m=n-86.7
#     print(type(m))
#     print('收您%.2f元,找零%.2f元\n老板，发财！'%(n,m))

##格式化输出
# print("十进制整数形式：%d"%1000000)
# print("加千分位的十进制整数形式：{0:,}".format (123456789))
# print("二进制进制整数形式：{:b}".format (123))
# print("八进制进制整数形式：%o"%123)
# print("十六进制整数形式：%x"%123)
# print("十六进制整数形式：%X"%123)
# print("正常输出字符串：{}".format ('abcdefg'))
# print("设置宽度的字符串：{:7}".format ('abcdefg'))
# print("设置宽度的字符串：{:>10}".format ('abcdefg'))
# print("小数形式的浮点数：{:b}".format (123))
# print("指数形式的浮点数：{:b}".format (123))
# print("设置宽度和小数位数的浮点数：{:b}".format (123))
# print("设置宽度和小数位数的浮点数：{:b}".format (123))
# print("设置宽度和小数位数的浮点数：{:b}".format (123))


# name=input("输入你的名字：")
# sex=int(input("输入你的年龄："))
# year=int(input("输入你的生日："))
# print('我的名字叫{}，今年{:d}岁，出生年月{:d}'.format(name,sex,year))#{}默认字符串


# n=input('输入你觉得是傻鸟的人：')
# print('{}是傻傻鸟'.format(n))


##求斐波那契数
# def dg(n):
#     if n<=0:
#         return "输入错误！"
#     elif n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return dg(n-1)+dg(n-2)
# n=int(input('请输入你要求的第n个斐波那契数:'))
# print('第{}位斐波那契数是{}'.format(n,dg(n)))





# #坤坤
# import turtle as t
# import math

# t.setup(1000, 750)
# t.setworldcoordinates(-800,-600,800,600)
# t.title('I am ikun!!')
# t.width(8)
# t.speed(0)
# t.pencolor('black')

# #以圆心和半径画圆
# def my_circle(rad,c_x,c_y,color=None):
#     if color is not None:
#         t.fillcolor(color)
#         t.begin_fill()
#     t.penup()
#     t.setheading(0)
#     t.goto(c_x,c_y-rad)
#     t.pendown()
#     t.circle(rad)
#     if color is not None:
#         t.end_fill()
# #求θ角度方向上椭圆的坐标
# def get_ellipse_xy(a,b,theta):
#     if theta < 0:theta=theta+math.pi*2
#     x = a * b / math.sqrt(b * b + a * a * math.tan(theta) * math.tan(theta))
#     if theta < math.pi/2:
#         return {'x':x,'y':x*math.tan(theta)}
#     elif theta < math.pi:
#         return {'x':x*(-1),'y':x*(-1)*math.tan(theta)}
#     elif theta < math.pi*3/2:
#         return {'x':x*(-1),'y':x*(-1)*math.tan(theta)}
#     else:
#         return {'x': x, 'y': x*math.tan(theta)}
# # 画一个椭圆，shape为椭圆形状参数，start_ang、end_ang为起始角度
# # shape = {"X0": 0,"Y0": 0,"a": 200,"b": 100,"angle": math.pi/3}
# def ellipse(shape,start_ang,end_ang,color=None):
#     if color is not None:
#         t.fillcolor(color)
#         t.begin_fill()
#     a = shape['a']
#     b = shape['b']
#     shape_ang = shape['angle']
#     theta = start_ang - shape_ang
#     x1, y1 = get_ellipse_xy(a, b, theta).values()
#     x = shape['X0'] + x1 * math.cos(shape_ang) - y1 * math.sin(shape_ang)
#     y = shape['Y0'] + x1 * math.sin(shape_ang) + y1 * math.cos(shape_ang)
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     step = math.pi/180*2 # 以方位角2°一步
#     num_steps = math.ceil((end_ang-start_ang)/step) # 总步数
#     for i in range(num_steps):
#         theta = theta + step
#         x1, y1 = get_ellipse_xy(a, b, theta).values()
#         t.goto(shape['X0'] + x1 * math.cos(shape_ang) - y1 * math.sin(shape_ang),
#                shape['Y0'] + x1 * math.sin(shape_ang) + y1 * math.cos(shape_ang))
#         if color is not None:
#             t.end_fill()
# #画篮球
# my_circle(150, -206, -212, '#BA7148')
# baskt_line1 = {"X0": -120,"Y0": -34,"a": 186,"b": 162,"angle": 0}
# ellipse(baskt_line1, math.pi/180*198, math.pi/180*290)
# baskt_line2 = {"X0": -294,"Y0": -402,"a": 186,"b": 162,"angle": 0}
# ellipse(baskt_line2, math.pi/180*21, math.pi/180*110)
# t.penup()
# t.goto(-346,-160)
# t.pendown()
# t.goto(-66,-274)

# # 画脸蛋
# face = {"X0": 80,"Y0": -22,"a": 256,"b": 198,"angle": 0}
# ellipse(face, 0, math.pi*2,'#F5D477')

# #眼睛
# my_circle(77, 63, 41, 'white')
# my_circle(68, 217, 41, 'white')
# my_circle(24, 100, 34, 'black')
# my_circle(24, 244, 34, 'black')

# #嘴巴
# t.width(5)
# mouse = {"X0": 145,"Y0": -73,"a": 75,"b": 53,"angle": 0}
# ellipse(mouse, 0, math.pi*2,'#F4A644')
# mouse_line = {"X0": 138,"Y0": -40,"a": 92,"b": 53,"angle": 0}
# ellipse(mouse_line, math.pi/180*208, math.pi/180*342,'#F4A644')

# #腮红
# t.width(1)
# t.pencolor('#F5D477')
# my_circle(62, -82, -62, 'red') # 左边
# face_cheek = {"X0": 294,"Y0": -66,"a": 37,"b": 60,"angle": -math.pi/180*12}
# ellipse(face_cheek, 0, math.pi*2,'red') # 右边

# #腮红有点遮住脸的轮廓，重新绘制一遍
# t.pencolor('black')
# t.width(8)
# ellipse(face, -math.pi/3, math.pi/3)

# # 定义一个画polygon的函数
# def draw_poly(poly_data,color=None):
#     x=poly_data['x']
#     y=poly_data['y']
#     t.penup()
#     t.goto(x[0], y[0])
#     t.pendown()
#     if color is not None:
#         t.fillcolor(color)
#         t.begin_fill()
#     for i in range(len(x)):
#         t.goto(x[i], y[i])
#     if color is not None:
#         t.end_fill()

# # 画头发
# poly_hair = {'x': [-258, -161, -74, 0, 55, 111, 211, 315, 362,
#                    329, 293, 283, 269, 227, 269, 283, 208, 194,
#                    160, 160, 85, 44, 61, 44, 31, 1, -33,
#                    1, -60, -51, -60, -62, -129, -142, -144, -108,
#                    -144, -142, -209, -216, -200, -216, -258],
#              'y': [57, 187, 238, 267, 251, 296, 260, 171,
#                    47, -9, 29, 61, 110, 166, 110, 61, 72, 132,
#                    178, 178, 174, 162, 206, 162,
#                    29, 35, 54, 35, 4, 40, 4, -37, -45, -8, 71,
#                    152, 71, -8, -31, 31, 90, 31, 57]
#             }
# draw_poly(poly_hair, '#D0CED1')

# # 头发下那个小三角
# hair2 = {'x': [160, 114, 85], 'y': [178, 218, 174]}
# draw_poly(hair2, '#797572')

# # 衣服
# poly_cloth = {'x': [-142, -112, -22, 50, 132, 218, 249, 247,
#                    295, 328, 318, 321, 309, 338, 353, -167,
#                    -150, -165, -166, -150, -162, -157, -142],
#               'y': [-135, -155, -144, -140, -150, -166, -163, -150,
#                    -145, -165, -194, -233, -244, -290, -326, -328,
#                    -248, -233, -209, -195, -167, -146, -135]
#              }
# draw_poly(poly_cloth, '#222222')
# cloth2 = {'x': [-58, 0, 89, 146, 205, 250, 212, 179, 89, 26, -27, -58],
#           'y': [-207, -203, -178, -184, -202, -208, -236, -246, -243, -237, -233, -207]
#          }
# t.width(2)
# draw_poly(cloth2, '#0A0A0C') #中间黑的那一块

# # 左右背带
# strap1 = {'x': [-150, -92, -57, -41, -39, -46], 'y': [-220, -227, -243, -277, -306, -328]}
# strap2 = {'x': [309, 269, 238, 224, 222], 'y': [-222, -233, -257, -292, -326]}
# t.width(18)
# t.pencolor('#D3D1D4')
# draw_poly(strap1)
# draw_poly(strap2)

# #中间背带
# t.width(10)
# strap3 = {'x': [-17, 90, 209, 90, 93],'y': [-251, -273, -248, -273, -290]}
# draw_poly(strap3)
# t.width(2)
# t.pencolor('white')
# my_circle(30, 97, -320, '#D1D1D3')

# # 文字kun
# k = {'x': [78, 78, 78, 88, 78, 88], 'y': [-312, -326, -319, -312, -319, -326]}
# draw_poly(k)
# u = {'x': [93, 93, 98, 103, 103], 'y': [-312, -323, -326, -323, -312]}
# draw_poly(u)
# n = {'x': [109, 109, 119, 119], 'y': [-326, -312, -326, -312]}
# draw_poly(n)

# t.resizemode("user")
# t.shapesize(0.8, 0.8)
# t.hideturtle()
# t.done()



# n=float(input('请输入体重(单位/kg)：'))
# m=float(input('请输入身高(单位/cm)：'))
# j=float(input('请输入年龄：'))
# i=665+9.6*n+1.7*m-4.7*j
# print('您的代谢基础=%.2f'%i)

# print('python超市收银系统')
# n=input('请输入商品名称：')
# m=float(9.9)
# print('商品单价：%.1f'%m)
# i=float(input('数量：'))
# c=m*i
# print('应付金额：%.1f'%c)
# j=float(input('实收：'))
# print("python超市购物小票")
# print('商品名称  单价    数量')
# print('牛奶      9.9     %.1f'%i)
# print('应付：%.1f'%c)
# print('实收：%.1f'%j)
# print('找零：%.1f'%(j-c))

# print('python格式化输出')
# print('十进制整数形式：{:d}'.format(1000000))
# print('设置宽度和小数位数浮点数：{:0>10.2f}'.format(123.456))
# print('设置宽度和小数位数浮点数：{:10.2f}'.format(123.456))
# print('设置宽度和小数位数浮点数：{:0<10.2f}'.format(123.456))
# print('设置宽度和小数位数浮点数：{:<10.2f}'.format(123.456))

# import turtle
# # 设置画笔速度  
# turtle.speed(0)
# # 重复 4 次画线和转向，绘制正方形  
# for i in range(4):  
#    turtle.forward(100)  # 画笔向前移动 100 个单位  
#    turtle.right(90)     # 画笔向右转 90 度
# # 结束绘制，关闭窗口  
# turtle.done() 



# import turtle
# # 设置画笔速度    
# turtle.speed(0)
# # 画一个半径为 100 的圆    
# turtle.circle(100)
# # 结束绘制，关闭窗口    
# turtle.done()  



# import turtle
# # 设置画笔速度  
# turtle.speed(0)
# # 初始化画笔位置  
# turtle.penup()  
# turtle.goto(-50, 0)  
# turtle.pendown()
# # 画六边形  
# for i in range(6):  
#    turtle.forward(100)  
#    turtle.right(60)
# # 结束绘制，关闭窗口  
# turtle.done() 


# s="ABCDF"
# n=int(input("请输入你的分数："))
# if n>=90 and n<=100:
#    print(s[0])
# elif n>=80 and n<90:
#    print(s[1])
# elif n>=70 and n<80:
#    print(s[2])
# elif n>=60 and n<70:
#    print(s[3])
# elif n>=0 and n<60:
#    print(s[4])
# else:
#    print("输入错误！")


# s="EEEEEEDCBAA"
# n=int(input("请输入你的分数："))
# if n<100 and n>0:
#    j=int(n/10)
#    print(s[j])
# else :
#    print("输入错误！")


# def  分数判断(n):
#    s="EEEEEEDCBAA"
#    if n<100 and n>0:
#       j=int(n/10)
#       return s[j]
#    else :
#       return "输入错误！"
# n=int(input("请输入你的分数："))
# print(分数判断(n))


from re import S


s="学python,大家一起在努力！"
# "0 12345678 9          15"
# print(s[1:10:2])
# print(s[1:10])
# print(s[0:])
# print(s[1:10:2])
# print(s[0:5])
# print(s[4:])

# print(s[15:7:-2])
# print(s[-7:-16:-1])
# print(s[-1:-16:-1])
# print(s[-1:-11:-1])
# print(s[-12::-1])
# t=s[1:2][-12::-1]
# print(t)
# print(s[1:2],s[-12::-1])

# a = 3
# b = 5
# eval('1')+a
# print(eval('1')+a)


#计算利息
import math
p=int(input('输入本金：'))
n=int(input('存几年：'))
i=float(input('利率（非百分制）：'))
a=float(1+i)
j=n
b=1
for j in range(j):
    b=b*a
F=p*b
print('利息:{:>16,.2f}元'.format(F-p))
t=int(F-p)/(n*365)
print('一个月就是:{:>10,.2f}元'.format(t*30))
print('一天要花:{:>12,.2f}元'.format(t))