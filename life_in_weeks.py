print("***Life in weeks calculator***")

Age = input("What is your current age?")
Age_as_int = int(Age)
years_remaining = 90 - Age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"Your Days remaining is{days_remaining},Your Weeks remaining is{weeks_remaining},Your Months remaining is{months_remaining}")
