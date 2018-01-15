x=[]
y=[]
a=[0]
su1=[]
#print("enter the no. of observations: ")
m=int(input())
n=int(input())
#n=m-1

def output(a,n):
    for i in a:
        print(eval("'%."+str(n)+"f'%i"))



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
    for k in a:
        retv+=k**b
    return retv
    
#get_variable(compute_solns(W))

for i in range(m):
    print("enter x-coordinate: ")
    x.append(int(input()))
    print("enter y-coordinate: ")
    y.append(int(input()))

print(x)
print(y)
for i in range(n+1):
    a.append([0])
    for j in range(n+1):
        a[i+1].append(power_add(x,i+j))
        

for i in range(n+1):
    su=0
    for j in range(m):
        su+=y[j]*x[j]**i
        
    a[i+1].append(su)

print(a)
get_variable(compute_solns(a))
