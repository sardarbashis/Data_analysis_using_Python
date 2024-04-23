player_scores = {}
with open("scores.csv", "r") as f:
    for line in f:
        # Check if the line contains a comma
        if ',' in line:
            player, score = line.strip().split(',')
            score = int(score)
            if player in player_scores:
                player_scores[player].append(score)
            else:
                player_scores[player] = [score]

# print(player_scores)

for player, score_list in player_scores.items():
    min_scores = min(score_list)
    max_scores = max(score_list)
    avg_scores = sum(score_list)/len(score_list)

    print(f"{player} ==> Min: {min_scores}, Max: {max_scores}, Avg: {avg_scores}")