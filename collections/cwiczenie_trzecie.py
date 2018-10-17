x = [1, -2, 3, -7, -4, 6, 11, 77, -22]
i = 0
j = 0
z = 0
for i in x:
    if i < 0:
        j = j + 1

    elif i > 0:
         z = z +1

print(f"Dodatnich liczb jest : {z}, ujemnych: {j}")