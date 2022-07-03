

class RulesGenerator:
	def __init__(self):
		self.dict_rules=dict()

	def add(self,name,list_rules):
		if name in self.dict_rules.keys():
			raise Exception(f'name {name} already used')
		
		if type(list_rules).__name__!='ListRules':
			raise Exception(f'list_rules must be a listRules')

		self.dict_rules[name]=list_rules
			
	def get(self,name):
		return self.dict_rules[name]

	def showRules(self):
		stringRules=''
		for ruleName in self.dict_rules.keys():
			stringRules+=f'{ruleName} -> {self.dict_rules[ruleName].getRulesName()}\n'
		return stringRules

	def count(self):
		return len(self.dict_rules)

	def __len__(self) :
		return self.count()

	def __str__(self) :
		return f'RulesGenerator(\n{self.showRules()})'
	

