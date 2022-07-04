from gensim.models import Word2Vec
from abc import ABC, abstractmethod

class NDETCStemmerAbstract(ABC):
	
	@property
	def model(self):
		return self._model

	@property
	def rootWord(self):
		return self._root_word_file

	@property
	def rareWord(self):
		return self._rare_word_file
	
	@property
	def compoundWord(self):
		return self._compound_word_file

	@property
	def stopWord(self):
		return self._stopword_file
	
	@model.setter
	def model(self, model_dir):
		self._model=Word2Vec.load(model_dir)

	@rootWord.setter
	def rootWord(self, root_word_dir):
		self._root_word_file=set(line.rstrip('\n') for line in open(root_word_dir))

	@rareWord.setter
	def rareWord(self, rare_word_dir):
		self._rare_word_file = set([line.rstrip('\n') for line in open(rare_word_dir)])

	@compoundWord.setter
	def compoundWord(self, compound_word_dir):
		self._compound_word_file = [line.rstrip('\n') for line in open(compound_word_dir)]
		self._compound_word_file = {word: word.replace(' ', '') for word in self._compound_word_file}
		self._compound_word_file = {y: x for x, y in self._compound_word_file.items()}
	
	@stopWord.setter
	def stopWord(self, stopword_dir):
		self._stopword_file = set([line.rstrip('\n') for line in open(stopword_dir)])

	def __str__(self):
		return f"NDETCStemmer(weight={self._weight}, left_context={self._left_context}, right_context={self._right_context}, parent={self._parent})"
	
	@abstractmethod
	def stem(self,input,fromFile=False):
		pass
