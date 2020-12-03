from time import time
from numba import jit, int64, void


def part1(intlist):
    intdic = {x:(2020-x) for x in intlist}
    for price in intdic:
        residual = intdic[price]
        try:
            matching = intdic[residual]
            if price == matching:
                return residual * matching
        except:
            pass

@jit(nopython = True, cache = True)
def part2(intlist):
    maxindex = len(intlist)- 1
    listrange = maxindex - 2
    for a in range(listrange):
        firstElement = intlist[a]
        i = a+1
        j = maxindex
        while (i<j):
            left = intlist[i]
            right = intlist[j]
            triad = firstElement + left + right
            if triad > 2020:
                i+=1
            elif triad < 2020:
                j-=1
            elif triad == 2020:
                return firstElement*left*right

def main():
    f = open('input.txt')
    intlist = (list(map(int, f.readlines())))
    intlist.sort()
    intlist = intlist[::-1]

    
    time1 = []
    time2 = []
    for i in range(100):
        start1 = time()
        part1(intlist)
        end1 = time()

        start2 = time()
        part2(intlist)
        end2 = time()

        timerlist = [end1-start1, start2 - end2]
        time1.append(timerlist[0])
        time2.append(timerlist[1])
    avgtime1 = sum(time1)/len(time1)
    avgtime2 = sum(time2)/len(time2)
    timerlist = [avgtime1, avgtime2]
    delim = '='*50 
    print(f"{delim}")
    print(f"{'runtime statistics' :^50}")
    print(f"{delim}")
    for i in range(len(timerlist)):
        print(f"part {i+1}: {timerlist[0]:e}")

if __name__ == '__main__':
    main()
