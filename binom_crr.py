import math

def binomial_crr(Option, K, T, S_0, sigma, r, q, N, Exercise):
    # create timestep
    deltaT = T / N
    # factor that the instrument will move up by
    # down factor = 1 / up factor
    up = math.exp((sigma * math.sqrt(deltaT)))
    # probabilities of up and down moves
    p_up = (up * math.exp(-q * deltaT) - math.exp(-r * deltaT)) / (up ** 2 - 1)
    p_down = math.exp(-r * deltaT) - p_up
    tree_values = [0] * N
    # populating initial tree values
    for i in range(N):
        # S_n = S_0 * u^{number of up ticks - number of down ticks}
        S_n = S_0 * up ** (2 * i - N + 1)
        # calculate exercise value at end
        tree_values[i] = (K - S_n) if Option == "P" else (S_n - K)
        # don't exercise if lose money
        tree_values[i] = max(tree_values[i], 0)
    # calculate earlier values
    for j in range(N - 1, -1, -1):
        for i in range(j):
            tree_values[i] = p_up * tree_values[i + 1] + p_down * tree_values[i]
            if Exercise == "A":
                exercise_val = K - S_0 * up ** (2 * i - j)
                tree_values[i] = max(tree_values[i], exercise_val)
    return tree_values[0]

print(binomial_crr("C", 100, 1, 100, 0.2, 0.05, 0.02, 50, "E"))