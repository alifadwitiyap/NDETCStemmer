from NDETCStemmer.RulesGenerator import RulesGenerator
from NDETCStemmer.Utility import generator_initiator
import re


class CandidateGenerator:
	def __init__(self, stemmer_input):
		self._word_candidate = dict()
		self._candidate_keys=0
		self._sub_candidate_keys1=''
		self._sub_candidate_keys2=''
		self._sub_candidate_keys3=''
		self._rules_generator=generator_initiator.init(RulesGenerator())

		for i in range(len(stemmer_input)):
			self._word_candidate[i] = [stemmer_input[i]]
		
	
	def generate(self):
		self._rules_generator.get('reduplication').execute(word_candidate=self._word_candidate)
		self._rules_generator.get('particle').execute(word_candidate=self._word_candidate)
		self._rules_generator.get('possessive_pronoun').execute(word_candidate=self._word_candidate)
		self._rules_generator.get('suffix').execute(word_candidate=self._word_candidate)
		self._rules_generator.get('prefix_ku').execute(word_candidate=self._word_candidate)
		self._rules_generator.get('prefix_kau').execute(word_candidate=self._word_candidate)

		for self._candidate_keys in self._word_candidate:
			for self._sub_candidate_keys1 in range(0, len(self._word_candidate[self._candidate_keys])):
				check_match={
					'matches_me':r'^me(.*)$',
					'matches_di':r'^di(.*)$',
					'matches_te':r'^te(.*)$',
					'matches_se':r'^se(.*)$',
					'matches_pe':r'^pe(.*)$',
					'matches_ke':r'^ke(.*)$',
					'matches_be':r'^be(.*)$',
					'matches_ng':r'^ng(.*)$',
					'matches_ny':r'^ny(.*)$',
				}

				for match_key in check_match:
					isMatch=re.match(check_match[match_key], self._word_candidate[self._candidate_keys][self._sub_candidate_keys1])
					if isMatch and match_key =='matches_me':
						self._matches_me()
						continue
					if isMatch and match_key =='matches_di':
						self._matches_di()
						continue
					if isMatch and match_key =='matches_te':
						self._matches_te()
						continue
					if isMatch and match_key =='matches_se':
						self._matches_se()
						continue
					if isMatch and match_key =='matches_pe':
						self._matches_pe()
						continue
					if isMatch and match_key =='matches_ke':
						self._matches_ke()
						continue
					if isMatch and match_key =='matches_be':
						self._matches_be()
						continue
					if isMatch and match_key =='matches_ng':
						self._matches_ng()
						continue
					if isMatch and match_key =='matches_ny':
						self._matches_ny()
						continue
		return self._word_candidate

	def _matches_me(self):
		self._rules_generator.get('prefix_me').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys1],keys=self._candidate_keys) # memakan
		for self._sub_candidate_keys2 in range(0, len(self._word_candidate[self._candidate_keys])):
			check_match={
					'matches_pe':r'^pe(.*)$',
					'matches_be':r'^be(.*)$',
					'matches_te':r'^te(.*)$',
					'matches_se':r'^se(.*)$',
				}
			for match_key in check_match:
				isMatch=re.match(check_match[match_key], self._word_candidate[self._candidate_keys][self._sub_candidate_keys2])
				if isMatch and match_key =='matches_pe':
					self._rules_generator.get('prefix_pe').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # memperlambat
					continue
				if isMatch and match_key =='matches_be':
					self._rules_generator.get('prefix_be').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # memberlakukan
					continue
				if isMatch and match_key =='matches_te':
					self._rules_generator.get('prefix_te').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # menertawakan
					continue
				if isMatch and match_key =='matches_se':
					self._rules_generator.get('prefix_se').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # menyerupai
					continue

	def _matches_di(self):
		self._rules_generator.get('prefix_di').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys1],keys=self._candidate_keys) # dimakan
		for self._sub_candidate_keys2 in range(0, len(self._word_candidate[self._candidate_keys])):
			check_match={
					'matches_pe':r'^pe(.*)$',
					'matches_be':r'^be(.*)$',
					'matches_ke':r'^ke(.*)$',
					'matches_te':r'^te(.*)$',
					'matches_me':r'^me(.*)$',
					'matches_se':r'^se(.*)$',
				}
			for match_key in check_match:
				isMatch=re.match(check_match[match_key], self._word_candidate[self._candidate_keys][self._sub_candidate_keys2])
				if isMatch and match_key =='matches_pe':
					self._rules_generator.get('prefix_pe').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # diperlambat
					continue
				if isMatch and match_key =='matches_be':
					self._rules_generator.get('prefix_be').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # diberlakukan
					continue
				if isMatch and match_key =='matches_ke':
					self._rules_generator.get('prefix_ke').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # dikehendaki, diketahui
					continue
				if isMatch and match_key =='matches_te':
					self._rules_generator.get('prefix_te').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # ditertawakan
					continue
				if isMatch and match_key =='matches_me':
					self._rules_generator.get('prefix_me').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # dimengerti
					continue
				if isMatch and match_key =='matches_se':
					self._rules_generator.get('prefix_se').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # diserupakan
					continue

	def _matches_te(self):
		self._rules_generator.get('prefix_te').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys1],keys=self._candidate_keys) # terbaca
		for self._sub_candidate_keys2 in range(0, len(self._word_candidate[self._candidate_keys])):
			check_match={
					'matches_pe':r'^pe(.*)$',
					'matches_be':r'^be(.*)$',
					'matches_ke':r'^ke(.*)$',
				}
			
			for match_key in check_match:
				isMatch=re.match(check_match[match_key], self._word_candidate[self._candidate_keys][self._sub_candidate_keys2])
				if isMatch and match_key =='matches_pe':
					self._rules_generator.get('prefix_pe').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # terperbaiki
					continue
				if isMatch and match_key =='matches_be':
					self._rules_generator.get('prefix_be').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # terberhentikan
					continue
				if isMatch and match_key =='matches_ke':
					self._rules_generator.get('prefix_ke').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # terkemuka
					continue

	def _matches_se(self):
		self._rules_generator.get('prefix_se').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys1],keys=self._candidate_keys) # setahun
		for self._sub_candidate_keys2 in range(0, len(self._word_candidate[self._candidate_keys])):
			check_match={
					'matches_pe':r'^pe(.*)$',
					'matches_be':r'^be(.*)$',
					'matches_se':r'^se(.*)$',
					'matches_ke':r'^ke(.*)$',
					'matches_me':r'^me(.*)$',
				}

			
			for match_key in check_match:
				isMatch=re.match(check_match[match_key], self._word_candidate[self._candidate_keys][self._sub_candidate_keys2])
				if isMatch and match_key =='matches_pe':
					self._rules_generator.get('prefix_pe').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # sependidikan
					for self._sub_candidate_keys3 in range(0, len(self._word_candidate[self._candidate_keys])):
						matches_ke = re.match(r'^ke(.*)$', self._word_candidate[self._candidate_keys][self._sub_candidate_keys3])
						matches_se = re.match(r'^se(.*)$', self._word_candidate[self._candidate_keys][self._sub_candidate_keys3])
						if matches_ke:
							self._rules_generator.get('prefix_ke').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys3],keys=self._candidate_keys) # sepengetahuan
							continue
						if matches_se:
							self._rules_generator.get('prefix_se').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys3],keys=self._candidate_keys) # sepersepuluh
							continue
					continue
				if isMatch and match_key =='matches_be':
					self._rules_generator.get('prefix_be').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # seberdudukan
					continue
				if isMatch and match_key =='matches_se':
					self._rules_generator.get('prefix_se').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # seseorang
					continue
				if isMatch and match_key =='matches_ke':
					self._rules_generator.get('prefix_ke').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # sekehendak
					continue
				if isMatch and match_key =='matches_me':
					self._rules_generator.get('prefix_me').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # semenyedihkam
					continue


	def _matches_be(self):
		self._rules_generator.get('prefix_be').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys1],keys=self._candidate_keys) # bertahan
		for self._sub_candidate_keys2 in range(0, len(self._word_candidate[self._candidate_keys])):
			check_match={
					'matches_ke':r'^ke(.*)$',
					'matches_se':r'^se(.*)$',
					'matches_pe':r'^pe(.*)$',
				}
			
			for match_key in check_match:
				isMatch=re.match(check_match[match_key], self._word_candidate[self._candidate_keys][self._sub_candidate_keys2])
				if isMatch and match_key =='matches_ke':
					self._rules_generator.get('prefix_ke').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # berkedudukan
					continue
				if isMatch and match_key =='matches_se':
					self._rules_generator.get('prefix_se').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # bersehaluan
					for self._sub_candidate_keys3 in range(0, len(self._word_candidate[self._candidate_keys])):
						matches_ke = re.match(r'^ke(.*)$', self._word_candidate[self._candidate_keys][self._sub_candidate_keys3])
						if matches_ke:
							self._rules_generator.get('prefix_ke').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys3],keys=self._candidate_keys) # bersekedudukan
							continue
					continue
				if isMatch and match_key =='matches_pe':
					self._rules_generator.get('prefix_pe').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # berpendidikan
					for self._sub_candidate_keys3 in range(0, len(self._word_candidate[self._candidate_keys])):
						matches_ke = re.match(r'^ke(.*)$', self._word_candidate[self._candidate_keys][self._sub_candidate_keys3])
						if matches_ke:
							self._rules_generator.get('prefix_ke').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys3],keys=self._candidate_keys) # berpengetahuan
							continue
					continue


	def _matches_pe(self):
		self._rules_generator.get('prefix_pe').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys1],keys=self._candidate_keys) # petinju
		for self._sub_candidate_keys2 in range(0, len(self._word_candidate[self._candidate_keys])):
			check_match={
					'matches_me':r'^me(.*)$',
					'matches_ke':r'^ke(.*)$',
					'matches_se':r'^se(.*)$',
					'matches_be':r'^be(.*)$',
				}
			
			for match_key in check_match:
				isMatch=re.match(check_match[match_key], self._word_candidate[self._candidate_keys][self._sub_candidate_keys2])
				if isMatch and match_key =='matches_me':
					self._rules_generator.get('prefix_me').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # pemerataan
					continue
				if isMatch and match_key =='matches_ke':
					self._rules_generator.get('prefix_ke').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # pengetahuan
					continue
				if isMatch and match_key =='matches_se':
					self._rules_generator.get('prefix_se').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # persemakmuran
					for self._sub_candidate_keys3 in range(0, len(self._word_candidate[self._candidate_keys])):
						matches_ke = re.match(r'^ke(.*)$', self._word_candidate[self._candidate_keys][self._sub_candidate_keys3])
						if matches_ke:
							self._rules_generator.get('prefix_ke').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys3],keys=self._candidate_keys) # persekemakmuran
							continue
					continue
				if isMatch and match_key =='matches_be':
					self._rules_generator.get('prefix_be').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # pemberhentian
					continue

	def _matches_ke(self):
		self._rules_generator.get('prefix_ke').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys1],keys=self._candidate_keys) # kejadian
		for self._sub_candidate_keys2 in range(0, len(self._word_candidate[self._candidate_keys])):
			check_match={
					'matches_te':r'^te(.*)$',
					'matches_be':r'^be(.*)$',
					'matches_se':r'^se(.*)$',
					'matches_pe':r'^pe(.*)$',
				}
			
			for match_key in check_match:
				isMatch=re.match(check_match[match_key], self._word_candidate[self._candidate_keys][self._sub_candidate_keys2])
				if isMatch and match_key =='matches_te':
					self._rules_generator.get('prefix_te').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # keterpurukan
					continue
				if isMatch and match_key =='matches_be':
					self._rules_generator.get('prefix_be').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # keberhasilan
					continue
				if isMatch and match_key =='matches_se':
					self._rules_generator.get('prefix_se').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # kesetimbangan
					continue
				if isMatch and match_key =='matches_pe':
					self._rules_generator.get('prefix_pe').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys2],keys=self._candidate_keys) # kepemudaan
					continue


	def _matches_ng(self):
		self._rules_generator.get('simulfix_ng').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys1],keys=self._candidate_keys) # ngebakso


	def _matches_ny(self):
		self._rules_generator.get('simulfik_ny').execute(word_candidate=self._word_candidate,word=self._word_candidate[self._candidate_keys][self._sub_candidate_keys1],keys=self._candidate_keys) # nyantai
