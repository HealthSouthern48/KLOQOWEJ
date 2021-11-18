# primary NPC to converse with
define s = Character("Shopkeeper")

# character definitions
image shopkeeper happy:
    # happy shopkeeper character
    "s smile"
    pause 4.75
    "s blink"
    pause 0.25
    repeat

image shopkeeper worry:
    # worried shopkeeper character
    "s concern"
    pause 4.75
    "s concern-blink"
    pause 0.25
    repeat

# intro block
label start:
    "Project KLOQOWEJ{p}\nby Isaiah, Jacob, Kyle, Naziya, Sheikh"

# play chapter 1
jump chapter_01

