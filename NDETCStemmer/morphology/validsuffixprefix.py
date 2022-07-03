import re


def is_valid_prefixsuffix_kan(word):
    rule1 = re.compile(r'^me(.*)kan$')  # me-ngata-kan -> mengata
    # rule2 = re.compile(r'^per(.*)kan$') # per-main-kan -> permain, pelankan -> pelankan
    rule2 = re.compile(r'^pe(.*)kan$') # per-main-kan -> permain, pelan-kan -> pelan
    # rule3 = re.compile(r'^ber(.*)kan$') # ber-dasar-kan -> berdasar, bengkokkan -> bengkokkan
    rule3 = re.compile(r'^be(.*)kan$') # ber-dasar-kan -> berdasar, bengkok-kan -> bengkok
    # rule4 = re.compile(r'^ter(.*)kan$') # ter-kumpul-kan -> terkumpul, teriakan -> teria (?)
    rule4 = re.compile(r'^te(.*)kan$') # ter-kumpul-kan -> terkumpul, teriakan -> teria (?)
    rule5 = re.compile(r'^di(.*)kan$')  # di-kata-kan -> dikata
    rule6 = re.compile(r'^ke(.*)kan$')  # NEW  kerjakan -> kerja, kembalikan -> kembali

    if re.match(rule1, word) or \
        re.match(rule2, word) or \
        re.match(rule3, word) or \
        re.match(rule4, word) or \
        re.match(rule5, word) or \
        re.match(rule6, word):          # NEW
        return True
    else:
        return False


def is_valid_prefixsuffix_an(word):
    rule1 = re.compile(r'^pe(.*)an$')  # per-main-an ->  permain, permain-kan -> permaink
    rule2 = re.compile(r'^be(.*)an$')  # be-pergi-an -> bepergi, belanja-kan -> belanjak
    rule3 = re.compile(r'^ke(.*)an$')  # ke-jatuh-an -> kejatuh, kembalikan -> kembalik
                                       # kerjakan -> kerjak
    rule4 = re.compile(r'^te(.*)an$')   # NEW
    rule5 = re.compile(r'^di(.*)an$')   # NEW
    if re.match(rule1, word) or \
            re.match(rule2, word) or \
            re.match(rule3, word) or \
            re.match(rule4, word) or \
            re.match(rule5, word):      # NEW
        return True
    else:
        return False


def is_valid_prefixsuffix_i(word):
    rule1 = re.compile(r'^me(.*)i$')  # mem-bau-i
    rule2 = re.compile(r'^per(.*)i$') # per-baik-i
    rule3 = re.compile(r'^di(.*)i$')  # di-datang-i
    rule4 = re.compile(r'^ter(.*)i$') # ter-saing-i
    # rule5 = re.compile(r'^ke(.*)i$') # ke-saing-i)
    if re.match(rule1, word) or \
            re.match(rule2, word) or \
            re.match(rule3, word) or \
            re.match(rule4, word):
            # re.match(rule5, word):
        return True
    else:
        return False

