"""
Basic python script i used to generate mappings between minecraft potions and new mcl potion names
The reason this is custom and is because minclonia does not support individual potion textures
each potion instance needs to have its image overloaded after loading into the game. Therefore
i define my own name for the mcl textures which are used and this script converts from minecraft names
to mineclonia names. 

I thought i would leave this in so others can use it if they so desire. Also makes it easier for me
if i want to update the mod to support new potions that maybe added.
"""

m = [
	"awkward",
	"mundane",
	"thick",
	"healing",
	"harming",
	"night_vision",
	"swiftness",
	"slowness",
	"leaping",
	"withering",
	"poison",
	"regeneration",
	"invisibility",
	"water_breathing",
	"fire_resistance",
	"strength",
	"weakness",
	"slow_falling",
	"turtle_master",
	"luck",
	"bad_luck",
	"ominous",
	"infestation",
	"oozing",
	"weaving",
	"wind_charged"
]

print("\n\n\n\n")
for i in m:
    if i == "infestation": i = "infested"

    cat = ["potions", "splash_potions", "lingering_potions"]
    for c in cat:
        catMap = "_"
        if c == "lingering_potions":
            catMap += "lingering"
        elif c == "splash_potions":
            catMap += "splash"
        else:
            catMap = ""
        mcImgName = i
        if mcImgName == "infestation": mcImgName = "infested"
		#I dont know if these TODOs are actually true
        #TODO carry on from here, I just need to regerate mappings then run compile the texture pack
        #TODO also problem with ominouse potion after that all of them work :)
        print("{\"item\", \""+c+"/"+mcImgName+".png\", \"potions\", \"mcl_potions_"+i+catMap+".png\", 1},")