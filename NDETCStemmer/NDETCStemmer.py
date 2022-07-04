
from NDETCStemmer.NDETCStemmerAbstract import NDETCStemmerAbstract
from NDETCStemmer.Utility import normalizer

from NDETCStemmer.CandidateGenerator import CandidateGenerator 

class NDETCStemmer(NDETCStemmerAbstract):
	def __init__(self,weight=1, left_context=1, right_context=1, parent=True):
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

		self.model='./NDETCStemmer/Model/w2vec_wiki_id_case'
		self.rootWord='./NDETCStemmer/DictFile/root_word.txt'
		self.rareWord='./NDETCStemmer/DictFile/rare_word.txt'
		self.compoundWords='./NDETCStemmer/DictFile/compound_word.txt'
		self.stopWord='./NDETCStemmer/DictFile/stopword.txt'


	def stem(self,stemmer_input,from_file=False,stopword=False):
		"""
		# stemmer_input         input string
		# from_file=True/False  True means that input word will be read from file, otherwise input word will be string
		# stopword=True/False  True means that input word will be remove words which exist in the list of stop word
		"""
		stemmer_input=normalizer.normalize(stemmer_input,from_file=from_file,stopword=stopword,stopword_file=self._stopword_file)
		candidate=CandidateGenerator(stemmer_input).generate()
		print(candidate)
		

		

