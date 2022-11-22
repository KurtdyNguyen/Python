class block:
    def __init__(self, pos, pts):
        self.pos = pos
        self.pts = pts

    def jump(self, step, end):
        if end < self.pos+step:
            return 0
        else:
            self.pos += step
            self.jump(step)
    
    def printf(self):
        return self.pts
        
x = list(map(int, str(input()).split(' ')))
a0 = list(map(int, str(input()).split(' ')))
a = []
for i in range(1, x[0]+1):
    a.append(block(i, a0[i-1]))