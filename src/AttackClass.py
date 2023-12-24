from BotClass import Bot
import math
import random


# Необходимо учитывать скорость корабля
# Необходимо учитывать размер корабля
# Необходимо учитывать направление корабля


class Attack():
    necessary_elements = [] #До определнного момента я помнил для чего я вводил списки
    
    def __init__(self, opponent_coords, dir, speed, cannonRadius = None):
        necessary_elements += [opponent_coords], [dir], [speed]

    
    necessary_elements[0] = Bot()
    attack_coords = necessary_elements[0].attack_opponents()
    reformation_ac = [] # на случай если атак кордс - кортеж
    for i in attack_coords:
        reformation_ac.append(i)
    
    def smart_attack(self, reformation_ac, dir, speed):
        tactical_shot = reformation_ac[::] # учитываю что первый элемент - y, а второй - x
        if speed > 0 and dir == 0:
            tactical_shot[0] -= speed
        if speed > 0 and dir == 1:
            tactical_shot[1] += speed
        if speed > 0 and dir == 2:
            tactical_shot[0] += speed
        if speed > 0 and dir == 3:
            tactical_shot[1] -= speed
            #Если скорость меньше 0 то изменение координат корабля будетобратно изменению координат при положительной скорости
        if speed < 0 and dir == 0:
            tactical_shot[0] += speed
        if speed < 0 and dir == 1:
            tactical_shot[1] -= speed
        if speed < 0 and dir == 2:
            tactical_shot[0] -= speed
        if speed < 0 and dir == 3:
            tactical_shot[1] += speed
        if cannonRadius[0] + 1 >= tactical_shot[0] and cannonRadius[1] + 1 >= tactical_shot[1]: #К координате предельно допустимого y и x прибавил по единице так как наш выстрел по точной координате захватывает по одной клетке рядом с этой координатой
            return tactical_shot
        else:
            return('Out of range')




