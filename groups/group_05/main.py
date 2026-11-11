"""
PhotoCensus - Group 00 (TEMPLATE)

Copy this folder to /groups/group_XX/ (XX = your group number)
and write your project here. Do not modify anything in /kit.
"""
import os
import sys

# Lets this file find black_box.py in /kit (do not remove these lines)
GROUP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(GROUP_DIR, "..", "..", "kit"))
from black_box import *   # noqa: E402,F401,F403


def show_menu(config):
    print('\n--- OPTIONS ---')
    print(f'-- Confiança Mínima atual {config["trust"]}--\n')
    print('1 - Configurar a confiança mínima')
    print('2 - Analisar uma foto')
    print('3 - Analisar uma pasta')
    print('0 - Sair')
    return input("Escolha uma opção: ")

def minimal_trust(config):
    while True:
        try:
            new = float(input("Defina a nova confiança mínima: "))
            if 0 <= new <= 1:
                break
            else:
                print("Defina um valor entre 0.0 e 1.0")
        except ValueError:
            print("Defina um valor entre 0.0 e 1.0")

            
    config["trust"] = new

def choose_folder():
    show_folders()
        
    folder = input("Escolha uma pasta: ")
    
    while not folder_exists(folder): 
        print("Digite um valor válido!")
        show_folders()
        folder = input("Escolha uma pasta: ")
    return folder

def choose_photo(folder):
    while True:
        try:
            number = int(input(f"Escolha uma foto (de 1 a {total_photos(folder)}): "))
            if 1 <= number <= total_photos(folder):
                break
            print("Digite um valor válido!")
        except ValueError:
            print("Digite um valor válido!")

    photo = photo_name(folder, number)
    return photo

def photo_analyze(config):
    folder = choose_folder()

    photo = choose_photo(folder)

    while True:
        print("\n1 - Análise geral")
        print("2 - Contar uma classe\n")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Caminho: {photo}")
            print(f"Objetos detectados: {count_objects(photo,config["trust"])}")
            print(f"Objeto de maior confiança: {main_object(photo)}")
            print(f"Maior confiança: {max_confidence(photo) *100:.0f}%")
            break

        elif opcao == "2":
            photo_class(config, photo)
            break 

        else:
            print("Digite um valor válido")

def photo_class(config, photo):

    show_classes()
    class_name = input("Digite uma classe para buscar objetos: ")


    print(f"Há {count_class(photo, class_name, config['trust'])} objetos com a classe {class_name}")

def folder_analyze():
    print("analisar pasta...")

def main():
    print("PhotoCensus - Group 05")
    show_folders()
    # Your menu (while loop) starts here...

    config = {"trust" : 0.5}

    acoes = {"1": minimal_trust,
             "2": photo_analyze
             }

    while True:
        opcao = show_menu(config)

        if opcao in acoes:
            acoes[opcao](config)
        elif opcao == "0":
            break
        else:
            print("Digite um valor válido!")



if __name__ == "__main__":
    main()
