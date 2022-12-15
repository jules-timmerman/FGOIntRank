class Gift:
	giftId = 0
	name = ""
	number = 0

	def __init__(self, giftId: int, number : int):
		self.giftId = giftId
		self.number = number

		self.name = self.getNameFromId(giftId)

	def getNameFromId(self, giftId:int):
		match giftId:
			case 2:
				return "Saint Quartz"
			case _:
				return "Unknown "+str(giftId)

	@staticmethod
	def createFromDict(d:dict) -> 'Gift':
		if d != None:
			return Gift(d["objectId"], d["num"])