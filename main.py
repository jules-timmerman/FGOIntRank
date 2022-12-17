import json
from relatedQuest import RelatedQuest
from servant import Servant

def main():
	servants = parseServants("nice_servant_lang_en.json")
	quests = parseQuests("nice_war_lang_en.json")
	for q in quests: # On fait l'association des deux
		for s in servants:
			if q.relatedId in s.related:
				s.relatedQuests += [q]
				break
	
	# ************************************

	print("1) Most Strengthening")
	print("2) Most Strenghthening - low rarity edition")
	s = input()
	if s == "1":
		mostStrengthening(servants) # Par nombre de Strengthening
	elif s == "2":
		mostStrengthening(list(filter(lambda x: x.rarity <= 3, servants))) # Par nombre en filtrant les low stars
	else:
		print("Enter a valid number...")


def mostStrengthening(servants : list[Servant]) -> None:
	print('Servants avec le plus de "Strengthening" (Interlude + Rank-Up):\n')
	for x in sorted(servants, key = (lambda x: (len(x.relatedQuests),5-x.rarity)), reverse=True):
		print(f"{x.name:^35} ({x.className:^15}) {x.rarity:}*\tNumber of Strengthening : {len(x.getInterludes())}+{len(x.getRankUps())}\tMax Bond : {x.maxBond():<2}\tMax Ascension : {x.maxAsc():<}")


# file : Chemin vers le json de servants
def parseServants(file : str) -> list[Servant]:
	with open(file) as f:
		l = json.load(f, object_hook = Servant.createFromDict)
		return list(filter(lambda x: x is not None, l))

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
		l = json.load(f, object_hook = RelatedQuest.parse)
		quests = []
		for q in l:
			quests += getQuests(q)
		quests = removeDuplicateQuests(quests)
		return list(filter(lambda x: (x is not None) and (isinstance(x, RelatedQuest)), quests))
 
if __name__ == "__main__":
	main()