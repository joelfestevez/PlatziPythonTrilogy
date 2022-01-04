# import random

# def read_word():
#     with open("./archivos/words.txt","r", encoding="utf-8") as f: 
#         words_list=[]
#         for line in f:
#             words_list.append(line.replace("\n","")) #Se arma la lista y elimino los saltos de linea
#     word=random.choice(words_list) #Escogemos una palabra aleatoriamente
#     return word

# def run():
#     word = read_word()
#     vidas=6
#     hided_word = word.replace(word,"_"*len(word))
#     print("Bienvenido al ahorcado\nTienes "+str(vidas)+" vidas\nAdivina la siguiente palabra:\n"+hided_word)
#     while True:
#         try:
#             character=input("\nIntroduce letra: ")
#             if character != str:
#                 raise ValueError
#             if character in word:
#                 pass
#             else:
#                 vidas -= 1
#                 print("Vas mal\nVidas: "+str(vidas))
#             if vidas == 0:
#                 print("Perdiste papito, la palabra era: "+word)
#                 break
                              
#         except ValueError:
#             print("Solo se admiten letras individuales")
        

# if __name__=="__main__":
#     run()

import os
import random

def read_words(filepath="./archivos/words.txt"):

    with open(filepath, 'r', encoding='utf-8') as f:
        list_words = [word.strip().upper() for word in f] # el strip() quita ese espacio final
        choosen_word = list_words[random.randint(0, len(list_words))]

    return choosen_word

def game(magic_word, letter, game_word):
    if letter in magic_word:
        for i in range(len(magic_word)):
            if letter == magic_word[i]:
                game_word[i] = letter

    return ' '.join(game_word)

def run():
    lives = 8
    letter = ''
    magic_word = read_words()
    game_word = ['_' for i in range(len(magic_word))]

    while lives > 0:
        os.system('cls')
        print(f'Vidas restantes: {"❤" * (lives)}')
        print('¡Adivina la palabra!')
        print(game(magic_word, letter, game_word))
        try:
            if len(letter) > 1:
                raise ValueError('Solo puedes ingresar una letra')
            else:
                if game(magic_word, letter, game_word).count('_') > 0:
                    if letter in game(magic_word, letter, game_word):
                        letter = input('Escoge una letra: ').upper()
                    else:
                        lives -= 1
                        if lives > 0:
                            os.system('cls')
                            print(f'Vidas restantes: {"❤" * (lives)}')
                            print('¡Adivina la palabra!')
                            print(game(magic_word, letter, game_word))
                            letter = input('Escoge una letra: ').upper()
                        else:
                            os.system('cls')
                            print('¡Te quedaste sin vidas!\nJuego terminado...\n')
                            print('La palabra era: ' + magic_word)
                else:
                    print('¡Ganaste! √')
                    break

        except ValueError as ve:
            return print(ve)
    

if __name__ == '__main__':
    run()

# Notas finales por revisar:
# Investiga la función enumerate (documentacion)
# El método get de los diccionarios te puede servir
# Dibuja el ahorcado con el codigo ascii y dibujar en pantalla
# Mejora la interfaz, emojis