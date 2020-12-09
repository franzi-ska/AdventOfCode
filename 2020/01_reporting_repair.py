with open('input/01.txt') as f:
    data = f.read().splitlines()
data = [int(i) for i in data]
data.sort()


for idx_n1, n1 in enumerate(data):
    for n2 in data[idx_n1+1:]:
        sum_n = n1+n2
        if sum_n == 2020:
            print('A1:', n1*n2)
        elif sum_n>2020:
            break

idx_max =len(data)
for idx1, n1 in enumerate(data[:-2]):
    for idx2 in range(idx1+1, idx_max-1):
        n2 = data[idx2]
        for idx3 in range(idx2+1, idx_max):
            n3 = data[idx3]
            s3 = n1+n2+n3
            if s3>2020:
                break
            elif s3 == 2020:
                print('A2:', n1*n2*n3)
