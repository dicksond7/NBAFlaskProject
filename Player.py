class Player:
    def __init__(self, name, minutes, fieldGoalPercentage, fieldGoalsAttempted, threePtPercentage, threesPerGame,
                 freeThrowPercentage, freeThrowsAttempted):
        self.name = name
        self.minutes = minutes
        self.fieldGoalsAttempted = fieldGoalsAttempted
        self.threePtPercentage = threePtPercentage
        self.threesPerGame = threesPerGame
        self.freeThrowsAttempted = freeThrowsAttempted
        self.freeThrowPercentage = freeThrowPercentage
        self.fieldGoalPercentage = fieldGoalPercentage

    def __str__(self):
        return "Name: " + self.name + "\n Minutes Per Game: " + str(self.minutes) + "\n Field Goals Attempted: " \
               + str(self.fieldGoalsAttempted) + "\nField Goal Percentage: " + str(
            self.fieldGoalPercentage) + "\n Free Throws " \
               + "Attempted: " + str(self.fieldGoalsAttempted) + "\n Free Throw Percentage: " + str(
            self.freeThrowPercentage)