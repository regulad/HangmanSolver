import json
from typing import List

with open("words.json") as fp:
    wordle_answers: List[str] = json.load(fp)

letters = input(
    "Enter the known letters, replacing unknowns with an underscore. EX: ab_ey\n"
    "If you do not know a letter, do not include it.\n"
    ">"
)

if len(letters) == 5:
    for word in wordle_answers:
        matching_letters: int = 0
        for word_letter, answer_letter in zip(word, letters):
            if word_letter == answer_letter:
                matching_letters += 1
        if matching_letters >= 4:
            print(f"Possible match: {word}")
else:
    raise RuntimeError("Wrong word length!")
