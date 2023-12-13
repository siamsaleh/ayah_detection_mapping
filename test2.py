import cv2

# Read gray image
img = cv2.imread("sample/page-600.png", 0)

# Create default parametrization LSD
lsd = cv2.createLineSegmentDetector(0)

# Detect lines in the image
lines = lsd.detect(img)[0]  # Position 0 of the returned tuple are the detected lines
print(len(lines))
# Draw detected lines in the image
drawn_img = lsd.drawSegments(img, lines)

# Show image
cv2.imshow("LSD", drawn_img)
cv2.waitKey(0)
