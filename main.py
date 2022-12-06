# Hagrids Hut
def hagridsHut():
    print("You made it to Hagrid's Hut!")
    print("Great Job!")
    quit()

# Dragons
def dragons():
    directions = ["fight", "flight"]
    print("You follow the path and see Hagrids hut in the distance. But you trip on a large chain. You follow the chain and find a big gold dragon with the chain attached to its ankle. The dragon notices you and goes to attack. What do you do?")
    userInput = ""
    while userInput not in directions:
        print("Options: fight/flight")
        userInput = input()
        if userInput == "fight":
            hagridsHut()
        elif userInput == "flight":
            print("You ran away and tripped on a rock. Since you got hurt you got sent to the hospital wing at Hogwarts.")
            print("Game Over, Better Luck Next Time")
            quit()
        else:
            print("Please enter a valid option.")

# Graup
def graup():
    directions = ["left", "forward", "backward"]
    print("You found Hagrid's brother Graup the giant. Graup is willing to help you find his brother. Graup points to the path forward. Which direction do you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            hippogrifs()
        elif userInput == "forward":
            dragons()
        elif userInput == "backward":
            centaurs()
        else:
            print("Please enter a valid option.")

# Hippogrifs
def hippogrifs():
    directions = ["left", "right", "forward", "backward"]
    print("You found a cage of hippogrifs in the middle of the forest. You look around and find a key hanging on a tree. You take the key and release the hippogrifs but they seem to run away from the path forward. Which direction do you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            werewolves()
        elif userInput == "right":
            graup()
        elif userInput == "forward":
            dragons()
        elif userInput == "backward":
            fluffy()
        else:
            print("Please enter a valid option.")

# werewolves
def werewolves():
    print("You found yourself in a clearing. All of a sudden you hear a howl, you turn around and find a werewolf running towards you. You try to run away but trip and hit your head.")
    print("Since you got hurt you got sent to the hospital wing at Hogwarts.")
    print("Game Over, Better Luck Next Time")
    quit()

# Centaurs
def centaurs():
    directions = ["left", "forward", "backward"]
    print("You come across centaurs. They are playing an archery game and an arrow flys right infront of you. As an aplogy for almost hurting you they offer to follow you get to Hargids, to keeo you safe. Which direction do you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/forward/backward")
        userInput = input()
        if userInput == "left":
            fluffy()
        elif userInput == "forward":
            graup()
        elif userInput == "backward":
            unicorns()
        else:
            print("Please enter a valid option.")

# Fluffy the three headed dog
def fluffy():
    directions = ["left", "right", "forward", "backward"]
    print("You started to hear what sounds like music in the middle of the forest. You come upon Fluffy the three headed dog. Once you come into the clearing the music stops. Fluffy wakes up and wants to play. There are four paths. Which direction do you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            acromantulas()
        elif userInput == "right":
            centaurs()
        elif userInput == "forward":
            hippogrifs()
        elif userInput == "backward":
            clearDarkPath()
        else:
            print("Please enter a valid option.")

# Acromantulas (the giant spider)
def acromantulas():
    directions = ["right", "forward", "backward"]
    print("You found a large spiderweb, with a large cave behind it. Thousands of spiders are crawling out of the cave. They show you three paths, Which direction do you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/forward/backward")
        userInput = input()
        if userInput == "right":
            fluffy()
        elif userInput == "forward":
            werewolves()
        elif userInput == "backward":
            thestrals()
        else:
            print("Please enter a valid option.")

# Clear Dark Path
def clearDarkPath():
    directions = ["left", "right", "forward", "backward"]
    print("You found yourself on what looks like a pathway but it seems to have gotten dark. You hear a branch break near you. Which direction do you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            thestrals()
        elif userInput == "right":
            unicorns()
        elif userInput == "forward":
            fluffy()
        elif userInput == "backward":
            forbiddenForest()
        else:
            print("Please enter a valid option.")

# Unicorns
def unicorns():
    directions = ["left", "right", "forward", "backward"]
    print("You found yourself around a lake that has a few unicorns. The unicorns seem to like you and want to follow you. Which direction do you want to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/forward/backward")
        userInput = input()
        if userInput == "left":
            clearDarkPath()
        elif userInput == "forward":
            centaurs()
        elif userInput == "backward":
            forbiddenForest()
        else:
            print("Please enter a valid option.")

# Thestrals
def thestrals():
    directions = ["right", "forward", "backward"]
    print("You found yourself in a clearing surrounded by thestrals. They all decide to follow you. Which direction do you want to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/forward/backward")
        userInput = input()
        if userInput == "right":
            clearDarkPath()
        elif userInput == "forward":
            acromantulas()
        elif userInput == "backward":
            forbiddenForest()
        else:
            print("Please enter a valid option.")

# Forbidden Forest
def forbiddenForest():
    directions = ["left", "right", "forward"]
    print("You have just entered the Forbidden Forest, there are three paths one to your right, one to your left or one in front of you. Which direction do you want to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            thestrals()
        elif userInput == "right":
            unicorns()
        elif userInput == "forward":
            clearDarkPath()
        else:
            print("Please enter a valid option.")

# Beginning Scene
if __name__ =="__main__":
    while True:
        print("Welcome to the Forbidden Forest Game!")
        print("You've been sent to get Hagrid from his hut.")
        print("However to get to Hagrid's Hut you need to go through the Forbidden Forest.")
        print("CAREFUL, You don't know who or what might be in there.")
        forbiddenForest()
