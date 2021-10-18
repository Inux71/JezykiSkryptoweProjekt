import sys


def load_data(filename: str):
    file = open(filename, 'r')
    data = []
    for line in file:
        line = line.strip()
        data.append([int(value) for value in line.split(' ')])
    file.close()
    return data


def print_data(filename: str, data: str):
    file = open('./output_data/' + filename, 'w')
    file.write(data)
    file.close()


def calc_sqr_vec_len(vector):
    return pow(vector[0], 2) + pow(vector[1], 2)


def sum_vectors(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1]]


def solve():
    for i in range(0, n):
        skip = False
        vector = [0, 0]
        global max_distance
        for j in range(0, len(indexes)):
            if i == indexes[j]:
                skip = True
                break
        if skip:
            continue
        else:
            indexes.append(i)
            for j in range(0, len(indexes)):
                vector = sum_vectors(vector, moves[indexes[j]])
            results.append(vector)
            distance = calc_sqr_vec_len(results[-1])
            if distance > max_distance:
                max_distance = distance
            while len(results) > 0:
                results.pop()
            solve()
            indexes.pop()


input_file = str(sys.argv[1])
data = load_data(input_file)
n = data[0][0]
moves = data[1:]
max_distance = -1
results = []
indexes = []
solve()
print_data('out' + str(input_file[-5]) + '.txt', str(max_distance))


###FILE GENERATOR###
'''file = open('./input_data/in2.txt', 'w')
file.write('10\n')
for i in range(0, 10):
    file.write(str(random.randint(-10000, 10000)) + ' ' + str(random.randint(-10000, 10000)) + '\n')
file.close()'''