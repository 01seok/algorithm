x, y = map(int, input().split())

days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_days = sum(month_days[:x-1]) + y
print(days[total_days % 7])