import random
import time
#print("Time taken:", time.time() - start_time)
def display_board():
    print(("+" + "-"*7)*3 + "+")
    print("|       "*3+ "|")
    print(f"|   {moves['m1']}   |   {moves['m2']}   |   {moves['m3']}   |")
    print("|       "*3+ "|")
    print(("+" + "-"*7)*3 + "+")
    print("|       "*3+ "|")
    print(f"|   {moves['m4']}   |   {moves['m5']}   |   {moves['m6']}   |")
    print("|       "*3+ "|")
    print(("+" + "-"*7)*3 + "+")
    print("|       "*3+ "|")
    print(f"|   {moves['m7']}   |   {moves['m8']}   |   {moves['m9']}   |")
    print("|       "*3+ "|")
    print(("+" + "-"*7)*3 + "+")
def enter_move():
    while True:
        user = int(input("Enter your guess: "))
        if user in free_squares:
            usersquares.append(user)
            del free_squares[free_squares.index(user)]
            moves["m"+str(user)] = "O"
            return user
        else:
            print("Already taken! Try again")
def victory_for():
    global start_time
    start_time = time.time()
    if 1 in usersquares:
        if 4 in usersquares and 7 in usersquares or 5 in usersquares and 9 in usersquares or 2 in usersquares and 3 in usersquares:
            print("You won!")
            quit()
    if 2 in usersquares:
        if 5 in usersquares and 8 in usersquares:
            print("You won!")
            quit()
    if 3 in usersquares:
        if 6 in usersquares and 9 in usersquares:
            print("You won!")
            quit()
    if 4 in usersquares:
        if 5 in usersquares and 6 in usersquares:
            print("You won!")
            quit()
    if 7 in usersquares:
        if 8 in usersquares and 9 in usersquares or 5 in usersquares and 3 in usersquares:
            print("You won!")
            quit()
    if 1 in cpusquares:
        if 4 in cpusquares and 7 in cpusquares or 5 in cpusquares and 9 in cpusquares or 2 in cpusquares and 3 in cpusquares:
            print("You lost!")
            quit()
    if 2 in cpusquares:
        if 5 in cpusquares and 8 in cpusquares:
            print("You lost!")
            quit()
    if 3 in cpusquares:
        if 6 in cpusquares and 9 in cpusquares:
            print("You lost!")
            quit()
    if 4 in cpusquares:
        if 5 in cpusquares and 6 in cpusquares:
            print("You lost!")
            quit()
    if 7 in cpusquares:
        if 8 in cpusquares and 9 in cpusquares or 5 in cpusquares and 3 in cpusquares:
            print("You lost!")
            quit()
    if len(free_squares) <= 0:
        print("Tie!")
        quit()
    
def draw_move():
    while True:
        cpu = random.choice(free_squares)

        if cpu in free_squares:

            del free_squares[free_squares.index(cpu)]
            cpusquares.append(cpu)
            
            moves["m"+ str(cpu)] = "X"
            print(f"CPU guess: {cpu}")
            
            return  
moves = {"m1" : 1,
         "m2" : 2,
         "m3" : 3,
         "m4" : 4,
         "m5" : 5,
         "m6" : 6,
         "m7" : 7,
         "m8" : 8,
         "m9" : 9}
free_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
usersquares = []
cpusquares = []
while True:
    victory_for()
    display_board()
    enter_move()
    display_board()
    victory_for()
    draw_move()
    
