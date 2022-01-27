import json
import requests
from typing import List, Tuple

lang: str = input("Please input a language. Current choices: en, it\n"
                  ">") or "en"


words: List[str] = []

if lang == "en":
    print("Loading English...")
    with requests.get(
        "https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json"
    ) as raw_dict:
        words.extend(raw_dict.json().keys())
elif lang == "it":
    words = []
    print("Loading Italian...")
    with requests.get(
            "https://raw.githubusercontent.com/pietroppeter/wordle-it/master/60_000_parole.txt"
    ) as raw_dict:
        words.extend([raw_line for raw_line in raw_dict.text.split("\n") if raw_line])
else:
    raise RuntimeError

print("=======================")
while True:
    letters = input(
        "Enter the known letters, replacing unknowns with an underscore. The string must be the exact length.\n"
        "If you do not know a letter, do not include it.\n"
        ">")
    print("Searching...")

    known_letters: int = len([char for char in letters if char != "_"])
    results: List[Tuple[str, int]] = []
    for word in [answer for answer in words if len(answer) == len(letters)]:
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
    sorted_results: List[Tuple[str, int]] = sorted(results,
                                                   key=lambda tup: tup[-1],
                                                   reverse=True)
    for sorted_result in sorted_results[:20]:
        print(
            f"Possible match: {sorted_result[0]} ({sorted_result[-1]}/{known_letters})"
        )
    if len(sorted_results) == 0:
        print("No results found!")
    print("=======================")
