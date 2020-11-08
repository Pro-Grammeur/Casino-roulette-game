# Jeu du Zcasino développé par @Pro_Grammeur en personne! ;)
# Jeu réaranger basé sur un TP d'Openclassrooms


from random import randrange

Gamer_Silver = 1000  # argent total du Gameur

gamerPseudo = input("\nRentrer votre @Pseudo dans la console: ")
gamerPassword = input("Rentrer votre mot de passe dans la console: ")


print("\nBienvenue à vous cher {}. Vous voilà maintenat dans le jeu du Zcasino! Vous débutez la partie avec 1000 $. La partie va commencer prenez place...\nLancement en cours... ... ... \n\nRappel des règles du jeu:\nVous devrer miser une certaine somme sur un nombre.\n Si vous avez choisi le bon nombre alors vous gagnez 3 fois votre mise.\n Si vous avez choisi un nombre différent du correct mais que votre nombre est pair alors vous gagnez la moitié de votre mise.\n Si vous avez choisi un nombre différent du correct et qu'il est impair alors vous perdez votre mise.\n Bonne continuation!\n* Si vous ne respectez pas la prochaine instruction, un message vous demandera de quitter le jeu, ou un message d'erreur s affichera...\n".format(gamerPseudo))

areYouA_Robot = input('* Rentrer votre mot de passe dans la console pour vous identifier et faire démarrer le jeu merci : ')

while Gamer_Silver > 0:
    if areYouA_Robot == gamerPassword:

        print("Votre jeu démarre...")

        # nombre sur lequel misera le joueur
        nb_choosebyGameur = int(input("Miser sur un nombre compris entre 0 et 20: "))

        # Tant que le nombre est plus grand que 20 ou égal à 0, le redemander
        while nb_choosebyGameur == 0 or nb_choosebyGameur > 20:
            print("La mise n'est pas comprise and 0 et 20 !")
            # nombre sur lequel misera le joueur
            nb_choosebyGameur = int(input("Miser sur un nombre compris entre 0 et 20: "))

        # combien mise le joueur ?
        miseGamer = int(input("Combien misez-vous sur ce nombre? (merci de rentrer un entier) : "))

        print('Votre démarche est en cours d examination... ')

        number_winner = randrange(1, 20)  # nombre gagnant

        # condition qui va accomplir certaines instructions si nb_choosebyGameur est le même que number_winner

        if nb_choosebyGameur == number_winner:
            print("Vous avez gagné!!! Bravo.")
            Gamer_Silver = (Gamer_Silver - miseGamer) + miseGamer * 3
            print("Vous quittez la partie avec {} $.".format(Gamer_Silver))
            # variable pour quittez le jeu
            varForquit = input("Entrer Q pour quittez le jeu :")
            if varForquit == "Q":
                print("Bravo à vous {}. Je vous félicite. On vous retrouve très vite à la table de la roulette!".format(gamerPseudo))
            break  # arret du jeu

        # j'aurais pu mettre "break" pour l'arrêt du jeu si Gameur gagne mais j'ai choisis de faire comme Openclassrooms...

        # condition qui va accomplir certaines instructions si nb_choosebyGameur est pair
        if nb_choosebyGameur != number_winner and nb_choosebyGameur % 2 == 0:
            print("Dommage, ce n'est pas ce nombre mais vous gagnez comme meme la moitié de votre mise parce que vous avez comme même misez sur un nombre pair. Le nombre gagnant, lui est pair...")
            Gamer_Silver = (Gamer_Silver - miseGamer) + miseGamer / 2
            print("Il  vous reste {} $.\n".format(Gamer_Silver)) # Créer une nouvelle ligne avec \n au lieu d'utiliser deux fois print

        # condition qui va accomplir certaines instructions si nb_choosebyGameur est impair
        if nb_choosebyGameur != number_winner and nb_choosebyGameur % 2 != 0:
            print("Dommage ce n'est pas ce nombre. Vous perdez votre mise.")
            Gamer_Silver -= miseGamer
            print("Il  vous reste {} $.\n".format(Gamer_Silver)) # Créer une nouvelle ligne avec \n au lieu d'utiliser deux fois print


else:
    # arrêt du jeu, il faut redémarrer le jeu
    print("Le jeu ne pourra pas démarrer, redémarrer le et suivez les instructions pas à pas.")
