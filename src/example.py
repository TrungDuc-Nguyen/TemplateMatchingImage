import cv2

path1 = r"D:/document/xulyanh/btl/code/lena1.png"
path2 = r"D:/document/xulyanh/btl/code/lena2.png"

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

sift = cv2.xfeatures2d.SIFT_create()

key1, des1 = sift.detectAndCompute(img1, None)
key2, des2 = sift.detectAndCompute(img2, None)

# img = cv2.drawKeypoints(img1, key1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)  # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0, 0] for i in range(len(matches))]

# ratio test as per Lowe's paper
for i, (m, n) in enumerate(matches):
    if m.distance < 0.7 * n.distance:
        matchesMask[i] = [1, 0]

draw_params = dict(matchColor=(0, 255, 0),
                   singlePointColor=(255, 0, 0),
                   matchesMask=matchesMask,
                   flags=0)

img = cv2.drawMatchesKnn(img1, key1, img2, key2, matches, None, **draw_params)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()