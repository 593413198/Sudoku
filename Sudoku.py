from copy import deepcopy
from time import clock
start = clock()

def f(x):
    ans = []
    for i in range(1,10):
        if i not in x:
            ans.append(i)
    return ans

def check(x,b,C):
    flag = False
    for i in range(1,10):
        for j in x:
            if j.count(i)>1:
                flag = True
                break
    for i in range(1,10):
        for j in b:
            if j.count(i)>1:
                flag = True
                break
    for i in range(1,10):
        for m in C:
            for n in m:
                if n.count(i)>1:
                    flag = True
                    break
    if flag==True:
        return "Error"
    else:
        return "True"
        
stack_x = []
stack_a = []
stack_b = []
stack_A = []
stack_B = []
stack_ans = []
stack_M = [] 
stack_N = []

x = [[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],]

num = 0
while num!=9:
    line = raw_input()
    k=-1
    for i in line:
        k+=1
        x[num][k]=int(i)
    num += 1 
    
change = False 

while True:
    a = deepcopy(x)
    for i in a:
        while True:
            if 0 in i:
                i.remove(0)
            else:
                break
            
    b = [[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],]
    for i in range(9):
        for j in range(9):
            b[i][j]=x[j][i]
    for i in b:
        while True:
            if 0 in i:
                i.remove(0)
            else:
                break
    
    A = [None,None,None,None,None,None,None,None,None]        
    for i in range(9):
        A[i]=f(a[i])
    
    B = [None,None,None,None,None,None,None,None,None]
    for i in range(9):
        B[i]=f(b[i])
        
    c = [[[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None]],[[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None]],[[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None]]]
    temp = []
    for i in range(3):
        for j in range(3):
            temp.append(x[i][j])
    for i in range(9):
        c[0][0][i]=temp[i]
    
    temp = []
    for i in range(3):
        for j in range(3,6):
            temp.append(x[i][j])
    for i in range(9):
        c[0][1][i]=temp[i]
        
    temp = []
    for i in range(3):
        for j in range(6,9):
            temp.append(x[i][j])
    for i in range(9):
        c[0][2][i]=temp[i]
    
    temp = []
    for i in range(3,6):
        for j in range(3):
            temp.append(x[i][j])
    for i in range(9):
        c[1][0][i]=temp[i]
    
    temp = []
    for i in range(3,6):
        for j in range(3,6):
            temp.append(x[i][j])
    for i in range(9):
        c[1][1][i]=temp[i]
    
    temp = []
    for i in range(3,6):
        for j in range(6,9):
            temp.append(x[i][j])
    for i in range(9):
        c[1][2][i]=temp[i]
    
    temp = []
    for i in range(6,9):
        for j in range(3):
            temp.append(x[i][j])
    for i in range(9):
        c[2][0][i]=temp[i]
    
    temp = []
    for i in range(6,9):
        for j in range(3,6):
            temp.append(x[i][j])
    for i in range(9):
        c[2][1][i]=temp[i]
    
    temp = []
    for i in range(6,9):
        for j in range(6,9):
            temp.append(x[i][j])
    for i in range(9):
        c[2][2][i]=temp[i]
    
    for i in c:
        for j in i:
            while True:
                if 0 in j:
                    j.remove(0)
                else:
                    break
    C = deepcopy(c)
    m=-1            
    for i in c:
        m+=1
        n=-1
        for j in i:
            n+=1
            c[m][n]=f(j)
    
    ans = [[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None]]
    for i in range(9):
        for j in range(9):
            if x[i][j]==0:
                ans[i][j]=list( set(A[i]) & set(B[j]) & set(c[i/3][j/3]))
            else:
                ans[i][j]=[]
    if change==True:
        print 'm,n:',stack_M[-1],stack_N[-1]
        print 'x:',x[stack_M[-1]][stack_N[-1]]
        print 'sdsadasdasdasd:',ans[stack_M[-1]][stack_N[-1]]
        if len(ans[stack_M[-1]][stack_N[-1]])!=0:
            ans[stack_M[-1]][stack_N[-1]].append('x')
        change=False
    
                
    if check(x,b,C)=="Error":
        print "Error exists"
        a = stack_a.pop();b = stack_b.pop();
        A = stack_A.pop();B = stack_B.pop();
        M = stack_M.pop();N = stack_N.pop();
        ans = stack_ans.pop();x = stack_x.pop();
        ans[M][N].pop()
        print "after [Error] back stack x:"
        for i in x:
            print i
            
    m = -1
    for i in ans:
        flag1 = False 
        m += 1
        n = -1
        for j in i:
            n += 1
            if x[m][n]==0 and ans[m][n]==[]:
                flag1 = True
                print "line "+str(m),"row "+str(n)+"   Error exists!"
                a = stack_a.pop();b = stack_b.pop();
                A = stack_A.pop();B = stack_B.pop();
                M = stack_M.pop();N = stack_N.pop();
                ans = stack_ans.pop();x = stack_x.pop();
                ans[M][N].pop()
                break
        if flag1==True:
            break

    only = False
    for i in range(9):
        for j in range(9):
            if len(ans[i][j])==1:
                print "There exists only one condition!"
                print "only a["+str(i)+"]["+str(j)+"]="+str(ans[i][j][0])
                only = True
                print ans[i][j],"!!!!!!!!!"
                print x[i][j]
                x[i][j]= ans[i][j][0]
                
    only2 = False
    if only == False:
        print "No only=1 exists@@@"
        flag2 = False
        m = -1
        for i in ans:
            m += 1
            n = -1
            for j in i:
                n += 1
                if len(j)==2:
                    only2=True
                    stack_a.append(deepcopy(a));stack_b.append(deepcopy(b));stack_A.append(deepcopy(A));stack_B.append(deepcopy(B));stack_M.append(deepcopy(m));stack_N.append(deepcopy(n));stack_ans.append(deepcopy(ans));stack_x.append(deepcopy(x))
                    
                    x[m][n]=ans[m][n][1] 
                    if check(x,b,C)=="Error":
                        x[m][n]=0
                        
                    flag2 = True 
                    break
            if flag2==True:
                break
    
    Check = []
    for i in x:
        for j in i:
            Check.append(j)
    if 0 not in Check:
        break
  
if check(x,b,C)=="True":
    print "answer:" 
    for i in x:
        print i
else:
    print "Sorry I cannot @-@"
    
end = clock()
print int(start)
print int(end)
print end-start

    
'''
simple:
600090020
972500803
035407001
000300059
050000010
320008400
500704190
701002584
040010007

medieum:
302700009
008000045
004001300
000059000
090030060
000260000
001400200
260000100
400002503

hard:
095008000
002006700
040000005
050020007
060050020
400070080
200000040
006100300
000300250


harded:
000000020
081006000
000000430
006001098
000000000
007000063
003569207
579200000
000007000


hardest in the world  by Finlander
800000000
003600000
070090200
050007000
000045700
000100030
001000068
008500010
090000400
'''
