from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

path = r"D:\document\xulyanh\btl\code\data\coca_cola2.jpg"
path2 = r"D:\document\xulyanh\btl\code\data\coca_cola3.jpg"

# img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
img = cv2.imread(path)
img1 = cv2.imread(path2)

sift = cv2.xfeatures2d.SIFT_create()
surf = cv2.xfeatures2d.SURF_create()

keypoints_sift, descriptors_sift = sift.detectAndCompute(img, None)
keypoints_sift1, descriptors_sift1 = sift.detectAndCompute(img1, None)

# img = cv2.drawKeypoints(img, keypoints_sift, None)

keypoints_surf, descriptors_surf = surf.detectAndCompute(img, None)
keypoints_surf1, descriptors_surf1 = surf.detectAndCompute(img1, None)

# Brute Force Matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bf.match(descriptors_sift, descriptors_sift1)
matches = sorted(matches, key=lambda x: x.distance)

bf_surf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches_surf = bf_surf.match(descriptors_surf, descriptors_surf1)
matches_surf=sorted(matches_surf, key=lambda x:x.distance)

matching_result = cv2.drawMatches(img, keypoints_sift, img1, keypoints_sift1, matches[:50], None, flags=2)
matching_result_surf = cv2.drawMatches(img, keypoints_surf, img1, keypoints_surf1, matches_surf[:50], None, flags=2)

# cv2.imwrite("result.jpg", img)

cv2.imshow("Matching result", matching_result_surf)
cv2.imshow("Matching result", matching_result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# plt.imshow(img)
# plt.show()
