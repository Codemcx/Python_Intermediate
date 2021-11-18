import os
import random
def normalize(s): # It removes the accents of a string
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s   

def read_words():

    with open("./archivos/words.txt", 'r', encoding="utf-8") as f:
        list_words = [word.strip().upper() for word in f] # el strip() quita ese espacio final
        choosen_word = list_words[random.randint(0, len(list_words))]
        choosen_wordf = normalize(choosen_word)
        
    return (choosen_wordf)
def new_game():
    new_game = int(input("Quieres jugar otra vez?: \n1. SI \n2. NO\nOpcion: "))
    
       
    if new_game == 1:
        run()
    if new_game == 2:
        print("Adios!")
    else:
        print("Por favor elige la Opcion 1 o 2")  
        new_game = (input("Quieres jugar otra vez?: \n1. SI \n2. NO\nOpcion: "))
        if new_game == 1:
            run()
        if new_game == 2:
            print("Adios!")
        else:
            print("Lo siento eligio una opcion no disponible, Adios!")


def game(magic_word, letter, game_word):
    if letter in magic_word:
        for i in range(len(magic_word)):
            if letter == magic_word[i]:
                game_word[i] = letter

    return ' '.join(game_word)



def run():
    lives = 5
    letter = ''
    magic_word = read_words()
    game_word = ['_' for i in range(len(magic_word))]

    while lives > 0:
        os.system('clear')
        print(f'Vidas restantes: {"❤" * (lives)}')
        print('¡Adivina la palabra!')
        print(game(magic_word, letter, game_word))
        try:
            if len(letter) > 1:
                if letter == magic_word:
                    os.system('clear')
                  
                    print('¡Arriesgaste y GANASTE! √')
                    print("La palabra era " + magic_word)
                    return new_game()
                else: 
                    os.system('clear')   
                    print("Arriesgaste y PERDISTE!")
                    print('La palabra era: ' + magic_word)
                    return new_game()
               
            else:
                if game(magic_word, letter, game_word).count('_') > 0:
                    if letter in game(magic_word, letter, game_word):
                        letter = input('Escoge una letra: ').upper()
                    else:
                        lives -= 1
                        if lives > 0:
                            os.system('clear')
                            print(f'Vidas restantes: {"❤" * (lives)}')
                            print('¡Adivina la palabra!')
                            print(game(magic_word, letter, game_word))
                            letter = input('Escoge una letra: ').upper()
                        else:
                            os.system('clear')
                            print('¡Te quedaste sin vidas!\nJuego terminado...\n')
                            print('La palabra era: ' + magic_word)
                            if lives == 0:
                                return new_game()  
                                
                            else:
                                break          
                else:
                    print('¡Ganaste! √')
                    return new_game()
        except ValueError as ve:
            return print(ve)
    

if __name__ == '__main__':
    run()

# Notas finales por revisar:
# Investiga la función enumerate (documentacion)
# El método get de los diccionarios te puede servir
# Dibuja el ahorcado con el codigo ascii y dibujar en pantalla
# Mejora la interfaz, emojis
