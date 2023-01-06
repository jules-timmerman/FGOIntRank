from fgolib import getServants
from servant import Servant
from material import Material, addMatToList
import os

def main():
	servants = getServants()
	menu(servants)	


def menu(servants : list[Servant]) -> None:
	print("1) Most Strengthening")
	print("2) Most Strenghthening - low rarity edition")
	print("3) Select Servants")
	print("4) Get Ascensions Materials")
	s = input()
	match s:
		case "1":
			mostStrengthening(servants) # Par nombre de Strengthening
		case "2":
			mostStrengthening(list(filter(lambda x: x.rarity <= 3, servants))) # Par nombre en filtrant les low stars
		case "3":
			selectServants()
		case "4":
			matList = getMaterials(servants)
			printMats(matList)
		case _:
			print("Enter a valid number...")

def selectServants() -> None:
	servants = getServants()
	print("Edit selection.txt with 0 and 1 (delete and retry if the file existed and is not correct / old)")
	s = input("Would you like to keep the previous file (might not work properly if it is too old / corrupted (y/N)")
	if not s == "y":
		with open("selection.txt", "w") as f:
			for s in servants:
				f.write(f"{s.name:^35} ({s.className:^15}) ({s.rarity}*)::1\n")
	
	input("Press Enter when done.")
	
	selected = []
	with open("selection.txt", "r") as f:
		i = 0
		for lines in f:
			k = int(lines.split("::")[1]) # Récupère l'entier (si bien formatté) (le 0 ou 1)
			if k == 1:
				selected += [servants[i]]
			i += 1
	menu(selected)

def getMaterials(servants : list[Servant]) -> list[tuple[int,Material]]:
	matList : list[tuple[int,Material]] = []
	for s in servants:
		if s.ascensions != None: # On trie les Servants bizarres
			mats = s.ascensions.getAscMats()
			for (i,m) in mats:
				matList = addMatToList(m,i,matList)
	return matList

def printMats(mats:list[tuple[int,Material]]):
	for (i,m) in mats:
		print(f"{m.name:^40} : {i}")



def mostStrengthening(servants : list[Servant]) -> None:
	print('Servants avec le plus de "Strengthening" (Interlude + Rank-Up):\n')
	for x in sorted(servants, key = (lambda x: (len(x.relatedQuests),5-x.rarity)), reverse=True):
		print(f"{x.name:^35} ({x.className:^15}) {x.rarity:}*\tNumber of Strengthening : {len(x.getInterludes())}+{len(x.getRankUps())}\tMax Bond : {x.maxBond():<2}\tMax Ascension : {x.maxAsc():<}")


if __name__ == "__main__":
	main()