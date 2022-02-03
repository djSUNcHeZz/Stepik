n = int(input())
list = [input().split(';') for x in range(n)] # ввод n строк, данные в строке разделены ;
results = {} # team: games, wins, =, loose, score
for team1, score1, team2, score2 in list:
    if team1 not in results:
        results.update([(team1, [0, 0, 0, 0, 0])]) # создаем ключ для команды
    if team2 not in results:
        results.update([(team2, [0, 0, 0, 0, 0])])
    results[team1][0] += 1 # игр
    results[team2][0] += 1
    if int(score1) == int(score2):
        results[team1][2] += 1 # ничья 1 очко
        results[team2][2] += 1
        results[team1][4] += 1 # итого очков
        results[team2][4] += 1
    elif int(score1) > int(score2):
        results[team1][1] += 1 # побед
        results[team2][3] += 1 # проигрыш 1 очко
        results[team1][4] += 3 # выигрыш 3 очка
    elif int(score1) < int(score2):
        results[team2][1] += 1
        results[team1][3] += 1
        results[team2][4] += 3
for team, res in results.items():
    print((team+':'), *res, end='\n')
