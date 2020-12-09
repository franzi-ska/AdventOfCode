with open('input/02.txt') as f:
    data = f.read().splitlines()

# data = [i.split('x') for i in data]
data = [sorted([int(i) for i in line.split('x')]) for line in data]

paper = 0
ribbon = 0
for present in data:
    x,y,z = present
    paper += 3*x*y+2*x*z+2*y*z
    ribbon += 2*(x+y)+x*y*z
print('A1:', paper)
print('A2:', ribbon)
