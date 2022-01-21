from pynput.keyboard import Key, Controller, Listener
import time
kb = Controller()
print('''
  _____   ____  _____   _____       _______                                 
 |  __ \ / __ \|  __ \ / ____|   /\|__   __|                                
 | |__) | |  | | |__) | |       /  \  | |                                   
 |  ___/| |  | |  ___/| |      / /\ \ | |                                   
 | |    | |__| | |    | |____ / ____ \| |     //By JasperDG//              
 |_|     \____/|_|_____\_____/_/____\_\_|    _____ _____ _  ________ _____  
     /\  | |  | |__   __/ __ \ / ____| |    |_   _/ ____| |/ /  ____|  __ \ 
    /  \ | |  | |  | | | |  | | |    | |      | || |    | ' /| |__  | |__) |
   / /\ \| |  | |  | | | |  | | |    | |      | || |    |  < |  __| |  _  / 
  / ____ \ |__| |  | | | |__| | |____| |____ _| || |____| . \| |____| | \ \ 
 /_/    \_\____/   |_|  \____/ \_____|______|_____\_____|_|\_\______|_|  \_\
     ''')
delay = float(input("clickDelay > "))
print("Starting in 5 seconds")
time.sleep(5)
print("Autoclicker started, press ctrl in the terminal window to stop")
while True:
    kb.press("c")
    time.sleep(delay)
    kb.release("c")
