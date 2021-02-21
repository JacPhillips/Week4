cheese= ['Cheedar','Stilton', 'Cornish Yarg']
cheese.insert(3,'Oke') #solution
#orginal code: cheese+='Oke'. This added each letter of the string 'oke' as an item in the list

#How would you add two new cheeses to the list with a single command?
cheese [:0]=['Red Leicester','Brie'] #solution 1
cheese.extend(['Parmasan', 'Camembert']) #solution 2
print(cheese)



