import sys
input = sys.stdin.readline

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
check_list = [0] * 26

word = input().strip().upper()

for ch in word:
    index = ord(ch) - ord('A')
    check_list[index] += 1


maxi = max(check_list)   

if check_list.count(maxi) >= 2:
    print('?')
   
else :
    max_index = check_list.index(maxi)
    print(alphabet[max_index])
    
    