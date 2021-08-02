import random

point = 0
pc_guess = "123456789"
#machine can guess between 1-10, you can set it from here
level = 6
#level is nothing but a loop number here, increasing it can increase max points

for i in range(1, level):
    user_input = input("Guess any number between 1-10 :")
    mG = random.choice(pc_guess)
    #mG >> machine_guess
    text = open("machine_guess.txt", "a")
    #using append to not lose any data
    #creating a text folder and saving the file, you can set any file name from here and change it in the last line also
    text.write(mG)
    #writing inside the text, after before every loops end
    if mG == user_input:
        point = point + 1

if point == 1 or 0:
    print("Your Point is ", point)
    #extra line to avoid grammatical mistake ;)
else:
    print("Your Points is :", point)

text.write("\n")
text.close()
# .txt file works done here !
print("")
print("</> You can check the Machine guessed number in machine_guess.txt file </>")
