c = [(0,1), (4,5), (8,9), (12,13), (16,17), (20,21)]
b = (20,10)
def guess(b,a):
    a0 = []
    a1 = []
    for i in range(len(a)):
        a0.append(a[i][0])
        a1.append(a[i][1])

    for i in range(len(a0)):
        if -2 < (int(a0[i]) - int(b[0])) < 2:
            out0 = a0[i]
    for i in range(len(a1)):
        if -2 < (int(a1[i]) - int(b[1])) < 2:
            out1 = a1[i]

    
    output = (out0,out1)
    return output
print(guess(b,c))
