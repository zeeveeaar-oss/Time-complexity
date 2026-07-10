n = 4
print("=== Counting Game points (n=",n, "rounds)")
print()

total = n * (n + 1) // 2
print("Formula way : total =", total, "| steps = 1")

total = 0
steps = 0
for round_num in range(1, n + 1):
    total += round_num
    steps += 1
print("Loop way  : total =", total, "|steps =", steps)

n = 10
nested_steps = 0
for round_nem in range(1, n + 1):
    for point in range(1, round_num + 1):
        nested_steps += 1

print()
print("=== Now with n =", n, "round ===")
print("formula way : steps = 1        (always just 1!)")
print("Loop way   : steps =", nested_steps, "(grows much faster)")
print()
print("Same answer - but ver different costs. That is time complexity!")