def load_data(filename: str):
    file = open(filename, 'r')
    data = []
    for line in file:
        line = line.strip()
        data.append([int(ch) for ch in line.split(' ')])
    file.close()
    return data


data = load_data('in1.txt')
n = data[0][0]
moves = data[1:]
print(n)