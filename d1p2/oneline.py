with open("input.txt")as f:print((lambda l:sum([l[1].count(j)*j for j in l[0]]))(list(map(sorted,zip(*[map(int,line.split())for line in f.read().splitlines()])))))
