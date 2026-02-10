min_input = input()
man_input = input()

min_i, min_m, min_s, min_e = map(int, min_input.split())
man_i, man_m, man_s, man_e = map(int, man_input.split())

s = min_i + min_m + min_s + min_e
t = man_i + man_m + man_s + man_e

print(s if (s>=t) else t)
