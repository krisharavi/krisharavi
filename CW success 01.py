import random
import time
from prettytable import PrettyTable
from datetime import datetime

p_dice = 0
c_dice = 0
Hum = 0
com = 0
game = True
play_BH = 0
comp_BH = 0
play_pos = 0
comp_pos = 0
play_tmove = 0
comp_tmove = 0

table = PrettyTable()
table.field_names = [f"{x:02}" for x in range(1,21)]
table.align = "c"

if game == True:
    input("Press enter to start the play ")

    while play_pos<20 and comp_pos<20:
        print("\n")
        print("-"*102)
        input("Press enter to dice roll ")
        p_dice = random.randint(1,6)
        print("\nPlayer dice roll: ",p_dice)

        if p_dice==6 and play_pos==0:
            print("Player can start the game!\n")
            play_pos=1
            
        elif p_dice!=6 and play_pos==0:
            print("Player : Roll 6 to start the game...\n")
          
        while play_pos>0:
            
            if p_dice==6 and play_pos>1:
                play_pos+=3
            elif p_dice==5 or p_dice==4:
                play_pos+=2
            else:
                play_pos+=0
                print("Invalid dice roll\n")
                break
            
            print("Player position is ",play_pos)
            play_tmove+=1
            break

        c_dice = random.randint(1,6)
        print("\nComputer dice roll: ",c_dice)    

        if c_dice==6 and comp_pos==0:
            print("Computer can start the game!")
            comp_pos=1
        elif c_dice!=6 and comp_pos==0:
            print("Computer : Roll 6 to start the game..")
            continue    
            
        while comp_pos>0:
            if c_dice==6 and comp_pos>1:
                comp_pos+=3
            elif c_dice==5 or c_dice==4:
                comp_pos+=2
            else:
                comp_pos+=0
                print("Invalid dice roll\n")
                break
            
            print("Computer position is ",comp_pos,"\n")
            comp_tmove+=1
            break
            
        print("20x2 Board Result : ")
        table.clear_rows()
        table.add_row(["X" if i == play_pos - 1 else " " for i in range(20)])
        table.add_row(["X" if i == comp_pos - 1 else " " for i in range(20)])
        print(table)

        if play_pos==7 or play_pos==14:
            print("Player: oops!! It was a black hole. Restart :(")
            play_pos=1
            play_BH+=1

        if comp_pos==7 or comp_pos==14:
            print("Computer : oops!! It was a black hole. Restart :(")
            comp_pos=1
            comp_BH+=1
            continue

        if play_pos>=20 or comp_pos>=20:
            if play_pos>=20:
                play_pos==20
                Hum+=1
                time.sleep(2)
                print("Congratulations!!! Player won the game :)")
                break

            elif comp_pos>=20:
                comp_pos==20
                com+=1
                time.sleep(2)
                print("Oops!!! Computer won the game :(")
                break
    #-------------------need to study-------------------
    now = datetime.now()
    print("\n")
    print("File name is : ",now)
    timestamp = now.strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(f"Human Player\n")
        f.write(f"Player total moves: {play_tmove}\n")
        f.write(f"Black Hole Hits: {play_BH}\n")
        if Hum == 1:
            f.write(f"Won the Game\n")
        else:
            f.write(f"Lost the Game\n")

        f.write(f"\nComputer\n")
        f.write(f"Computer moves: {comp_tmove}\n")
        f.write(f"Black Hole Hits: {comp_BH}\n")
        if com == 1:
            f.write(f"Won the Game\n")
        else:
            f.write(f"Lost the Game\n")    
     

        
    
