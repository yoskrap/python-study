false_list = [1,2,4,7]
# 시간복잡도는 O(1)
n = int(input())

if n in false_list : 
    print(-1)
    exit(0)

if n % 3 == 0 : 
    a = n // 15
    b = n % 15 

    print(3 * a + b // 3) 
    

elif n % 3 == 1:
    a = n // 15
    b = n % 15 
    if b in false_list : 
        a -= 1
        b += 15
    print(3 * a + ((b - 10) // 3) + 2 )    
    

else :
    a = n // 15
    b = n % 15
    if b in false_list : 
        a -= 1
        b += 15 
    print(3 * a + ((b - 5) // 3) + 1)
    
    