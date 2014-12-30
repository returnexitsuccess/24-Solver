import math

def replace(ls, a, b):
    #replaces instances of "a" in a list "ls" with b
    i = 0
    while (i < len(ls)):
        if (ls[i] == a):
            ls[i] = b
        i += 1
    return ls

print "Please input four numbers separated by new lines:"
a = float(raw_input())
b = float(raw_input())
c = float(raw_input())
d = float(raw_input())
abcd = [a, b, c, d]
arr = [0, 0, 0, 0]
brk = False
counter = 0
i = 0
while (i < 24):   
    abcd = [a, b, c, d]
    arr[0] = abcd.pop(i / 6)
    arr[1] = abcd.pop((i % 6) / 2)
    arr[2] = abcd.pop(i % 2)
    arr[3] = abcd.pop(0)
    j = 0
    while (j < 64):
        ops = [0, 0, 0]
        ops[2] = j % 4
        ops[1] = (j / 4) % 4
        ops[0] = (j / 16) % 4
        origops = [ops[0], ops[1], ops[2]]
        k = 0
        while (k < 6):
            total = [arr[0], arr[1], arr[2], arr[3]]
            ops = [origops[0], origops[1], origops[2]]
            #print str(i) + " " + str(j) + " " + str(k)
            temp = [0, 1, 2]
            order = [0, 0, 0]
            order[0] = temp.pop(k / 2)
            order[1] = temp.pop(k % 2)
            order[2] = temp.pop(0)
            origorder = [order[0], order[1], order[2]]
            l = 0
            while (l < 3):
                index = order[l]
                if (ops[index] == 0):
                    total[index] += total.pop(index + 1)
                    ops.pop(index)
                elif (ops[index] == 1):
                    total[index] -= total.pop(index + 1)
                    ops.pop(index)
                elif (ops[index] == 2):
                    total[index] *= total.pop(index + 1)
                    ops.pop(index)
                elif (ops[index] == 3):
                    if (total[index + 1] == 0):
                        total[0] = 0
                        break
                    total[index] /= total.pop(index + 1)
                    ops.pop(index)
                order = replace(order, index + 1, index)
                order = replace(order, index + 2, index + 1)
                l += 1
            if (math.fabs(total[0] - 24) < 10**-5):
                brk = True
                break
            k += 1
        if (brk):
            break
        j += 1
    if (brk):
        break
    i += 1

origops = replace(origops, 0, "+")
origops = replace(origops, 1, "-")
origops = replace(origops, 2, "*")
origops = replace(origops, 3, "/")

if (brk):
    print origorder
    print origops
    print arr
else:
    print "Solution not found"

raw_input()
