print("=== COOKING DISASTER MAD LIBS ===\n")

# Ask the player for words
noun1      = input("Give me a noun (a thing): ")
noun2      = input("Give me another noun: ")
verb1      = input("Give me a verb (an action word): ")
adjective1 = input("Give me an adjective (a describing word): ")
adjective2 = input("Give me another adjective: ")
number     = input("Give me a number: ")
food       = input("Give me a food: ")
body_part  = input("Give me a body part: ")
celebrity  = input("Give me a celebrity's name: ")

# Print the story
print(f"""
--- YOUR STORY ---

It was supposed to be a simple dinner, but the moment I touched the {noun1},
everything went wrong.

I had been cooking for {number} minutes when I accidentally dropped the {noun2}
into the {food}. The smell was absolutely {adjective1}.

I tried to {verb1} the mess before anyone noticed, but it was too late.
My {body_part} was covered in sauce, and the kitchen looked {adjective2}.

Just then, {celebrity} walked through the door.
They took one look at the disaster and said,
"I've eaten at {noun1} before, but this is something else entirely."

We ordered pizza.

THE END.
""")
