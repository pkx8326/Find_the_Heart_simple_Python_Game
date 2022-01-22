#!/usr/bin/env python
# coding: utf-8

# In[105]:


'''You have three guesses to find the position of a read heart among these nine blue squares!'''
import random

play_again = ("")

#constants

alien = "👾"
heart = "💖"
square = "🟦"
blood_title = ""
games = 0
win = 0
lost = 0


heart_coor = ("11", "12", "13", "21", "22", "23", "31", "32", "33")

#array_map = [row1, row2, row3]


while play_again not in ("N", "n"):
    lives = 1
    blood = ""
    row1 = [square, square, square]
    row2 = [square, square, square]
    row3 = [square, square, square]
    
    print("Find the heart 💖:")
    print("You have 🩸🩸🩸 left.")
    print(f'''
    1     2      3
1{row1}
2{row2}
3{row3}
    ''')
    
    #Randomize a coordinate
    rand_num = random.randint(0,8)
    rand_coor = heart_coor[rand_num]

    #A while loop to keep the game on until the heart is found or until he/she spends all the 3 lives
    coor_input = ""
    while (coor_input != rand_coor) and (lives <= 3):

        #Getting player's coordinate
        coor_input = ""
        while coor_input not in heart_coor:
            coor_input = input("Enter the heart's coordinates: ")

        #Checking if player's coordinate matches with the randomized coordinate
        if coor_input == rand_coor:
            print("You found it!")
            #Localizing the heart and show it:
            if rand_coor == "11":
                row1[0] = heart
            elif rand_coor == "12":
                row1[1] = heart
            elif rand_coor == "13":
                row1[2] = heart
            elif rand_coor == "21":
                row2[0] = heart
            elif rand_coor == "22":
                row2[1] == heart
            elif rand_coor == "23":
                row2[2] = heart
            elif rand_coor == "31":
                row3[0] = heart
            elif rand_coor == "32":
                row3[1] = heart
            else:
                row3[2] = heart

            print(f'''
    1     2      3
1{row1}
2{row2}
3{row3}            
                ''')
            win += 1
            games += 1
        else:
            if coor_input == "11":
                row1[0] = alien
                print("Not quite yet!")
                print(f'''
    1     2      3
1{row1}
2{row2}
3{row3}            
                ''')
                lives += 1
                if lives == 4:
                    print("Game Over! You've spent all the lives.")
                    lost += 1
                    games += 1
                    break
                else:
                    blood = ""
                    for i in range(0,4-lives):
                        blood += "🩸"
                    print(f"You have {blood} left.")
            elif coor_input == "12":
                row1[1] = alien
                print("Not quite yet!")
                print(f'''
    1     2      3
1{row1}
2{row2}
3{row3}
                ''')
                lives += 1
                if lives == 4:
                    print("Game Over! You've spent all the lives.")
                    lost += 1
                    games += 1
                    break
                else:
                    blood = ""
                    for i in range(0,4-lives):
                        blood += "🩸"
                    print(f"You have {blood} left.")
            elif coor_input == "13":
                row1[2] = alien
                print("Not quite yet!")
                print(f'''
    1     2      3
1{row1}
2{row2}
3{row3}
                ''')
                lives += 1
                if lives == 4:
                    print("Game Over! You've spent all the lives.")
                    lost += 1
                    games += 1
                    break
                else:
                    blood = ""
                    for i in range(0,4-lives):
                        blood += "🩸"
                    print(f"You have {blood} left.")
            elif coor_input == "21":
                row2[0] = alien
                print("Not quite yet!")
                print(f'''
    1     2      3
1{row1}
2{row2}
3{row3}
                ''')
                lives += 1
                if lives == 4:
                    print("Game Over! You've spent all the lives.")
                    lost += 1
                    games += 1
                    break
                else:
                    blood = ""
                    for i in range(0,4-lives):
                        blood += "🩸"
                    print(f"You have {blood} left.")
            elif coor_input == "22":
                row2[1] = alien
                print("Not quite yet!")
                print(f'''
    1     2      3
1{row1}
2{row2}
3{row3}
                ''')
                lives += 1
                if lives == 4:
                    print("Game Over! You've spent all the lives.")
                    lost += 1
                    games += 1
                    break
                else:
                    blood = ""
                    for i in range(0,4-lives):
                        blood += "🩸"
                    print(f"You have {blood} left.")
            elif coor_input == "23":
                row2[2] = alien
                print("Not quite yet!")
                print(f'''
    1     2      3
1{row1}
2{row2}
3{row3}
                ''')
                lives += 1
                if lives == 4:
                    print("Game Over! You've spent all the lives.")
                    lost += 1
                    games += 1
                    break
                else:
                    blood = ""
                    for i in range(0,4-lives):
                        blood += "🩸"
                    print(f"You have {blood} left.")
            elif coor_input == "31":
                row3[0] = alien
                print("Not quite yet!")
                print(f'''
    1     2      3
1{row1}
2{row2}
3{row3}
                ''')
                lives += 1
                if lives == 4:
                    print("Game Over! You've spent all the lives.")
                    lost += 1
                    games += 1
                    break
                else:
                    blood = ""
                    for i in range(0,4-lives):
                        blood += "🩸"
                    print(f"You have {blood} left.")
            elif coor_input == "32":
                row3[1] = alien
                print("Not quite yet!")
                print(f'''
    1     2      3
1{row1}
2{row2}
3{row3}
                ''')
                lives += 1
                if lives == 4:
                    print("Game Over! You've spent all the lives.")
                    lost += 1
                    games += 1
                    break
                else:
                    blood = ""
                    for i in range(0,4-lives):
                        blood += "🩸"
                    print(f"You have {blood} left.")
            else:
                row3[2] = alien
                print("Not quite yet!")
                print(f'''
    1     2      3
1{row1}
2{row2}
3{row3}
                ''')
                lives += 1
                if lives == 4:
                    print("Game Over! You've spent all the lives.")
                    lost += 1
                    games += 1
                    break
                else:
                    blood = ""
                    for i in range(0,4-lives):
                        blood += "🩸"
                    print(f"You have {blood} left.")

    play_again = ("")
    while play_again not in ("Y", "y", "N","n"):
        play_again = input("Play again? Y/N:")

if games > 1 and win > 1 and lost > 1:
    print(f"You've played {games} games. You have won {win} times, and lost {lost} times.")
else:
    if games == 1:
        print(f"You have played {games} game. You have won {win} time, and lost {lost} time.")
    elif games > 1 and win == 0:
        print(f"You have played {games} games. You have won {win} time, and lost {lost} times.")
    elif games > 1 and lost == 0:
        print(f"You have played {games} games. You have won {win} times, and lost {lost} time.")
    elif games > 1 and lost == 1 and win == 1:
        print(f"You have played {games} games. You have won {win} time, and lost {lost} time.")
    else:
        print(f"You have played {games} games. You have won {win} times, and lost {lost} times.")


# In[ ]:




