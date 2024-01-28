class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        # Track the number of losses of each player
        losses = {}

        #Track all the players who played matches
        players = set()

        for match in matches:

            # make a set of all players
            players.add(match[0])
            players.add(match[1])
            
            # Increment count if a player lost a match
            if match[1] in losses :
                losses[match[1]] = losses[match[1]] + 1
            else:
                losses[match[1]] = 1

        # Create list of players who lost zero matches
        lost_zero = []

        #Create list of players who lost exactly one match
        lost_one = []

        for player in players:
            if player not in losses:
                lost_zero.append(player)
            else:
                if losses[player] == 1:
                    lost_one.append(player)

        answer = [sorted(lost_zero), sorted(lost_one)]
        return answer

            