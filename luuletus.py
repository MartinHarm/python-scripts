poem = """
Lets write a poem.

Fill the blanks!

Roses are [firstBlank],
[secondBlank] are blue,
I love to [thirdBlank]
And so will you!
"""
print(poem)

print('firstBlank')
firstBlank = input()

print('secondBlank')
secondBlank = input()

print('thirdBlank')
thirdBlank = input()

poem = f"""
Roses are {firstBlank},
{secondBlank} are blue,
I love to {thirdBlank}
And so will you!
"""
print(poem)