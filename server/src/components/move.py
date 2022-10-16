
__author__ = "Connor Killingbeck, Huy Anh Nguyen, Kevin Dau, Khoa Nguyen" # Insert your name here if you're writing the initial code
__maintainer__ = "" # Insert your name here if you're fixing bugs or make improvements

import random, json
class Move:
	#Default Move and its required components
	
	#Move Reference Information
	moveID = 0                  #This is used to pull the moves information from the accomanying move storage file
	moveName = ""               #Name of Move
	moveType = ""               #Type of the Move
	moveAttackType = ""         #Physical or Emotional
	moveMaxPowerPoints = 0      #Unchanging maximum uses per move
	moveSpeed = 0               #The speed of the move in tandem with the speed of the emoji results in who goes first
	moveEffectString = ""       #The String containing the required information for the moves effects.
	
	#Move Elements
	moveCurrentPowerPoints = 0  #How many power points the move currently has
	moveAttackPower = 0         #The Moves attack power, how much "oomph" it packs. Max Value: 200
	moveAccuracy = 0            #The Moves accuracy, how often it succeeds. max Value: 100
	
	
	#Main definition function, makes use of the passed moveID to load correctly.
	def __init__(self, random: bool, id: int):
		"""
		Initializes the arguments for an Emojimon's Move, whose data acquired using its id value in the database
		Parameters:
		random (bool): whether or not we want to generate this randomly.
		Needs to be here since Python does not allow constructor overloading
		passedMoveID (int): the index of the Move in the database that leads to a JSON object
		"""
		if not id and not random:
			raise ValueError('if random is set to false, then the id value must be set to the default value of 0')
		
		if random:
			self.random_gen()
			self.moveID = id
		else:
			# This is supposed to fetch this Move's data from the database using the id parameter
			pass

	def random_gen(self):
		"""
		Randomly generate everything in the move stats, including its name
		"""
		types = ["Normal", "Robot", "Ninja", "Fire", "Water", "Dinosaur", "Earth", "Sound", "Wind", "Darkness", "Light", "Plasma", "Solar", "Lunar", "Meme", "Magic"]
		self._name_gen()
		self.speed = random.randint(1, 6)   # All ranges here are balanced using eyeballs and hopes. And wishes.
		self.attk_pw = random.randint(0, 5)
		self.attk_type = random.choice(['physical', 'emotional'])
		self.moveType = random.choice(types)
		if self.attk_type == 'emotional':
			self.fp = random.randint(1, 5)

	def _name_gen(self):
		"""
		Randomly generate the name of the move
		"""
		FILE_PATH = "move_names.json"
		# This is band-aid solution currently used for generating random move name based on the emoji's elements.
		# If possible, the keys in the json file would be the index of the elemental types instead in the future.
		# Or using an online dictionary API...
		with open(FILE_PATH) as f:
			words = json.load(f)
		self.moveName = f"{random.choice(words[self.emoji.el_type])} {random.choice(words['nouns'])}"


	def getMoveName(self):
		"""
		Returns the name of this Move.
		"""
		return self.moveName
	
	def getMoveID(self):
		"""
		Returns the identification number of this Move.
		"""
		return self.moveID
	
	def getMoveType(self):
		"""
		Returns the type of this Move
		"""
		return self.moveType
	
	def determineSameTypeAttackBonus(self, userInfo: dict):
		"""
		Returns True if this Move being used is of the same type as the user (ex: a Fire move is used by a Fire user.)
		user_info: a dictionary containing the information needed to apply to move effect scaling.
		"""
		#tempEmoji = getMoveOwnerAsEmojimon()
		#check if the emoji's type and getMoveType return the same type, if so, return true
		pass
	
	def determineTypeEffectivenessMultiplier(self, moveTarget):
		"""
		Determines the move type's multiplier if 
		checking whether this Move's type is effective against the opponent Emojimon's type 
		returns True.
		"""
		pass
	
	def typeEffectivesChart(moveType, defenderType):
		"""
		Goes through the chart and return the multiplier 
		that is going to be applied on this Move.
		"""
		typeChart = [["Move Type >", "Normal", "Robot", "Ninja", "Fire", "Water", "Dinosaur", "Earth", "Sound", "Wind", "Darkness", "Light", "Plasma", "Solar", "Lunar", "Meme", "Magic"],
					 ["Normal",         "1",       "1",     "1",    "1",    "1",       "2",       "1",    "1",     "1",     "1",        "1",     "2",     "2",     "1",    "1",      "1"],
					 ["Robot",          "0.5",     "1",     "1",  "0.5",    "2",       "1",       "1",  "0.5",     "1",     "1",        "1",     "2",     "2",   "0.5",    "1",      "3"],
					 ["Ninja",          "0.5",     "1",     "2",    "1",    "1",       "1",       "1",    "1",     "1",   "0.5",        "3",     "1",     "1",     "1",    "2",      "1"],
					 ["Fire",           "1",       "1",     "1",    "1",    "3",     "0.5",       "2",    "1",     "2",   "0.5",        "1",     "1",     "1",     "1",    "1",      "1"],
					 ["Water",          "1",     "0.5",     "1", "0.25",    "1",       "1",       "1",    "1",     "1",     "1",        "1",     "2",     "1",     "3",    "1",      "1"],
					 ["Dinosaur",     "0.5",       "1",     "1",    "2",    "1",       "3",       "1",    "1",     "1",     "2",        "1",     "1",   "0.5",     "2",    "1",      "2"],
					 ["Earth",          "1",       "1",   "0.5",  "0.5",    "2",       "1",       "1",    "1",   "0.5",     "1",        "1",     "1",     "1",     "1",    "1",      "1"],
					 ["Sound",          "1",     "0.5",     "1",    "1",    "1",       "1",       "2",    "1",     "2",     "2",        "1",     "1",     "1",     "1",    "3",      "2"],
					 ["Wind",         "0.5",     "0.5",     "2",    "2",    "1",       "1",       "1",    "2",     "1",     "1",        "1",     "1",     "1",     "1",  "0.5",      "1"],
					 ["Darkness",     "0.5",       "1",     "2",    "1",    "1",       "1",       "1",    "1",   "0.5",     "1",        "3",     "1",     "2",  "0.25",    "1",   "0.25"],
					 ["Light",          "1",       "1",   "0.5",    "1",    "1",       "1",       "2",    "1",     "1",  "0.25",        "1",     "1",     "1",     "1",    "1",    "0.5"],
					 ["Plasma",         "2",       "1",     "1",    "1", "0.25",     "0.5",       "1",    "1",     "1",     "1",     "0.25",     "1",     "3",     "1",  "0.5",      "1"],
					 ["Solar",          "2",       "2",     "1",  "0.5",  "0.5",     "0.5",       "1",  "0.5",   "0.5",  "0.25",        "1",     "1",     "1",     "2",    "1",      "1"],
					 ["Lunar",          "1",       "2",     "2",    "1",    "2",       "1",       "1",  "0.5",     "1",     "2",        "1",   "0.5",     "1",     "1",    "1",      "1"],
					 ["Meme",         "0.5",       "3",   "0.5",    "1",    "1",       "1",     "0.5",    "3",     "1",     "1",        "1",     "1",     "1",     "1",    "3",      "1"],
					 ["Magic",          "1",       "1",     "1",    "2",    "1",       "2",     "0.5",    "3",     "2",     "1",        "1",   "0.5",     "1",     "1",    "1",      "1"]]
		
		type1Point = 0
		type2Point = 0
		
		for type1 in typeChart[0]:
			if(moveType == type1):
				break
			else:
				type1Point += 1
		
		for x in range(16):
			if(defenderType == typeChart[x][0]):
				break
			else:
				type2Point += 1
		
		return typeChart[type2Point][type1Point]
			
	 
"""  Test Code
def main():
	print(Move.typeEffectivesChart("Magic", "Dinosaur"))
	pass
	   
	
if __name__ == "__main__":
	main()
	
"""  
	
	
	