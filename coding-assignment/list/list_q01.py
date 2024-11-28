# Write a program that converts a given number of days into weeks and days.
total_days = int(input("Enter the number of days: "))
weeks = total_days // 7
days = total_days % 7
result = [weeks, days]
print(f"{total_days} days is equivalent to {result[0]} week(s) and {result[1]} day(s).")