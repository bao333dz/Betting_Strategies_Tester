# This is a simulation to apply risk management by Kelly formula in a betting game with modifiable winrate.

import random

win = 0
lose = 0
i = 0

for _ in range(1000): # Run the simulation 1000 times
    balance = 1000 # Initial balance
    o = 0 # Count plays in each iteration
    i += 1 # Loop iteration count
    print(f"Iteration {i}")

    while balance > 1 and balance < 2000: # Play until account busts or doubles
        pick = random.choice([1,2]) # The winrate can be modified here by changing the ratio of 1s to 2s in this list

        if pick == 1: # Win
            balance = balance + ((balance * 0.1)*1.9) # The risk and reward ratio is adjusted here the standard is 1.9
            o += 1
            print (f"Play {o} of iteration {i}. Current balance: {balance:.2f}")
        
        else: # Lose
            balance = balance - (balance * 0.1)
            o += 1
            print (f"Play {o} of iteration {i}: lose, current balance: {balance:.2f}")

    if balance <= 1: # Account busted
        lose += 1

    else: # Doubled account
        win += 1

print("")
print(f"After 1000 plays, you doubled the account {win} times and busted {lose} times.")
