import pytest

from src.noun import Case, Gender, Noun, declined_article


@pytest.fixture
def nouns():
    return {
        "Mann": Noun("der", "Mann", "Mannes", "Männer", "Männern"),
        "Frau": Noun("die", "Frau", "Frau", "Frauen", "Frauen"),
        "Kind": Noun("das", "Kind", "Kindes", "Kinder", "Kindern"),
    }


def test_declined_article():
    assert declined_article(Gender.MASCULINE, Case.NOMINATIVE) == "der"
    assert declined_article(Gender.MASCULINE, Case.ACCUSATIVE) == "den"
    assert declined_article(Gender.MASCULINE, Case.GENITIVE) == "des"
    assert declined_article(Gender.MASCULINE, Case.DATIVE) == "dem"

    assert declined_article(Gender.FEMININE, Case.NOMINATIVE) == "die"
    assert declined_article(Gender.FEMININE, Case.ACCUSATIVE) == "die"
    assert declined_article(Gender.FEMININE, Case.GENITIVE) == "der"
    assert declined_article(Gender.FEMININE, Case.DATIVE) == "der"

    assert declined_article(Gender.NEUTER, Case.NOMINATIVE) == "das"
    assert declined_article(Gender.NEUTER, Case.ACCUSATIVE) == "das"
    assert declined_article(Gender.NEUTER, Case.GENITIVE) == "des"
    assert declined_article(Gender.NEUTER, Case.DATIVE) == "dem"

    assert declined_article(Gender.MASCULINE, Case.NOMINATIVE, plural=True) == "die"
    assert declined_article(Gender.MASCULINE, Case.ACCUSATIVE, plural=True) == "die"
    assert declined_article(Gender.MASCULINE, Case.GENITIVE, plural=True) == "der"
    assert declined_article(Gender.MASCULINE, Case.DATIVE, plural=True) == "den"


def test_nomenative(nouns):
    assert nouns["Mann"].nominative() == "der Mann"
    assert nouns["Frau"].nominative() == "die Frau"
    assert nouns["Kind"].nominative() == "das Kind"
    assert nouns["Mann"].nominative(plural=True) == "die Männer"


def test_accusative(nouns):
    assert nouns["Mann"].accusative() == "den Mann"
    assert nouns["Frau"].accusative() == "die Frau"
    assert nouns["Kind"].accusative() == "das Kind"
    assert nouns["Mann"].accusative(plural=True) == "die Männer"


def test_genitive(nouns):
    assert nouns["Mann"].genitive() == "des Mannes"
    assert nouns["Frau"].genitive() == "der Frau"
    assert nouns["Kind"].genitive() == "des Kindes"
    assert nouns["Mann"].genitive(plural=True) == "der Männer"


def test_dative(nouns):
    assert nouns["Mann"].dative() == "dem Mann"
    assert nouns["Frau"].dative() == "der Frau"
    assert nouns["Kind"].dative() == "dem Kind"
    assert nouns["Mann"].dative(plural=True) == "den Männern"
