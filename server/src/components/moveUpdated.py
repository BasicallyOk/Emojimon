
__author__ = "Connor Killingbeck" # Insert your name here if you're writing the initial code
__maintainer__ = "" # Insert your name here if you're fixing bugs or make improvements

class Move:
    #Default Move and its required components
    
    #Move Reference Information
    moveID = 0                  #This is used to pull the moves information from the accomanying move storage file
    moveName = ""               #Name of Move
    moveType = ""               #Type of the Move
    moveAttackType = ""         #Physical or Emotional
    moveMaxPowerPoints = 0      #Unchanging maximum uses per move
    moveSpeed = 0               #The speed of the move in tandem with the speed of the emoji results in who goes first
    moveOwner = None            #The emoji that this move belong to
    moveEffectString = ""       #The String containing the required information for the moves effects.
    
    #Move Elements
    moveCurrentPowerPoints = 0  #How many power points the move currently has
    moveAttackPower = 0         #The Moves attack power, how much "oomph" it packs. Max Value: 200
    moveAccuracy = 0            #The Moves accuracy, how often it succeeds. max Value: 100
    
    
    #Main definition function, makes use of the passed moveID to load correctly.
    def __init__(self, passedMoveID):
        #load move attributes from file
        pass
    
    #A Simple Function that returns the name of the Move
    def getMoveName(self):
        return self.moveName
    
    #A Simple Function that returns the moves Identification number
    def getMoveID(self):
        return self.moveID
    
    #A Simple Function that returns the type of the move
    def getMoveType(self):
        return self.moveType
    
    #A Simple Function that returns the Emoji that this move belongs to
    def getMoveOwnerAsEmojimon(self):
        return self.moveOwner
    
    #A function that returns True if the move is being used is the same type as the moves user
    def determineSameTypeAttackBonus(self):
        #tempEmoji = getMoveOwnerAsEmojimon()
        #check if the emoji's type and getMoveType return the same type, if so, return true
        pass
    
    #A function that determins the move type multiplier. If the moves type is effective aginst the opponent.
    def determineTypeEffectivenessMultiplier(self, moveTarget):
        pass
    
    #The actual function that goes through the chart looking for the desired type
    def typeEffectivesChart(moveType, defenderType):
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
    
    
    