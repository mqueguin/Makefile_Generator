word = raw_input("Tapez le nom du prog que le Makefile va creer: ")
srcs = raw_input("Tapez le dossier qui contient vos .c : ")
includes = raw_input("Tapez le dossier qui contient vos .h :")
libft = raw_input("Tapez le chemin vers la libft : ")
libft_dir = raw_input("Tapez le chemin vers votre libft.a : ")
mlx = input("Si mlx tapez 1 ou 0 sinon : ")
if mlx == 1: 
    mlxa = raw_input("Tapez le chemin vers mlx_a : ")
    mlx_dir = raw_input("Tapez le chemin vers la mlx : ")
    flags_mlx_mac = "-framework OpenGL -framework AppKit"

cc = raw_input("Tapez le compilateur que vous voulez clang ou gcc : ")
flags = raw_input("Tapez les flags dont vous avez besoins a la compilation : ")
msg_compil = raw_input("(Falcutatif) Tapez un message pour la compilation (exemple : [LOADED]) : ")


file = open("Makefile", "w")
file.write("NAME	        =		" + word)
file.write("\n\nSRCS        =       $(wildcard " + srcs + "/*.c)\n\n")
file.write("INCLUDE_DIR     =       ./" + includes + "/\n\n")
file.write("LIB_DIR         =       ./" + libft + "/\n\n")
file.write("LIBFT           =       ./" + libft + "/" + libft_dir + "\n\n")

file.write("\n.PHONY:           all     clean   fclean  re")
file.close()

print("Les couleurs sont a rajouter a la main !!!\n")