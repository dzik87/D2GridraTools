#Create functions from pointers in array and decompile them
#@author dzik
#@category Diablo 2
#@keybinding 
#@menupath 
#@toolbar

from ghidra.app.cmd.function import CreateFunctionCmd
from ghidra.app.cmd.disassemble import DisassembleCommand



# helper function to get a Ghidra Address type
# accepts hexstring
def getAddress(addr):
    # Address getAddress(java.lang.String addrString)
    return currentProgram.getAddressFactory().getAddress(addr)

base = currentAddress
for i in range(52):
    number = currentProgram.getMemory().getInt(base.add(i*4))
    addr = getAddress("{:08X}".format(number))

    cmd = DisassembleCommand(addr, None, False)
    cmd.applyTo(currentProgram, monitor)

    cmd = CreateFunctionCmd(addr)
    cmd.applyTo(currentProgram)