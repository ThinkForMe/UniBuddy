"""
This program aims at helping new students 
navigate their university and find clubs to join
It is my first program
"""

# Welcome message, explains the purpose of the tool
print("""
Welcome to Unibuddy!
Your go to app to easily navigate your new environnment!
Let us begin...
""")
colour_list = ["Blue", "Red", "Yellow", "Green"]
light_year_distance = 9460730472580.8
user_name = input("Please enter your First Name: ").capitalize()

#Error handling. User must be a living adult.
while True:
    try:
        user_age = int(input("Please enter your age in full years: "))
        if user_age < 18:
            print(f"Sorry {user_name}, you are too young to proceed")
        elif user_age > 120:
            print(f"Sorry {user_name} you are dead...")
        else:
            
            break 
    except ValueError as e:
        print(e)

#Error handling on the colour choice
user_color = input("Please choose the colour you prefer \
between blue, red, yellow and green: ").capitalize()
while True:
    if not user_color in colour_list:
        user_color = input(f"Please {user_name} \
choose between blue, red, yellow and green: ").capitalize()
    else:
        break
print(f"\nWelcome {user_name}! I like {user_color} too!")

#A huge number to scare everyone
user_age_mins = user_age * 365 * 24 * 60
print(f"You have lived {user_age_mins:,} minutes so far!")

#A little space age info!
if user_age == 19:
    destination = "Eta Cassiopeiae in Cassiopeiae Constellation"
elif user_age == 20:
    destination = " Gliese 784 in Telescopium Constellation"
elif user_age == 21:
    destination = "GL Virginis in Virgo Constellation"
elif user_age == 22:
    destination = "Xi Boötis in Boötes Constellation"
elif user_age == 23:
    destination = "Beta Hydri in Hydrus Constellation"
elif user_age == 24:
    destination = "Alpha Piscis Austrini in Piscis Austrini Constellation"
elif user_age >= 25:
    destination = "WISEPC J115013.88+630240.7 in Ursa Major Constellation"
else :
    destination = "somewhere between Alpha Centauri and Altair"

print(f"""
At {user_age} you could have travelled \
{user_age * light_year_distance:,} km at speed of light.
You would have reached {destination} by now...
Let me suggest some clubs for you...""")

#club offer depending on colour chosen
if user_color == "Red":
    print("""
- You can join the football Red team, they usually lose...\n\
- You can join the Organ Dissection Society, if you like gore...\n\
- We have a great Arsenal fan club, they usually lose too...
""")
elif user_color == "Blue":
    print("""
- You can join the Sky Observation Society, you'd learn what Altair is...\n\
- You can join the Blue football team, they hardly win...\n\
- You can go to the Swimming Team, bring your plastic ducks...
""")
elif user_color == "Green":
    print("""
Green ? bad choice...
-grab a movie or a book, that's all we got for you. Green... really ?
""")
elif user_color == "Yellow":
    print("""
Yellow? Now we are talking, hope is back!\n\
- You can join the Yellow football team, always winning!\n\
- You can be part of the Sun Worshippers Fraternity\n\
- You can try your luck at the Pasta Kings League \n\
- You can join the Citrus Cocktail Society!
""")

 #ending text   
print(f"We hope you will enjoy your stay with us {user_name}\n\
Don't forget to rate us on TrustInLoop: *****")
