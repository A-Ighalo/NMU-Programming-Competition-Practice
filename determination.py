# determination.py

def madlibs():
    print("Welcome to the Determination Mad Libs!")
    print("Please provide the following words:")

    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")
    adj2 = input("Enter another adjective: ")
    verb2 = input("Enter another verb: ")
    noun3 = input("Enter one more noun: ")

    story = f"""
    In the face of adversity, the {adj1} hero stood tall.
    With each {noun1} that came their way, they only grew stronger.
    Determined to {verb1} against all odds, they pressed forward.
    No {noun2} was too great, no challenge too daunting.
    In the end, their {adj2} spirit allowed them to {verb2} their ultimate {noun3}.
    """

    print(story)