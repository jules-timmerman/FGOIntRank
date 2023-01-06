class Material:
	name = ""
	id = 0

	def __init__(self, name = "", id = 0) -> None:
		self.name = name
		self.id = id

# We assume that parse is only called with a correct dict (from "item" so with "id", "name" etc...)
def parseMat(d:dict) -> Material:
	return Material(name = d["name"], id = d["id"])

# Add a certain amount of a material to the list
def addMatToList(mat : Material, amount : int, l : list[tuple[int,Material]]) -> list[tuple[int,Material]]:
	retL = []
	added = False
	matid = mat.id
	for i in range(len(l)):
		a,m = (l[i])
		if m.id == matid:
			retL += [((a+amount), m)]
			added = True
		else:
			retL += [(a,m)]
	if not added:
		retL += [(amount,mat)]
	return retL