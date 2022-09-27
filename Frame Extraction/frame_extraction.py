# import the necessary packages
import os
import os.path
import cv2
import numpy as np

# declare variables
dataset_dir_path = "Dataset Name"
frames_dir_path = "Dataset_Frames"

# name of class to be loaded
classes = ['Class1', 'Class2'] 

def frame_extraction(video_path):
	dir_path = os.path.splitext(video_path)[0]
	frame_path = os.path.join(frames_dir_path, os.path.relpath(dir_path, 'Dataset Name//'))
	vidObj = cv2.VideoCapture(video_path)
	count = 0
	
	while True:
		success, frame = vidObj.read()
		
		if success:
			count += 1
		
		if not success:
			break
		
		try:
			os.makedirs(frame_path, exist_ok = True)
			pass
		
		except OSError as error:
			pass
		
		cv2.imwrite(frame_path+"/"+str(count)+'.jpg', frame)

def load_data(dataset_dir_path): 
	classes_list = os.listdir(dataset_dir_path) 
	
	for class_name in classes_list:
		print("[INFO]-||- " + class_name + " class frames are being extracted")
		
		if class_name in classes:
			videos_list = os.listdir(os.path.join(dataset_dir_path, class_name))
			
			for video in videos_list:
				frame_extraction(os.path.join(os.path.join(dataset_dir_path, class_name), video))

load_data(dataset_dir_path)

