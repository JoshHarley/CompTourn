def updateScore(result, playerList, villainList):
    for player in playerList:
        if result.lower() == player.name.lower():
            player.score += 1
            for villain in villainList:
                if villain.name == player.villain:
                    villain.score += 1
