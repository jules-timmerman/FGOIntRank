from material import Material, parseMat, addMatToList

# Class used to encode all fours ascensions data
class Ascensions:
	ascensionsMats : list[list[tuple[int,Material]]] = [[],[],[],[]]

	def __init__(self, ascensionMats = [[],[],[],[]]) -> None:
		self.ascensionsMats = ascensionMats

	def getAscMats(self):
		l = []
		for asc in self.ascensionsMats:
			for (i,m) in asc:
				l = addMatToList(m,i,l)
		return l

# We assume here that the dictionnary has the correct form ("0", "1", etc...)
def parseAsc(d : dict) -> Ascensions:
	if "0" in d.keys(): # Some servants don't have ascensions (ie Beasts etc...)
		l = [[],[],[],[]] # List of ascensionsMats
		for i in range(0,4):
			ascL = d[str(i)]["items"]
			for dp in ascL:
				l[i] += [(dp["amount"], parseMat(dp["item"]))]
		return Ascensions(l)
	return None