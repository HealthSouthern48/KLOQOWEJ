# =================================================================
# file:         shopkeeper.rpy
# description:  Main entry point of the game
# author:       Sheikh Saad Abdullah (A00447871)
# design:       Naziya Tasnim (A00447506)
# =================================================================

# ----------------------------------------------------------------
# CHARACTER DEFINITIONS FOR SHOPKEEPER
# ----------------------------------------------------------------

# primary NPC to converse with
define s = Character("Shopkeeper")

# happy shopkeeper character
image shopkeeper happy:
    "s smile"
    pause 4.75
    "s blink"
    pause 0.25
    repeat

# worried shopkeeper character
image shopkeeper worry:
    "s concern"
    pause 4.75
    "s concern-blink"
    pause 0.25
    repeat
