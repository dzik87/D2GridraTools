#Set proper comment on function header
#@author dzik
#@category Diablo 2
#@keybinding 
#@menupath 
#@toolbar

from ghidra.util.exception import CancelledException, InvalidInputException

def main():
    monitor.initialize(currentProgram.getFunctionManager().getFunctionCount())
    for func in currentProgram.functionManager.getFunctions(1): 
        if "{}".format(func.getEntryPoint()) == "00681a48":
            break
            
        if func.hasCustomVariableStorage():
            s = ""
            for arg in func.getParameters():
                s = s + "\n{}".format(arg)
            func.setComment("Diablo 2 1.14d reverse team\nhttps://blizzhackers.dev\n\nFunction uses custom registers for function arguments!{}".format(s))
        else:
            func.setComment("Diablo 2 1.14d reverse team\nhttps://blizzhackers.dev")
            
        monitor.incrementProgress(1)
        monitor.setShowProgressValue(True)
                
try:
    main()
except CancelledException:
    pass