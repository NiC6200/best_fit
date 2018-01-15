import pygame,time

x = []
y = []
a = [0]
b=[]
su1 = []
print("enter the no. of observations: ")

m = int(input())
print('enter max power: ')
n = int(input())


# n=m-1

def output(a, n):
    br=[]
    for i in a:
        br.append(eval("'%." + str(n) + "f'%i"))
    print(br)
    for i in br:
        b.append(float(i))

    print(b)

def compute_solns(temp):
    A = temp
    result = [0]
    result.insert(1, A)
    for _ in range(len(A) - 2):

        n = len(A) - 1
        a1 = A[1][1]
        for j in range(1, n + 2):
            A[1][j] /= a1

        temp = [0]

        for i in range(2, n + 1):
            a1 = A[i][1]
            # print(a1)
            temp.append([0])
            for j in range(1, n + 2):
                A[i][j] = A[i][j] / a1 - A[1][j]
                if j != 1:
                    temp[i - 1].append(A[i][j])
        # print(A)
        A = temp
        result.insert(1, temp)
    return result


def get_variable(A):
    X = []
    n = len(A) - 1
    for i in range(1, n + 1):
        lhs = 0
        for j in range(2, i + 1):
            lhs += A[i][1][j] * X[j - 2]
        rhs = A[i][1][i + 1]
        x = (rhs - lhs) / A[i][1][1]

        X.insert(0, x)

    output(X, 2)


# get_variable(compute_solns(W))


def power_add(a, b):
    retv = 0
    for k in a:
        retv += k ** b
    return retv


# get_variable(compute_solns(W))


for i in range(m):
    print('enter x-coordinate: ')
    x.append(int(input()))
    print('enter y-coordinate: ')
    y.append(int(input()))

# print(x)
#print(y)
for i in range(n + 1):
    a.append([0])
    for j in range(n + 1):
        a[i + 1].append(power_add(x, i + j))

for i in range(n + 1):
    su = 0
    for j in range(m):
        su += y[j] * x[j] ** i

    a[i + 1].append(su)

#print(a)
get_variable(compute_solns(a))








######################################################################################




x_min=-10
x_max=100
y_min=-10
y_max=100
height=1000
width=1000
coordinatex=width/(x_max-x_min)
coordinatey=height/(y_max-y_min)
line_spacingx=5*coordinatex
line_spacingy=5*coordinatey


def my_coordinatex(x):
    return x/coordinatex+x_min

def my_coordinatey(y):
    return -y/coordinatey+y_min

def board_coordinatex(x):
    return coordinatex*(x-x_min)

def board_coordinatey(y):
    return height-coordinatey*(y-y_min)



white=pygame.Color(255,255,255)
black=pygame.Color(0,0,0)
red=pygame.Color(255,0,0)
blue=pygame.Color(0,0,255)
green=pygame.Color(0,255,0)



pygame.init()
board=pygame.display.set_mode((width,height))

board.fill(white)
pygame.display.update()
# time.sleep(1)


for i in range(0, width + 1, int(line_spacingx)):
    pygame.draw.line(board, black, (i, height), (i, 0))

for i in range(0, height + 1, int(line_spacingy)):
    pygame.draw.line(board, black, (width, i), (0, i))

pygame.draw.line(board, black, (int(board_coordinatex(0)),int(board_coordinatey(y_max))), (int(board_coordinatex(0)), int(board_coordinatey(y_min))),3)
pygame.draw.line(board, black, (int(board_coordinatex(x_max)),int(board_coordinatey(0))), (int(board_coordinatex(x_min)), int(board_coordinatey(0))),3)



def join_point(surf,col,a,b,t):
    pygame.draw.line(surf,col,a,b,t)

def f(func, x):
    y = 0
    for i in range(len(func)):
        y += x ** i * func[i]
    return y


def mark_point(surf, col, a):
    pygame.draw.line(surf, col, (
    int(board_coordinatex(a[0]) + line_spacingx / 4), int(board_coordinatey(a[1]) + line_spacingy / 4)), (
                     int(board_coordinatex(a[0]) - line_spacingx / 4),
                     int(board_coordinatey(a[1]) - line_spacingy / 4)), 3)

    pygame.draw.line(surf, col, (
    int(board_coordinatex(a[0]) + line_spacingx / 4), int(board_coordinatey(a[1]) - line_spacingy / 4)), (
                     int(board_coordinatex(a[0]) - line_spacingx / 4),
                     int(board_coordinatey(a[1]) + line_spacingy / 4)), 3)


def draw_graph(surf, col, a, rang):
    if rang == 'full':
        rang = range(0, width)

    yp = int(board_coordinatey(f(a, my_coordinatex(1))))
    for i in rang:
        yo = int(board_coordinatey(f(a, my_coordinatex(i))))
        # print(y)
        if yo < height and yo > 0 and yp > 0 and yp < height:
            # print(i,y)
            join_point(board, col, [i, yo], [i - 1, yp], 3)
        yp = yo



for i in range(len(x)):
    mark_point(board,blue,[x[i],y[i]])

draw_graph(board,red,b,'full')

pygame.display.update()
time.sleep(20)
pygame.quit()