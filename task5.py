#!/usr/bin/python
class Solve(object):
    def Circle(self, go):
        """left right"""
        lr = 0
        """down up"""
        dup = 0
        for i in range(len(go)):
            if(go[i] == 'R'):
                lr = lr + 1
            if (go[i] == 'L'):
                lr = lr - 1
            if(go[i] == 'U'):
                dup = dup + 1
            if(go[i] == 'D'):
                dup = dup - 1
        if(lr == 0 and dup == 0):
            return True
        else:
            return False

s = Solve()

print("Output:"),
print(s.Circle("UD"))
