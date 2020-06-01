import random #imports a randomiser
sunk=[0,0] #sees if all ships are sunk
count=[0] #shows whos go it is
currentnum=[0] #holds valid coordinates
validnums=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","1","2","3","4","5","6","7","8","9"] #all valid inputs
nums=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"] #nums shown in the x and y coordinates
validplayers=["1","2"] #shows how many players are valid to use
validyes=["Y","N"] #shows valid inputs for next game
totals=0 #used to allow players to place their own ships and counts the amount
prevhit=0 #used for ai to see if the last shot was a hit
array1=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #used to hold all positions of ships for p1
array2=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #used to hold all positions of hit ships in p1
array1seen=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #used to hold all positions of ships for p2
array2seen=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #used to hold all positions of hit ships in p2
player=[1,1] #holds name of players
x1=[0,0,0,0,0] #holds x coordinates for boats
y1=[0,0,0,0,0] #holds y coordinates for boats
nos=["first","second"] #shows if the coordinate is 1st or 2nd

for i in range(0,21): #loops through all index of 2D array
    for j in range(0,21): #loops through all index of an array
        array1[i].append(1) #adds an index
        array1[i][j]="  " #sets new index to blank
        #repeats
        array2[i].append(1)
        array2[i][j]="  "
        array1seen[i].append(1)
        array1seen[i][j]="  "
        array1seen[i][0]=i
        array2seen[i].append(1)
        array2seen[i][j]="  "
        array2seen[i][0]=i

for i in range(0,21): #loops through array
    array1seen[0][i]=nums[i] #sets top lines to numbers
    array2seen[0][i]=nums[i]
for i in range(0,21):
    array1seen[i][0]=nums[i] #sets side lines to numbers
    array2seen[i][0]=nums[i]


def empty(array): #defines functions used to reset board
    global array2
    global array1
    array=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(0,21):
        for j in range(0,21):
            array[i].append(1)
            array[i][j]="  "





def entering(person,array,length): #used to allow player to enter coordinates of ships
    for j in range(0,2): #loops twice to add 2 sets of coordinates
        print(person,"what is the",nos[j],"x-coordinate of ship number of length", length) #shows if it is 1st or 2nd coordinate and shows length
        x1[j]=input() #uses an input for x coordinate
        valid(x1[j]) #checks if the num is valid or not
        x1[j]=int(currentnum[0]) #resets x1 coordinate to the validated number

        print("what is the",nos[j],"y-coordinate of your ship number of length", length) #shows if it is 1st or 2nd coordinate and shows length
        y1[j]=input() #uses an input for y coordinate
        valid(y1[j]) #checks if the num is valid or not
        y1[j]=int(currentnum[0]) #resets x1 coordinate to the validated number

    for i in range(2,length): #loops the number of times of length - 2
        if x1[0]==x1[1]: #checks if the x coordinate is the same
            if y1[0]<y1[1]: #checks if 1st y is less than 2nd y
                y1[i] = y1[0] + i-1 #adds y positions for all parts of boats
                x1[i] = x1[0]
            else:
                 y1[i] = y1[1] + i-1
                 x1[i] = x1[0]

        else: #if y cooridinate is the same
            if x1[0]<x1[1]: #checks if 1st x is less than 2nd x
                x1[i]=x1[0]+i-1 #adds y positions for all parts of boats
                y1[i] = y1[0]
            else:
                x1[i]=x1[0]+i-1
                y1[i] = y1[0]


    while array[y1[0]][x1[0]]==" S" or array[y1[1]][x1[1]]==" S" or array[y1[2]][x1[2]]==" S" or array[y1[3]][x1[3]]==" S" or array[y1[4]][x1[4]]==" S" or ((y1[0]-y1[1]!=length-1 and y1[1]-y1[0]!=length-1) and (x1[0]-x1[1]!=length-1 and x1[1]-x1[0]!=length-1)):
        #checks if this coordinate has already been taken
        print("INVALID you cant go there")
        #repeats previous process
        for j in range(0, 2):
            print(person,"what is the",nos[j],"x-coordinate of ship number of length", length)
            x1[j]=input()
            valid(x1[j])
            x1[j]=int(currentnum[0])

            print("what is the",nos[j],"y-coordinate of ship number of length", length)
            y1[j]=input()
            valid(y1[j])
            y1[j]=int(currentnum[0])

    for i in range(0,length): #checks if the boat is at the edges
        if y1[0]==y1[1]:
            if x1[0]>x1[1]:
                for i in range(-1,length-1):
                    array[y1[0]][x1[1]+i]=" S"
            else:
                for i in range(-1,length-1):
                    array[y1[0]][x1[0]+i]=" S"
        else:
            if y1[0]<y1[1]:
                for i in range(-2,length-2):
                    array[y1[1]+i][x1[0]-1]=" S"
            else:
                for i in range(-2,length-2):
                    array[y1[0]+i][x1[0]-1]=" S"
    print(*nums[0:21]) #prints the top of the board
    for i in range(1,len(array)): #prints the rest of the board
        print(nums[i],*array[i])


def printer(toprint):
    for i in range(0,len(toprint)): #prints the board
        print(*toprint[i])



def valid(num):
    while num not in validnums: #used to validate entered numbers
        num=input("INVALID please re-enter")
    currentnum[0]=num

def game(locatex,locatey): #used for player1
    if array2[locatex][locatey]==" S": #checks if the shot hit a ship
        print("\n") #prints a space
        print("CONGRATULATIONS",player[0]," YOU HIT A SHIP") #congratulates player
        print("\n") #space
        sunk[0]=sunk[0]+1 #increments sunk counter
        count[0]=count[0]+1 #increments whos go it is
        array2seen[locatex][locatey]=" X" #changes the text to x to show the ship has been hit
        array2[locatex][locatey]=" X" #changes the text to x to show the ship has been hit
    else:
        array2seen[locatex][locatey]=" O" #changes the text to O to show the spot has been shot at

def game2(locatex,locatey):#used for player2 same as before
    if array1[locatex][locatey]==" S":
        print("\n")
        print("CONGRATULATIONS",player[1],"YOU HIT A SHIP")
        print("\n")
        sunk[1]=sunk[1]+1
        count[0]=count[0]+1
        array1seen[locatex][locatey]=" X"
        array1[locatex][locatey]=" X"
    else:
        array1seen[locatex][locatey]=" O"

def cpu(): #used for ai
    global prevhit
    global x
    global y
    global timeforrand
    if prevhit!=0: #if the last shot was a hit
        print("Implementing AI")
        while array1[x][y]==" O" or array1[x][y]==" X": #if the current shot is aiming for a position that has already been shot at
            if prevhit!=1: #if previous shot was not a hit
                direction=timeforrand #resets direction for a randomdirection
            bx=x #sets bx to x
            by=y #sets by to y
            timeforrand=random.randint(0,3) #gets random number for 4 directions
            if prevhit!=1: #if previous shot was not a hit
                timeforrand=direction #random direction is direction
            if timeforrand==0: #if randomnum is 0
                x=bx+1 #next position is previous position + 1
            elif timeforrand==1: #repeat depending on direction
                x=bx-1
            elif timeforrand==2:
                y=by+1
            elif timeforrand==3:
                y=by-1



    else:
        x=int(validnums[random.randint(0,19)]) #random selects x coordinate
        y=int(validnums[random.randint(0,19)]) #random selects y coordinate
        while array1[x][y]==" O" or array1[x][y]==" X": #checks if that coordinate has already been shot at
            x=int(validnums[random.randint(0,19)])
            y=int(validnums[random.randint(0,19)])


    if array1[x][y]==" O": #if the position is a miss
        x=int(validnums[random.randint(0,19)]) #sets next position to random number
        y=int(validnums[random.randint(0,19)])
    if array1[x][y]==" S": #if the position is a hit
        print("THE COMPUTER SUNK A SHIP")
        sunk[1]=sunk[1]+1 #increases sunk counter
        count[0]=count[0]+1 #increases go counter
        array1[x][y]=" X" #changes text to X to show it has been hit
        prevhit=prevhit+1 #shows that the last shot was a hit
    else:
        array1[x][y]=" O"  #sets text to O to show it was a miss
        prevhit=0 #resets prevhit to 0


    print(*nums[0:21]) #prints board
    for i in range(1,len(array1)):
        print(nums[i],*array1[i])



def check(xcoo,ycoo): #used for player1 to check position
    if array2seen[xcoo][ycoo]==" O" or array2seen[xcoo][ycoo]==" X": #checks if position has already been taken
        print("You have already gone there")
        guessx=input("What is the x coordinate of your attack")
        valid(guessx)
        guessx=int(currentnum[0])

        guessy=input("What is the y coordinate of your attack")
        valid(guessy)
        guessy=int(currentnum[0])

        check(guessy,guessx) #checks new coordinates

        game(guessy,guessx) #checks if the shot was a hit or miss

def check2(xcoo,ycoo): #same as above but for p2
    if array1seen[xcoo][ycoo]==" O" or array1seen[xcoo][ycoo]==" X":
        print("You have already gone there")
        guessx=input("What is the x coordinate of your attack")
        valid(guessx)
        guessx=int(currentnum[0])

        guessy=input("What is the y coordinate of your attack")
        valid(guessy)
        guessy=int(currentnum[0])

        check2(guessy,guessx)

        game2(guessy,guessx)


def randomenter(array): #used to randomly enter boat positions
    global array1
    global array2
    totals=0 #checks how many positions have been selected

    while totals!=18:
            empty(array)

            totals=0

            for i in range(0,5): #loops through the boats
                if i==3: #on 3rd loop
                    rang=4 #used to show range
                elif i==4:
                    rang=5
                else:
                    rang=3
                x2=int(validnums[random.randint(0,13)]) #sets x position
                y2=int(validnums[random.randint(0,13)]) #sets y position
                while array[x2][y2]==" S": #checks if the position has already been taken
                    x2=int(validnums[random.randint(0,13)])
                    y2=int(validnums[random.randint(0,13)])
                xory=random.randint(0,1) #selects vert or horiz direction
                if xory==0: #if horiz
                    for k in range(0,rang): #loops through length of boat
                        array[x2+k][y2]=" S" #sets all position texts to S
                else:
                    for k in range(0,rang): #same as above but for vert
                        array[x2][y2+k]=" S"

            for l in range(1,len(array)):
                totals=totals+array[l].count(" S") #increases total counter




players=input("How many people are playing")
while players not in validplayers: #checks how many players or playing
    print("INVLAID")
    players=input("How many people are playing")

player[0]=input("What is the name of player1") #finds names of players
enterrandom=input("Do you want to place your own ships, Y or N") #allows placement of own ships or not
while enterrandom.upper() not in validyes: #checks if the input is valid
    print("INVALID")
    enterrandom=input("Do you want to place your own ships, Y or N")
if enterrandom.upper()=="N": #if they want random placement
    randomenter(array1) #activates random boat plaement
else:
    print(*nums[0:21]) #prints empty board
    for i in range(1,len(array1)):
        print(nums[i],*array1[i])

    for i in range(1,4): #placement of 3 boats of length 3
        entering(player[0],array1,3) #activates entering function


    for i in range(1,2): #placement of 1 boats of length 4
        entering(player[0],array1,4) #activates entering function


    for i in range(1,2): #placement of 1 boats of length 5
        entering(player[0],array1,5)#activates entering function







if players=="1":
    randomenter(array2) #randomly places cpu ships


    while sunk[0] != 18 and sunk[1] != 18: #loops until all ships are sunk
        count[0]=count[0]+1 #increases counter
        if count[0]%2==1: #if p1 goes
            print("Your Go",player[0],"!")
            print("\n")
            printer(array2seen) #activates printer function to show board
            print("\n")
            guessx=input("What is the x coordinate of your attack")
            valid(guessx) #validates the guessx
            guessx=int(currentnum[0])

            guessy=input("What is the y coordinate of your attack")
            valid(guessy) #validates the guessy
            guessy=int(currentnum[0])

            check(guessy,guessx) #checks the guess is valid

            game(guessy,guessx) #sees if the guess is correct

        else:
            print("Computer's Go!")
            cpu() #activates cpu function
        print("\n")






else:
    for i in range(0,50): #prints a huge chunk of empty space
       print("\n")
    #same as for p1 ship placement
    player[1]=input("what is the name of player 2")
    enterrandom=input("Do you want to place your own ships, Y or N")
    while enterrandom.upper() not in validyes:
        print("INVALID")
        enterrandom=input("Do you want to place your own ships, Y or N")
    if enterrandom.upper()=="N":
        randomenter(array2)
    else:
        print(*nums[0:21])
        for i in range(1,len(array2)):
            print(nums[i],*array2[i])

        for i in range(1,4):
            entering(player[1],array2,3)


        for i in range(1,2):
            entering(player[1],array2,4)


        for i in range(1,4):
            entering(player[1],array2,5)



        for i in range(0,50):
           print("\n")


    while sunk[0] != 18 and sunk[1] != 18:
        count[0]=count[0]+1
        print("\n")
        if count[0]%2==1:
            print(player[0],"Go!")
            print("\n")
            printer(array2seen)
            print("\n")
            guessx=input("What is the x coordinate of your attack")
            valid(guessx)
            guessx=int(currentnum[0])

            guessy=input("What is the y coordinate of your attack")
            valid(guessy)
            guessy=int(currentnum[0])

            check(guessy,guessx)

            game(guessy,guessx)
        else:
            print(player[1],"Go!")
            print("\n")
            printer(array1seen)
            print("\n")
            guessx=input("What is the x coordinate of your attack")
            valid(guessx)
            guessx=int(currentnum[0])

            guessy=input("What is the y coordinate of your attack")
            valid(guessy)
            guessy=int(currentnum[0])

            check2(guessy,guessx)

            game2(guessy,guessx)
    print("Congratulations", player[count[0]%2], ", Won")
