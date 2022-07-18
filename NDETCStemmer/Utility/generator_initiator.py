from NDETCStemmer.morphology import *
from NDETCStemmer.ListRules import ListRules


def init(generator_rules):
	generator_rules.add('particle',ListRules([particle_rule]))
	generator_rules.add('suffix',ListRules([suffix2e_rule_v2]))
	generator_rules.add('possessive_pronoun',ListRules([possessive_pronoun_rule]))
	generator_rules.add('reduplication',ListRules([reduplication1_rule,reduplication1_rule,reduplication2_rule]))
	generator_rules.add('infix',ListRules([infix1_rule,infix2_rule,infix3_rule,infix4_rule]))
	generator_rules.add('prefix_ku',ListRules([prefix41_rule]))
	generator_rules.add('prefix_kau',ListRules([prefix40_rule]))
	generator_rules.add('prefix_se',ListRules([prefix37_rule]))
	generator_rules.add('prefix_ke',ListRules([prefix38_rule]))
	generator_rules.add('simulfix_ng',ListRules([simulfix1_rule,simulfix4_rule,simulfix5_rule]))
	generator_rules.add('simulfik_ny',ListRules([simulfix2_rule,simulfix3_rule]))
	generator_rules.add('prefix_di',ListRules([prefix39a_rule,prefix39b_rule]))
	generator_rules.add('prefix_te',ListRules([prefix6a_rule,prefix6b_rule,prefix7_rule,prefix8_rule,prefix9_rule]))
	generator_rules.add('prefix_be',ListRules([prefix1a_rule,prefix1b_rule,prefix2_rule,prefix3_rule,
	prefix4_rule,prefix5_rule,prefix5b_rule]))
	generator_rules.add('prefix_me',ListRules([prefix10_rule,prefix11_rule,prefix12_rule,prefix13a_rule,
	prefix13b_rule,prefix14_rule,prefix15a_rule,prefix15b_rule,prefix16_rule,prefix17a_rule,prefix17b_rule,
	prefix17c_rule,prefix17d_rule,prefix18a_rule,prefix18b_rule,prefix19_rule,prefix19b_rule]))
	generator_rules.add('prefix_pe',ListRules([prefix20_rule,prefix21a_rule,prefix21b_rule,prefix22_rule,
	prefix23_rule,prefix24_rule,prefix25_rule,prefix26a_rule,prefix26b_rule,prefix27_rule,prefix28a_rule,
	prefix28b_rule,prefix29_rule,prefix30a_rule,prefix30b_rule,prefix31_rule,prefix32_rule,prefix33_rule,
	prefix34_rule,prefix35_rule,prefix36_rule]))

	return generator_rules