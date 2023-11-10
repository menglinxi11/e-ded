import time

def focus_timer(minutes):
    seconds = minutes * 60
    for i in range(seconds, 0, -1):
        mins, secs = divmod(i, 60)
        time_display = f"{mins:02d}:{secs:02d}"
        print(f"\rTime remaining: {time_display}", end='', flush=True)
        time.sleep(1)
    print("\nTime's up! Stay focused!")

focus_timer(25)
