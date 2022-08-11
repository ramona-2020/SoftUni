jobs = [int(job) for job in input().split(', ')]
target_index = int(input())

target_job = jobs[target_index]
cycles = 0

for i in range(len(jobs)):
    current_job = jobs[i]
    if current_job < target_job or current_job == target_job and target_index >= i:
        cycles += current_job

print(cycles)