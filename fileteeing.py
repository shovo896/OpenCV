import cv2
import numpy as np

# Load images
img1_color = cv2.imread("gamma_transformed0.1.jpg")
img2_color = cv2.imread("log_transformed.jpg")

# Convert to grayscale
img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)

height, width = img2.shape

# ORB detector
orb_detector = cv2.ORB_create(5000)

# Find keypoints and descriptors
kp1, d1 = orb_detector.detectAndCompute(img1, None)
kp2, d2 = orb_detector.detectAndCompute(img2, None)

# Check if descriptors are found
if d1 is None or d2 is None:
    raise ValueError("No descriptors found! Try different images or ORB parameters.")

# Brute Force matcher
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = matcher.match(d1, d2)

if len(matches) < 4:
    raise ValueError("Not enough matches found to compute homography!")

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Keep top 90% matches
matches = matches[:int(len(matches) * 0.9)]
no_of_matches = len(matches)

# Store matched points
p1 = np.zeros((no_of_matches, 1, 2))
p2 = np.zeros((no_of_matches, 1, 2))

for i in range(no_of_matches):
    p1[i, 0, :] = kp1[matches[i].queryIdx].pt
    p2[i, 0, :] = kp2[matches[i].trainIdx].pt

# Compute Homography
homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)

# Warp perspective
transformed_img = cv2.warpPerspective(img1_color, homography, (width, height))

# Save result
cv2.imwrite('output.jpg', transformed_img)
# sorry fix this on 23 rd line 
