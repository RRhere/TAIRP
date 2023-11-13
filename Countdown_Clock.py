import time

def countdown(timer):
    while timer:
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        timer -= 1

    print("Time Up!")

def main():
    try:
        minutes = int(input("Enter the countdown time in minutes: "))
        countdown(minutes * 60)
    except ValueError:
        print("Please enter a valid number")

if __name__ == "__main__":
    main()
