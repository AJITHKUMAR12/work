from os import path
def createpath(filename):
    if not (path.isfile(filename)):
        file = open(filename, "w")
        file.write("hi,this is demo")
        file.close()
filename="C:\Ajith Documents\latest\demo.txt"
createpath(filename)
print("file created")