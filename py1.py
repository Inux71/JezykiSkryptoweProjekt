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


def sum_vectors(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1]]


data = load_data('in1.txt')
n = data[0][0]
moves = data[1:]
max_distance = -1
distance = 0
count = 0
results = []

for i in range(0, n):
    results.append(sum_vectors([0, 0], moves[i]))
    distance = calc_sqr_vec_len(results[-1])
    if distance > max_distance:
        max_distance = distance
    for j in range(0, n):
        if j == i:
            continue
        else:
            results.append(sum_vectors([0, 0], sum_vectors(moves[i], moves[j])))
            distance = calc_sqr_vec_len(results[-1])
            if distance > max_distance:
                max_distance = distance
            for k in range(0, n):
                if k == j or k == i:
                    continue
                else:
                    results.append(sum_vectors([0, 0], sum_vectors(moves[i], sum_vectors(moves[j], moves[k]))))
                    distance = calc_sqr_vec_len(results[-1])
                    if distance > max_distance:
                        max_distance = distance
                    for l in range(0, n):
                        if l == k or l == j or l == i:
                            continue
                        else:
                            results.append(sum_vectors([0, 0], sum_vectors(moves[i], sum_vectors(moves[j], sum_vectors(moves[k], moves[l])))))
                            distance = calc_sqr_vec_len(results[-1])
                            if distance > max_distance:
                                max_distance = distance
                            for m in range(0, n):
                                if m == l or m == k or m == j or m == i:
                                    continue
                                else:
                                    results.append(sum_vectors([0, 0], sum_vectors(moves[i], sum_vectors(moves[j], sum_vectors(moves[k], sum_vectors(moves[l], moves[m]))))))
                                    distance = calc_sqr_vec_len(results[-1])
                                    if distance > max_distance:
                                        max_distance = distance

print(max_distance)