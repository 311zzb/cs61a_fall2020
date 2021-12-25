# All cards available in a standard deck.
from classes import *

#TAs
sean = TACard('Sean, the Over-Caffeinated', 1000, 2300)
jade = TACard('Jade, Singher of Songs', 1700, 1700)
richard_r = TACard('Richard, Protector of Baby Yoda', 2100, 1800)
griffin = TACard('Griffin, the Goblin Keeper', 1300, 1500)
albert = TACard('Albert, Lethargy Incarnate', 1000, 2300)
shayna = TACard('Shayna, Queen of the Bones', 1111, 2235)
addison = TACard('Addison, from operator import add', 1000, 2000)
cesar = TACard('Cesar, City Slicker', 1337, 2020)
catherine = TACard('Catherine, Supporter of Cats', 1900, 1000)
amrita = TACard('Amrita-tron 3000', 2150, 1750)

#Tutors
laryn = TutorCard('Laryn, Lord of Lambdas', 2300, 2300)
parth = TutorCard('Parth, the Protector of Piazza', 1500, 2200)
todd = TutorCard('Todd, Protector of Corgis', 2300, 1000)
crystal = TutorCard('Crystal, Fat Bear Week 2020 Runner-Up', 2023, 1738)
ben = TutorCard('Ben, the Panda stuck in an Infinite Loop', 1024, 2020)
cyrus = TutorCard('Cyrus, King of Phonies', 1700, 2200)
roy = TutorCard('Roy, Eater of Oranges', 2229, 2268)
animesh = TutorCard('Animesh, without a cool hat', 1000, 2300)
megan = TutorCard('Megan, Lord of the Kiwi Bots', 2000, 1100)
yersultan = TutorCard('Yersultan, Yogurt Man', 1246, 1790)
connie = TutorCard('Connie, Carb Connoisseur', 2123, 1029)
jenny = TutorCard('Jenny, the Spy Among Other Jennys', 1500, 2000)
jeffrey = TutorCard('Jeffrey, Freezer of Fruit', 2300, 1000)
marie = TutorCard('Marie, Arbiter of Justice and Herald of Seraphs, True Heir to the Last Monarch of Ra’toth', 1150, 2200)
linh = TutorCard('Linh, Phantom of the Classroom', 1919, 2299)
benny = TutorCard('Benny, Practitioner of Day-Night Reversal', 1694, 2009)
tim = TutorCard('Tim Tu, Tyrant Tutor of Twos', 2222, 2222)
emma = TutorCard('Emma, the Perpetually Unrested', 2000, 1834)
richard_z = TutorCard('Richard, Headband Merchant', 1337, 1614)
brandon = TutorCard('Brandon, the Deadline Demon', 1250, 1000)
daphne = TutorCard('Daphne, Daphrying Pan', 1801, 1350)
jamie = TutorCard('Jamie, Anagrammer of Rice Or Sun', 2234, 1828)



# Professors
denero = ProfessorCard('John DeNero, Protector of Abstraction Barriers', 5000, 5000)

# A standard deck contains all standard cards.
standard_cards = [denero, sean, jade, richard_r, griffin, albert, shayna, addison, cesar, catherine, amrita, laryn, parth, todd, crystal, ben, cyrus, roy, animesh, megan, yersultan, connie, jenny, jeffrey, marie, linh, benny, tim, emma, richard_z, brandon, daphne, jamie]
standard_deck = Deck(standard_cards)

# The player and opponent's decks are the standard deck by default.
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()

