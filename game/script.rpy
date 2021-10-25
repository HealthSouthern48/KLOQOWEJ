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
    hide shopkeeper happy

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

            if len(cart) == 4:
                s "Sorry, we're out of stock. Please come by later for more fresh produce."
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



############################### GAME #############################
init python:

    class PongDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            self.PADDLE_WIDTH = 12
            self.PADDLE_HEIGHT = 95
            self.PADDLE_X = 240
            self.BALL_WIDTH = 15
            self.BALL_HEIGHT = 15
            self.COURT_TOP = 129
            self.COURT_BOTTOM = 650

            # Some displayables we use.
            self.paddle = Solid("#ffffff", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
            self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

            # If the ball is stuck to the paddle.
            self.stuck = True

            # The positions of the two paddles.
            self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
            self.computery = self.playery

            # The speed of the computer.
            self.computerspeed = 380.0

            # The position, delta-position, and the speed of the
            # ball.
            self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
            self.by = self.playery
            self.bdx = .5
            self.bdy = .5
            self.bspeed = 350.0

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = None

        def visit(self):
            return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            oldbx = self.bx

            if self.stuck:
                self.by = self.playery
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed

            # Move the computer's paddle. It wants to go to self.by, but
            # may be limited by it's speed limit.
            cspeed = self.computerspeed * dtime
            if abs(self.by - self.computery) <= cspeed:
                self.computery = self.by
            else:
                self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

            # Handle bounces.

            # Bounce off of top.
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play("pong_beep.opus", channel=0)

            # Bounce off bottom.
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play("pong_beep.opus", channel=0)

            # This draws a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Render the paddle image. We give it an 800x600 area
                # to render into, knowing that images will render smaller.
                # (This isn't the case with all displayables. Solid, Frame,
                # and Fixed will expand to fill the space allotted.)
                # We also pass in st and at.
                pi = renpy.render(self.paddle, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                    hit = False

                    if oldbx >= hotside >= self.bx:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True

                    elif oldbx <= hotside <= self.bx:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True

                    if hit:
                        renpy.sound.play("pong_boop.opus", channel=1)
                        self.bspeed *= 1.10

            # Draw the two paddles.
            paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
            paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)

            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2), int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.bx < -50:
                self.winner = "eileen"

                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.bx > width + 50:
                self.winner = "player"
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            y = max(y, self.COURT_TOP)
            y = min(y, self.COURT_BOTTOM)
            self.playery = y

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

screen pong():

    default pong = PongDisplayable()

    add "bg pong field"

    add pong

    text _("Player"):
        xpos 240
        xanchor 0.5
        ypos 25
        size 40

    text _("Eileen"):
        xpos (1280 - 240)
        xanchor 0.5
        ypos 25
        size 40

    if pong.stuck:
        text _("Click to Begin"):
            xalign 0.5
            ypos 50
            size 40

label play_pong:

    window hide  # Hide the window and  quick menu while in pong
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show

show eileen vhappy

if _return == "eileen":

    e "I win!"

else:

    e "You won! Congratulations."
