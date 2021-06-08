import random
min = 1
max = 20
x = 1
y = 20
value = (1,20)

roll_again = 'yes' or 'no'
if roll_again =='yes' or roll_again == 'y' :
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
elif roll_again == 'no' or roll_again == 'n':
    print ("wow, way to quit loser")

while value == (1) :
    from playsound import playsound
    playsound('mario_killed.mp3')
while value == (20) :
    from playsound import playsound
    playsound('quack_sound_effect.mp3')       

roll_again = input("Roll the dices again?")

while True:
        answer = input('Do you want to continue?:')
        if answer.lower().startswith("y"):
            print ("Git it gurl")
            print (random.randint(min, max))
        elif answer.lower().startswith("n"):
            print ("wow, way to give up")
            exit()