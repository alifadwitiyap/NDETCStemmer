
from NDETCStemmer.NDETCStemmerAbstract import NDETCStemmerAbstract
from NDETCStemmer.Utility import normalizer
from NDETCStemmer.BestWordSelector import BestWordSelector
from NDETCStemmer.CandidateGenerator import CandidateGenerator 
from NDETCStemmer.ModelDownloader import ModelDownloader
from NDETCStemmer.ModelDownloader import CustomModelDownloader
from typing import Optional
import os

class NDETCStemmer(NDETCStemmerAbstract):
	def __init__(self,weight=1, left_context=1, right_context=1, parent=True, custom_downloader: Optional[CustomModelDownloader] = None):
		"""
		# weight               weight similarity  
		# left_context          maximum left context to eval
		# right_context         maximum right context to eval
		# parent=True/False     True means that parent of ambiguous word include in the evaluation, otherwise excluding
		"""
		self._model=None
		self._root_word_file=None
		self._rare_word_file=None
		self._compound_word_file=None
		self._stopword_file=None
		self._weight=weight
		self._left_context=left_context
		self._right_context=right_context
		self._parent=parent
		
		downloader = ModelDownloader()
		if custom_downloader is not None:
			downloader = custom_downloader
		downloader.run()
		self.path=os.path.dirname(__file__) 
		self.model=os.path.join(self.path,'Model','w2vec_wiki_id_case')
		self.rootWord=os.path.join(self.path,'DictFile','root_word.txt')
		self.rareWord=os.path.join(self.path,'DictFile','rare_word.txt')
		self.compoundWord=os.path.join(self.path,'DictFile','compound_word.txt')
		self.stopWord=os.path.join(self.path,'DictFile','stopword.txt')



	def stem(self,stemmer_input,from_file=False,stopword=False,):
		"""
		# stemmer_input         input string
		# from_file=True/False  True means that input word will be read from file, otherwise input word will be string
		# stopword=True/False  True means that input word will be remove words which exist in the list of stop word
		"""
		stemmer_input=normalizer.normalize(stemmer_input,from_file=from_file,stopword=stopword,stopword_file=self._stopword_file)
		word_candidate=CandidateGenerator(stemmer_input).generate()
		selector=BestWordSelector(stemmer_input=stemmer_input,model=self._model,root_word=self.rootWord,rare_word=self.rareWord,compound_word=self.compoundWord,weight=self._weight,left_context=self._left_context,right_context=self._right_context,parent=self._parent)
		best_word=selector.select(word_candidate)

		# # for test only 
		# return best_word

		output = ''
		for candidate_keys in range(len(best_word)):
			output += best_word[candidate_keys][0] + ' '

		return output

		

		

