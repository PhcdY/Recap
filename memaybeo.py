so_lan_fibo = int(input("Hay nhap so thu tu cua Fibonacci muon tinh: "))
sequence = []
if so_lan_fibo == 1:
    list.append(0)
elif so_lan_fibo == 2:
    list.append(0)
    list.append(1)
else:
    list.append(0)
    list.append(1)
    for i in range(0, so_lan_fibo):
        u1 = 0
        u2 = 1
        next = u1 + u2
        u2 = next
        list.append(u2)

print(sequence)