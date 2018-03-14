import webbrowser
import time
#import datetime
#now = datetime.datetime.now()
# person = input("Enter your name ")
# print ("Hello " , person  , " this is your breake timer")

#print ("current time is: " + (now.strftime("   %H:%M:%S    %d-%m-%Y  \n")) )
print ("current time is : " + time.ctime() )
#print (now.strftime("%Y-%m-%d %H:%M:%S \n"))
total_breaks = 3
break_count = 0
print("the program will start shortly \n")
print ("if you want to Exit press e or press anykey to continue ")
answer = raw_input()
if answer == "e":
       print ("thank you goodbye")
else:
              print ("the break counter will start \n")
              while (break_count < total_breaks):
                     time.sleep(5)
                     webbrowser .open("https://www.youtube.com/watch?v=ZPNgL1Ss7fU", new = 2 )
                     break_count += 1
                     if (break_count == 3):
                            print (" i hope you enjoyed your bracks ")
