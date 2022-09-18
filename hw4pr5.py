# CSCI 1550: HW 4, Problem 5
# Filename: hw4pr5.py
# Name: Peter Morales
#
# Task(s): Creating the int8 class!


class int8: 
    num = 0
       
    def int2int8(val):
       a = (val & 255)
       return a

    def setVal(self, val): 
        self.num = int8.int2int8(val)

    def getVal(self):
        outVal = int8.int2int8(self.num)
        return outVal

    def __add__(self,obj):
        outZa = int8()
        outZa.num = (self.num + obj.num)
        return outZa

    def __neg__(self):
        outZn = int8()
        outZn.num = (int8.int2int8(~(self.num) + 1))
        return outZn
        
    def __sub__(self,obj):
        outZs = int8()
        outZs.num = (int8.int2int8(self.num + -obj.num))
        return outZs
    
    def __divBy2__(self):
        outZd = int8()
        outZd.setVal(self.getVal()>>1)
        return outZd
    
    def __mod2__(self):
        outZm = int8()
        outZm.num = (((self.num + 1)>>1) + -(self.num>>1))
        return outZm.num
    
    def __bit2Str__(self):
        outZb2s = int8()
        outZb2s.num = str(self)
        return outZb2s
    
    def int8ToString(self):
        outZint2str = str((int8.__mod2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(self)))))))))) + str((int8.__mod2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(self))))))))) + str((int8.__mod2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(self)))))))) + str((int8.__mod2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(self))))))) + str((int8.__mod2__(int8.__divBy2__(int8.__divBy2__(int8.__divBy2__(self)))))) + str((int8.__mod2__(int8.__divBy2__(int8.__divBy2__(self))))) + str((int8.__mod2__(int8.__divBy2__(self)))) + str((int8.__mod2__(self)))
        return outZint2str
    
    def __repr__(self):
        outZr = (int8.int2int8(self.num))
        x = str(outZr)
        return x

