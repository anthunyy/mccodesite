from PIL import ImageGrab
import time
import keyboard
time.sleep(5)
while True:
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    screenshot.close()
    screenshot = ImageGrab.grab(bbox=(100, 100, 500, 500))
    time.sleep(3600)

