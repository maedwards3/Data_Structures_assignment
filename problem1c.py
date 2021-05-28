import random

contestants = {
    "contestantOne": "Jeremy Volz",
    "contestantTwo": "Dan Drapeau",
    "contestantThree": "Colin Jansen",
    "contestantFour": "Sabrina Fillinger",
    "contestantFive": "Joseph Wilson"
}

contestants["contestantSix"] = "Jess Gramp"
contestants["contestantSeven"] = "Jimmy Dean"
contestants["contestantEight"] = "Drogo Bean"
contestants["contestantNine"] = "Chance Pants"
contestants["contestantTen"] = "Suzy Bunz"

entry_list = list(contestants.items())

random_entry = random.choice(entry_list)
