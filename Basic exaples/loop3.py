from turtle import*
speed('fastest')
colors=['red','blue','green']
pensize(10)
for i in range(20,0,-1):
    pencolor(colors[i%3])
    forward(200)
    left(360/6)
    dot(i*8)
    mainloop()