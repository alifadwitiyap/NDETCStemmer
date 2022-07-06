class BestWordSelector:
	def __init__(self,stemmer_input,model,root_word,rare_word,compound_word,weight,left_context,right_context,parent):
		self.stemmer_input=stemmer_input
		self.word_candidate={}
		self.model=model
		self.root_word=root_word
		self.rare_word=rare_word
		self.compound_word=compound_word
		self.weight=weight
		self.left_context=left_context
		self.right_context=right_context
		self.parent=parent
		self.best_word={}
		self.candidate_key=0
		self.sub_candidate_key=0

		for i in range(len(self.stemmer_input)):
			self.best_word[i]=[]


	def select(self,word_candidate={}):
		self.word_candidate=word_candidate
		for self.candidate_key in self.word_candidate:
			for self.sub_candidate_key in range(0, len(self.word_candidate[self.candidate_key])):
				self.rootWordFilter()
				self.compoundWordFilter()
			if len(self.best_word[self.candidate_key]) < 1:
				self.handleEmptyBestWord()
			if len(self.best_word[self.candidate_key]) > 1:
				self.rareWordFilter()
				self.modelFilter()

		return self.best_word

	def rootWordFilter(self):
		if self.word_candidate[self.candidate_key][self.sub_candidate_key] in self.root_word:
			self.best_word[self.candidate_key].append(self.word_candidate[self.candidate_key][self.sub_candidate_key])

	def compoundWordFilter(self):
		if self.word_candidate[self.candidate_key][self.sub_candidate_key] in self.compound_word.keys():
			self.best_word[self.candidate_key].append(self.compound_word[self.word_candidate[self.candidate_key][self.sub_candidate_key]])

	def rareWordFilter(self):
		for self.sub_candidate_key in range(0, len(self.word_candidate[self.candidate_key])):
			if self.word_candidate[self.candidate_key][self.sub_candidate_key] in self.rare_word:
				self.best_word[self.candidate_key].remove(self.word_candidate[self.candidate_key][self.sub_candidate_key])

	def handleEmptyBestWord(self):
		self.best_word[self.candidate_key].append(self.stemmer_input[self.candidate_key])

	def modelFilter(self):
		highest_score_word = self.modelEvaluateScore()
		self.best_word[self.candidate_key] = [highest_score_word]

	def modelEvaluateScore(self):
		score = dict()                                      # create a dict of score
		for ambiguous_word in self.best_word[self.candidate_key]:          # for ambiguous word in best word 
			score[ambiguous_word] = 0                       # inisialisasi score kata ambigu dengan nilai 0


		MAX_LEFT_CONTEXT_SIZE = self.candidate_key                                    # maximum left context size in input word
		MAX_RIGHT_CONTEXT_SIZE = len(self.stemmer_input) - 1 - self.candidate_key             # maximum right context size in input word

		if self.left_context >= MAX_LEFT_CONTEXT_SIZE:
			self.left_context = MAX_LEFT_CONTEXT_SIZE                   # real left context size

		if self.right_context >= MAX_RIGHT_CONTEXT_SIZE:
			self.right_context = MAX_RIGHT_CONTEXT_SIZE                  # real right context size


		if self.parent:
			for b_word in self.best_word[self.candidate_key]:
				sum_score = 0
				count = 0
				for i_word in self.stemmer_input[self.candidate_key - self.left_context:self.candidate_key + self.right_context + 1]:
					if (b_word in self.model.wv) and (i_word in self.model.wv):
						if b_word == i_word:
							sum_score += self.weight * self.model.wv.similarity(b_word, i_word)
						else:
							sum_score += self.model.wv.similarity(b_word, i_word)
					count += 1
				score[b_word] = sum_score / count
		else:
			for b_word in self.best_word[self.candidate_key]:
				sum_score = 0
				count = 0
				
				for i_word in self.stemmer_input[self.candidate_key - self.left_context:self.candidate_key]:
					if (b_word in self.model.wv) and (i_word in self.model.wv):
						if b_word == i_word:
							sum_score += self.weight * self.model.wv.similarity(b_word, i_word)
						else:
							sum_score += self.model.wv.similarity(b_word, i_word)
					count += 1

				for i_word in self.stemmer_input[self.candidate_key + 1:self.candidate_key + self.right_context + 1]:
					if (b_word in self.model.wv) and (i_word in self.model.wv):
						if b_word == i_word:
							sum_score += self.weight * self.model.wv.similarity(b_word, i_word)
						else:
							sum_score += self.model.wv.similarity(b_word, i_word)
					count += 1

				score[b_word] += sum_score / count

		max_score = -1
		highest_score_word = ''

		for word in score:
			if score[word] >= max_score:
				max_score = score[word]
				highest_score_word = word

		return highest_score_word