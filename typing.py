
"""typing.py

This software is copyrighted under the MIT license (https://opensource.org/license/mit);
see also the "LICENSE" file at https://github.com/evrende/strictly-typing/tree/main.

Source code written in Python 3.12.3.

This program enables typing practice in a terminal emulator.

It depends on a file named source.txt for a set of string data
to supply words or arbitrary strings for the user to practice typing.

For more information, see its README.md file.
"""

from random import choice, random as r
from time import perf_counter as get_time

# some global variables:

stock = [] # to hold string data

# get data from external file:
with open('source.txt', 'r') as k:
    for line in k:
        # filter out empty lines:
        if (line[:-1]):
            stock.append(line[:-1])

# guard against a too-short source list:
firstlies = ["fifth", "fourth", "third", "second", "first"]
while (len(stock) < 5):
    stock.append(firstlies.pop());

stop = len(stock) // 12
# add some items using '+' and '=':
for i in range(stop):
    result = choice(range(3, 101))
    addend1 = result - choice(range(0, result + 1))
    addend2 = result - addend1
    stock.append(f"{addend1} + {addend2} = {result}")

# and some paired symbols for setting around words/numbers:
frames = ["[]", "[]", "{}", "{}", "()", "()", "''", '""', "--", "__", "<>", "//"]


def intro():
    """Welcome user."""
    print("\nWelcome to typing practice!")


def get_number():
    """Randomly compose a string containing only digits."""
    number = ""
    # make a string of 2 to 8 digits:
    n = choice(range(2, 9))
    for i in range(n):
        number += str(choice(range(0, 10)))
    # let about 1/4 get "$" etc.
    if (r() < 1/4):
        number = number2money(number)
    return number # a string


def number2money(number: str):
    """Decorate number from get_number with '$' and punctuation."""    
    # disallow '04', etc:
    if ((len(number) == 2) and (number[0] == "0")):
        number = "72" # car je l'aime
    # add a decimal point:
    elif (len(number) > 2):
        number = number[:-2] + "." + number[-2:]
        # avoid unwanted 0's:
        if (("0" in number) and ("0." not in number)):
            while(number[0] == "0"):
                number = number[1:]
    # add a comma:
    if (len(number) > 6):
        number = number[:-6] + "," + number[-6:]
        # disallow this beginning:
        if (number[:2] == "0,"):
            number = number[2:]
    # add a dollar sign:
    return "$" + number


def build_line(fund: list, word_count: int, num_rate: float, add_frames: bool):
    """Compose a line of text for user to type."""
    # define extra punctuation:
    extra_punctuation = (",", ";", ":")
    # set numbers to control frequency of frames, capitals, trailing punctuation:
    frames_rate, caps_rate, trailing_rate = 0.40, 0.12, 0.33

    model = "" # the beginning of a line
    for i in range(word_count):
        # set "frames" [e.g.] around some items:
        frame = choice(frames) if (add_frames and (r() < frames_rate)) else ("", "")
        # select a word from list or compose a series of digits:
        word_or_num = get_number() if (r() < num_rate) else choice(fund)
        # capitalize a fraction of the words to be shown:
        word_or_num = word_or_num.capitalize() if (r() < caps_rate) else word_or_num
        # set a symbol after each unframed equation:
        if (("+" in word_or_num) and (frame[0] == "")):
            word_or_num += " " + choice(["@", "#", "$", "%", "^", "&", "*", "/", "\\", "|"])
        # add punctuation after some items:
        trailing_punct = choice(extra_punctuation) if (r() < trailing_rate) else ""
        # add these components to line:
        model += frame[0] + word_or_num + frame[1] + trailing_punct + " "

    # remove trailing space:
    model = model[:-1]
    # and any trailing punctuation:
    if (model[-1] in extra_punctuation):
        model = model[:-1]
    # end line decisively (or with "?"):
    model += "." if (r() < 0.84) else choice(["?", "!"])
    # and put final periods inside quotes:
    if (model[-2:] in ["'.", '".']):
        model = model[:-2] + model[-1] + model[-2]
    # same for commas:
    model = model.replace("',", ",'")
    model = model.replace('",', ',"')
    return model # a string


def lines_match(from_user: str, model: str):
    """Compare model with user's input."""
    if (from_user == model):
        return True
    return False


def validate_ints(s: str, caller: str):
    """Ensure that parameter s translates to an appropriate integer."""
    # helps determine number words, lines, words per line
    # prepare for missing or invalid entries:
    default = 5
    n = -1
    if (s): # (exists)
        # is it only digits?
        for char in s:
            if (ord(char) not in range(48, 58)):
                # if not, assign default value:
                if (not caller):
                    return 25 # for number rate
                elif (caller == "get_word_count"):
                    return 3 # for words in list
                n = default; break # (disallows negatives)
    else:
        n = default

    if (n < 0): # if n not yet touched,
        # make it a positive integer:
        n = 1 if (int(s) == 0) else int(s)

    # set some reasonable restrictions:
    if (caller in ["lines", "wpl"]):
        limit = 300 if (caller == "lines") else 10 # (words per line)
        if (n > limit):
            n = limit
    elif (caller == "get_word_count"):
        if (n > len(stock)):
            # inform user of list length:
            z = "s" if (len(stock) > 1) else ""
            print("That's more than the available number of items!")
            print(f"Your list will have {len(stock)} item{z} for practice.")
            n = len(stock)

    return n # an integer
        

def working_set(n: int):
    """Compose a list of n words/strings for practice."""
    # n gives user's chosen number of (different) words
    # get and return that many (if possible), in a simple list:
    fund = []
    # "safeguard" n:
    if (n > len(stock)):
        n = len(stock)
    # control timing:
    base_time = get_time()
    while (len(fund) < n):
        cand = choice(stock)
        # try for uniqueness:
        if (cand not in fund):
            fund.append(cand)
        # but don't allow to run forever:
        if (get_time() - base_time > 0.4):
            s = "" if (len(fund) == 1) else "s"
            print("That's more than the number of available unique words.")
            print(f"Your practice list will have {len(fund)} unique item{s}.")
            break;
    return fund # a list


def make_own_list():
    """Let user enter any number of their own words."""
    L, item = [], ""
    print("(Enter X or \\ when finished.)")
    while ("accepting submissions"):
        item = input("Enter practice word: ")
        # disallow blanks:
        while (not item):
            item = input("Please enter a string for your practice list: ")
        if (item in ["X", "\\"]):
            # these sentinel values will
            break # the while loop
        L.append(item)
    if (not L): # if L is empty,
        print("Don't you want to enter anything? To make your own list,")
        response = input("enter any text; or leave blank to use words from source file: ")
        if (response): # call self:
            return make_own_list()
        else: # use existing data:
            L = get_word_count()
    return L # a list


def get_word_count():
    """Let user determine length of practice list."""
    word_count = input("For a limited set of words, enter an integer: ")
    if (word_count == ""):
        # no restriction: use full set
        working_list = stock
    else:
        n = validate_ints(word_count, "get_word_count")
        working_list = working_set(n)
    return working_list # a list


def query_user():
    """Get specifications/parameter values from user."""

    own_list = input("Enter O or W to define your own list: ")
    if (own_list.lower() in ["o", "w"]):
        working_list = make_own_list()
    # choosing own list defines the number of words to use;
    else:
        working_list = get_word_count()

    number_of_lines = input("How many lines to practice? ")
    number_of_lines = validate_ints(number_of_lines, "lines")

    words_per_line = input("How many words per line?    ") # (spaces for alignment)
    words_per_line = validate_ints(words_per_line, "wpl")

    print("You can replace words with numbers.")
    num_rate = input("Enter '40' to replace 40 percent (default is 25): ")
    if not num_rate:
        num_rate = "25"
    num_rate = validate_ints(num_rate, "") / 100
    if (num_rate > 1):
        num_rate = 0.25

    # optionally set "frames" around some items:
    print("By default, some words and numbers will be enclosed in symbols, ")
    message = "like {this}; enter any text NOT to include such symbols: "
    frames = input(message)
    # draw an underline before play starts:
    adjustment = 1 if (frames) else 0
    print((len(message) - 1 + len(frames) + adjustment) * "-")
    frames = True if (not frames) else False # makes sense, right?

    return (working_list, number_of_lines, words_per_line, num_rate, frames)
         #  list,         integer,         integer,        float,    string


def closing(no_errors):
    """Congratulate user for a perfect performance and say goodbye."""
    if (no_errors):
        print("\n" + choice(["Good job!", "Perfect!", "¡Bien hecho!"]))
    print("\nMay the force be with you!")


def play():
    """Coordinate other functions, run the show."""
    # rename this function 'main' if you like
    intro()
    # get user preferences:
    (WL, lines, wpl, NR, frames) = query_user()
    # take note of perfect sessions:
    no_mistakes = True # (line-level, not word-level)
    # build, display, and check lines:
    for i in range(lines):
        model = build_line(WL, wpl, NR, frames)
        while ("checking for match"):
            # display model line:
            print("\n" + model)
            # record user input:
            attempt = input()
            # check/compare:
            if (lines_match(attempt, model)):
                break # while
            else:
                print("\nTry again:")
                no_mistakes = False # :(
    # send closing message:
    closing(no_mistakes)


if __name__ == "__main__":
    play()

