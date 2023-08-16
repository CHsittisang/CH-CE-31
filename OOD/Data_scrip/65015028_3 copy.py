import time

st = time.time()

def task_to_measure(n):
        if n <= 0:
                raise ValueError("n must be a positive integer.")
        elif n == 1 or n == 2:
                return n - 1
        else:
                return task_to_measure(n-1) + task_to_measure(n-2)

n = 35
result = task_to_measure(n)

en = time.time()
elapsed_time = en - st
print('\nExecution time:', elapsed_time, 'seconds\n')