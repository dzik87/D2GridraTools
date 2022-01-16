#Set proper comment on function header with sign
#@author dzik
#@category Diablo 2
#@keybinding F6
#@menupath 
#@toolbar

from ghidra.util.exception import CancelledException, InvalidInputException
from datetime import date

today = date.today()
nick = ghidra.framework.client.ClientUtil.getUserName()

def main():
    func = currentProgram.functionManager.getFunctionContaining(currentAddress);
    
    func.setComment("Diablo 2 1.14d reverse team\nhttps://blizzhackers.dev\n\nFunction: {}\nAddress: {}.0x{}\nDate: {}\nLast editor: {}".format(func.getName(), currentProgram.getName().rsplit(".",1)[0], func.getEntryPoint(), today.strftime("%Y.%m.%d"), nick))
        
    if func.hasCustomVariableStorage():
        s = ""
        for arg in func.getParameters():
            s = s + "\n{}".format(arg)
        func.setComment("{}\n\nFunction uses custom registers for function arguments!{}".format(func.getComment(), s))
                
try:
    main()
except CancelledException:
    pass