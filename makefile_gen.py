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
bonus = input("Tapez 1 si vous voulez la regle bonus sinon 0 : ")
if bonus == 1:
    name_b = raw_input("Le nom du programme bonus : ")
    srcs_b = raw_input("Tapez le dossier ou sont vos .c bonus : ")
    includes_b = raw_input("Tapez le dossier ou sont vos .h bonus : ")


file = open("Makefile", "w")
file.write("NAME	        =		" + word)
if bonus == 1:
    file.write("\n\nNAME_B          =       " + name_b)
file.write("\n\nSRCS            =       $(wildcard " + srcs + "/*.c)\n\n")
if bonus == 1:
    file.write("SRCS_B      =       $(wildcard " + srcs_b + "/*.c)\n\n")
file.write("INCLUDES_DIR     =       " + includes + "/\n\n")
if bonus == 1:
    file.write("INCLUDES_DIR_B  =       " + includes_b + "/\n\n")
file.write("LIB_DIR         =       " + libft + "/\n\n")
file.write("LIBFT           =       " + libft_dir + "\n\n")
file.write("CC              =       " + cc + "\n\n")
file.write("OBJS            =       ${SRCS:.c=.o}\n\n")
if bonus == 1:
    file.write("OBJS_B          =       ${SRCS_B:.c=.o}\n\n")

if mlx == 1:
    file.write("MLX         =       " + mlxa + "\n\n")
    file.write("MLX_DIR     =       " + mlx_dir + "/\n\n")

file.write("RM          =       rm -rf\n\n")
if mlx == 1:
    file.write("LFLAGS       =       " + flags_mlx_mac + "\n\n")
file.write("FLAGS       =       " + flags + "\n\n")

file.write(".c.o:\n")
file.write("\t\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR} -c $< -o ${<:.c=.o}\n")
file.write("\t\t\t\t\t@echo \"\\x1b[32m" + msg_compil + "\\033[0m ${<:.s=.o}\"\n\n")

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
    file.write("\t\t\t\t\t\t@${CC} ${FLAGS} ${LFLAGS} -I${INCLUDES_DIR} -o ${NAME} ${OBJS} ${LIBFT} ${MLX}\n")
else:
    file.write("\t\t\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR} -o ${NAME} ${OBJS} ${LIBFT}\n")
file.write("\t\t\t\t\t\t@echo \"\\nlibft.a has been created\"\n")
file.write("\t\t\t\t\t\t@echo \"" + word + " has been created\"\n\n")

if bonus == 1:
    file.write("bonus:\t\t${OBJS_B}\n")
    if mlx == 1:
        file.write("\t\t\t\t\t\t@make -C ${MLX_DIR} 2>/dev/null\n")
    if libft_compil == 1:
        file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} 2>/dev/null\n")
        file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} bonus 2>/dev/null\n")
    else:
        file.write("\t\t\t\t\t\t@make -C ${LIB_DIR}\n")
        file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} bonus\n")
    if mlx == 1: 
        file.write("\t\t\t\t\t\t@${CC} ${FLAGS} ${LFLAGS} -I ${INCLUDES_DIR_B} -o ${NAME_B} ${OBJS_B} ${LIBFT} ${MLX}\n")
    else:
        file.write("\t\t\t\t\t\t@${CC} ${FLAGS} -I ${INCLUDES_DIR_B} -o ${NAME_B} ${OBJS_B} ${LIBFT}\n")
    file.write("\t\t\t\t\t\t@echo \"\\nlibft.a has been created\"\n")
    file.write("\t\t\t\t\t\t@echo \"" + name_b + " has been created\"\n\n")

file.write("clean:\n")
file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} clean\n")
file.write("\t\t\t\t\t\t@${RM} ${OBJS} ${OBJS_B}\n")
file.write("\t\t\t\t\t\t@echo \"\\n *.o files deleted\\n\"\n\n")

file.write("fclean:\t\tclean\n")
file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} fclean\n")
file.write("\t\t\t\t\t\t@${RM} ${NAME} ${NAME_B}\n")
file.write("\t\t\t\t\t\t@echo \"\\nPrograms The libft and " + word + " have been deleted\\n\"\n\n")

file.write("re:\t\tfclean all\n\n")
file.write(".PHONY:           all     clean   fclean  re\n")
file.close()

print("Les couleurs sont a rajouter a la main !!!\n")