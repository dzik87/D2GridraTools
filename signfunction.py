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
    
    comment = func.getComment();
    if comment:
      comment = filter(lambda x: '@description: ' in x, comment.splitlines())
    if comment and len(comment) > 0:
        comment = comment[0].split('@description: ')[1]
    else:
        comment = ""
    
    func.setComment("""Diablo 2 1.14d reverse team
https://blizzhackers.dev
        
@Date: {}
@Author: {}
@Function: {}
@Address: {}.0x{}
@description: {}""".format(today.strftime("%Y.%m.%d"), nick, func.getName(), currentProgram.getName().rsplit(".",1)[0], func.getEntryPoint(), comment))
        
    if func.hasCustomVariableStorage():
        s = ""
        for arg in func.getParameters():
            s = s + "\n{}".format(arg)
        func.setComment("{}\n\nFunction uses custom registers for function arguments!{}".format(func.getComment(), s))
                
try:
    main()
except CancelledException:
    pass
