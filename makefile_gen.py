# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    make_gen.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mdupuis <mdupuis@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/09 19:03:29 by mdupuis           #+#    #+#              #
#    Updated: 2022/03/12 11:27:48 by mqueguin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# python3 make_gen.py pour lancer le script.

import colorama
from colorama import Fore
from colorama import Style

colorama.init()
print("*" * 49)
print(f"**********\\\\\{Fore.GREEN + Style.BRIGHT}Makefile_generator v1.5{Style.RESET_ALL}///**********")
print("*" * 49)
print(f"\nPremiere version par {Fore.YELLOW + Style.BRIGHT}mqueguin{Style.RESET_ALL}, merci a toi l'ami :)\n")
print(f"{Fore.RED + Style.BRIGHT}ATTENTION:{Style.RESET_ALL} Ne pas oublier de rajouter le header de 42!\n\n")

###############################################################################################################
#Project:
prog = input("-- Nom de l'executable que le Makefile va creer: ")
srcs = input("-- Path de vos sources : ")
includes = input("-- Path de vos includes : ")

#libft:
libft_ok = input("-- Votre libft est-elle autorisee ? (o/n) : ")
while libft_ok not in ["o", "n"]:
    libft_ok = input("-- Votre libft est-elle autorisee ? (o/n) : ")
if libft_ok == "o":
    libft = input("-- Path vers votre libft : ")
    libft_dir = input("-- Path de votre libft.a : ")

#mlx:
mlx = input("-- Vous servez-vous de la Minilibx pour ce projet ? (o/n) : ")
while mlx not in ["o", "n"]:
    mlx = input("-- Vous servez-vous de la Minilibx pour ce projet ? (o/n) : ")
if mlx == "o": 
    mlxa = input("-- Path vers mlx.a : ")
    mlx_dir = input("-- Path de la mlx : ")
    flags_mlx_mac = "-framework OpenGL -framework AppKit"

#compilation:
cc = input("-- Quel compilateur voulez-vous utiliser ? (gcc/clang): ")
while cc not in ["gcc", "clang"]:
    cc = input("-- Quel compilateur voulez-vous utiliser ? (gcc/clang): ")
flags = input("-- Flags de compilation ?  : ")
msg_compil = input("(Falcutatif) Tapez un message pour la compilation (exemple : [LOADED]) : ")
if libft_ok == "o":
    libft_compil = input("-- Souhaites-tu cacher la compilation de la libft dans /dev/null ? (o/n) : ")
    while libft_compil not in ["o", "n"]:
        libft_compil = input("-- Souhaites-tu cacher la compilation de la libft dans /dev/null ? (o/n) : ")

#bonus:
bonus = input("-- Avez-vous besoin des regles bonus ? (o/n) : ")
while bonus not in ["o", "n"]:
    bonus = input("-- Avez-vous besoin des regles bonus ? (o/n) : ")
if bonus == "o":
    prog_b = input("Le nom du programme bonus : ")
    srcs_b = input("-- Path de vos .c bonus : ")
    includes_b = input("-- Path de vos .h bonus : ")

#start writting:
file = open("Makefile", "w")
file.write("""
#Colors:
########################
BOLD = \\033[1m
BLUE = \\033[0;34m
CYAN = \\033[36m
GREEN = \\033[32m
ORANGE = \\033[93m
PURPLE = \\033[0;95m
RED = \\033[0;91m
END = \\033[0m
########################\n\n""")

file.write("NAME	        =		" + prog)
if bonus == "o":
    file.write("\n\nNAME_B          =       " + prog_b)

file.write("\n\nSRCS            =       $(wildcard " + srcs + "/*.c)\n\n")
if bonus == "o":
    file.write("SRCS_B      =       $(wildcard " + srcs_b + "/*.c)\n\n")

file.write("INCLUDES_DIR     =       " + includes + "/\n\n")
if bonus == "o":
    file.write("INCLUDES_DIR_B  =       " + includes_b + "/\n\n")

if libft_ok == "o":
    file.write("LIB_DIR         =       " + libft + "/\n\n")
    file.write("LIBFT           =       " + libft_dir + "\n\n")

file.write("CC              =       " + cc + "\n\n")

file.write("OBJS            =       ${SRCS:.c=.o}\n\n")
if bonus == "o":
    file.write("OBJS_B          =       ${SRCS_B:.c=.o}\n\n")

if mlx == "o":
    file.write("MLX         =       " + mlxa + "\n\n")
    file.write("MLX_DIR     =       " + mlx_dir + "/\n\n")

file.write("RM          =       rm -rf\n\n")

if mlx == "o":
    file.write("LFLAGS       =       " + flags_mlx_mac + "\n\n")
file.write("FLAGS       =       " + flags + "\n\n")

file.write(".c.o:\n")
file.write("\t\t\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR} -c $< -o ${<:.c=.o}\n")
file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${GREEN}" + msg_compil + "${END} ${PURPLE}${<:.s=.o}${END}\"\n\n")

file.write("all:\t\t\t${NAME}\n\n")

file.write("${NAME}:\t\t${OBJS}\n")
if mlx == "o" and libft_ok == "n":
    file.write("\t\t\t\t\t\t@make -C ${MLX_DIR} 2>/dev/null\n")
    file.write("\t\t\t\t\t\t@${CC} ${FLAGS} ${LFLAGS} -I${INCLUDES_DIR} -o ${NAME} ${OBJS} ${MLX}\n")
    file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${CYAN} mlx.a${END}   ${GREEN}[ OK ]${END}\"\n")
elif libft_ok == "o" and mlx == "n":
    if libft_compil == "o":
        file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} 2>/dev/null\n")
        file.write("\t\t\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR} -o ${NAME} ${OBJS} ${LIBFT}\n")
    else:
        file.write("\t\t\t\t\t\t@make -C ${LIB_DIR}\n")
        file.write("\t\t\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR} -o ${NAME} ${OBJS} ${LIBFT}\n")
    file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${CYAN} libft.a${END}   ${GREEN}[ OK ]${END}\"\n")
elif mlx == "o" and libft_ok == "o":
    file.write("\t\t\t\t\t\t@${CC} ${FLAGS} ${LFLAGS} -I${INCLUDES_DIR} -o ${NAME} ${OBJS} ${LIBFT} ${MLX}\n")
    file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${CYAN} mlx.a${END}   ${GREEN}[ OK ]${END}\"\n")
    file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${CYAN} libft.a${END}   ${GREEN}[ OK ]${END}\"\n")
else:
    file.write("\t\t\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR} -o ${NAME} ${OBJS}\n")
file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${CYAN}" + prog + "${END}   ${GREEN}[ OK ]${END}\"\n")

if bonus == "o":
    file.write("bonus:\t\t${OBJS_B}\n")
    if mlx == "o" and libft_ok == "n":
        file.write("\t\t\t\t\t\t@make -C ${MLX_DIR} 2>/dev/null\n")
        file.write("\t\t\t\t\t\t@${CC} ${FLAGS} ${LFLAGS} -I${INCLUDES_DIR_B} -o ${NAME_B} ${OBJS_B} ${MLX}\n")
        file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${CYAN} mlx.a${END}   ${GREEN}[ OK ]${END}\"\n")
    elif libft_ok == "o" and mlx == "n":
        if libft_compil == "o":
            file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} 2>/dev/null\n")
            file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} bonus 2>/dev/null\n")
            file.write("\t\t\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR_B} -o ${NAME_B} ${OBJS_B} ${LIBFT}\n")
        else:
            file.write("\t\t\t\t\t\t@make -C ${LIB_DIR}\n")
            file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} bonus\n")
            file.write("\t\t\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR_B} -o ${NAME_B} ${OBJS_B} ${LIBFT}\n")
        file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${CYAN} libft.a${END}   ${GREEN}[ OK ]${END}\"\n")
    elif mlx == "o" and libft_ok == "o":
        file.write("\t\t\t\t\t\t@${CC} ${FLAGS} ${LFLAGS} -I${INCLUDES_DIR_B} -o ${NAME_B} ${OBJS_B} ${LIBFT} ${MLX}\n")
        file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${CYAN} mlx.a${END}   ${GREEN}[ OK ]${END}\"\n")
        file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${CYAN} libft.a${END}   ${GREEN}[ OK ]${END}\"\n")
    else:
        file.write("\t\t\t\t\t\t@${CC} ${FLAGS} -I${INCLUDES_DIR_B} -o ${NAME_B} ${OBJS_B}\n")
    file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${CYAN}" + prog_b + "${END}   ${GREEN}[ OK ]${END}\"\n")

file.write("clean:\n")
file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} clean\n")
file.write("\t\t\t\t\t\t@${RM} ${OBJS} ${OBJS_B}\n")
file.write("\t\t\t\t\t\t@echo \"\\n${BOLD}${RED}\\t\\t *.o files deleted.${END}\"\n\n")

file.write("fclean:\t\tclean\n")
file.write("\t\t\t\t\t\t@make -C ${LIB_DIR} fclean\n")
file.write("\t\t\t\t\t\t@${RM} ${NAME} ${NAME_B}\n")
file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${RED}libft.a deleted.${END}\"\n")
file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${RED}Program " + prog + " deleted.${END}\"\n")
if bonus == "o":
    file.write("\t\t\t\t\t\t@echo \"\\t\\t${BOLD}${RED}Program " + prog_b + " deleted.${END}\"\n")

file.write("\nre:\t\tfclean all\n\n")

file.write(".PHONY:           all     clean   fclean  re\n")
file.close()

print(f"\n\t\t{Fore.RED}!!Attention!!{Fore.RESET}")
print(f"--- {Style.BRIGHT}Les couleurs sont prevues pour Linux.{Style.RESET_ALL}")
print("Si vous etes sur macOS, changez les codes couleur en haut du makefile.\n\n")
print(f"--- Les {Style.BRIGHT}WILDCARDS{Style.RESET_ALL} sont, normalement, interdits.\nPensez donc a modifier vos fichiers sources a la main dant le makefile.\n\n")
print(f"{Style.BRIGHT}Merci d'utiliser Makefile_generator et a bientot !!{Style.RESET_ALL}")
