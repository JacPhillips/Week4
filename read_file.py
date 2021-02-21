
slurp= open('pelican.txt')
contents=slurp.read()

print(type(contents),contents,"\n")#print contents and type

read_file=open('pelican.txt').readlines()#converting the contents into a list

print(type(read_file),"\n",read_file)#type is now a list

print("Number of items in read_file:",len(read_file),"\n")

for line in read_file:
    print(line,end="")#removes blank lines