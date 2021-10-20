# primary NPC to converse with
define s = Character("Shopkeeper")

# default values
default player_name = "Player"
default passed_say = ""
default nothing = False
default last_say = "Anything else on your list?"
default stock = {"lettuce": 1.25, "cucumber": 1.50, "spinach": 0.75, "bread": 1.75}
#default items = stock.keys()
default lettuce = False
default cucumber = False
default spinach = False
default bread = False
default cart = []

# intro block
label start:
    "Project KLOQOWEJ{p}\nby Isaiah, Jacob, Kyle, Naziya, Sheikh"

# chapter 1: Grocery Shopping
label ch1_start:
    python:
        name = renpy.input("Hello, what is your name?").strip() or player_name

    "Welcome, [name]!{p}\nI hope you enjoy the game."

# scene 1: At the shop
label ch1_sc1:
    menu:
        s "{cps=0}How are you feeling, [name]?{/cps}"

        "I'm fine. Thank you.":
            $ feeling_well = True
        "I'm not feeling too well.":
            $ feeling_well = False

    if feeling_well:
        s "I'm glad to hear that!"
        s "Let's get you some veggies to stay healthy."
    else:
        s "Oh, I'm sorry to hear that."
        s "Maybe some fresh veggies can brighten your mood."

# scene 2: Picking groceries
label ch1_sc2:
    $ items = stock.keys()

    menu buy_groceries:
        s "{cps=0}What [passed_say]can I get you today?{/cps}"

        "[items[0]!c]" if not lettuce:
            $ cart.append(items[0])
            $ lettuce = True
        "[items[1]!c]" if not cucumber:
            $ cart.append(items[1])
            $ cucumber = True
        "[items[2]!c]" if not spinach:
            $ cart.append(items[2])
            $ spinach = True
        "[items[3]!c]" if not bread:
            $ cart.append(items[3])
            $ bread = True
        "Nothing":
            python:
                nothing = True
                last_say = "Are you sure?"

    $ if len(cart) > 0: passed_say = "else "

    menu last:
        s "{cps=0}[last_say]{/cps}"

        "Yes":
            if nothing:
                s "Ok, then."

                if len(cart) == 0:
                    extend "See you later."
                    jump end

                jump checkout

            jump buy_groceries
        "No":
            if nothing:
                if len(cart) == 4:
                    s "Sorry, we're out of stock. Please come by later for more fresh produce."
                    jump checkout

                s "Ok, then. Let's see what I can get you."
                python:
                    nothing = False
                    last_say = "Anything else on your list?"
                jump buy_groceries

            jump checkout

label checkout:
    $ cost = 0
    while len(cart) > 0:
        $ item = cart.pop(0)
        s "Here's your [item]. It costs [stock[item]:.2] dollars."
        $ cost += stock[item]

    menu payment:
        s "In total, these cost [cost:.2] dollars. Would you like to pay in cash, or with credit card?"

        "Cash":
            "{i}You hand a [10 if cost > 5 else 5] dollar bill to the shopkeeper.{/i}"
            s "Here's your change."
            "{i}The shopkeeper returns [(amt - cost):.2] dollars to you.{/i}"
        "Card":
            "{i}You swipe the card at the POS terminal.{p}\nThe machine beeps and accepts your payment.{/i}"

    s "Here's your receipt."

# end script
label end:
    s "Have a nice day, [name]. {p}Come again!"

    return
