from turtle import *
from random import randint

for n in range(50):
    ran_num = randint(20,100)
    ran_deg = randint(45,120)
    forward(ran_num)
    right(ran_deg)

done()
