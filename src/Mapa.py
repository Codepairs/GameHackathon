import random

map = []

def generate_map():
    while len(map) < 20:
        line = []
        for i in range(20):
            line.append(random.randint(0,1))
        map.append(line)

# Вызов функции для генерации двумерного массива
generate_map()

# Вывод двумерного массива в терминале
for line in map:
    print(' '.join(str(x) for x in line))