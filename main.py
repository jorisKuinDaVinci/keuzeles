""""


21-11-2023

"""
KEEP = ("reset_pico.py", "main.py")
import os

files = os.listdir()


try:
    os.uname()
    for file in range(len(files)):
        if files[file] not in KEEP:
            f = open(files[file], "w")
            f.write("no code :(")
            f.write("je moet de code nog schrijven")
            f.close()
            print(f"bestand {files[file]} gereset")
    print("pico volledig gereset")
except:
    print("save en run het bestand op de pico en niet op je laptop")
    exit
    
   


