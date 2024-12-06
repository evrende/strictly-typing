
This repo is called "strictly-typing" to highlight the fact that the program it contains is about typing per se and not about measuring typing speed. The name also relates to the way the program operates: It presents one line at a time to the user, and requires that each line be copied perfectly before proceeding to the next. The program is designed to provide practice with most keys on a standard (US) English keyboard and, by default, lines will generally include symbols and numbers in addition to the words or text strings that the user can include and edit in an auxiliary file. The lines presented for copying are randomly assembled and thus do not make for coherent sentences unless by pure chance. As the inclusion of numbers and symbols can result in rather "dense" material, users may wish to practice in fairly short sessions. I conceived of this style of practice as a way to gain greater comfort especially with the various symbols available on the keyboard. When practicing this kind of material, I've often tried to take an approach that puts more emphasis on relaxation and good technique than on speed, as I've found that practicing in this way seems to be beneficial for my normal, everyday typing.

Some notes about the program:

Written in Python 3.12, the program uses one external text file ("source.txt") containing practice words and phrases. This file is included in this repository, but with a minimal set of data. Those wishing to use the program are very much encouraged to personalize the content of this external file by giving it a set of words or text strings of relevance to their own purposes.

The program is written for use in a terminal emulator. To run it, navigate to the directory where you've stored its files and enter

python3 typing.py

at your command-line prompt (or just python ..., as your system may require).

In running the program, you will be presented with a number of choices regarding how you would like to use it.

The first option allows you to enter one or more words/strings to practice that are not necessarily in the external file. If you change your mind after choosing this option, you can still opt to use items from source.txt instead. To do this, don't enter anything other than "X" or "\\" at the "Enter practice word:" prompt. If you stay with the "own list" option, there is no limit to the number of words you can enter. You signal that you've finished by entering a capital "X" or a backslash ("\\").

If you don't choose to supply your own words, you are then given the option of choosing how many to include from the external file. If you enter nothing here, all available words/strings will be added to your practice list. If you enter one or more digits, you will get either the corresponding number of items or the number of available items, whichever is smaller. If you enter something other than a digit here, you will automatically get three (3) items in your practice list. If you enter (only) one or more zeros (0), you will get one (1) item in your practice list. Additionally, depending on the length of source.txt, your list may include one or more simple arithmetic equations; these provide practice with the "+" and "=" symbols. To summarize this step, entering nothing will put all available items into your practice list, while entering something will give you a number of practice items less than or equal to the number of available items.

Next, you can choose the number of practice lines you'd like to have in your session. Leaving this blank or entering something other than digits will result in a default value of five (5) lines being supplied. Entering one or more zeros (0) will give you one (1) line. The program currently sets a limit at 300 lines; it is assumed that this will suffice for most sessions! You can change either the default value mentioned above or the 300-line limit inside the "validate_ints" function in typing.py.

Next, you can choose the number of items to include in each line. Again here, the default is five (5) items, and entering one or more zeros (0) will give you one (1) item per line. To prevent most lines from wrapping in a reasonably wide terminal window, a limit of ten (10) words is imposed; higher-valued entries will be reset to this number. Again, you can change it in the "validate_ints" function.

Next is an option to replace items in the practice set with randomized sequences of digits. Users can enter 0 to have no such replacements, 100 to replace all items with numbers, or any integer between these extremes. Leaving this option blank will cause roughly one-fourth (1/4) of list itmes to be replaced with numbers, as will entering an integer greater than 100 or entering anything other than digits. Each number supplied will have between two (2) and eight (8) digits; e.g., '52331', '904'. Also, about one-fourth (1/4) of these numbers will begin with a "$" symbol and include periods and commas if sufficiently long. To change the default (1/4) rate for numbers, change the numbers currently set to 25 both in the "validate\_ints" and the "query\_user" functions. (In the latter, be sure to change both the string and decimal ("float") forms.)

Finally, users can choose to allow or disable the inclusion of "frames" around some of the words and numbers displayed in each line. Such "frames" are various paired symbols enclosing displayed items; e.g., 'example', /41382/, {example}. Entering nothing at the prompt will allow this behavior; entering something will disable it. When the option is enabled, a "frame" will be applied about forty percent (40%) of the time. This setting can be changed by changing the value of the "frames\_rate" variable defined in the "build\_line" function.

I hope this has provided a satisfactory guide to using the program. Of course, more information can be found by reading typing.py itself, in which I've tried to provide a decent number of explanatory comments.

I hope this program will be of some value to your typing practice!

