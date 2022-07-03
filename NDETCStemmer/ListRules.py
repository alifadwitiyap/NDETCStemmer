import inspect
class ListRules:
	def __init__(self,rules) :
		#if want to add more rules func with different parameter please setting execute func too
		for rule in rules:
			funcParameter=list(inspect.signature(rule).parameters)
			if funcParameter == ['word','word_candidate','keys'] or funcParameter == ['word_candidate']:
				continue
			else:
				raise Exception(f'{rule.__name__} function must have 3 parameters: word, word_candidate, keys or must have 1 parameter: word_candidate')
		
		self.list_rules=rules
	
	def getRulesName(self) :
		stringRules=''
		for rule in self.list_rules:
			stringRules+=f'{rule.__name__}, '
		return stringRules

	def count(self) :
		return len(self.list_rules)

	def execute(self,word_candidate=None,word=None,keys=None) :
		for rule in self.list_rules:
			try:
				rule(word,word_candidate,keys)
			except TypeError as e:
				rule(word_candidate)

	def __str__(self) :
		return f'ListRules({self.getRulesName()})'

	def __len__(self) :
		return self.count()