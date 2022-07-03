import re

"""
    =============================================================
    PREFIX RULE 6A
    =============================================================
    Rule 6a: terV -> ter-V
    example: terasing terusir terindah terelok
    terabai terisak terubah terolah teroke teronggok terurai
"""


def prefix6a_rule(word, word_candidate, keys):
    matches = re.match(r'^ter([aiueo].*)$', word)
    if matches:
        if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 6B
    =============================================================
    Rule 6b: terV -> te-RV
    example: terencana terangkum terasa teraba
"""


def prefix6b_rule(word, word_candidate, keys):
    matches = re.match(r'^ter([aiueo].*)$', word)
    if matches:
        if len('r'+ matches.group(1)) > 2 and ('r'+ matches.group(1)) not in word_candidate[keys]:
            word_candidate[keys].append('r'+ matches.group(1))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 7
    =============================================================
    Rule 7: terCerV -> ter-CerV where C != 'r'
    example: tergerak terberat terserah termerah terkeras terlerai
"""


def prefix7_rule(word, word_candidate, keys):
    matches = re.match(r'^ter([bcdfghjklmnpqstvwxyz])(er[aiueo].*)$', word)
    if matches:
        if len(matches.group(1) + matches.group(2)) > 2 and \
                (matches.group(1) + matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1) + matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 8
    =============================================================
    Rule 8: terCP -> ter-CP where C != 'r' and P != 'er'
    example: terpuruk terburuk terwaras terbuat
"""


def prefix8_rule(word, word_candidate, keys):
    matches = re.match(r'^ter([bcdfghjklmnpqrstvwxyz])(.*)$', word)
    if matches:
        if len(matches.group(1) + matches.group(2)) > 2 and \
                (matches.group(1) + matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1) + matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 9
    =============================================================
    Rule 9: teC1erC2 -> te-C1erC2 where C1 != 'r'
    example: teterbang
"""


def prefix9_rule(word, word_candidate, keys):
    matches = re.match(r'te([bcdfghjklmnpqstvwxyz])(er.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1) + matches.group(2))
    return word_candidate

