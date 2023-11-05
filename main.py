from random import randint

options = ["pierre", "feuille", "ciseaux"]

while True:
  joueur = input("pierre, feuille ou ciseaux ? : ").lower()
  if joueur not in options:
    print("Choix invalide")
    continue

  ordinateur = options[randint(0,2)]
  print(f"L'ordinateur a choisi {ordinateur}")
  
  if joueur == ordinateur:
    print("Egalité!")
  elif joueur == "pierre" and ordinateur == "ciseaux":
    print("Vous gagnez!")
  elif joueur == "feuille" and ordinateur == "pierre":
    print("Vous avez gagnez!")
  elif joueur == "ciseaux" and ordinateur == "feuille":
    print("Vous avez gagnez!")
  else:
    print("Vous avez perdu !")
