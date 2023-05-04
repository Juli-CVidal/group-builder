import random
import math


def show_invalid_message():
    print("Opción inválida, reintente")


def ask_value_in_range(min_value: int, max_value: int) -> int:
    user_input = min_value - 1
    while (min_value > user_input or max_value < user_input):
        user_input = input(f"Ingrese un valor entre {min_value} y {max_value}: ")
        if (not user_input.isdigit()): 
            show_invalid_message()
            continue
        user_input = int(user_input)
        print("\n")

    return user_input


def ask_option(options: list) -> int:
        for index, option in enumerate(options):
            print(f"{index+1}. {option}")

        print("Elija una opción")
        return ask_value_in_range(1,len(options)) - 1


def get_group_size(option: int, total_members: int) -> int:
    print("Cuántos integrantes deben ir por groupo? " if option == 0 else "Cuántos grupos quiere? ")
    group_size = ask_value_in_range(1,total_members)
    return group_size if option == 0 else math.ceil(total_members / group_size)
   

def build_groups(names: list, group_size: int) -> list:
    num_groups = math.ceil(len(names) / group_size)
    groups = [[] for _ in range(num_groups)]

    for index, name in enumerate(names):
        group_index = index % num_groups
        groups[group_index].append(name)
    
    index = 0
    for name in names[num_groups * group_size:]:
        groups[index].append(name)
        index = (index + 1) % num_groups
    
    return groups


OPTIONS = ["Separar por cantidad de integrantes",
           "Separar por cantidad de grupos"]

try:
    with open("names.txt", "r") as reader:
        names = reader.read().splitlines()
except FileNotFoundError:
    print("No se pudo encontrar el archivo 'names.txt'")
except Exception as e:
    print(f"Se produjo un error al leer el archivo: {str(e)}")
    
total_members = len(names)
option = ask_option(OPTIONS)
group_size = get_group_size(option, total_members)

random.shuffle(names)
groups = build_groups(names,group_size)

with open("groups.txt","w") as writter:
    for index,group in enumerate(groups):
        writter.write(f"Campamento #{index+1}:\n")
        for member in group:
            writter.write(f"{member}\n")
        writter.write("\n")

print("Grupos creados exitosamente. Revise el archivo 'groups.txt'")