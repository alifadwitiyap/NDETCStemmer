
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
		self._root_words=None
		self._rare_words=None
		self._compound_words=None
		self._weight=weight
		self._left_context=left_context
		self._right_context=right_context
		self._parent=parent

		self.model='./NDETCStemmer/Model/w2vec_wiki_id_case'
		self.rootWords='./NDETCStemmer/DictFile/root_words.txt'
		self.rareWords='./NDETCStemmer/DictFile/rare_words.txt'
		self.compoundWords='./NDETCStemmer/DictFile/compound_words.txt'


	def stem(self,inputStemmer,fromFile=False,stopword=False):
		"""
		# inputStemmer         input string
		# fromFile=True/False  True means that input word will be read from file, otherwise input word will be string
		# stop word=True/False  True means that input word will be remove words which exist in the list of stop word
		"""
		normalizeText=normalizer.normalize(inputStemmer,fromFile=fromFile,stopword=stopword)
		candidate=CandidateGenerator(normalizeText).generate()
		print(candidate)
		

		

