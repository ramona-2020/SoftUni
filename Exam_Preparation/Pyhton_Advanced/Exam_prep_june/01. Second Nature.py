from collections import deque


flowers = deque(int(d) for d in input().split())
buckets = list(int(b) for b in input().split())

second_nature_flowers = []

while flowers and buckets:
	current_flower = flowers[0]
	current_bucket = buckets[-1]

	if flowers[0] == buckets[-1]:  # 1
		second_nature_flowers.append(flowers[0])
		flowers.popleft()
		buckets.pop()
	elif buckets[-1] > flowers[0]:
		buckets[-1] -= flowers[0]
		if buckets:
			buckets[-2] += buckets[-1]

		flowers.popleft()
		buckets.pop()
	elif flowers[0] > buckets[-1]:
		while flowers and buckets and flowers[0] >= buckets[-1]:
			flowers[0] -= buckets[-1]
			buckets.pop()

	if flowers and flowers[0] <= 0:
		flowers.popleft()



# Prints result
# Line 1:
if buckets:
	print("Buckets:")
	print(' '.join(str(b) for b in buckets[::-1]))
if flowers:
	print("flowers")
	print(' '.join(str(f) for f in flowers))

# Line 2:
# Second Nature Flowers:
if second_nature_flowers:
	print("second nature flowers")
	print(' '.join(str(f) for f in second_nature_flowers))
else:
	print("second nature flowers")
	print("None")