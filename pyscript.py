from PIL import ImageGrab
import time
import keyboard
import os
time.sleep(5)
while True:
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    screenshot.close()
    screenshot = ImageGrab.grab(bbox=(100, 100, 500, 500))
    os.system("cd mccodesite/mccodesite")
    os.system("git add --all")
    time.sleep(2.5)
    os.system("git commit -m \"new screenshot\"")
    time.sleep(2.5)
    os.system("git push")
    time.sleep(3600)

