image = np.zeros((512, 512, 3), np.uint8)
drawing = False
ix, iy = -1, -1

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing
    
    #Check to see if the Left mouse button is pressed.
    if event == cv2.EVENT_LBUTTONDOWN:
        #enable drawing
        drawing = True
        ix, iy = x, y
    
    #If mouse is moved while the left mouse button is pressed start drawing
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(image, (x,y), 10, (0, 255, 0), -1)
    
    #If mouse button is released stop drawing
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


#create a window to draw (Note: you draw on 'blank' named window to see the drawing on 'image' named window)
cv2.namedWindow('blank')
#create a callback function
cv2.setMouseCallback('blank', draw_circle)

while True:
    #display the blank image.
    cv2.imshow('image', image)
    
    key = cv2.waitKey(1) & 0xFF
    #If 'c' key is pressed at any point in time then break
    if key == ord('c'):
        break
        
cv2.destroyAllWindows()
