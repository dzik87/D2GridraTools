#Export function addresses and parameters info
#@author dzik
#@category Diablo 2
#@keybinding 
#@menupath 
#@toolbar

import json

from ghidra.util.exception import CancelledException, InvalidInputException

try:
    i = 0
    for func in currentProgram.functionManager.getFunctions(1):
        if func.getCallingConventionName() == "__thiscall":
            i = i + 1
            func.setCallingConvention("unknown")
            
    print("Found {} functions with __thiscall calling convention".format(i))
        
except CancelledException:
    pass