from gensim.models import Word2Vec
from abc import ABC, abstractmethod

class NDETCStemmerAbstract(ABC):
	
	@property
	def model(self):
		return self._model

	@property
	def rootWords(self):
		return self._root_words

	@property
	def rareWords(self):
		return self._rare_words
	
	@property
	def compoundWords(self):
		return self._compound_words
	
	@model.setter
	def model(self, modelDir):
		self._model=Word2Vec.load(modelDir)

	@rootWords.setter
	def rootWords(self, rootWordsDir):
		self._root_words=set(line.rstrip('\n') for line in open(rootWordsDir))

	@rareWords.setter
	def rareWords(self, rareWordsDir):
		self._rare_words = set([line.rstrip('\n') for line in open(rareWordsDir)])

	@compoundWords.setter
	def compoundWords(self, compoundWordDir):
		self._compound_words = [line.rstrip('\n') for line in open(compoundWordDir)]
		self._compound_words = {word: word.replace(' ', '') for word in self._compound_words}
		self._compound_words = {y: x for x, y in self._compound_words.items()}
	

	def __str__(self):
		return f"NDETCStemmer(weight={self._weight}, left_context={self._left_context}, right_context={self._right_context}, parent={self._parent})"
	
	@abstractmethod
	def stem(self,input,fromFile=False):
		pass
