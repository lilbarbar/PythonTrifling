from pathlib import Path

#Absolute path --> start from root of hard disk
#Relative path --> current directory soemwhere else

path = Path("ecommerce")
print(path.exists()) #checks to see if Path exists

path = Path("ecommerce1")
print(path.exists()) #checks to see if Path exists


path = Path("emails")
print(path.mkdir()) #Makes a direcotty

print (path.rmdir()) #removes direcotry




p = Path('Python Truffle')


#.glob() searches for files and directories in path
print(p.glob("*"))  # * means eveyrthing all files and directories
print (p.glob("*.*")) #get files in directories
print (p.glob("*.py")) #all python files


#generator objects are returned (advanced but can be looped through)


for file in p.glob('*'):  #doesn' twork
    print (file)



    #PYPI Python Packiage index (packages built by people which are made by one to be rused in another)