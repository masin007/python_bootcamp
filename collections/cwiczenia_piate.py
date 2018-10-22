# x = [1 ,2 ,3]
#
# for i in x:
#     print(f"{i:3}", end="")




# i = 0
# j = 0
# x = 0
# print("   ", end="")
# while x<10:
#     print(f"{x:3}", end="")
#     x +=1
# print()
# print()
#
# for i in range(0,10):
#     print(f"{i}"," ", end="")
#     for j in range(0,10):
#         print(f"{i*j:3}", end="")
#     print()

print("   ", end="")
for x in range(10):
    print(f"{x:3}", end="")

print()
print()


for x in range(10):
    print(x, end="  ")
    for y in range(10):
        print(f"{x*y:3}", end="")
    print()