import os


def load_data(filename: str):
    file = open('./input_data/' + filename, 'r')
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


files = os.listdir('./input_data/')
file_number = len(files)
for f in range(1, file_number + 1):
    data = load_data('in' + str(f) + '.txt')
    n = data[0][0]
    moves = data[1:]
    max_distance = -1
    results = []
    indexes = []
    solve()
    print_data('out' + str(f) + '.txt', str(max_distance))