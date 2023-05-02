def updateScore(playerList, villainList):
    playerWon = input("Who won the last round?  ")
    for player in playerList:
        if playerWon.lower() == player.name.lower():
            player.score += 1
            for villain in villainList:
                if player.villain == villain.name:
                    villain.score += 1

