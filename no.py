import random
win = 0; lose = 0

def game():
    global win, lose
    nbTry = 0
    maxTry = 1
    min = 0
    max = 9
    find = random.randint(min, max)
    while nbTry < maxTry:
        print("")
        print("<=============================================>")
        print("|")
        print("| Essai n° " + str(nbTry + 1))
        print("|")
        print("<--------------------------------------------->")
        print("|")
        txt = "False"
        while txt.isdigit() == False:
            txt = input("| Entrer un chiffre : ")
            if not txt.isdigit() or max < int(txt) or int(txt) < min:
                txt = "False"
        print("|")
        print("<--------------------------------------------->")
        if find == int(txt):
            win += 1
            print("\033[1;32m<--------------------------------------------->\033[0m")
            print("\033[1;32m|\033[0m")
            print(
                "\033[1;32m| Vous avez gagner ! Le chiffre était bien "
                + str(find)
                + " !!\033[0m"
            )
            print("\033[1;32m|\033[0m")
            print("\033[1;32m<=============================================>\033[0m")
            break
        else:
            print("|")
            print("| \033[1;31mMauvaise Réponse !!\033[0m")
        nbTry += 1
        print("|")
        print("<=============================================>")
        print("")
    if nbTry == maxTry:
        lose += 1
        print("\033[1;31m<=============================================>\033[0m")
        print("\033[1;31m|\033[0m")
        print(
            "\033[1;31m| Vous avez perdu, le chiffre était " + str(find) + " !!\033[0m"
        )
        print("\033[1;31m|\033[0m")
        print("\033[1;31m<=============================================>\033[0m")
def score():
    print("\033[1;34m")
    print("<=============================================>")
    print("|")
    print("<--------------------------------------------->")
    print("|")
    if win or lose:
        ratio = (win / (win + lose)) * 100
        print(
            "| Win : "
            + str(win)
            + " | Lose : "
            + str(lose)
            + " | Ratio : "
            + str(round(ratio, 2))
            + " %"
        )
    else:
        print("| Win : " + str(win) + " | Lose : " + str(lose) + " | Ratio : 0 %")
    print("|")
    print("<--------------------------------------------->")
    print("|")
    print("<=============================================>")
    print("\033[0m")

while True:
    start = "False"
    score()
    while start.lower() != "n" and start.lower() != "y" and start.lower() != "":
        start = input("Do you want to play ? ( Y / N : DEFAULT ) : ")
    if start.lower() == "y":
        game()
    else:
        print("")
        break
