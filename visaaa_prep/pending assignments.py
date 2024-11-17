X, Y, Z = map(int, input().split())
total_required_minutes = X * Y
total_available_minutes = Z * 24 * 60
if total_required_minutes <= total_available_minutes:
    print("YES")
else:
    print("NO")
