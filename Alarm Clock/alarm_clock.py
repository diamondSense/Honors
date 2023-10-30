from playsound import playsound
import time


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# def alarm(seconds):
#     time_elapsed = 0

#     print(CLEAR)
#     while time_elapsed < seconds:
#         time.sleep(1)
#         time_elapsed += 1

#         time_left = seconds - time_elapsed
#         minutes_left = time_left // 60
#         seconds_left = time_left % 60

#         print(f"\r{CLEAR_AND_RETURN}Alarm in: {minutes_left:02d}:{seconds_left:02d}",end="")
        

def alarm(secs):
	for x in range(secs,-1,-1):
		print(CLEAR)
		minutes, seconds = divmod(x,60)
		print(f"\r{CLEAR_AND_RETURN}{minutes:02d}:{seconds:02d}",end="")
		time.sleep(1)
	print("\nTime Up!")


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds

 
alarm(total_seconds)
playsound("alarm.mp3")

