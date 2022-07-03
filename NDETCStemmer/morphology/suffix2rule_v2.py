from NDETCStemmer.morphology.validsuffixprefix import *


def suffix2e_rule_v2(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches_an = re.match(r'^(.*)an$', word_candidate[keys][i])
            matches_kan = re.match(r'^(.*)kan$', word_candidate[keys][i])
            matches_valid_ps_kan = is_valid_prefixsuffix_kan(word_candidate[keys][i])
            matches_valid_ps_an = is_valid_prefixsuffix_an(word_candidate[keys][i])
            matches_i = re.match(r'^(.*)i$', word_candidate[keys][i])
            if matches_an:               
                if matches_kan:                  
                    if matches_valid_ps_kan:
                        if len(matches_kan.group(1)) > 2 and matches_kan.group(1) not in word_candidate[keys]:
                            word_candidate[keys].append(matches_kan.group(1))       # mengenakan -> mengena, mengenakkan -> mengenak
                            matches_an_2 = re.match(r'^(.*)an$', matches_kan.group(1))
                            if matches_an_2:
                                if len(matches_an_2.group(1)) > 2 and matches_an_2.group(1) not in word_candidate[keys]:
                                    word_candidate[keys].append(matches_an_2.group(1)) # memperadilankan -> peradil, pelankan -> pel (?)
                            # if matches_an:
                            #    if len(matches_an.group(1)) > 2 and matches_an.group(1) not in word_candidate[keys]:
                            #        word_candidate[keys].append(matches_an.group(1)) # teriakan -> teriak
                            if matches_valid_ps_an:
                                if len(matches_an.group(1)) > 2 and matches_an.group(1) not in word_candidate[keys]:
                                    word_candidate[keys].append(matches_an.group(1))        # perbaikan - > perbaik
                    elif matches_valid_ps_an:
                        if len(matches_an.group(1)) > 2 and matches_an.group(1) not in word_candidate[keys]:
                            word_candidate[keys].append(matches_an.group(1))    # kerusakan -> kerusak
                            # matches_ke_kan = re.match(r'^ke(.*)$', matches_kan.group(1))
                            # matches_te_an = re.match(r'^te(.*)an$', matches_an.group(1))
                            # if len(matches_ke_kan.group(1)) < 4 and matches_ke_kan.group(1) not in word_candidate[keys]:
                            #    word_candidate[keys].append('ke'+ matches_ke_kan.group(1))  # kerjakan -> kerja
                            # if len(matches_te_an.group(1)) < 4 and matches_te_an.group(1) not in word_candidate[keys]:
                            #    word_candidate[keys].append('te'+ matches_te_an.group(1))  # teriakan-> teriak
                    elif matches_kan:
                        if len(matches_kan.group(1)) > 2 and matches_kan.group(1) not in word_candidate[keys]:
                           word_candidate[keys].append(matches_kan.group(1))     # bacakan -> baca, tebalkan -> tebal
                        if len(matches_an.group(1)) > 2 and matches_an.group(1) not in word_candidate[keys]:
                            matches_vk = re.match(r'^(.*)[bcdfghjklmnpqrstvwx]k$', matches_an.group(1))     # periksa huruf akhir tidak vokal+k
                            if not matches_vk:
                                word_candidate[keys].append(matches_an.group(1))     # tusukan-> tusuk, bacakan -> bacak
                elif matches_an:
                    if len(matches_an.group(1)) > 2 and matches_an.group(1) not in word_candidate[keys]:
                        word_candidate[keys].append(matches_an.group(1))        # permainan -> permain
            elif matches_i:
                valid_prefixsuffix_i = is_valid_prefixsuffix_i(word_candidate[keys][i])
                if valid_prefixsuffix_i:
                    if len(matches_i.group(1)) > 2 and matches_i.group(1) not in word_candidate[keys]:
                        word_candidate[keys].append(matches_i.group(1))
                else:
                    if len(matches_i.group(1)) > 2 and matches_i.group(1) not in word_candidate[keys]:
                        word_candidate[keys].append(matches_i.group(1))
                        # matches_an = re.match(r'^(.*)an$', word_candidate[keys][i])
    return word_candidate


def suffix2d_rule_v2(word_candidate):
    for keys in word_candidate:
        for i in range(0, len(word_candidate[keys])):
            matches = re.match(r'^(.*)in$', word_candidate[keys][i])
            if matches:
                if len(matches.group(1)) > 2 and matches.group(1) not in word_candidate[keys]:
                        word_candidate[keys].append(matches.group(1))
    return word_candidate

