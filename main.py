import json
from relatedQuest import parseQuests
from servant import parseServants, Servant

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
	match s:
		case "1":
			mostStrengthening(servants) # Par nombre de Strengthening
		case "2":
			mostStrengthening(list(filter(lambda x: x.rarity <= 3, servants))) # Par nombre en filtrant les low stars
		case _:
			print("Enter a valid number...")


def mostStrengthening(servants : list[Servant]) -> None:
	print('Servants avec le plus de "Strengthening" (Interlude + Rank-Up):\n')
	for x in sorted(servants, key = (lambda x: (len(x.relatedQuests),5-x.rarity)), reverse=True):
		print(f"{x.name:^35} ({x.className:^15}) {x.rarity:}*\tNumber of Strengthening : {len(x.getInterludes())}+{len(x.getRankUps())}\tMax Bond : {x.maxBond():<2}\tMax Ascension : {x.maxAsc():<}")


if __name__ == "__main__":
	main()