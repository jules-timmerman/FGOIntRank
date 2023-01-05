import json

from gift import Gift
from condition import Condition

class RelatedQuest:
	name = ""
	relatedId = 0
	gifts = []
	releaseConditions = []

	def __init__(self, name :str, relatedId : int, gifts : list[Gift], releaseConditions: list[Condition]):
		self.name = name
		self.relatedId = relatedId
		self.gifts = gifts
		self.releaseConditions = releaseConditions

	
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
	
# Recursively retrieve RelatedQuests in a dictionnary
def getQuests(d: dict) -> list[RelatedQuest]:
	tempL = []
	for k in d.keys():
		if isinstance(d[k], RelatedQuest):
			tempL += [d[k]]
		elif isinstance(d[k],dict):
			tempL += getQuests(d[k])
		elif isinstance(d[k], list):
			for x in d[k]:
				if isinstance(x, RelatedQuest):
					tempL += [x]
				elif isinstance(x,dict):
					tempL += getQuests(x)
	return tempL 


# We get duplicates due to Road to 7....
def removeDuplicateQuests(quests: list[RelatedQuest]):
	l = []
	ids = []
	for q in quests:
		if not q.relatedId in ids:
			l += [q]
			ids += [q.relatedId]
	return l

def parseQuests(file : str) -> list[RelatedQuest]:
	with open(file) as f:
		l = json.load(f, object_hook = parse)
		quests = []
		for q in l:
			quests += getQuests(q)
		quests = removeDuplicateQuests(quests)
		return list(filter(lambda x: (x is not None) and (isinstance(x, RelatedQuest)), quests))


class RankUp(RelatedQuest):
	def __init__(self, name :str, relatedId : int, gifts : list[Gift], releaseConditions: list[Condition]):
		super().__init__(name, relatedId, gifts, releaseConditions)


class Interlude(RelatedQuest):
	def __init__(self, name :str, relatedId : int, gifts : list[Gift], releaseConditions: list[Condition]):
		super().__init__(name, relatedId, gifts, releaseConditions)