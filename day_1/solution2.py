def sol():
    with open('input.txt') as f:
        intlist = (list(map(int, f.readlines())))
        maxindex = len(intlist)- 1
        intlist.sort(reverse = True)
        print(intlist)
        for a in range(maxindex - 2):
            firstElement = intlist[a]
            i = a+1
            j = maxindex
            while (i<j):
                left = intlist[i]
                right = intlist[j]
                triad = firstElement + left + right
                print(triad)
                if triad > 2020:
                    i+=1
                elif triad < 2020:
                    j-=1
                elif triad == 2020:
                    return firstElement*left*right
print(sol())

