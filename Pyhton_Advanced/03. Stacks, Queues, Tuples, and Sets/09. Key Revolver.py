from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(b) for b in input().split()]
locks = deque([int(b) for b in input().split()])
intelligence_value = int(input())

bullets_used = 0
current_barrel_size = gun_barrel_size
while True:
	if len(bullets) == 0 or len(locks) == 0:
		if len(locks) == 0:
			bullets_total_price = bullets_used * bullet_price
			print(f"{len(bullets)} bullets left. Earned ${intelligence_value - bullets_total_price}")
		else:
			print(f"Couldn't get through. Locks left: {len(locks)}")
		break

	if current_barrel_size == 0 and len(bullets) > 0:
		print("Reloading!")
		current_barrel_size = gun_barrel_size

	current_bullet = bullets.pop()
	if locks[0] > current_bullet:
		locks.popleft()
		print("Bang!")
	else:
		print("Ping!")

	bullets_used += 1
	current_barrel_size -= 1