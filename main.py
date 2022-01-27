import json
from typing import List, Tuple


filename: str = input(
    "Please enter a dictionary filename.\n"
    "If none is entered, the default english one will be used. You can use it.json for italian.\n"
    ">"
) or "words.json"

with open(filename) as fp:
    wordle_answers: List[str] = json.load(fp)


while True:
    letters = input(
        "Enter the known letters, replacing unknowns with an underscore. EX: ab_ey\n"
        "If you do not know a letter, do not include it.\n"
        ">"
    )
    
    if len(letters) == 5:
        known_letters: int = len([char for char in letters if char != "_"])
        results: List[Tuple[str, int]] = []
        for word in wordle_answers:
            matching_letters: int = 0
            try:
                for word_letter, answer_letter in zip(word, letters):
                    if word_letter == answer_letter:
                        matching_letters += 1
                    elif answer_letter != "_":
                        raise RuntimeError  # Breaking a layer out
            except RuntimeError:
                continue
            else:
                results.append((word, matching_letters))
        sorted_results: List[Tuple[str, int]] = sorted(results, key=lambda tup: tup[-1], reverse=True)
        for sorted_result in sorted_results[:10]:
            print(f"Possible match: {sorted_result[0]} ({sorted_result[-1]}/{known_letters})")
    else:
        raise RuntimeError("Wrong word length!")
