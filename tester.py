print("Welcome, this script can simulates any betting strategies you want to test based on user-defined winrate, risk per bet, risk-reward ratio, and desired balance increase.")
import random

win = 0
lose = 0
i = 0
avg = 0
count = 0

# User inputs winrate as a percentage
wr = float(input("Enter the estimate winrate (%): "))
wr = wr / 100

# User inputs risk per bet as a percentage
risk = float (input("Enter your risk per bet (the recommend is 10%, according to Kelly formula) (%): "))
risk = risk / 100

# User inputs the R:R ratio
reward = float (input("Enter your risk and reward ratio per bet (the usual is 1.9): ")) 

# User inputs desired balance increase multiplier
x = float(input("How will you want your balance to be increased? (Enter a multiplier, e.g., 2 for double): "))


# Run the simulation 1000 times
for _ in range(1000):

    # Initial balance
    balance = 1000

    # Count plays in each iteration
    o = 0

    # Loop iteration count
    i += 1 
    print(f"Iteration no {i}")

    # Play until account busts or desired balance is reached
    while balance > 1 and balance < 1000 * x:

        # Generate a random number between 0 and 1
        rate = random.random()

        # Win
        if rate < wr:
            balance = balance + ((balance * risk) * reward)
            o += 1
            print (f"Play {o} of iteration {i}: Win, Current balance: {balance:.2f}")
        
        # Lose
        else: 
            balance = balance - (balance * risk)
            o += 1
            print (f"Play {o} of iteration {i}: Lose, Current balance: {balance:.2f}")
    
    # Total plays in this iteration
    count = (count + o)

    # Account busted
    if balance <= 1: 
        lose += 1

    # Desired balance reached
    else: 
        win += 1

# Average plays per iteration
print(count)
avg = count / 1000
print(f"After 1000 iterations, you reached the desired balance {win} times and busted {lose} times.")
print(f"{avg:.0f} is the average number of plays per iteration.")
