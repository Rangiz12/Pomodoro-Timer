import time
from playsound import playsound

def play_sound(sound_file):
  playsound(sound_file)

def main():
  # Get user input for work and break intervals
  work_minutes = int(input("Enter work interval duration (minutes): "))
  break_minutes = int(input("Enter break interval duration (minutes): "))
  num_cycles = int(input("Enter number of Pomodoro cycles (optional, default: 4): ") or 4)

  # Define sound files for notifications (replace with actual filenames)
  work_start_sound = "work_start.wav"
  work_end_sound = "work_end.wav"
  break_start_sound = "break_start.wav"
  break_end_sound = "break_end.wav"
  
  for cycle in range(1, num_cycles + 1):
    print(f"Pomodoro Cycle {cycle}")
    
    # Work interval
    play_sound(work_start_sound)
    print(f"Work for {work_minutes} minutes...")
    time.sleep(work_minutes * 60)
    play_sound(work_end_sound)
    print("Work interval complete!")
    
    # Break interval
    play_sound(break_start_sound)
    print(f"Break for {break_minutes} minutes...")
    time.sleep(break_minutes * 60)
    play_sound(break_end_sound)
    print("Break interval complete!")

if __name__ == "__main__":
  main()
