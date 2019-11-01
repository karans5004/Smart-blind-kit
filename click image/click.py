import cv2

camera = cv2.VideoCapture(0)
i = 0
while i < 10:
    input('Press Enter to capture or 1 to exit')
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.jpg', image)
    i += 1
del(camera)
