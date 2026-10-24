import time

my_time = int (input("Enter the time in seconds:"))

for x in range (my_time,0,-1):
    seconds = x % 60
    minutes = int (x/60) % 60  # e perdorim 2 here 60
    # pasi heren e dyte Sepse duam që minutat të jenë nga 0 deri në 59.
    hours = int (x /3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's Up")