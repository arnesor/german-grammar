"""Command-line interface."""
import random
import secrets

import click

from .noun import Case
from .noun import Noun


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


@click.command()
@click.version_option()
def main() -> None:
    """German Grammar."""
    nouns = [
        Noun("der", "Mann", "Mannes", "Männer", "Männern"),
        Noun("die", "Frau", "Frau", "Frauen", "Frauen"),
        Noun("das", "Kind", "Kindes", "Kinder", "Kindern"),
    ]

    correct_answers = 0
    num = int(input("Number of exercises: "))
    print("Replace 'X' in the sentences below with the correct article and noun:")
    for _ in range(num):
        noun = secrets.choice(nouns)
        answer_case = secrets.choice(list(Case))
        answer_plural = random.choices([True, False], weights=(25, 75))[0]  # nosec
        if answer_plural:
            plural_text = "plural"
        else:
            plural_text = "singular"
        answer = input(
            f"({noun.nominative()} in {answer_case.name.lower()}, {plural_text}) "
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
    main(prog_name="german-grammar")  # pragma: no cover
