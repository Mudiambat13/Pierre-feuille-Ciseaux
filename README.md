
# Pierre-feuille-ciseaux

For this project we will need the random module and the randint function 

```from random import randint```

We define an  ```options ```  list containing the 3 possible choices in the game.

We enter an infinite loop ```while True```  to be able to replay as many times as we want..

The player is asked to enter their choice, and the string is lower-cased using ```.lower() ```to simplify the comparison afterwards.

We check that the player's choice is one of the 3 valid options. If not, "Invalid choice" is displayed and we loop with ```continue ``` to ask the player again.

A random choice is generated for the computer using ```randint(0,2)```, which gives 0, 1 or 2. This index is used to select an item at random from the ```options ```list.

The choice of computer is displayed.
The choices are compared and the result displayed according to the rules of the game.

And the loop starts all over again!
