from relatedQuest import parseQuests
from servant import parseServants, Servant

# Tentative de centralisation de tout en une librarie
allServants = None

def getServants() -> list[Servant]:
	global allServants

	if allServants != None:
		return allServants
	servants = parseServants("nice_servant_lang_en.json")
	quests = parseQuests("nice_war_lang_en.json")
	for q in quests: # On fait l'association des deux
		for s in servants:
			if q.relatedId in s.related:
				s.relatedQuests += [q]
				break
	allServants = servants
	return servants