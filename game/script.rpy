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

# intro block
label start:
    "Project KLOQOWEJ{p}\nby Isaiah, Jacob, Kyle, Naziya, Sheikh"

# play chapter 1
jump chapter_01

