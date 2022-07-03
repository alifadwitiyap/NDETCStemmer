import re

"""
    =============================================================
    REDUPLICATION 1
    =============================================================
    Reduplication 1: word-word -> word

    example: buku-buku -> buku
             kumpul-kumpul -> kumpul
             mondar-mandir -> mondar, mandir 
             pontang-panting -> pontang, panting
             mengagak-agak

"""


def reduplication1_rule(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'(.*)-(.*)$', word_candidate[keys][i])
            if matches:
                if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
                    word_candidate[keys].append(matches.group(1))
                if len(matches.group(2)) > 2 and matches.group(2) not in word_candidate[keys]:
                    word_candidate[keys].append(matches.group(2))
                if len(matches.group(1)) <= 2 and matches.group(2) not in word_candidate[keys]:
                    word_candidate[keys].append(matches.group(2))
    return word_candidate


"""
    =============================================================
    REDUPLICATION 2
    =============================================================
    Reduplication 2: [bdtprsl]e([bdtprsl].*)an -> ([bdtprsl].*)

    example: dedaunan -> daun
             tetumbuhan -> tumbuh
             pepohonan -> pohon
             reramuan -> ramu
             rerumputan -> rumput 
             bebajuan -> baju
             reruntuhan -> runtuh
"""


def reduplication2_rule(word_candidate):
    matches_2 = False
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            # matches = re.match(r'[bdtprsl]e([bdtprsl].*)an$', word_candidate[keys][i])
            matches = re.match(r'[bdtprsl]e([bdtprsl].*)an$', word_candidate[keys][i])
            if len(word_candidate[keys][i]) >= 5:
                if word_candidate[keys][i][0] ==  word_candidate[keys][i][2]:
                    matches_2 = True
            if matches and matches_2:
                if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
                    word_candidate[keys].append(matches.group(1))
    return word_candidate


"""
    =============================================================
    REDUPLICATION 3
    =============================================================
    Reduplication 3: [bdtprsl]e([bdtprsl].*) 

    example: lelaki -> laki
             reruntuh -> runtuh

"""


def reduplication3_rule(word_candidate):
    matches_2 = False
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'[bdtprsl]e([bdtprsl].*)$', word_candidate[keys][i])
            if len(word_candidate[keys][i]) >= 5:
                if  word_candidate[keys][i][0] ==  word_candidate[keys][i][2]:
                    matches_2 = True
            if matches and matches_2:
                if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
                    word_candidate[keys].append(matches.group(1))
    return word_candidate


"""
    =============================================================
    REDUPLICATION 4
    =============================================================
    Reduplication 4: word-ku/mu/nya -> word

    example: band-ku -> band
             band-nya -> band
             band-mu -> band
"""


def reduplication4_rule(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'(.*)-ku$', word_candidate[keys][i])
            if matches:
                if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
                   word_candidate[keys][1] = 'halo' # matches.group(1)
    return word_candidate


