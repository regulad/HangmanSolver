import json
from typing import List, Tuple

with open("words.json") as fp:
    wordle_answers: List[str] = json.load(fp)

letters = input(
    "Enter the known letters, replacing unknowns with an underscore. EX: ab_ey\n"
    "If you do not know a letter, do not include it.\n"
    ">"
)

if len(letters) == 5:
    results: List[Tuple[str, int]] = []
    for word in wordle_answers:
        matching_letters: int = 0
        for word_letter, answer_letter in zip(word, letters):
            if word_letter == answer_letter:
                matching_letters += 1
        results.append((word, matching_letters))
    sorted_results: List[Tuple[str, int]] = sorted(results, key=lambda tup: tup[-1], reverse=True)
    for sorted_result in sorted_results[:10]:
        print(f"Possible match: {sorted_result[0]} ({sorted_result[-1]}/5)")
else:
    raise RuntimeError("Wrong word length!")
