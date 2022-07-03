import re


"""
    =============================================================
    PREFIX RULE 10
    =============================================================
    Rule 10: me{l|r|w|y}V -> me-{l|r|w|y}V
    Example: melipat meringkas mewarnai meyakinkan
"""


def prefix10_rule(word, word_candidate, keys):
    matches = re.match(r'^me([l|r|w|y])([aiueo])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)+matches.group(3)) > 2 and \
                (matches.group(1)+matches.group(2)+matches.group(3)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2)+matches.group(3))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 11
    =============================================================
    Rule 11: mem{b|f|v} -> mem-{b|f|v} sastrawi
    Rule 11: mem{b|f|v|p} -> mem-{b|f|v|p} modified by bun
    example: membangun memfitnah memvonis memperoleh
"""


def prefix11_rule(word, word_candidate, keys):
    matches = re.match(r'^mem([bfvp])(.*)$', word)
    if matches:
        if len(matches.group(1) + matches.group(2)) > 2 and \
                (matches.group(1) + matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1) + matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 12
    =============================================================
    Rule 12: mempe -> mem-pe-           sastrawi
    Rule 12: mempe{r|l} -> mem-pe-      modified by ?
    example: memperbarui -> barui mempelajari -> ajari
    memperbodoh memperbanyak memperbudak
"""


def prefix12_rule(word, word_candidate, keys):
    matches = re.match(r'^mempe[r|l](.*)$', word)
    if matches:
        if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 13A
    =============================================================
    Rule 13a: memV -> me-mV                    
    example: meminum -> minum memakan -> makan
"""


def prefix13a_rule(word, word_candidate, keys):
    matches = re.match(r'mem([aiueo].*)$', word)
    if matches:
        if len('m'+ matches.group(1)) > 2 and 'm'+ matches.group(1) \
                not in word_candidate[keys]:
            word_candidate[keys].append('m'+ matches.group(1))
    return word_candidate

"""
    =============================================================
    PREFIX RULE 13B
    =============================================================
    Rule 13b: mem{rV|V} -> me-p{rV|V}          
    example: memukul -> pukul memroses -> proses
"""


def prefix13b_rule(word, word_candidate, keys):
    matches = re.match(r'^mem(r?[aiueo])(.*)$', word)
    if matches:
        if len('p'+ matches.group(1) + matches.group(2)) > 2 and \
                ('p'+ matches.group(1) + matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('p'+ matches.group(1) + matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 14
    =============================================================
    Rule 14: men{c|d|j|s|t|z} -> men-{c|d|j|s|t|z}
    example: mencinta -> men-cinta mendua -> men-dua
    menjauh -> men-jauh menziarahi -> men-ziarahi mensyarat -> men-syarat *
"""


def prefix14_rule(word, word_candidate, keys):
    matches = re.match(r'^men([cdjstz])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 15A
    =============================================================
    Rule 15a: men{V} -> me-n{V}
    example: menuklir -> me-nuklir
"""


def prefix15a_rule(word, word_candidate, keys):
    matches = re.match(r'^men([aiueo])(.*)$', word)
    if matches:
        if len('n'+ matches.group(1)+matches.group(2)) > 2 and \
                ('n'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('n'+ matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 15B
    =============================================================
    Rule 15b: men{V} -> me-t{V}
    example: menangkap -> me-tangkap
"""


def prefix15b_rule(word, word_candidate, keys):
    matches = re.match(r'^men([aiueo])(.*)$', word)
    if matches:
        if len('t'+ matches.group(1)+matches.group(2)) > 2 and \
                ('t'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('t'+ matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 16
    =============================================================
    Rule 19: meng{g|h|q|kh} -> meng-{g|h|q|kh}
    example: menggila -> gila menghajar -> hajar mengqasar -> qasar
"""


def prefix16_rule(word, word_candidate, keys):
    matches = re.match(r'^meng([g|h|q|k])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 16 V2
    =============================================================
    Rule 16 V2: meng{g|h|q|kh} -> meng-{g|h|q|kh}
    example: menggila -> gila menghajar -> hajar mengqasar -> qasar

def prefix16_rule_v2(word, word_candidate, keys):
    matches = re.match(r'^meng([g|h|q|k])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
            (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate

"""

"""
    =============================================================
    PREFIX RULE 17A
    =============================================================
    Rule 17a: mengV -> meng-V
    example: mengudara -> meng-udara
"""


def prefix17a_rule(word, word_candidate, keys):
    matches = re.match(r'^meng([aiueo])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)) > 2 and \
                (matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2))
    return word_candidate

"""
    =============================================================
    PREFIX RULE 17B
    =============================================================
    Rule 17b: mengV -> meng-kV
    example: mengupas -> meng-kupas
"""


def prefix17b_rule(word, word_candidate, keys):
    matches = re.match(r'^meng([aiueo])(.*)$', word)
    if matches:
        if len('k'+ matches.group(1)+matches.group(2)) > 2 and \
                ('k'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('k'+ matches.group(1)+matches.group(2))
    return word_candidate

"""
    =============================================================
    PREFIX RULE 17C
    =============================================================
    Rule 17c: mengV -> meng-V- where V = 'e'
    example: mengesa -> meng-esa
             mengebom -> meng-ebom
"""


def prefix17c_rule(word, word_candidate, keys):
    matches = re.match(r'^menge(.*)$', word)
    if matches:
        if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 17D
    =============================================================
    Rule 17d: mengV -> me-ngV
    example:  mengeri -> ngeri    note: periksa ulang 
"""


def prefix17d_rule(word, word_candidate, keys):
    matches = re.match(r'^meng(.*)$', word)
    if matches:
        if len('ng'+ matches.group(1)) > 2 and ('ng'+ matches.group(1)) not in word_candidate[keys]:\
            word_candidate[keys].append('ng' + matches.group(1))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 18A
    =============================================================
    Rule 18a: menyV -> me-nyV
    example: menyanyi -> me-nyanyi
"""


def prefix18a_rule(word, word_candidate, keys):
    matches = re.match(r'^meny([aiueo])(.*)$', word)
    if matches:
        if len('ny'+ matches.group(1)+matches.group(2)) > 2 and \
                ('ny'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('ny'+ matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 18B
    =============================================================
    Rule 18b: menyV -> meny-sV
    example: menyuara -> meny-suara
"""


def prefix18b_rule(word, word_candidate, keys):
    matches = re.match(r'^meny([aiueo])(.*)$', word)
    if matches:
        if len('s'+ matches.group(1)+matches.group(2)) > 2 and \
                ('s'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('s'+ matches.group(1)+matches.group(2))
        # if len('c'+ matches.group(1)+matches.group(2)) > 2 and \
        #    ('c'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
        #    word_candidate[keys].append('c'+ matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 19
    =============================================================
    Rule 19: mempV -> mem-pV where V != 'e'
    example: mempopulerkan -> populerkan
"""


def prefix19_rule(word, word_candidate, keys):
    matches = re.match(r'^memp([aiuo])(.*)$', word)
    if matches:
        if len('p'+ matches.group(1)+matches.group(2)) > 2 and \
                ('p'+ matches.group(1)+matches.group(2)) not in word_candidate[keys]:
            word_candidate[keys].append('p'+ matches.group(1)+matches.group(2))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 19 B
    =============================================================
    Rule 19b: mersatu -> satu
    example: 
"""


def prefix19b_rule(word, word_candidate, keys):
    matches = re.match(r'^mer(.*)$', word)
    if matches:
        if len(matches.group(1)) > 2 and \
                matches.group(1)not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1))
    return word_candidate

