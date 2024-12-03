with open("input.txt")as f:print(sum([abs(i[0]-i[1])for i in zip(*list(map(sorted,zip(*[map(int,line.split())for line in f.read().splitlines()]))))]))
