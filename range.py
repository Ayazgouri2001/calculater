##range
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

##seq pr loop chala rahe
seq = range(5)
for i in seq:
    print(i)

#stop range 1 element hota h
for i in range(10): #range stop
    print(i)

#star stop range me to element hote h  
for i in range(2, 10):
    print(i)   

# step inte se increase karna 3 ele hote
for i in range(2, 10, 2):
    print(i)    

##even num print
for i in range(2, 101, 2):
    print(i)    

#1 to 100 num print
num = (1)
for i in range(101):
    print(i) 

#100 to 1 print 
for i in range(100, 0, -1):
    print(i)

##multiplication
n = int(input("enter number : "))     
for i in range(1, 11):
    print(n * i)