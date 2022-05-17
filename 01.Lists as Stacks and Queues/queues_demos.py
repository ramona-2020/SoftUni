from collections import deque

q = deque()  # Queue
s = []  # Stack
q_list = []  # Queue with list

for i in range(1, 6):
	q.append(i)
	s.append(i)
	q_list.append(i)

print("Queue:")
while q:
	print(q.popleft())

print("Stack:")
while s:
	print(s.pop())

print("Queue with list:")
while q_list:
	print(q_list.pop(0))
