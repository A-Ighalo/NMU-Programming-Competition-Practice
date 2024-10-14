# joyful.py

def madlibs():
    print("Welcome to the Joyful Mad Libs!")
    print("Please provide the following words:")

    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")
    adj2 = input("Enter another adjective: ")
    verb2 = input("Enter another verb: ")
    noun3 = input("Enter one more noun: ")

    story = f"""
    On a {adj1} day, the world seemed full of {noun1}.
    Friends gathered to {verb1} and share in the {noun2}.
    Their {adj2} spirits lifted everyone around them.
    As they continued to {verb2}, their joy spread like wildfire.
    In that moment of pure {noun3}, everything felt absolutely wonderful.
    """

    print(story)