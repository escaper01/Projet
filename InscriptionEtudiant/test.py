
	# # Detect face
	# #Loading the HOG face detector and the shape predictpr for allignment

	# print("[INFO] Loading the facial detector")
	# detector = dlib.get_frontal_face_detector()
	# predictor = dlib.shape_predictor('face_recognition_data/shape_predictor_68_face_landmarks.dat')   #Add path to the shape predictor ######CHANGE TO RELATIVE PATH LATER
	# fa = FaceAligner(predictor , desiredFaceWidth = 96)
	# #capture images from the webcam and process and detect the face
	# # Initialize the video stream
	# print("[INFO] Initializing Video stream")
	# vs = VideoStream(src=0).start()
	# #time.sleep(2.0) ####CHECK######

	# # Our identifier
	# # We will put the id here and we will store the id with a face, so that later we can identify whose face it is
	
	# # Our dataset naming counter
	# sampleNum = 0
	# # Capturing the faces one by one and detect the faces and showing it on the window
	# while(True):
	# 	# Capturing the image
	# 	#vs.read each frame
	# 	frame = vs.read()
	# 	#Resize each image
	# 	frame = imutils.resize(frame ,width = 800)
	# 	#the returned img is a colored image but for the classifier to work we need a greyscale image
	# 	#to convert
	# 	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# 	#To store the faces
	# 	#This will detect all the images in the current frame, and it will return the coordinates of the faces
	# 	#Takes in image and some other parameter for accurate result
	# 	faces = detector(gray_frame,0)
	# 	#In above 'faces' variable there can be multiple faces so we have to get each and every face and draw a rectangle around it.
		
		
			


	# 	for face in faces:
	# 		print("inside for loop")
	# 		(x,y,w,h) = face_utils.rect_to_bb(face)

	# 		face_aligned = fa.align(frame,gray_frame,face)
	# 		# Whenever the program captures the face, we will write that is a folder
	# 		# Before capturing the face, we need to tell the script whose face it is
	# 		# For that we will need an identifier, here we call it id
	# 		# So now we captured a face, we need to write it in a file
	# 		sampleNum = sampleNum+1
	# 		# Saving the image dataset, but only the face part, cropping the rest
			
	# 		if face is None:
	# 			print("face is none")
	# 			continue


			

	# 		cv2.imwrite(directory+'/'+str(sampleNum)+'.jpg'	, face_aligned)
	# 		face_aligned = imutils.resize(face_aligned ,width = 400)
	# 		#cv2.imshow("Image Captured",face_aligned)
	# 		# @params the initial point of the rectangle will be x,y and
	# 		# @params end point will be x+width and y+height
	# 		# @params along with color of the rectangle
	# 		# @params thickness of the rectangle
	# 		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
	# 		# Before continuing to the next loop, I want to give it a little pause
	# 		# waitKey of 100 millisecond
	# 		cv2.waitKey(50)

	# 	#Showing the image in another window
	# 	#Creates a window with window name "Face" and with the image img
	# 	cv2.imshow("Add Images",frame)
	# 	#Before closing it we need to give a wait command, otherwise the open cv wont work
	# 	# @params with the millisecond of delay 1
	# 	cv2.waitKey(1)
	# 	#To get out of the loop
	# 	if(sampleNum>300):
	# 		break
	
	# #Stoping the videostream
	# vs.stop()
	# # destroying all the windows
	# cv2.destroyAllWindows()
