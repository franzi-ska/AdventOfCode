
class Ferry(object):
    front_facing_directions = {0:'E', 1:'S', 2:'W',  3:'N'}

    def __init__(self, x0=0, y0=0):
        self.front = 0
        self.x = x0
        self.y = y0

    def E(self, value):
        self.x += value
    def W(self, value):
        self.x -= value
    def N(self, value):
        self.y += value
    def S(self, value):
        self.y -= value

    def F(self, value):
        getattr(self, self.front_facing_directions[self.front])(value)

    def L(self, value):
        self.front -= value/90
        self.front %= 4

    def R(self, value):
        self.front += value/90
        self.front %= 4

    def get_distance(self):
        return abs(self.x) + abs(self.y)


# class Waypoint(object)
#

with open('input/12.txt') as f:
    data = [(i[0], int(i[1:])) for i in f.read().splitlines()]

ship = Ferry()
for (d, v) in data:
    # print(d,v)
    getattr(ship, d)(v)

print(ship.get_distance())

#%%

with open('input/12.txt') as f:
    data = [(i[0], int(i[1:])) for i in f.read().splitlines()]

sin = {0:0, 90:1, 180:0, 270:-1}
cos = {0:1, 90:0, 180:-1, 270:0}
class Ferry_with_Waypoint():
    def __init__(self,  point_dx, point_dy):
        self.ferry_x = 0
        self.ferry_y = 0
        self.point_dx = point_dx
        self.point_dy = point_dy

    def N(self, value):
        self.point_dy += value
    def S(self, value):
        self.point_dy -= value
    def E(self, value):
        self.point_dx += value
    def W(self, value):
        self.point_dx -= value
    def L(self, value):
        self.rotate(value)
    def R(self, value):
        self.rotate(360-value)
    def F(self, value):
        self.ferry_x += self.point_dx *value
        self.ferry_y += self.point_dy *value


    def rotate(self, theta):
        dx = (self.point_dx * cos[theta] - self.point_dy*sin[theta])
        dy = (self.point_dx * sin[theta] + self.point_dy*cos[theta])
        self.point_dx = dx
        self.point_dy = dy

    def move(self, move):
        getattr(self, move[0])(move[1])

    def Manhattan_distance(self):
        # print(self.ferry_x, self.ferry_y)
        return abs(self.ferry_x) + abs(self.ferry_y)

    def __str__(self):
        return 'ship:({},{})\twaypoit:({},{})'.format(
                    self.ferry_x, self.ferry_y, self.point_dx, self.point_dy)

ship2 = Ferry_with_Waypoint(10, 1)
for move in data:
    ship2.move(move)

print('A2:',ship2.Manhattan_distance())
