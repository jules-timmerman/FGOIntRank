from gift import Gift
from condition import Condition

class RelatedQuest:
	name = ""
	relatedId = 0
	gifts = []
	releaseConditions = []

	def __init__(self, name :str, relatedId : int, gifts, releaseConditions):
		self.name = name
		self.relatedId = relatedId
		self.gifts = gifts
		self.releaseConditions = releaseConditions

	@staticmethod
	def parse(d:dict):
		if ("type" in d.keys() and d["type"] == "friendship") or ("spotName" in d.keys() and d["spotName"] == "Rank-Up Quest"): # Suffisant pour une strengthening ?
			name = d["name"]
			relatedId = d["id"]
			
			gifts = [Gift.createFromDict(g) for g in d["gifts"]]

			releaseCondtions = [Condition.createFromDict(c) for c in d["releaseConditions"]]
			
			if "spotName" in d.keys() and d["spotName"] == "Rank-Up Quest":
				return RankUp(name, relatedId, gifts, releaseCondtions)
			return Interlude(name, relatedId, gifts, releaseCondtions)
		return d
	


class RankUp(RelatedQuest):
	def __init__(self, name :str, relatedId : int, gifts, releaseConditions):
		super().__init__(name, relatedId, gifts, releaseConditions)


class Interlude(RelatedQuest):
	def __init__(self, name :str, relatedId : int, gifts, releaseConditions):
		super().__init__(name, relatedId, gifts, releaseConditions)