import re


"""
    =============================================================
    PARTICLE
    =============================================================
    Particle checking: word-lah|tah|kah|pun -> word
    
    Example: word-lah: engkaulah -> engkau; menjumlah -> menjum
             word-tah: apatah -> apa; membantah -> memban
             word-kah: bukankah -> bukan; sedekah -> sede *dekah
             word-pun: biarpun -> biar; pengampun -> pengam
"""


def particle_rule(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'^(.*)(lah|tah|kah|pun)$', word_candidate[keys][i])
            if matches:
                if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
                    word_candidate[keys].append(matches.group(1))
    return word_candidate

