﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = DynamicCharacter('player_name')
define player_thinking = Character(what_italic = True)

define roomie = Character("Roommate")

# define romanceable characters
define dom = Character("Dominic")
define vic = Character("Victoria")
define a = Character("Artist")
define t = Character("Tsun")

# Gallery code
default galleryList = ["anime_street_art", "red_anime_character"]
default Lightbox_image = ""

# Pronoun data setup
default subj_pron = ""
default obj_pron = ""
default posses_adj = ""
default posses_pron = ""
default reflex_pron = ""

# Flags
default club = "no club"
default skippedClass = "false"

label start:
    $ portrait_number = 0
    $ rebelPoints = 0  
    $ prepPoints = 0 
    $ artistPoints = 0 
    $ tsunPoints = 0 

    scene dorm room

    "DATING SIM DEMO"

    #####################################################################
    #
    #  FIRST SCENE
    #  > Roommate introduction
    #  > Name input
    #  > Pronoun choice
    #  > Portrait choice
    #  > Personality test
    #
    #####################################################################

    # Andrea: Start proper story?
    roomie "Oh my goodness you're here! You're here!"
    show roommate happy with dissolve
    roomie "You're my new roommate, right?"

    # ALEXIS: Name input
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Default"
    $ player_name = name

    roomie "Ah [player_name]! It's so nice to meet you!"
    player "It's nice to meet you too!"

    # ANDREA: Pronoun Selection
    roomie "Ah, also, what are your pronouns?"
    player "Oh, thanks for asking! I use..."
    menu:
        "They/Them":
            $ subj_pron = "they"
            $ obj_pron = "them"
            $ posses_adj = "their"
            $ posses_pron = "theirs"
            $ reflex_pron = "themselves"
        "She/Her":
            $ subj_pron = "she"
            $ obj_pron = "her"
            $ posses_adj = "her"
            $ posses_pron = "hers"
            $ reflex_pron = "herself"
        "He/Him":
            $ subj_pron = "he"
            $ obj_pron = "him"
            $ posses_adj = "his"
            $ posses_pron= "his"
            $ reflex_pron = "himself"

    roomie "Well, it's wonderful to meet you [player_name]. I already know we're going to have a lot of fun together."
    player "What do you mean?"
    roomie "Well, first things first, lets get you settled in!"

    hide roommate happy with dissolve
    
    "Your roommate helps you put your bags down, and leaves you to start unpacking. There's a mirror next to your bed you glance at yourself in."

    player_thinking "What do I look like?"

    # AMELA: Character appearance selection

    screen portrait_selection():
        # Screen that displays 4 image buttons in a 2x2 grid.
        # The player clicks on an image to set their "appearance".

        vpgrid:
            cols 2
            spacing 20

            xalign 0.5
            yalign 0.5

            imagebutton auto "portraits/portrait1_%s.png" action Return(1)
            imagebutton auto "portraits/portrait2_%s.png" action Return(2)
            imagebutton auto "portraits/portrait3_%s.png" action Return(3)
            imagebutton auto "portraits/portrait4_%s.png" action Return(4)

    call screen portrait_selection

    # player appearance set by portrait selected
    $ portrait_number = _return

    # FIXME: delete this code later; for testing purposes now
    if portrait_number == 1:
    #    roomie "Your appearance is Red"
    elif portrait_number == 2:
    #    roomie "Your appearance is Green"
    elif portrait_number == 3:
    #   roomie "Your appearance is Blue"
    elif portrait_number == 4:
    #    roomie "Your appearance is Purple"
    else:
    #    roomie "Something went wrong"

    roomie "Finished?"

    player "Yeah, I'm almost done. Why, what's up?"

    roomie "I found this personality quiz on a blog earlier, you should take it!"

    show roommate happy with dissolve

    player "A personalitiy quiz?"

    "She hands you a piece of torn notebook paper with some questions written down on them"

    #start of quiz
    roomie "Would you rather"
    menu:
            "Read a book at home":
                $ artistPoints += 1
                $ prepPoints += 1
            "Go out to a raging party":
                $ rebelPoints += 1
                $ tsunPoints += 1

    roomie "Would you rather have"
    menu:
        "A close group of friends":
            $ artistPoints += 1
            $ tsunPoints += 1
        "A large number of acquaintances":
            $ rebelPoints += 1
            $ prepPoints += 1

    roomie "One a first date you would like to go to "
    menu:
        "To a movie theater":
            $ artistPoints += 1
            $ rebelPoints += 1
        "On a picnic":
            $ prepPoints += 1
            $ tsunPoints += 1

    player "What kind of blog did you find this on, again?" 

    roomie "No matter, thanks!"

    hide roommate with dissolve

    player_thinking "That was weird. Oh well, time to..."

    #####################################################################
    #
    #  SECOND SCENE ????
    #
    #####################################################################

    jump choose_club

label choose_club:
    "Choose a club."

    menu:
        "Graphic Design Club":
            $ club = "graphic design club"
            jump meet_artist
        "Debate Team":
            $ club = "debate team"
            jump meet_prep
        "No club":
            $ club = "no club"
            jump meet_tsun

label meet_artist:
    "MEET THE ARTIST"
    jump skip_class

label meet_tsun:
    "MEET TSUN"
    jump skip_class

label meet_prep:
    "MEET PREP"

    jump skip_class

label skip_class:
    player_thinking "I'm not really feeling it today. Do I skip class?"

    # jump to meet_badboy, else go to class, then jump to free time
    menu:
        "Skip class":
            jump meet_badboy
        "Go to class":
            pass
    player_thinking "I'm going to class."
    jump free_time_1

label meet_badboy:
    $ skippedClass = "true"

    player_thinking "You know what? I think I will skip class."

    player_thinking "I deserve a break! I'm only human, right?"

    scene outside campus 2

    player_thinking "I find myself taking a pleasant stroll throughout campus."

    player_thinking "Around me I hear people chatting, leaves gently rustling, the distant ringing of bells..."

    player_thinking "It's really peaceful. I'm glad I took this time for myself."

    player_thinking "Even if I might regret it later..."

    player_thinking "As I walk around, someone catches my eye."

    show badboy

    player_thinking "A boy wearing all black, with facial piercings and what looks like a snake tattoo peeking out of his shirt."

    player_thinking "He looks so... edgy."

    player_thinking "I don't realize that I'm staring until he looks right back at me with a devilish smirk."

    dom "You like what you see?"

    menu:
        "I like it a lot, actually":
            player "Yes! A lot, actually!"
            dom "Whoa! Didn't expect that..."
            player_thinking "Eep. Was that too forward?"
        "W-what?":
            $ rebelPoints += 1
            player "Er, sorry, I didn't mean to stare..."
            dom "Haha! I was just teasing."

    dom "So, what're you up to? Heading to class?"

    player "No, I'm... skipping class, actually..."

    dom "Whoa! Got ourselves a rule-breaker over here!"

    player_thinking "I feel my face going pink..."

    dom "I'm doing the same, actually. Going to class is lame."

    player_thinking "He's so right."

    dom "You just moved in to ROOMMATE's place, right? [player_name], is it?"

    player_thinking "Oh! This must be Dominic."

    player "Yeah. She told me about you. I didn't expect to bump into you like this."

    dom "Heh. I'm sure she only had great things to say about me..."

    dom "Well, you're least likely to find me in a classroom-setting, that's for sure."

    dom "Because I'm too cool for school, y'know."

    dom "Anyways, I gotta bounce. Got hooligan activities to attend to. Because I'm a hooligan."
    
    player_thinking "He sounds like he's kidding, but somehow I can't tell."

    dom "I'm sure we'll bump into each other again. Later!"

    hide badboy

    player_thinking "Before I can even say goodbye, he starts sprinting past me like a madman."

    player_thinking "Those hooligan activities must be urgent..."
    
    jump free_time_1

label free_time_1:
    player_thinking "I have some free time... what should I do?"

    call screen MapUI
    ""
    return

label library_1:
    scene library
    "LIBRARY 1: PREP IS THERE"
    jump halloween_party

label schoolstore_1:
    scene school store
    "SCHOOL STORE 1: ARTIST IS THERE"
    jump halloween_party

label tenniscourts_1:
    scene tennis courts

    if skippedClass == "true":
        dom "Well, well, well, if it isn't the rule-breaker! You skipping class again?"
        player_thinking "That voice sounds familiar..."
        show badboy
        player_thinking "It's Dominic!"
        player "No! I just had some free time, actually. I haven't seen the tennis courts before..."
    else:
        dom "Hey! You're ROOMMATE's friend, right? What're you doing here?"
        player_thinking "Who could that be?"
        show badboy
        player_thinking "This must be Dominic."
        player "I just had some free time. I hadn't seen the tennis courts yet..."

    dom "Well, I gotta tell you, there isn't much to see..."

    dom "Apart from me, of course."

    player_thinking "He's so smug..."

    player "Do you come here to play tennis, or just to loiter like a hooligan?"

    player_thinking "He cracks a smirk at that."

    dom "I think you know the answer to that."

    dom "But since we're both here, might as well have ourselves a game, no?"

    player "Pausing the hooligan activities for now?"

    dom "There's always time for them."

    player_thinking "I guess we're playing a friendly game of tennis."

    player_thinking "Should I..."

    menu:
        "Try my best":
            player_thinking "I go 100% tryhard mode. I'm running around the court as swiftly as my legs can take me."
            player_thinking "Dominic looks surprised. Guess he didn't expect me to go so hard."
            player_thinking "But I play to win!"
        "Not sweat it":
            $ rebelPoints += 1
            player_thinking "I don't try too hard. I can see that Dominic clearly doesn't, either."
            player_thinking "We both goof off as we swing our rackets around with the mindset of 'If I don't hit the ball, I don't hit the ball. Big whoop.'"
            player_thinking "By the end of it, we're both laughing at each other."

    dom "Are the tennis courts everything you hoped for?"
    
    player "Oh, yes. And so much more."

    dom "Heh. That was actually the first time I'd done anything besides loitering at this place. Was pretty fun."

    player_thinking "I peek down at my watch and realize it's almost time for my next class."

    player "Hey, I've got class to get to, but thanks for the game."

    if skippedClass == "true":
        dom "Going to class? I'm surprised."
        player "Hey!"

    dom "For sure. I also have... things. But good game."

    hide badboy

    player_thinking "Before I can open my mouth to speak, Dominic sprints towards the nearest tennis net, leaps over it, and continues sprinting towards the exit gate."

    player_thinking "That guy must not have a care in the world..."

    jump halloween_party

label dorms_1:
    scene dorm room
    "DORMS 1: TSUN IS THERE"
    jump halloween_party

label halloween_party:
    player_thinking "HALLOWEEN PARTY -- where should I go?"
    menu:
        "Haunted house":
            jump haunted_house
        "Pumpkin patch":
            jump pumpkin_patch

label haunted_house:
    "Haunted house event"

    menu:
        "Side with bad boy":
            pass
        "Side with tsundere":
            pass

    jump free_time_2

label pumpkin_patch:
    "Pumpkin patch event"

    menu:
        "Side with prep":
            pass
        "Side with artist":
            pass
    jump free_time_2

label free_time_2:
    player_thinking "I have some free time... what should I do?"

    # TODO: probably nicer way to do this using "call" instead of "jump",
    # having two separate free_time labels is fine for now

    menu:
        "Library":
            jump library_2
        "School store":
            jump schoolstore_2
        "Tennis courts":
            jump tenniscourts_2
        "Dorms":
            jump dorms_2

    return

label library_2:
    "LIBRARY 2: TSUN IS THERE"
    jump route_determination

label schoolstore_2:
    "SCHOOL STORE: BADBOY IS THERE"

    jump route_determination

label tenniscourts_2:
    "TENNIS COURTS: PREP IS THERE"

    jump route_determination

label dorms_2:
    "DORMS: ARTIST IS THERE"

    jump route_determination

label route_determination:
    # check which character has the most points here --
    # whoever it is, trigger their route
    # set flag to current route

    "Route determined here"

    return

label BADBOY_START:
    # badboy route
    return

label ARTIST_START:
    # artist route
    return

label PREP_START:
    # prep route
    return

label TSUNDERE_START:
    # tsundere route
    return

label FINAL_PARTY:
    # new year's party event
    return

label BAD_END:
    # general bad ending
    return

# TODO: good endings for whichever route
# check flag variable for route
