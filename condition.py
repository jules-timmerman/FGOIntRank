class Condition:
	name = "" # questClear, svtLimit, svtGet, svtFriendship
	value = 0

	def __init__(self, name: str, value : int):
		self.name = name
		self.value = value
	
	@staticmethod
	def createFromDict(d:dict):
		if d != None:
			return Condition(d["type"], d["value"])