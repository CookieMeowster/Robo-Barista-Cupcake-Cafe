#With this cafe script, you can order a drink and the program will calculate the total price based on your order. 
#It also checks for profanity in your name and handles invalid inputs gracefully.
#I learned how to use the better_profanity library to filter out inappropriate names, and I added kaomoji for personality. It also adds a more engaging user experience
#The program also includes error handling for invalid inputs, ensuring valid options for their users order.
#I worked on this bot with a Youtuber called NetworkChuck. I even added a little more than what was in the video.

import time

from better_profanity import profanity

def type_text(text, delay=0.02):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


type_text("Hello, welcome to Cupcake Cafe! What can I get for you today?\n" + "(ㅅ´ ˘ `)" )

type_text("What is your name?\n")
name = input().strip()

if profanity.contains_profanity(name):
    print("GETTT OUTTA HERE YOU SAD DEGEN HOOMAN!! ( ｡ •̀ ᴖ •́ ｡)💢")
    raise SystemExit
else:
    type_text(f"Hello, {name}, thanks for coming in today!\n")
    type_text(f"{name}, we have coffee, tea, and hot chocolate.\n"
              f"(ㅅ´ ˘ `) What would you like to order?")

while True:
    menu = input().strip().casefold()

    if menu in ("tea", "coffee", "hot chocolate", "hotchocolate"):
        break

    type_text("Please enter tea, coffee, or hot chocolate (≖_≖ )...")

price = 5 

while True:
    type_text("How many would you like?\n")
    answer = input().strip()

    try:
        quantity = int(answer)
        if quantity > 0:
            break
    except ValueError:
        pass

    type_text("(っ- ‸ - ς) Please enter a whole number, like 1 or 2.\n")

total_price = price * quantity

print(f"Thank you, {name}!")

type_text(f"Great choice by the way ◝ (˶˃ ᵕ ˂˶) ◜♡ ! {menu} is a nummy drink.\n"
    "We have small, medium, and large.\n"
)

while True:
    size = input("( ∩´͈ ᐜ `͈∩) What size would you like? ").strip().casefold()

    if size in ("small", "medium", "large"):
        break

    type_text("Hooman pls enter small, medium, or large. (っ- ‸ - ς) \n\n\n")

type_text(
    f"That sounds perfect, {name}! ദ്ദി ( ◡̀  ̫ ◡́)✧ So, {quantity} {size} {menu}.\n"
)

while True:
    extras = input(
        " Would you like...✧｡٩(ˊᗜ ˋ )و✧*｡ whipped cream, caramel drizzle, and chocolate chips? "
    ).strip().casefold()

    if extras in (
        "whipped cream",
        "caramel drizzle",
        "chocolate chips",
        "no extras",
        "no extra",
        "no extras please",
        "nothing",
        "none",
        "no",
    ):
        break

    type_text(
        "Please enter whipped cream, caramel drizzle, chocolate chips, or no extras (´•︵•`)..."
    )
extras_price = 1.50
nothing = ("no extras", "nothing", "none", "no", "no extra", "no extras please")
if extras.lower() in nothing:
    type_text(f"Your order is {quantity} {size} {menu} with no extras.\n")
else:
    total_price += extras_price * quantity

type_text(f"Your total is ${total_price:.2f}.\n")

while True:
    try:
        amount_paid = float(input(f"Please enter exactly ${total_price:.2f}: $ "))
    except ValueError:
        type_text("Please enter the amount as a number.\n")
        continue

    if round(amount_paid, 2) == round(total_price, 2):
        break

    type_text(f"That amount doesn't match. (ᵕ ó ᴗ ò) Please enter ${total_price:.2f}.")
type_text( f"Thank you, {name}!\nYour order will be ready in a moment.")
