import re

"""
    =============================================================
    PREFIX RULE 1A
    =============================================================
    Rule 1a: berV -> ber-V
    
    example: berA: beradab -> adab 
             berI: berizin -> izin 
             berU: berusaha -> usaha
             berE: beredar -> edar
             berO: berotak -> otak 
            
             beribadah berijazah berinsting berikan* beruang* berobat
"""


def prefix1a_rule(word, word_candidate, keys):
    matches = re.match(r'^ber([aiueo].*)$', word)
    if matches:
        if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 1B
    =============================================================
    Rule 1b: berV -> be-rV
    example: berA: berambut -> rambut
             berI: berinduk -> induk 
             berU: berusuk -> rusuk
             berE: berenang -> renang
             berO: berongga -> rongga
             
             berencana berakit berantai berusuk beratus
"""


def prefix1b_rule(word, word_candidate, keys):
    matches = re.match(r'^ber([aiueo].*)$', word)
    if matches:
        if len('r'+ matches.group(1)) > 2 and ('r'+ matches.group(1)) not in word_candidate[keys]:
            word_candidate[keys].append('r'+ matches.group(1))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 2
    =============================================================
    Rule 2: berCAP -> ber-CAP where C != 'r' and P != 'er'
    C = consonant A = Anything letter P = shortword fragment
    example: berbag: berbagai -> bagai
             berbua: berbuah -> berbuah
"""


def prefix2_rule(word, word_candidate, keys):
    matches = re.match(r'ber([bcdfghjklmnpqrstvwxyz])([a-z])(.*)', word)
    if matches:
        if len(matches.group(1)+matches.group(2)+matches.group(3)) > 2 and \
                (matches.group(1)+matches.group(2)+matches.group(3)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2)+matches.group(3))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 3
    =============================================================
    Rule 3: berCAerV -> ber-CAerV where C != 'r'
    example: berdaerah -> daerah
"""


def prefix3_rule(word, word_candidate, keys):
    matches = re.match(r'ber([bcdfghjklmnpqrstvwxyz])([a-z])er([aiueo])(.*)', word)
    if matches:
        if len((matches.group(1) + matches.group(2) + 'er' + matches.group(3) + matches.group(4)))>2 and \
                (matches.group(1)+matches.group(2)+ 'er' + matches.group(3) + matches.group(4)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1) + matches.group(2) + 'er' + matches.group(3) + matches.group(4))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 4
    =============================================================
    Rule 4: belajar -> bel-ajar
    example: belajar -> ajar
"""


def prefix4_rule(word, word_candidate, keys):
    if word == 'belajar' and 'ajar' not in word_candidate[keys]:
        word_candidate[keys].append("ajar")
    if word == 'beberapa' and 'berapa' not in word_candidate[keys]:
        word_candidate[keys].append("berapa")
    return word_candidate


"""
    =============================================================
    PREFIX RULE 5
    =============================================================
    Rule 5: beC1erC2 -> be-C1erC2 where C1 != 'r' '''
    example: bekerja -> be-kerja
"""


def prefix5_rule(word, word_candidate, keys):
    matches = re.match(r'^be([bcdfghjklmnpqstvwxyz])(er[bcdfghjklmnpqrstvwxyz])(.*)$', word)
    if matches:
        if len(matches.group(1)+matches.group(2)+matches.group(3))>2 and \
                (matches.group(1)+matches.group(2)+matches.group(3)) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1)+matches.group(2)+matches.group(3))
    return word_candidate


"""
    =============================================================
    PREFIX RULE 5b
    =============================================================
    Rule 5b: bersi-word -> word 
    example: bersikeras -> keras
             bersikukuh -> kukuh
             bersitegang -> tegang
             bersimaharajalela -> maharajalela
             bersimbah -> mbah      # error
"""


def prefix5b_rule(word, word_candidate, keys):
    matches = re.match(r'^bersi(.*)$', word)
    if matches:
        if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1))
    return word_candidate
