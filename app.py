print("\n******Let's play an amazing Game 'Madlibs'*******")

day = input("\nEnter a day: ").capitalize()
place = input("\nEnter a place: ").capitalize()
owner_name = input("\nEnter the owner's name: ").capitalize()
person_name = input("\nEnter the person name: ").title()
adjective = input("\nEnter an adjective: ").lower()
food = input("\nEnter food name: ").lower()
verb = input("\nEnter a verb: ").lower()
title = input("\nEnter title: ").title()

print(f"""\nCheck your story!
\nOn the day of the {day}, the family stops at a {place} called the Tower, owned by {owner_name}.
{person_name} complains that people are {adjective}, explaining that he recently let two men buy {food} on credit.
The grandmother {verb} if he has heard about The Misfit, and {person_name}'s wife worries that he will rob them.
Arguing that “{title},” {person_name} and the grandmother lament the state of the world.""")
