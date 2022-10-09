"""
Emojimon interface class to abstract base_emojimon and instance_emojimon
"""

# import statements go here

__author__ = "Khoa Nguyen" # Insert your name here if you're writing the initial code
__maintainer__Khoa Nguyen = "" # Insert your name here if you're fixing bugs or make improvements

class Emojimon:
    """EmojimonInterface class"""

    # Define class attributes 
    _id: 0 # In the case of Base_Emojimon, emojidex id

    # Emojimon stats, will mean different things depending on which class it is
    # Each stat's minimum is 1
    # All stats must sum up to 24
    attack: 4
    special_attack: 4
    defense: 4
    special_defense: 4
    speed: 4
    hp: 4

    # Level up modifiers, must add up to 7
    attack_mod = 1.2
    special_attack_mod = 1.2
    defense_mod = 1.2
    special_defense_mod = 1.2
    speed_mod = 1
    hp_mod = 1.2
    
    def get_modifiers(self):
        """
        Getter function for modifiers

        Returns:
            Return a dictionary with key-value pair being modifier-modifier value
        """
        return {
            "attack_mod": self.attack_mod,
            "special_attack_mod": self.special_attack_mod,
            "defense_mod": self.defense_mod,
            "special_defense_mod": self.special_defense_mod,
            "speed_mod": self.speed_mod,
            "hp_mod": self.hp_mod
        }

    def get_stats(self):
        """
        Getter function for stats

        Keyword arguments:
            param1 (int) -- give description of what this is, as well as what it should include

        Returns:
            If anything is returned, describe it here
        """
        pass


def main(): 
    """Main driver code for testing"""
    pass


if __name__ == "__main__":
    """Runs when specifically called from command line"""
    main() import json
import random
from utils import Utils


class Emojimon:
	"""
	The class for Emojimon, handles everything in relation to an emoji
	"""
	# Elemental type and identification
	# TODO: make elements a list in database and this be the index instead, keep it consistent
	el_type = "default"
	_id = 0  # All emojis should have id higher than 1, this is simply the default

	# Default stat for an emojimon
	hp = 1
	attack = 1
	sp_attack = 1
	defense = 1
	sp_defense = 1
	speed = 1

	# Default improvement stats
	hp_improv = 1
	attack_improv = 1
	sp_attack_improv = 1
	defense_improv = 1
	sp_defense_improv = 1
	speed_improv = 1

	# Experience point and evolutionary stats
	level = 1
	xp_requirement = 100
	# This means you need 100 more xp to level up, must be handled in a level up function
	xp_remaining = 100
	evolve_lvl = 100
	# This is the id of the emojimon this one will evolve to. It should evolve to the next emojidex id, but just in case
	evolve_to = 0  # 0 means no evolution

	# Evolutionary stats for xp requirement for level up
	xp_mult = 1.5  # This will mean xp_remaining will increase by 1.5 every single level up

	# Dictionary whose key-value correspond to level and the list of moves that reaching that level unlocks
	move_unlock = {} # TODO: add default moves once that is ready
	# List of moves that this emojimon can use (stored by id)
	move_pool = [] 
	# List of moves that is currently being used (locked to 4 moves) (stored by id)
	move_list = []

	def __init__(self, random: bool, id: int):
		"""
		Constructor
		Parameter:
			random (bool): whether or not we want to generate this randomly. 
				Needs to be here since Python does not allow for constructor overloading
			id (int): if random is true, id will be used as the id of the generated emojimon, else, it will be used to query from the database
		"""
		if not id and not random:
			raise ValueError(
				'If random is set to false, data must be a non-empty json string')

		if random:
			self.random_gen()
			self._id = id
			#TODO: randomizing evolution
		else:
			# TODO: Allow for querying id from database
			self.fetch_emojimon(id)
			pass

	def fetch_emojimon(self, id: int):
		"""
		Fetch emojimon object from the database, for now it will be a local json document
		Parameter: 
			id (int): emojidex id of the emoji
		"""
		pass

	def random_gen(self):
		# TODO: dual-types?
		types = ["Normal", "Robot", "Ninja", "Fire", "Water", "Dinosaur", "Earth", "Sound", "Wind", "Darkness", "Light", "Plasma", "Solar", "Lunar", "Meme", "Magic"]

		# Randomize element type
		self.el_type = random.choice(types)

		# Emojimon Stat
		self.hp = random.randint(1, 20)
		self.attack = random.randint(1, 20)
		self.sp_attack = random.randint(1, 20)
		self.defense = random.randint(1, 20)
		self.sp_defense = random.randint(1, 20)
		self.speed = random.randint(1, 20)

		# Emojimon improvement stats
		self.hp_improv = random.uniform(1, 2)
		self.attack_improv = random.uniform(1, 2)
		self.sp_attack_improv = random.uniform(1, 2)
		self.defense_improv = random.uniform(1, 2)
		self.sp_defense_improv = random.uniform(1, 2)
		self.speed_improv = random.uniform(1, 2)

		# XP_mult randomizer
		self.xp_mult = random.uniform(1.3, 2)

	def add_xp(self, xp_gained: int):
		"""
		Handles adding xp to an emoji, if the emoji receives enough xp it will also level up and potentially evolve
		Parameter:
			xp_gained (int): The amount of xp gained by this emojimon
		"""
		self.xp_remaining -= xp_gained
		if self.xp_remaining <= 0:
			self.level_up_handler()
			self.xp_remaining = self.xp_requirement * self.xp_mult + self.xp_remaining

	def level_up_handler(self):
		"""
		Handles leveling 
		"""
		self.level += 1
		if self.level == self.evolve_lvl:
			self.evolve_handler()

	def evolve_handler(self):
		pass

	def get_move_list(self):
		return self.move_list

	def learn_move(self, move_id: int):
		"""
		Adds a move to the move list of the emojimon
		Some items can allow you to learn moves that is not part of the move_unlock
		Parameter:
			move_id (int): The id of the move to be added
		"""
		self.move_list.append(move_id)
		if len(self.move_list) > 4:
			self.move_list.pop(0)

	def check_for_move_unlock(self):
		"""
		Learn moves that are unlocked at the current level
		Fairly inefficient, is there a better way?
		"""
		if self.level in self.move_unlock:
			for move in self.move_unlock[self.level]:
				if move not in self.move_list:
					self.move_list.append(move)

	def get_id(self):
		"""
		Getter method for returning the id of the Emojimon object.
		"""
		return self._id

	def get_info(self):
		"""
		Getter method for getting the information needed to apply to move effect scaling
		"""
		info_dict = {
			"hp": self.hp,
			"attack": self.attack,
			"sp_attack": self.sp_attack,
			"defense": self.defense,
			"sp_defense": self.sp_defense,
			"speed": self.speed,
		}
		return info_dict
	
	def convert_python(self, json_file):
		"""
		converts json objects to python objects
		"""
		
		data= json.load(open(json_file, "rt"))
		
		for key in data:
			self.__dict__[key] = data[key]


def main():
	"""
	Main function
	"""
	emojimon = Emojimon(random=True, id=0)
	print(emojimon.__dict__)
	Utils.json_encoder(emojimon)


if __name__ == '__main__':
	main()
