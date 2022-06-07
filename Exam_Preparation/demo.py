# -----S

lines = [5, 5, 9, 10, 7, 8, 7, 9]
min_el = min(lines)
max_el = max(lines)

missing_items = sorted(list(set(el for el in lines if lines.count(el) > 1)))

print(missing_items)