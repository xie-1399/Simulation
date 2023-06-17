#RISCV Decode unit
from RISCV import *
class Decode(object):
    def __init__(self,pc):
        self.extension = ["I"]
        self.pc = pc
        self.ir = {}


    #add more extensions after
    def addextension(self,extension):
        self.extension.append(extension)

    def decodein(self,ir):
        self.ir.update(ir)

    #No order
    def decodeout(self,key):
        self.ir.pop(key)

    def registeraddress(self,type):
        kind = typeregister.get(type,default="N")
        assert kind != "N","type register error"
        return kind

    def dealir(self,ir):
        '''
        :return: opcode irtype rs1 rs2 im
        '''
