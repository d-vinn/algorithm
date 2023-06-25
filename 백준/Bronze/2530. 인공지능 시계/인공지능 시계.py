h, m, s = map(int, input().split())
t = int(input())

p_h = t//3600
p_m = (t%3600)//60
p_s = t%60

if (s+p_s)//60 > 0 :
  p_m += 1

if (m+p_m)//60 > 0:
  p_h += 1

e_h = (h+p_h)%24
e_m = (m+p_m)%60
e_s = (s+p_s)%60

print(e_h, e_m, e_s)