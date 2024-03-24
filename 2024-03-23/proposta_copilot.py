
def get_combinations(notes, amount):
    dp = [[] for _ in range(amount + 1)]
    dp[0] = [[]]

    for note in notes:
        for i in range(note, amount + 1):
            for comb in dp[i - note]:
                dp[i].append(comb + [(note, notes[note])])

    return dp[amount]

notas = [10, 20, 50]
valor = 30
print(get_combinations(notas, valor))