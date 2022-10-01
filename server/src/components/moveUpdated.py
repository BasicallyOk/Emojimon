
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
        tempEmoji = getMoveOwnerAsEmojimon()
        #check if the emoji's type and getMoveType return the same type, if so, return true
        
    
        
    
    
    
        
    
    
    