import random

from src.noun import Case, Noun


def example_sentence(case: Case, plural: bool) -> str:
    if case == Case.NOMINATIVE:
        if plural:
            return "X gehen zu der Schule."
        else:
            return "X geht zu der Schule."
    if case == Case.ACCUSATIVE:
        return "Ich gehe nicht ohne X."
    if case == Case.GENITIVE:
        return "Das Haus X ist rot."
    else:  # Case.DATIVE
        return "Ich gehe mit X."


def main():
    nouns = [
        Noun("der", "Mann", "Mannes", "Männer", "Männern"),
        Noun("die", "Frau", "Frau", "Frauen", "Frauen"),
        Noun("das", "Kind", "Kindes", "Kinder", "Kindern"),
    ]

    correct_answers = 0
    num = int(input("Number of exercises: "))
    print("Replace 'X' in the sentences below with the correct article and noun:")
    for i in range(num):
        noun = random.choice(nouns)
        answer_case = random.choice(list(Case))
        answer_plural = random.choices([True, False], weights=(25, 75))[0]
        if answer_plural:
            plural_text = "plural"
        else:
            plural_text = "singular"
        answer = input(
            f"({noun.nominative()} in {str(answer_case)}, {plural_text}) "
            f"{example_sentence(answer_case, answer_plural)}: "
        )
        correct_answer = noun.declined(answer_case, answer_plural)
        if answer == correct_answer:
            print("  Correct!")
            correct_answers += 1
        else:
            print(f"  Wrong! The correct answer is: {correct_answer}")

    print(f"Score: {correct_answers}/{num}")


if __name__ == "__main__":
    main()
