
import time, os, ctypes

user_def_minutes = int(input("How many minutes to study? "))        # user defines how many mins program runs

timer = 0

while timer < (user_def_minutes):                                   # convert minutes to seconds
     
    appstokill = ["Battle.net.exe", "Overwatch.exe", "Wow.exe"]     # list of programs to kill
    tasks = str((os.popen('tasklist').readlines()))                 # all processes running
    for bad_task in appstokill:                                     # cycles through list
        if bad_task in tasks:                                       # looks for programs to kill in all processes running
            os.system("TASKKILL /F /IM %s" % bad_task)              # kills the bad program
            print("Killed %s... get back to work!" % bad_task)      # outputs which program it killed

    time.sleep(60)                                                  # pauses for a minute
    timer += 1                                                      # adds a minute to timer
    

    print((user_def_minutes - timer), "minutes remaining.")         # outputs remaining minutes
        
ctypes.windll.user32.MessageBoxW(0, "You can quit studying now!", "Time's up!", 0) # popup box



    
    
