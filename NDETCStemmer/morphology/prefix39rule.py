import re

"""
    =============================================================
    PREFIX RULE 38
    =============================================================
    Rule 38: keC -> ke-C
    example: kebaikan -> baikan
"""


def prefix38_rule(word, word_candidate, keys):
    matches = re.match(r'^ke([abcdefghijklmnopqrstuvwxyz])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 39A
    =============================================================
    Rule 39a: diV -> di-V
    example: diambil -> di-ambil
"""


def prefix39a_rule(word, word_candidate, keys):
    matches = re.match(r'^di(.*)$', word)
    if matches:
        if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 39B
    =============================================================
    Rule 39b: diC -> di-C
    example: dibalas -> balas
"""


def prefix39b_rule(word, word_candidate, keys):
    matches = re.match(r'^di([aiueo])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 40
    =============================================================
    Rule 40:kauC -> kau-C
    example: kaubuka -> kau-buka
"""


def prefix40_rule(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'^kau([a-z])(.*)$', word_candidate[keys][i])
            if matches:
                if len(matches.group(1)+matches.group(2)) > 2 and \
                        (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
                    word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 41
    =============================================================
    Rule 41: kuC -> ku-C
    example: kubuka -> ku-buka
"""


def prefix41_rule(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'^ku(.*)$', word_candidate[keys][i])
            if matches:
                if len(matches.group(1)) > 2 and matches.group(1)  not in word_candidate[keys]:
                    word_candidate[keys].append(matches.group(1))
    return word_candidate

