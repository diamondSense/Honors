from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

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
playsound("alarm.wav")

