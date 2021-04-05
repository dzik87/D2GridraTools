#Change namespace in range
#@author dzik
#@category Diablo 2
#@keybinding 
#@menupath 
#@toolbar

c = 0
n = currentProgram.functionManager.getFunctionAt(currentAddress).getParentNamespace()

for f in currentProgram.functionManager.getFunctions(currentAddress, True):
    cn = f.getParentNamespace()
    if cn == n:
        c = c + 1
        print(f.getName())
        if c == 2:
            break
    else:
        f.setParentNamespace(n)
    