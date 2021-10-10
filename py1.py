def load_data(filename: str):
    file = open(filename, 'r')
    data = []
    for line in file:
        line = line.strip()
        data.append([int(value) for value in line.split(' ')])
    file.close()
    return data


def calc_sqr_vec_len(vector):
    return pow(vector[0], 2) + pow(vector[1], 2)


data = load_data('in1.txt')
n = data[0][0]
moves = data[1:]
start = [0, 0]