word = raw_input("Tapez le nom du prog que le Makefile va creer: ")

file = open("Makefile", "w")
file.write("NAME	=		" + word)
file.close()
