from dataclasses import dataclass
from enum import IntEnum


class Gender(IntEnum):
    MASCULINE = (0,)
    FEMININE = (1,)
    NEUTER = 2


class Case(IntEnum):
    NOMINATIVE = (0,)
    ACCUSATIVE = (1,)
    GENITIVE = (2,)
    DATIVE = 3


def declined_article(gender: Gender, case: Case, plural: bool = False) -> str:
    m_case = ("der", "den", "des", "dem")
    f_case = ("die", "die", "der", "der")
    n_case = ("das", "das", "des", "dem")
    p_case = ("die", "die", "der", "den")
    if plural:
        return p_case[case]
    if gender == Gender.MASCULINE:
        return m_case[case]
    if gender == Gender.FEMININE:
        return f_case[case]
    else:  # Gender.NEUTER
        return n_case[case]


@dataclass
class Noun:
    article: str
    noun: str
    genitive_noun: str
    plural_noun: str
    plural_dative_noun: str

    def gender(self) -> Gender:
        if self.article == "der":
            return Gender.MASCULINE
        if self.article == "die":
            return Gender.FEMININE
        else:
            return Gender.NEUTER

    def nominative(self, plural: bool = False):
        if not plural:
            return self.article + " " + self.noun
        else:
            return (
                declined_article(self.gender(), Case.NOMINATIVE, plural=True)
                + " "
                + self.plural_noun
            )

    def accusative(self, plural: bool = False):
        if not plural:
            return declined_article(self.gender(), Case.ACCUSATIVE) + " " + self.noun
        else:
            return (
                declined_article(self.gender(), Case.ACCUSATIVE, plural=True)
                + " "
                + self.plural_noun
            )

    def genitive(self, plural: bool = False):
        if not plural:
            return (
                declined_article(self.gender(), Case.GENITIVE)
                + " "
                + self.genitive_noun
            )
        else:
            return (
                declined_article(self.gender(), Case.GENITIVE, plural=True)
                + " "
                + self.plural_noun
            )

    def dative(self, plural: bool = False):
        if not plural:
            return declined_article(self.gender(), Case.DATIVE) + " " + self.noun
        else:
            return (
                declined_article(self.gender(), Case.DATIVE, plural=True)
                + " "
                + self.plural_dative_noun
            )

    def declined(self, case: Case, plural: bool) -> str:
        if case == Case.NOMINATIVE:
            return self.nominative(plural)
        if case == Case.ACCUSATIVE:
            return self.accusative(plural)
        if case == Case.GENITIVE:
            return self.genitive(plural)
        else:  # Case.DATIVE:
            return self.dative(plural)
