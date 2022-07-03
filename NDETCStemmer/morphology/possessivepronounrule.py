import re

"""
    =============================================================
    POSSESIVE PRONOUN
    =============================================================
    Possesive Pronoun: word-ku|-mu|-nya -> word
    
    Example: word-ku: bukuku -> buku; memaku -> mema
             word-mu: kursimu -> kursi; meramu -> mera
             word-nya: rumahnya -> rumah; bertanya -> berta
"""


def possessive_pronoun_rule(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'^(.*)(ku|mu|nya)$', word_candidate[keys][i])
            if matches:
                if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
                    word_candidate[keys].append(matches.group(1))
    return word_candidate

