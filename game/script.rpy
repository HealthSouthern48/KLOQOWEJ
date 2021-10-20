# primary NPC to converse with
define s = Character("Shopkeeper")

# character animation
image shopkeeper happy:
    "s smile"
    pause 4.75
    "s blink"
    pause 0.25
    repeat

image shopkeeper worry:
    "s concern"
    pause 4.75
    "s concern-blink"
    pause 0.25
    repeat

# default values
default player_name = "Player"
default passed_say = ""
default nothing = False
default last_say = "Anything else on your list?"
default stock = {"lettuce": 1.25, "cucumber": 1.50, "spinach": 0.75, "bread": 1.75}
default lettuce = False
default cucumber = False
default spinach = False
default bread = False
default cart = []

# intro block
label start:
    "Project KLOQOWEJ{p}\nby Isaiah, Jacob, Kyle, Naziya, Sheikh"

# chapter 1: Grocery Shopping
label chapter_01:
    python:
        name = renpy.input("Hello, what is your name?").strip() or player_name

    "Welcome, [name]!{p}\nI hope you enjoy the game."

# scene 1: At the shop
label at_shop:
    # background image: Store scene
    scene bg store
    show shopkeeper happy at left

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
        show shopkeeper worry at left
        s "Oh, I'm sorry to hear that."
        s "Maybe some fresh veggies can brighten your mood."
        hide shopkeeper worry

# scene 2: Picking groceries
label pick_items:

    menu buy_groceries:
        s "{cps=0}What [passed_say]can I get you today?{/cps}"

        "Lettuce" if not lettuce:
            $ cart.append("lettuce")
            $ lettuce = True
        "Cucumber" if not cucumber:
            $ cart.append("cucumber")
            $ cucumber = True
        "Spinach" if not spinach:
            $ cart.append("spinach")
            $ spinach = True
        "Bread" if not bread:
            $ cart.append("bread")
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
                    extend " See you later."
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

# scene 3: Checking out
label checkout:
    # change background
    scene bg counter
    show shopkeeper happy at left

    $ cost = 0
    while len(cart) > 0:
        $ item = cart.pop(0)
        $ price = stock[item]
        s "Here's your [item]. It costs [price:.2f] dollars."
        $ cost += stock[item]

    menu payment:
        s "In total, these cost [cost:.2f] dollars. Would you like to pay in cash, or with credit card?"

        "Cash":
            $ amt = 10 if cost > 5 else 5
            "{i}You hand a [amt] dollar bill to the shopkeeper.{/i}"
            s "Here's your change."
            $ amt -= cost
            "{i}The shopkeeper returns [amt:.2f] dollars to you.{/i}"
        "Card":
            "{i}You swipe the card at the POS terminal.{p}\nThe machine beeps and accepts your payment.{/i}"

    s "Here's your receipt."

# end script
label end:
    s "Have a nice day, [name]. {p}Come again!"

    hide shopkeeper happy

    "{b}{i}The End{/i}{/b}"

    return
