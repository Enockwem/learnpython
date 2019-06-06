
name = []
myname = input("Enter the name: ")
for letter in myname:
    name.append(letter)
    n = name.count('a')
    m = name.count('e')
    number = name.count(letter)
#print(n)
#print(m)
if (n > m):
    print (n)
    print("There are more a's than e's in the statement written above")
elif(n < m):
    print (m)
    print("There are more e's than a's in the statement written above")
elif((m == n) and m != 0 ):
    print (m)
    print("There are equal numbers in the statement written above")
else:
    print("There are no a's and e's in the statement written above")
#print(counta)
#print(countb)