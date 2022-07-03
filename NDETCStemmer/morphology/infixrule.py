import re

"""
    =============================================================
    INFIX 1
    =============================================================
    Infix 1: (w)-el-(ord) -> word

    example: gelembung -> gembung
             pelatuk -> patuk
             selidik -> sidik
             telunjuk -> tunjuk 

"""


def infix1_rule(word_candidate):
    for keys in word_candidate:
        matches = re.match(r'(.*)el(.*)$', word_candidate[keys][0])
        if matches:
            combine = (matches.group(1)) + (matches.group(2))
            if len(combine) > 2 and combine not in word_candidate[keys]:
                word_candidate[keys].append(combine)
    return word_candidate


"""

def infix1_rule(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'(.*)el(.*)$', word_candidate[keys][i])
            if matches:
                combine = (matches.group(1)) + (matches.group(2))
                if len(combine) > 2 and combine not in word_candidate[keys]:
                    word_candidate[keys].append(combine)
    return word_candidate

"""

"""
    =============================================================
    INFIX 2
    =============================================================
    Infix 2: (w)-em-(ord) -> word

    example: pemerintah -> perintah
             jemari -> jari
             kemuning -> kuning
             temali -> tali
             temurun -> turun
             gemilang -> gilang
             gemuruh -> guruh
             gemetar -> getar       

"""
"""
def infix2_rule(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'(.*)em(.*)$', word_candidate[keys][i])
            if matches:
                combine = (matches.group(1)) + (matches.group(2))
                if len(combine) > 2 and combine not in word_candidate[keys]:
                    word_candidate[keys].append(combine)
    return word_candidate
"""


def infix2_rule(word_candidate):
    for keys in word_candidate:
        matches = re.match(r'(.*)em(.*)$', word_candidate[keys][0])
        if matches:
            combine = (matches.group(1)) + (matches.group(2))
            if len(combine) > 2 and combine not in word_candidate[keys]:
                word_candidate[keys].append(combine)
    return word_candidate


"""
    =============================================================
    INFIX 3
    =============================================================
    Infix 3: (w)-er-(ord) -> word

    example: serabut -> sabut
             seruling -> suling
             gerigi -> gigi     
"""


def infix3_rule(word_candidate):
    for keys in word_candidate:
        matches = re.match(r'(.*)er(.*)$', word_candidate[keys][0])
        if matches:
            combine = (matches.group(1)) + (matches.group(2))
            if len(combine) > 2 and combine not in word_candidate[keys]:
                word_candidate[keys].append(combine)
    return word_candidate


"""

def infix3_rule(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'(.*)er(.*)$', word_candidate[keys][i])
            if matches:
                combine = (matches.group(1)) + (matches.group(2))
                if len(combine) > 2 and combine not in word_candidate[keys]:
                    word_candidate[keys].append(combine)
    return word_candidate

"""

"""
    =============================================================
    INFIX 4
    =============================================================
    Infix 4: (w)-in-(ord) -> word

    example: kinerja -> kerja
             sinambung -> sambung
             tinambah -> tambah 
"""


def infix4_rule(word_candidate):
    for keys in word_candidate:
        matches = re.match(r'(.*)in(.*)$', word_candidate[keys][0])
        if matches:
            combine = (matches.group(1)) + (matches.group(2))
            if len(combine) > 2 and combine not in word_candidate[keys]:
                word_candidate[keys].append(combine)
    return word_candidate


"""
def infix4_rule(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'(.*)in(.*)$', word_candidate[keys][i])
            if matches:
                combine = (matches.group(1)) + (matches.group(2))
                if len(combine) > 2 and combine not in word_candidate[keys]:
                    word_candidate[keys].append(combine)
    return word_candidate
"""

