
# Debugging



# Starting the Debugger


def seq(n):
    for i in range(n):
        print(i)
    return

seq(5)


import pdb

#interactive debugging
def seq(n):
    for i in range(n):
        pdb.set_trace() # breakpoint
        print(i)
    return

seq(5)


# c : continue
# q: quit
# h: help
# list
# p: print
# p locals()
# p globals()



# Debugger Commands















