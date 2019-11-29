# import the necessary packages
from imutils.video import VideoStream
import zxing
import imutils
import cv2

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()

# initialize the zxing BarCodeReader
reader = zxing.BarCodeReader()

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to
	# have a maximum width of 400 pixels
	frame = vs.read()

    # create the image that will be used by the decoder
	imageName = '_.jpg'
	cv2.imwrite(imageName, frame)

    # find the barcode in the frame and decode it
	barcodes = reader.decode(imageName)

    # check if some info was found
	if barcodes is not None:
		# print the value read
		print(barcodes.raw)

		# get the barcode top-left position
		x1 = int(barcodes.points[0][0])
		y1 = int(barcodes.points[0][1])

		# draw the barcode data and barcode type on the image
		cv2.putText(frame, barcodes.raw, (x1, y1 - 50),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

	# show the output frame
	cv2.imshow("Reading PDF 417 with Webcam", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()