 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character. we still need to decide the name of the character

#Hi

define m = Character("Main Guy")
define p = Character("Pilot")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it. (Jaise art aate rhenge, add them to the images waala folder and add them here. For bg, use scene and for character art, use show)

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    m "Zzz... Zzz"
    #make stylistic edits here i'll be designating them with this symbol in the comments "$"
    p "Ladies and Gentlemen, we have now reached our cruising altitiude of 30 thousand feet." 
    p "Refreshments will be served shortly."
    p "Thank you for your attention."
    # $
    m "(*sigh that's one way to wake up I guess...)"
    # $
    # hello world OwO

    # This ends the game.

    return
