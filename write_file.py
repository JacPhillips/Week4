our_handle=open('pelican.txt','w')
our_handle.write("A wonderful bird is the pelican\n His bill hold more than his belican\n")
lines=["He can take in his beak,\n", "Enough food for a week,\n","But I'm damned if I see how the helican.\n"]
our_handle.writelines(lines)
our_handle.close()#close it then open for reading
our_handle=open('pelican.txt','r')
print(our_handle.read())

#Why is the "\n" required? To makes line by putting each element on its own line
