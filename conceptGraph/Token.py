class Token:
	def __init__(self, token_id, diction):
		self.id = int(token_id)
		self.head =  int(diction["head"])
		self.content = diction["content"]
		self.pos = diction["pos"]
		self.if_then = diction["if_then"]
		self.concepts = []
		self.children = diction["children"]
		self.quant = 1


	def match_concepts(self,lexicon):
		# return concepts list based on token (word, and depend tree info)
		concepts_list = lexicon.match_lexicon(self)
		self.concepts = concepts_list
		return concepts_list
