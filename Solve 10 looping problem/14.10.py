#Exponential Backoff
# Implement an exponential backoff strategy that doubles the wait time btw retires, starting from 1 second, but stops after 5 retiers


import time

wait_time = 1
max_retires = 5
attempts = 0


while  attempts < max_retires:
    print("attempt ", attempts + 1 ,"-wait time " , wait_time )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
    
    