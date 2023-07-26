S = input()
cro = ["c=", "c-", "dz=", "z=", "lj", "nj", "s=", "d-"]
for i in cro:
    S = S.replace(i, "A")
    
print(len(S))