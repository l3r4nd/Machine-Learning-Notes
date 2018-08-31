#importing neccessary libraries
import cv2
import os

#set up the path to video
path = r"C:\Users\Prasad\Downloads\Video"
os.chdir(path)
file = os.listdir()[2]

# Capture Target Video
vid = cv2.VideoCapture(file)
# Frames to capture every sec
images_per_sec = 5
# Get info about the video
total_frames = int(vid.get(cv2.cv2.CAP_PROP_FRAME_COUNT))
fps = int(vid.get(cv2.cv2.CAP_PROP_FPS))
duration = total_frames//fps

# Set up Capture interval
interval = fps//images_per_sec
index = 0
file_name = file.split('.')[0]

try:
    os.makedirs(file_name)
except FileExistsError:
    print('File Already Exists.')
    
while True:
    status, img = vid.read()
    # Break the loop if status is False
    if status != True:
        break
    # Capture time in msec and convert it into sec
    time = int(vid.get(cv2.cv2.CAP_PROP_POS_MSEC)/1000)
    write_format = file_name + '/' + str(time) + '_' + file_name + '_frame_' + str(int(vid.get(cv2.cv2.CAP_PROP_POS_FRAMES))) + '.jpg'
    if index % interval == 0:
        cv2.imwrite(write_format, img)
    index += 1
        
vid.release()
cv2.destroyAllWindows()
