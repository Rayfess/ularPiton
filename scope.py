gscop = 100
def changeScope():
# overwrite
    global gscop
    gscop = 1 

changeScope()
print(gscop) # will output 1

def mainf():
    msg = "Hello from the main"

    def subf():
        # overwrite
        nonlocal msg
        msg = "Hello from the sub"

    subf()
    print(msg)

mainf() #will output subf msg



