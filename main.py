from client import *
import numpy as np
import random
from random import seed,randint
from datetime import datetime
key="fSvT9CdkUBUTlwu6EZON9pjEOHcbbsvzlAGMrRkuGgMIkRE6oh"

p_size=15


# array=[0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]

# brr=[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]


# ini=np.zeros((p_size,11))
# ini_mse=np.zeros((p_size))



# for i in range(0,p_size):
#     ini[i]=array

# ini_mse=brr

# np.savetxt('pop.csv',ini,delimiter=',')
# np.savetxt('mse.csv',ini_mse,delimiter=',')


def sorting(pre,mse):
    return pre[(mse).argsort()]




def mutate(pre):
    for i in range(0,p_size):
        for j in range(0,11):
            seed(datetime.now())
            r=randint(1,10)
            if r==1 or r==2 or r==3 or r==4:
                seed(datetime.now())
                c=randint(0,1)
                if c==0:
                    pre[i][j]=pre[i][j] + pre[i][j]/20
                if c==1:
                    pre[i][j]=pre[i][j] - pre[i][j]/20
    return pre


def crossing(pre):
    temp=np.zeros((15,11))
    temp[0]=pre[0]
   
    
    for i in range(0,15):
        list1=[0,1,2,3,4,5,6]
        seed(datetime.now())
        a=random.choice(list1)
        list1.remove(a)
        seed(datetime.now())
        b=random.choice(list1)
        
        temp[i]=pre[a]
        c=randint(0,5)
        x=randint(0,5-c)
        temp[i,x:x+c]=pre[b,x:x+c]
    return temp
        









for k in range(0,1):
    for j in range(0,1):
        pre=np.loadtxt('pop.csv',delimiter=',')
        mse=np.loadtxt('mse.csv',delimiter=',')
        f=open("count.txt","r")
        count=f.read()
        count=int(count)
        f=open("s.txt","a")
        f.write('Generation ')
        f.write(str(count))
        f.write("\n\nInitial\n\n")
        f.write(str(pre))
        pre=crossing(pre)
        f.write("\n\nAfter crossing\n\n")
        f.write(str(pre))
        pre=mutate(pre)
        f.write("\n\nAfter mutation\n\n")
        f.write(str(pre))
        f.write("\n\n-----------------------------------------------------------------------------------------------------------------------------------\n\n")

        for i in range(0,p_size):
            temperr=get_errors(key,list(pre[i]))
            mse[i]=temperr[0]+temperr[1]

        pre=sorting(pre,mse)
        mse=sorting(mse,mse)
        print(pre)
        print()
        print(mse)
        print()
        f=open("count.txt","w")
        count+=1
        f.write(str(count))
        np.savetxt('pop.csv',pre,delimiter=',')
        np.savetxt('mse.csv',mse,delimiter=',')
            
        
        f.close()




