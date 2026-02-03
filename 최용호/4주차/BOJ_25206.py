import sys
input = sys.stdin.readline

grade = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5,
          'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 
          'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}
total = 0.0
gpa_sum = 0.0

for i in range(20):
    class_name , gpa_str , abcd = input().split()
    if abcd == 'P' :
        continue

    gpa = float (gpa_str)
    total += gpa * grade[abcd] 
    gpa_sum += gpa

print(f'{total / gpa_sum : .6f}')