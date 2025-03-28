import os

running = True

os.system("title BatchRunner")

print("""
  ____        _       _     _____                             
 |  _ \      | |     | |   |  __ \                            
 | |_) | __ _| |_ ___| |__ | |__) |   _ _ __  _ __   ___ _ __ 
 |  _ < / _` | __/ __| '_ \|  _  / | | | '_ \| '_ \ / _ \ '__|
 | |_) | (_| | || (__| | | | | \ \ |_| | | | | | | |  __/ |   
 |____/ \__,_|\__\___|_| |_|_|  \_\__,_|_| |_|_| |_|\___|_|   
 """)

print("BatchRunner ")
print("Run .bat as cmd")

while running:
    commande = input()
    print("")
    if commande != "exit" :
        with open("Temp.bat", "w") as fichier:
            fichier.write(commande + "\n" + "pause")
    
        os.startfile("Temp.bat")
    else:
        running = False
        exit()