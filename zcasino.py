import random
import math

# 1.le joueur parie un numero (user input)
paris = int(input("Entrez le numéro sur lequel vous pariez (entre 0 et 49) : "))
# 2.le joueur mise une somme (user input)
mise = float(input("Entrez la somme que vous misez : "))
# 3.la roulette se lance (random)
numero_roulette = random.randint(0, 49)
# 4.le programme compare le pari au numéro de la roulette ( if ==)
if paris == numero_roulette:
# 5.si le numéro du pari est égal  au numéro de la roulette  mise*3 (if)
  gain = mise * 3
  math.ceil(gain)
  print("Félicitations ! Vous avez gagné :", gain)
# 6.si le numéro du pari n'est  pas egal au numéro de la roulette (ifelse)
elif paris % 2 == 0 and numero_roulette % 2 == 0:
# 7.si le numéro est misé est  pair ett que la roulette indique un nombre pair  if nombre % 2 == 0: (impair rouge pair noir )
# 8.le joueur touche mise*0,5
   gain = mise * 0.5
   print("Bravo !  vous etes sur la couleur noire " ,  gain)
# 9.si le numéro misé par le joueur est impair et que la roulette indique que le nombre est impair (impair rouge)
elif paris  % 2 != 0 and numero_roulette % 2 != 0:
# 10. le joueur touche mise*0,5
   gain = mise * 0.5
   print("Bravo ! Vous êtes sur la couleur rouge  :", gain)
# 11. else le joueur perd sa mise
else:
    print("Dommage ! Vous avez perdu votre mise.")
