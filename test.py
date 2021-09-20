print("ATTENTION: Ne pas oublier de rajouter le header de 42!\n\n")
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
libft_compil = input("1 Si tu veux cacher la compilation de la libft avec /dev/null sinon 0 : ")

file = open("Makefile", "w")
file.write("NAME	        =		" + word)
file.write("\n\nSRCS            =       $(wildcard " + srcs + "/*.c)\n\n")
file.write("INCLUDES_DIR     =       " + includes + "/\n\n")
file.write("LIB_DIR         =       " + libft + "/\n\n")
file.write("LIBFT           =       " + libft_dir + "\n\n")
file.write("CC              =       " + cc + "\n\n")
file.write("OBJS            =       ${SRCS:.c=.o}\n\n")

if mlx == 1:
    file.write("MLX         =       " + mlxa + "\n\n")
    file.write("MLX_DIR     =       " + mlx_dir + "/\n\n")

file.write("RM          =       rm -rf\n\n")
if mlx == 1:
    file.write("FLAGS       =       " + flags + " " + flags_mlx_mac + "\n\n")
else:
    file.write("FLAGS       =       " + flags + "\n\n")

file.write(".c.o:\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR} -c $< -o $@\n")
file.write("\t\t\t\t\t@echo \"" + msg_compil + "\"\n\n")

file.write("all:\t\t\t${NAME}\n\n")
file.write("${NAME}:\t\t${OBJS}\n")
if mlx == 1:
    file.write("\t\t\t\t\t\t@make -C ${MLX_DIR} 2>/dev/null\n")
if libft_compil == 1:
    file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} 2>/dev/null\n")
    file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} bonus 2>/dev/null\n")
else:
    file.write("\t\t\t\t\t\t@make -C ${LIB_DIR}\n")
    file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} bonus\n")

if mlx == 1:
    file.write("\t\t\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR} -o ${NAME} ${OBJS} ${LIBFT} ${MLX}\n")
else:
    file.write("\t\t\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR} -o ${NAME} ${OBJS} ${LIBFT}\n")
file.write("\t\t\t\t\t\t@echo \"libft.a has been created\"\n")
file.write("\t\t\t\t\t\t@echo \"" + word + " has been created\"\n\n")
file.write("\n.PHONY:           all     clean   fclean  re\n")
file.close()

print("Les couleurs sont a rajouter a la main !!!\n")