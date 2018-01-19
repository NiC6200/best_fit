import random

x=[]
y=[]
a=[0]
su1=[]
final=[]
print("enter the no. of observations: ")
m=int(input())
#m=2
print("enter the power of the curve: ")
n=int(input())
#n=m-1

def output(a,n):
    for i in a:
        #final.append(float((eval("'%."+str(n)+"f'%i"))))
        final.append(i)
    print(final)


def compute_solns(temp):
    A=temp
    result=[0]
    result.insert(1,A)
    for _ in range(len(A)-2):
        
        n=len(A)-1
        a1=A[1][1]
        for j in range(1,n+2):
            A[1][j]/=a1
        
        temp=[0]
        
        for i in range(2,n+1):
            a1=A[i][1]
            #print(a1)
            temp.append([0])
            for j in range(1,n+2):
                A[i][j]=A[i][j]/a1-A[1][j]
                if j!=1:
                    temp[i-1].append(A[i][j])
        #print(A)
        A=temp
        result.insert(1,temp)
    return result


def get_variable(A):
    
    X=[]
    n=len(A)-1
    for i in range(1,n+1):
        lhs=0
        for j in range(2,i+1):
            lhs+=A[i][1][j]*X[j-2]
        rhs=A[i][1][i+1]
        x=(rhs-lhs)/A[i][1][1]
        
        X.insert(0,x)
        
    output(X,2)
    
#get_variable(compute_solns(W))

    
    
    
def power_add(a,b):
    retv=0
    for k in list(a):
        retv+=k**b
    return retv
    
#get_variable(compute_solns(W))

for i in range(m):
    print("enter x-coordinate: ")
    x.append(int(input()))
    print("enter y-coordinate: ")
    y.append(int(input()))

#x=[1,2,3,4,5]
#y=[5,10,2,3,0]

#x=[random.randint(100,200) for _ in range(50)]
#y=[random.randint(100,200) for _ in range(50)]

#x=[145, 18, 74, 59, 27, 188, 107, 22, 129, 18, 151, 125, 118, 20, 31, 174, 30, 188, 134, 24, 83, 91, 61, 69, 92, 80, 161, 19, 150, 171, 131, 27, 2, 75, 87, 88, 41, 34, 82, 49, 118, 80, 88, 142, 46, 37, 88, 10, 181, 6]
#y=[61, 156, 19, 24, 53, 101, 91, 0, 173, 133, 25, 68, 82, 160, 180, 76, 50, 81, 55, 83, 125, 148, 125, 143, 66, 184, 173, 51, 23, 134, 17, 194, 73, 113, 55, 165, 92, 188, 177, 81, 141, 98, 70, 152, 128, 14, 138, 192, 104, 102]

#x=[10,20,30,40,50]
#y=[10,20,30,40,50]
#x=[20, 25, 45, 90, 15]
#y=[35, 40, 10, 90, 60]
#x=[4,5,9,18,3]
#y=[7,8,2,18,12]
#x=[10,20]
#y=[35,50]
print(x)
print(y)
for i in range(n+1):
    a.append([0])
    for j in range(n+1):
        a[i+1].append(power_add(list(x),i+j))
        

for i in range(n+1):
    su=0
    for j in range(m):
        su+=y[j]*x[j]**i
        
    a[i+1].append(su)

print(a)
get_variable(compute_solns(a))







#######################################################################################












import pygame,time


x_min=0
x_max=100
y_min=0
y_max=100
height=800
width=800
coordinatex=width/(x_max-x_min)
coordinatey=height/(y_max-y_min)
line_spacingx=5*coordinatex
line_spacingy=5*coordinatey


pygame.init()
board=pygame.display.set_mode((800,800))

#a=[10,5]

white=pygame.Color(255,255,255)
black=pygame.Color(0,0,0)
red=pygame.Color(255,0,0)
blue=pygame.Color(0,0,255)
green=pygame.Color(0,255,0)
yellow=pygame.Color(255,255,0)




board.fill(white)
    #pygame.display.update()
    #time.sleep(1)


def update_variables():

    print(x_min,x_max,' ',line_spacingx,coordinatex,width)


def my_coordinatex(x):
    return x/coordinatex+x_min

def my_coordinatey(y):
    return -y/coordinatey+y_min

def board_coordinatex(x):
    return coordinatex*(x-x_min)

def board_coordinatey(y):
    return height-coordinatey*(y-y_min)

def join_point(surf,col,a,b,t):
    pygame.draw.line(surf,col,a,b,t)
    #pygame.display.update()

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
    #pygame.display.update()


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
            #pygame.display.update()
        yp = yo
    pygame.display.update()

            
def draw_board():
    
    board.fill(white)
    
    for i in range(0,width+1,int(line_spacingx)):
        pygame.draw.line(board,black,(i,height),(i,0))
    
    for i in range(0,height+1,int(line_spacingy)):
        pygame.draw.line(board,black,(width,i),(0,i))
    
    #pygame.draw.line(board,black,(int(board_coordinatex(0)),int(board_coordinatey(y_max))),(int(board_coordinatex(x_max)),int(height/2)),5)
    #pygame.draw.line(board,black,(int(width/2),0),(int(width/2),height),5)
    
    draw_graph(board,black,[0,0],'full')
    pygame.draw.line(board,black,(int(board_coordinatex(0)),int(board_coordinatey(y_max))),(int(board_coordinatex(0)),int(board_coordinatey(y_min))),3)



    
    pygame.display.update()
                     


#time.sleep(2)





draw_board()

for i in range(len(x)):
    mark_point(board,red,[x[i],y[i]])
    
draw_graph(board,blue,final,'full')

#mark_point(board,red,[25,-45])
#draw_graph(board,blue,[5,2],'full')
#draw_graph(board, green, [1,5,1 ], 'full')
#draw_graph(board, red, [-100,0,1 ], 'full')
#time.sleep(5)


while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_RIGHT:
                x_min+=int(line_spacingx/4)
                x_max+=int(line_spacingx/4)
                
            if event.key==pygame.K_LEFT:
                x_min-=int(line_spacingx/4)
                x_max-=int(line_spacingx/4)
                
            if event.key==pygame.K_UP:
                y_min+=int(line_spacingy/4)
                y_max+=int(line_spacingy/4)
                
            if event.key==pygame.K_DOWN:
                y_min-=int(line_spacingy/4)
                y_max-=int(line_spacingy/4)
                
            if event.key==pygame.K_a and x_max-x_min-2*int(line_spacingx/4)>0:
                x_max-=int(line_spacingx/4)
                x_min+=int(line_spacingx/4)
                y_max-=int(line_spacingy/4)
                y_min+=int(line_spacingy/4)
                coordinatex=width/(x_max-x_min)
                coordinatey=height/(y_max-y_min)
                line_spacingx=5*coordinatex
                line_spacingy=5*coordinatey
                
            if event.key==pygame.K_s:
                x_max+=int(line_spacingx/4)
                x_min-=int(line_spacingx/4)
                y_max+=int(line_spacingy/4)
                y_min-=int(line_spacingy/4)
                coordinatex=width/(x_max-x_min)
                coordinatey=height/(y_max-y_min)
                line_spacingx=5*coordinatex
                line_spacingy=5*coordinatey
                
            
            elif event.type==pygame.K_q:
                pygame.quit()
                quit()
                
            print(x_min,x_max,' ',line_spacingx,coordinatex,width)
            draw_board()
            #mark_point(board,red,[25,-45])
            #draw_graph(board,blue,[5,2],'full')
            #draw_graph(board, green, [1,5,1 ], 'full')
            #draw_graph(board, yellow, [-100,0,1 ], 'full')
            #draw_graph(board, black, [math.cos()],'full')
            
            for i in range(len(x)):
                mark_point(board,red,[x[i],y[i]])
    
            draw_graph(board,blue,final,'full')
            pygame.display.update()
            #time.sleep(5)











