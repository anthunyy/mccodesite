from PIL import ImageGrab
import time

# Capture the entire screen
time.sleep(5)
screenshot = ImageGrab.grab()

# Save the screenshot to a file
screenshot.save("screenshot.png")

# Close the screenshot
screenshot.close()

# Capture a specific region (left, top, right, bottom)
screenshot = ImageGrab.grab(bbox=(100, 100, 500, 500))
