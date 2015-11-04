import turtle
num1=15
print(num1)
num2=num1/2
print(num2)
list1=[1,2,3]
print(list1)
i=0
for i in list1 :
	print(i)
	print(i*2)
	print(list1[-1]+list1[-2]+list1[-3])
#turtle.penup()
turtle.begin_fill()
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)
turtle.end_fill()
turtle.penup()
turtle.goto(100,200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.mainloop()