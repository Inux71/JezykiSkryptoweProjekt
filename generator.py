import random
import os


def generate_file():
    steps = random.randint(1, 10)
    size = len(path)
    file = open('./input_data/in' + str(size + 1) + '.txt', 'w')
    file.write(str(steps) + '\n')
    for i in range(0, steps):
        if i == steps - 1:
            file.write(str(random.randint(-10000, 10000)) + ' ' + str(random.randint(-10000, 10000)))
        else:
            file.write(str(random.randint(-10000, 10000)) + ' ' + str(random.randint(-10000, 10000)) + '\n')
    file.close()


path = os.listdir('./input_data/')
generate_file()