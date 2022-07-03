import re

"""
    =============================================================
    PREFIX RULE 20
    =============================================================
    Rule 20: pe{w|y}V -> pe-{w|y}V
    example: pewarna -> pe-warna peyoga -> pe-yoga
"""


def prefix20_rule(word, word_candidate, keys):
    matches = re.match(r'^pe([w|y])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 21A
    =============================================================
    Rule 21a: perV -> per-V
    example: peradil -> per-adil
"""


def prefix21a_rule(word, word_candidate, keys):
    matches = re.match(r'^per([aiueo])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 21B
    =============================================================
    Rule 21b: perV -> pe-rV
    example: perumah -> pe-rumah
"""


def prefix21b_rule(word, word_candidate, keys):
    matches = re.match(r'^pe(r[aiueo])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 22
    =============================================================
    Rule 22: penyV -> pe-nyV
    example: penyanyi -> pe-nyanyi
             penyala -> pe-nyala
             penyalang -> pe-nyala
             nyali
"""


def prefix22_rule(word, word_candidate, keys):
    matches = re.match(r'^peny([aeiou])(.*)$', word)
    if matches:
        if len('ny' + matches.group(1) + matches.group(2)) > 2 \
                and 'ny' + matches.group(1) + matches.group(2) not in word_candidate[keys]:
            word_candidate[keys].append('ny'+ matches.group(1) + matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 23
    =============================================================
    Rule 23: perCAP -> per-CAP where C != 'r' and P != 'er'
    example: permuka -> per-muka
"""


def prefix23_rule(word, word_candidate, keys):
    matches = re.match(r'^per([bcdfghjklmnpqstvwxyz])([aiueoy].*)$', word) #aiueoy y for ny
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 24
    =============================================================
    Rule 24: perCAerV -> per-CAerV where C != 'r'
    example: perdaerah -> daerah
"""


def prefix24_rule(word, word_candidate, keys):
    matches = re.match(r'^per([bcdfghjklmnpqstvwxyz])([aiueo]er.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 25
    =============================================================
    Rule 25: pem{b|f|v} -> pem-{b|f|v}
    example: pembangun -> bangun pemfitnah -> fitnah
    pemvonis -> vonis
"""


def prefix25_rule(word, word_candidate, keys):
    matches = re.match(r'^pem([b|f|v])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 26A
    =============================================================
    Rule 26a: pem-V -> pe-mV
    example: peminum pemakan
"""


def prefix26a_rule(word, word_candidate, keys):
    matches = re.match(r'^pem([aiueo])(.*)$', word)
    if matches:
        if len('m' + matches.group(1)+ matches.group(2)) > 2 and \
                ('m' + matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('m'+ matches.group(1)+ matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 26B
    =============================================================
    Rule 26b: pem{rV|V} -> pe-p{rV|V}
    example: pemukul -> pe-pukul 
"""


def prefix26b_rule(word, word_candidate, keys):
    matches = re.match(r'^pem([r]?[aiueo])(.*)$', word)
    if matches:
        if len('p'+ matches.group(1)+matches.group(2)) > 2 and \
                ('p'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('p'+ matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 27
    =============================================================
    Rule 27: pen{c|d|j|z} -> pen-{c|d|j|z}
    example: pencinta -> pen-cinta pendahulu -> pen-dahulu
    penjarah -> pen-jarah penziarah -> pen-ziarah
"""


def prefix27_rule(word, word_candidate, keys):
    matches = re.match(r'^pen([c|d|j|z])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 28A
    =============================================================
    Rule 28a: pen{V} -> pe-n{V}
    example: penasihat -> pe-nasihat
"""


def prefix28a_rule(word, word_candidate, keys):
    matches = re.match(r'^pen([aiueo])(.*)$', word)
    if matches:
        if len('n'+ matches.group(1)+matches.group(2)) > 2 and \
                ('n'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('n'+ matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 28B
    =============================================================
    Rule 28b: pen{V} -> pe-t{V}
    example: penangkap -> pe-tangkap
"""


def prefix28b_rule(word, word_candidate, keys):
    matches = re.match(r'^pen([aiueo])(.*)$', word)
    if matches:
        if len('t'+ matches.group(1)+matches.group(2)) > 2 and \
                ('t'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('t'+ matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 29
    =============================================================
    Rule 29: peng{k|g|h|q} -> peng-{k|g|h|q|l}
    example: penggila -> peng-gila penghajar -> peng-hajar
             pengqassar -> peng-qassar penglihat -> lihat
             pengkhianat -> khianat
"""


def prefix29_rule(word, word_candidate, keys):
    matches = re.match(r'^peng([k|g|h|q|l])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 30A
    =============================================================
    Rule 30a: pengV -> peng-V
    example: pengudara -> peng-udara
"""


def prefix30a_rule(word, word_candidate, keys):
    matches = re.match(r'^peng([aiueo])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 30B
    =============================================================
    Rule 30b: pengV -> peng-kV
    example: pengupas -> peng-kupas
"""


def prefix30b_rule(word, word_candidate, keys):
    matches = re.match(r'^peng([aiueo])(.*)$', word)
    if matches:
        if len('k'+ matches.group(1)+matches.group(2)) > 2 and \
                ('k'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('k'+ matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 31
    =============================================================
    Rule 31: penyV -> peny-sV
    example: penyuara -> peny-suara
"""

def prefix31_rule(word, word_candidate, keys):
    matches = re.match(r'^peny([aiueo])(.*)$', word)
    if matches:
        if len('s'+ matches.group(1)+matches.group(2)) > 2 and \
                ('s'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('s'+ matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 32
    =============================================================
    Rule 32: pelV -> pe-lV except pelajar -> ajar
    example: pelajar -> ajar pelabuhan -> labuhan
"""


def prefix32_rule(word, word_candidate, keys):
    if word == 'pelajar':
        word_candidate[keys].append('ajar')
    else:
        matches = re.match(r'^pel([aiueo])(.*)$', word)
        if matches:
            if len('l'+ matches.group(1)+matches.group(2)) > 2 and \
                    ('l'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
                word_candidate[keys].append('l'+ matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 33
    =============================================================
    Rule 33: per{sy}-> per-sy
    example: persyaratan -> syarat
"""


def prefix33_rule(word, word_candidate, keys):
    matches = re.match(r'^per([sy])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 34
    =============================================================
    Rule 34: peCP -> pe-CP where C != {r|w|y|l|m|n} and P != 'er'
    example: petarung -> pe-tarung
"""


def prefix34_rule(word, word_candidate, keys):
    matches = re.match(r'^pe([bcdfghjklpqstvwxz])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 35
    =============================================================
    Rule 35: terC1erC2 -> ter-C1erC2 where C1 != 'r'
    example: terpercaya -> percaya
"""


def prefix35_rule(word, word_candidate, keys):
    matches = re.match(r'^ter([bcdfghjklmpqstvwxyz])(er.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 36
    =============================================================
    Rule 36: peC1erC2 -> pe-C1erC2 where C1 != {r|w|y|l|m|n}
    example: pekerja -> pe-kerja peserta -> serta
"""


def prefix36_rule(word, word_candidate, keys):
    matches = re.match(r'^pe([bcdfghjkpqrstvxz])(er[bcdfghjklmnpqrstvwxyz].*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 37
    =============================================================
    Rule 37: se-word -> word
    example: selangkah ->  se-langkah
"""


def prefix37_rule(word, word_candidate, keys):
    matches = re.match(r'^se([a-z])(.*)$', word)
    if matches:
        if len(matches.group(1)+ matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate

