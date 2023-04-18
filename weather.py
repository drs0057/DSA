num_days = input("How many day's temperature? ")

temperatures = []
for i in range(int(num_days)):
    temp = input(f"Day {i + 1}'s high temp: ")
    temperatures.append(int(temp))

average_temp = sum(temperatures) / len(temperatures)

above_avg_count = 0
for temp in temperatures:
    above_avg_count += 1 if temp > average_temp else 0

print(f"Average = {round(average_temp)}")
print(f"{above_avg_count} day(s) above average.")