def genarator(jakismax):
    for i in range(0, jakismax, 2):
        yield i

for x in genarator(15):
    print(x)