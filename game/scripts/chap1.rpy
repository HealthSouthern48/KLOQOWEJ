# =================================================================
# file:         chap1.rpy
# description:  Main entry point of the game
# author:       Sheikh Saad Abdullah (A00447871)
# =================================================================

# ----------------------------------------------------------------
# CHAPTER 1: Grocery Shopping
# ----------------------------------------------------------------
label chapter_01:
    python:
        name = renpy.input("Hello, what is your name?").strip() or player_name

    "Welcome, [name]!{p}\nI hope you enjoy the game."

# scene 1: At the shop
label at_shop:
    # background image: Store scene
    scene bg store
    show shopkeeper happy at left

    # TODO: comment
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
    hide shopkeeper happy

    # TODO: comment
    menu buy_groceries:
        s "{cps=0}What [passed_say]can I get you today?{/cps}"

        "Lettuce" if not cart["lettuce"]:
            $ cart["lettuce"] = True
        "Cucumber" if not cart["cucumber"]:
            $ cart["cucumber"] = True
        "Spinach" if not cart["spinach"]:
            $ cart["spinach"] = True
        "Bread" if not cart["bread"]:
            $ cart["bread"] = True
        "Nothing":
            python:
                nothing = True
                last_say = "Are you sure?"

    $ if any(cart.values()): passed_say = "else "

    # TODO: comment
    menu pickup_done:
        s "{cps=0}[last_say]{/cps}"

        "Yes":
            if nothing:
                s "Ok, then."

                if not any(cart.values()):
                    show shopkeeper happy at left
                    extend " See you later."
                    jump bye_chap1

                jump checkout

            if all(cart.values()):
                s "Sorry, we're out of stock."
                extend " Please come by later for more fresh produce."
                jump checkout

            jump buy_groceries
        "No":
            if nothing:
                if all(cart.values()):
                    s "Sorry, we're out of stock."
                    extend " Please come by later for more fresh produce."
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
    $ shopping_cart = [item for item in cart.keys() if cart[item]]
    while len(shopping_cart) > 0:
        $ item = shopping_cart.pop(0)
        $ price = stock[item]
        s "Here's your [item]. It costs [price:.2f] dollars."
        $ cost += stock[item]

    # TODO: comment
    menu payment:
        s "In total, these cost [cost:.2f] dollars. Would you like to pay in cash, or with credit card?"

        "Cash":
            $ amt = 10 if cost > 5 else 5
            "{i}You hand a [amt] dollar bill to the shopkeeper.{/i}"
            $ amt -= cost
            if amt > 0:
                s "Here's your change."
                "{i}The shopkeeper returns [amt:.2f] dollars to you.{/i}"
        "Credit Card":
            "{i}You swipe the credit card at the POS terminal.{p}\nThe machine beeps and accepts your payment.{/i}"

    s "Here's your receipt."

# end script for chapter 1
label bye_chap1:
    s "Have a nice day, [name]. {p}Come again!"

    hide shopkeeper happy

    "{b}{i}The End{/i}{/b}"

# return to caller
jump end_chap1
