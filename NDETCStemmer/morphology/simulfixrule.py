import re

"""
    =============================================================
    SIMULFIX RULE 1
    =============================================================
    Rule 1: ngeV -> V
    
    example: ngebakso -> bakso 
             ngelawak -> lawak 
             ngerampok -> rampok
             ngerusak -> rusak
             ngetawain -> tawa
             ngegulai -> gulai     

"""


def simulfix1_rule(word, word_candidate, keys):
    matches = re.match(r'^nge(.*)$', word)
    if matches:
        if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1))
    return word_candidate


"""
    =============================================================
    SIMULFIX RULE 2
    =============================================================
    Rule 1: ny+v -> s+v

    example: nyoto -> soto 
             nyablon -> sablon 
             nyambal -> sambal
             nyambel -> nyambel
             nyimak -> simak
             nyikut -> sikut

"""


def simulfix2_rule(word, word_candidate, keys):
    matches = re.match(r'^ny([aiueo].*)$', word)
    if matches:
        if len('s'+ matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
            word_candidate[keys].append('s'+ matches.group(1))
    return word_candidate


"""
    =============================================================
    SIMULFIX RULE 3
    =============================================================
    Rule 1: ny+v -> s+v

    example: nyoba -> coba 
             nyatut -> catut 
             nyium -> cium
             nyontohin -> contoh

"""


def simulfix3_rule(word, word_candidate, keys):
    matches = re.match(r'^ny([aiueo].*)$', word)
    if matches:
        if len('c'+ matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
            word_candidate[keys].append('c'+ matches.group(1))
    return word_candidate


"""
    =============================================================
    SIMULFIX RULE 4
    =============================================================
    Rule 4: ng{aiueo} -> k{aiueo}

    example: ngopi -> kopi
             ngumpul -> kumpul
             ngotak -> kotak
             ngebut -> kebut
"""


def simulfix4_rule(word, word_candidate, keys):
    matches = re.match(r'^ng([aiueo].*)$', word)
    if matches:
        if len('k' + matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
            word_candidate[keys].append('k' + matches.group(1))
    return word_candidate


"""
    =============================================================
    SIMULFIX RULE 5
    =============================================================
    Rule 5: ng{aiueo} -> {aiueo}

    example: ngobrol -> obrol
             ngasal -> asal
             ngiri -> iri
             ngundang -> undang             
             
"""


def simulfix5_rule(word, word_candidate, keys):
    matches = re.match(r'^ng([aiueo].*)$', word)
    if matches:
        if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
            word_candidate[keys].append(matches.group(1))
    return word_candidate

