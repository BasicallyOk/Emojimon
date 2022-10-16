from server.src.components.emojimon import Emojimon

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
    moveOwner:Emojimon = None            #The emoji that this move belong to
    moveEffectString = ""       #The String containing the required information for the moves effects.
    
    #Move Elements
    moveCurrentPowerPoints = 0  #How many power points the move currently has
    moveAttackPower = 0         #The Moves attack power, how much "oomph" it packs. Max Value: 200
    moveAccuracy = 0            #The Moves accuracy, how often it succeeds. max Value: 100
    
    
    #Main definition function, makes use of the passed moveID to load correctly.
    def __init__(self, passedMoveID, moveParent: Emojimon):
        #load move attributes from file
        if(passedMoveID == -1):
            self.moveID = passedMoveID
            self.moveName = "Randomly Generated Test Move"
            self.moveType = "Normal"
            self.moveAttackType = "Physical"
            self.moveMaxPowerPoints = 420
            self.moveSpeed = 1
            self.moveOwner = moveParent
            self.moveEffectString = "COCK AND BALLS!"
            
            self.moveCurrentPowerPoints = 69
            self.moveAttackPower = 50
            self.moveAccuracy = 50
        pass
    
    #A Simple Function that returns the name of the Move
    def getMoveName(self):
        ''''''
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
    
    #A function that returns 1.5 if the move is being used is the same type as the moves user, if not, it returns 1
    def determineSameTypeAttackBonus(self):
        if self.getMoveType == self.moveOwner.getEmojiType[0] or self.getMoveType == self.moveOwner.getEmojiType[1]:
            return 1.5
        else:
            return 1
    
    #A function that determines the move type multiplier. If the moves type is effective aginst the opponent.
    def determineTypeEffectivenessMultiplier(self, moveTarget:Emojimon):
        defendingTypes = moveTarget.getEmojiType()
        type1Mod = self.typeEffectivesChart(self.getMoveType(), defendingTypes[0])
        type2Mod = 1
        if defendingTypes[1] != "Null":
            type2Mod = self.typeEffectivesChart(self.getMoveType(), defendingTypes[1])
        
        return type1Mod * type2Mod
    
    #The actual function that goes through the chart looking for the desired type
    def typeEffectivesChart(self, moveType, defenderType):
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
        
        return (int)(typeChart[type2Point][type1Point])
    
    def moveDamageCalculation(self, attackedEmoji: Emojimon):
        """
        The actual damage calculation functions!

        Keyword arguments:
            attackedEmoji (Emojimon) -- the attacked emoji whose defensive stats will be used

        Returns:
            the final damage value as an int
        """
        #tick down power points
        self.moveCurrentPowerPoints -= 1
        
        if self.moveAttackPower == 0:
            return 0 #The move is a non damaging move and we can skip this step
        
        if self.moveAttackType == "Physical":
            attackVal = (self.moveAttackPower + self.moveOwner.attack) * self.determineSameTypeAttackBonus()
            curvedAttackVal = attackVal ** 1.2
            
            defenseVal = attackedEmoji.defense
            curvedDefenseVal = defenseVal ** 0.5
            
            pretypeDamage = curvedAttackVal / curvedDefenseVal
            
            return max(pretypeDamage * self.determineTypeEffectivenessMultiplier(attackedEmoji))
            
        else:
            attackVal = (self.moveAttackPower + self.moveOwner.sp_attack) * self.determineSameTypeAttackBonus()
            curvedAttackVal = attackVal ** 1.2
            
            defenseVal = attackedEmoji.sp_defense
            curvedDefenseVal = defenseVal ** 0.5
            
            pretypeDamage = curvedAttackVal / curvedDefenseVal
            
            return max(pretypeDamage * self.determineTypeEffectivenessMultiplier(attackedEmoji))
    
    
    def canAct(self):
        #returns true if the move has more than 0 power points, or uses left. False otherwise
        if(self.moveCurrentPowerPoints < 1):
            return False
        else:
            return True
            
     

def main():
    em1 = Emojimon(True, 1)
    em2 = Emojimon(True, 2)
    moveTest = Move(-1, em1)
    
    print(em1.getEmojiType())
    print(em2.getEmojiType())
    print(moveTest.getMoveType())
    
    print(moveTest.determineTypeEffectivenessMultiplier(em2))
    
    pass
       
    
if __name__ == "__main__":
    main()


    
    
    