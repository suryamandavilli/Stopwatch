import time

print("Press Enter to start the Stopwatch")
print("Press Ctrl+C to stop the Stopwatch")

while True:
    try:
        input()
        start_time =time.time()
        print("Stopwatch started")

    except KeyboardInterrupt:
        print("Stop watch stopped...")
        end_time = time.time()
        print("Total time:", round(end_time-start_time,2), "seconds")
        break