def main():
    # Definir une listpi ou avoir les pierres, definir des integer aléatoir, appels des fonctions
    Listpi = []
    randtas = random.randint(3, 7)
    randpi = random.randint(5, 12)
    nom1, nom2 = joueurs()
    player = nom1 # choisir le nom 1 comme le joueur
   
    tabl(Listpi, randtas, randpi, joueur ) # Saisir initiale

    jouerencore(Listpi, randtas, randpi, nom1, nom2, joueur) 

#  une fonction sans parametre et retourne les noms des joueurs 

  def joueurs():
    return input("Entrer le nom du joueur1  : "), input("Entrer le nom du  joueur2: ")

#  accepter des listpi vides , aleatoire integers pour pierre et tas 

# afficher le 1 er tableau

def tabl(Listpi, randtas, randpi, joueur):

    # avoir le 1 er tableau
    
    print("regardons le tableau maintenant .")
    print("-" * 25)
    for i in range(0, randtas):
        randpi = random.randint(5,23)
        print('tas {}: {}'.format(i + 1, 'O' * randpi))
        Listpi.append(randpi)
    print("-" * 25)

    # appeler la fonction nim
    nim_sum(Listpi, randtas)


#  returner des erreur pour des input invalid mse a jeure du tableau
def get_valid_input(Listpi, randtas, joueur):

  
   while True:
pierres = input('{}, combien de pierres a enlever ? '.format(joueur))
tas = input('de quels tas : ')
        
        
        
        
        
         if (pierres and tas) and (pierres.isdigit()) and (piles.isdigit()):
            if (int(pierres) > 0) and (int(tas) <= len(Listpi)) and (int(tas) > 0):
                if (int(pierres) <= Listpi[int(tas) - 1]):
                    if (int(pierres) != 0) and (int(tas) != 0):
                        break
        
      
       
        print("erreur refaire loperation , {}.".format(joueur))
   
    # mise a jour
Listpi[int(tas) - 1] -= int(pierres)

    # Keep playing game
    continue_game(Listpi, randtas, joueur)


   #afficher le nouveau tableau
def continue_game(Listpi, randtas, joueur): 
    print("regardons le tableau maintenant .")
    print("-" * 25)
    for i in range(0, randtas):
        print("tas {}: {}".format(i + 1, 'O' * Listpi[i]))

    print("-" * 25)
    if Listpi != [0] * len(Listpi):
        nim_sum(Listpi, randtas)

# afficher le gagnant de la partie et si ils veut joueur une autre fois
def jouerencore(Listpi, randtas, randpi, nom1, nom2, joueur):

    
    while True:
        get_valid_input(Listpi, randtas, joueur)
       
        if Listpi == [0] * len(Listpi):
            print("{} le vainqueur de cette partie est !".format(joueur))
            user = input("vous voulez jouer une autre fois? Entrer y pour oui, nimporte quel touche pour  no: ")

            if user.lower() == 'y':
               # revenir au condition de depart pour le nouvelle partie
               Listpi = []
                randtas = random.randint(3, 7)
                nom1, nom2 = joueurs()
                player = name1
            tabl(Listpi, randtas, randpi, joueur)
               get_valid_input(Listpi, randtas, joueur)
               
            else:
                break
          
       # permutation de joueur 2->1, 1->2 
        if joueur == nom1:
            joueur = nom2

        else:
            joueur = nom1


#  calculer nim sum 
def nim_sum(Listpi, randtas):
    nim = 0

    # Calculer nim sum pour tous les elements de listpi
    for i in Listpi:
        nim = nim ^ i
        
    print("Hint: nim sum is {}.".format(nim))

    # Detreminer combien de pierres a enlever et de quel tas
    pierres_a_enlever = max(Listpi) - nim
    pierres_a_enlever = abs(stones_to_remove)    
   
    if (nim > 0) and (len(Listpi) > 3) and (nim != max(Listpi)) and (nim !=1):
    print("choisir {} pierres du tas  {}".format(pierres_a_enlever ,Listpi.index(max(Listpi))+ 1 ))

    if (nim > 0) and (len(Listpi) > 3) and (nim == max(Listpi)) and (nim !=1):
        print("choisir {} pierres du tas  {}.".format(nim, Listpi.index(max(Listpi))+ 1 ))

    if (nim > 0) and len(Listpi) <= 3 and (pierres_a_enlever!= 0):
        print("choisir {} pierres du tas  {}".format(pierres_a_enlever, Listpi.index(max(Listpi))+ 1 ))

    if (nim > 0) and len(Listpi) <= 3 and (pierres_a_enlever == 0):
        print("choisir {} pierres du tas {}".format(nim, Listpi.index(max(Listpi))+ 1 ))

elif (nim == 1) and (len(Listpi) <= 3):
print("choisir {} pierres du tas {}".format(nim, Listpi.index(max(Listpi))+ 1 ))

    if (nim == 1) and (nim == max(Listpi)) and (nim != 0) and (len(Listpi) > 3):

        print("choisir {} pierres du tas {}".format(nim, Listpi.index(max(Listpi))+ 1))
        
    if nim == 0:
        print("choisir tous les pierres du tas {}.".format(Listpi.index(max(Listpi))+ 1 ))

main()
