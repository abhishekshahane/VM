class VM:
    def __init__(self, instructions):
        self.program = instructions
        self.IP = 0

        self.FLAG_exit = False
        self.REG_a = 0
        self.REG_b = 0
        self.REG_c = 0
        self.REG_d = 0

    def step(self):
        if (self.program[self.IP] == 0x00):
            self.FLAG_exit = True
        elif self.program[self.IP] == 0x01:
            reg = self.getByte()
            number = self.getNumber()
            self.setRegister(reg, number)
        elif (self.program[self.IP] == 0x02):
                a = self.getByte()
                b = self.getByte()
                value = self.getRegister(b)
                self.setRegister(a, value)
            
        self.IP += 1

            
    def getRegister(self, id):
        if (self.program[self.IP] == 0x00 ):
            return self.REG_a
        elif (self.program[self.IP] == 0x01):
            return self.REG_b
        elif (self.program[self.IP] == 0x02):
            return self.REG_c
        elif (self.program[self.IP] == 0x03):
            return self.REG_d
        
    def getNumber(self):
        number = self.getByte()
        for i in range(3):
            # Shift to the left by 8 bytes
            number = number << 8
            number += self.getByte()
        return number
    
    def setRegister(self, id, value):
        if id == 0x00:
            self.REG_a = value
            return
        elif id == 0x01:
            self.REG_b = value
            return
        elif id == 0x02:
            self.REG_c = value
            return
        elif id == 0x03:
            self.REG_d = value
            return
        
    def debug(self):
        print(f"a: {self.REG_a}\nb: {self.REG_b}\nc: {self.REG_c}\nd: {self.REG_d}\n")
        
    def run(self):
        while self.FLAG_exit != True:
            self.step()
            
    def getByte(self):
        self.IP += 1
        return self.program[self.IP]
        
    
            
instructions = [0x01, 0x01, 0x12, 0x32, 0x56, 0x78, 0x02, 0x00, 0x01, 0x00]
vm = VM(instructions)
vm.run()
vm.debug()