# PDF417 Barcode Reader using a Webcam

I have started this project due to a need of reading a PDF417 barcode using a Webcam. I tried to use the zBar package but I was not able to achieve my goal, other people had the same problem.

In this project I used the zXing package to decode the PDF417 barcode.

The idea was to create a barcode reader that is always working and trying to read the code in front the camera and the solution to be able to do it was to save one image each second and try to decode the barcode on this image.

That is just a initial idea and I'll add more features during the project evolution.
