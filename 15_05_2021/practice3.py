# pong
from os import system
from time import sleep
from random import random
WIDTH = 20
HEIGHT = 10

bx = WIDTH/2
by = HEIGHT/2
bvx = 1
bvy = 1

p1x = 2
p1y = HEIGHT/2

p2x = 18
p2y = HEIGHT/2

def update(ball_x, ball_y, ball_vx, ball_vy , player1_y, player2_y):
    ball_x = ball_x + ball_vx
    ball_y = ball_y + ball_vy
    
    #player1_vy = int((ball_y-player1_y)*(random()+0.5))
    #player1_y = player1_y + player1_vy
    player1_y = ball_y
    player2_y = ball_y
    #print(f"{ball_x},{ball_y} , ----:> {player1_y}")
    if( ball_x >= WIDTH ):
        res = ("player 2 lost")
    if( ball_x <= 0 ):
        res = ("player 1 lost")
        
    if( ball_y >= HEIGHT ):
        ball_vy = ball_vy * -1
    if( ball_y <= 0 ):
        ball_vy = ball_vy * -1
    
    if( ball_x == p1x  and ball_y == player1_y):
        ball_vx = ball_vx * -1
    if( ball_x == p2x  and ball_y == player2_y):
        ball_vx = ball_vx * -1
        
    return ball_x, ball_y, ball_vx, ball_vy, player1_y, player2_y
    
i = 100
while i > 0:
    i -= 1
    system("cls")
    bx,by,bvx,bvy,p1y,p2y = update(bx, by, bvx, bvy , p1y, p2y )
    print("-------------------")
    for i in range(0,int(by)):
        print(" ")
    sp = " "*int(bx)
    print(sp + "x")
    for i in range(int(by),HEIGHT):
        print(" ")
    print("-------------------")
    
    sleep(0.1)