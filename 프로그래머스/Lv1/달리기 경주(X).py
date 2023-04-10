# 시간초과
def solution(players, callings):
    for calling in callings:
        idx = players.index(calling)
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
    return players

# 정답1
def solution2(players, callings):
    dic_players = {player: idx for idx, player in enumerate(players)}
    dic_idx = {idx: player for idx, player in enumerate(players)}
    
    for calling in callings:
        idx = dic_players[calling]
        front = idx - 1
        
        curr_player = calling
        front_player = dic_idx[front]
        
        dic_players[curr_player], dic_players[front_player] = front, idx
        dic_idx[idx], dic_idx[front] = front_player, curr_player
        
    return list(dic_idx.values())

# 정답2
def solution3(players, callings):
    dic_players = {player: idx for idx, player in enumerate(players)}
    
    for calling in callings:
        idx = dic_players[calling]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        dic_players[players[idx]] = idx
        dic_players[players[idx-1]] = idx-1
    
    return players

print(solution3(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))