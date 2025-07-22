class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        if not players or not trainers:
            return 0
        players = sorted(players)
        trainers = sorted(trainers)
        player_idx = 0
        trainer_idx = 0
        match_count = 0
        while player_idx < len(players) and trainer_idx < len(trainers):
            if players[player_idx] <= trainers[trainer_idx]:
                match_count += 1
                player_idx += 1
                trainer_idx += 1
            else:
                trainer_idx += 1
        return match_count
