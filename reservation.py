'''
This program checks the name that the user inputs with the name that is already
set in a variable. If the user's name is the same as the reserved name, the
program will print "Right this way", but if it is not the same, it will print
"Sorry, we don't have a reservation under that name." 
'''
# Miki Ando
name = str(input("Name: "))
reservation_name= "Ando"

if name == reservation_name:
    print "Right this way!"
else:
    print "Sorry, we don't have a reservation under that name"
