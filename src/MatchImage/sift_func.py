from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

def load_data():
    path = r"D:/document/xulyanh/btl/code/src/MatchImage/data.txt"

    f = open(path, "r")
    s = f.read()
    data = s.split("\n")

    return data

def load_key_des():
    data = load_data()
    list_key = {}
    list_des = {}
    for i in range(0, len(data)):
        img = cv2.imread(data[i])
        sift = cv2.xfeatures2d.SIFT_create()
        keypoints, descriptors = sift.detectAndCompute(img, None)
        list_key[data[i]] = keypoints
        list_des[data[i]] = descriptors
    return list_key, list_des


def draw_key_sift(path1, path2):
    # bf = cv2.BFMatcher()
    # match = bf.knnMatch(des1, des2, k=2)
    # match2 = bf.knnMatch(des1, des3, k=2)
    # good = []
    # good2 = []
    # for m, n in match:
    #     if m.distance < 0.75 * n.distance:
    #         good.append([m])
    #
    # for m, n in match2:
    #     if m.distance < 0.75 * n.distance:
    #         good2.append([m])
    # print(len(good))
    # print(len(good2))
    # # print("n: ", match.n, "\n m", match.m)
    # img4 = cv2.drawMatchesKnn(img1, key1, img2, key2, good, None, flags=2)
    # img5 = cv2.drawMatchesKnn(img1, key1, img3, key3, good, None, flags=2)

    # FLANN parameters

    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    sift = cv2.xfeatures2d.SIFT_create()

    key1, des1 = sift.detectAndCompute(img1, None)
    key2, des2 = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)  # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1, des2, k=2)
    # Need to draw only good matches, so create a mask
    # matchesMask1 = [[0, 0] for i in range(len(matches1))]
    # matchesMask2 = [[0, 0] for i in range(len(matches2))]
    # ratio test as per Lowe's paper
    # for i, (m, n) in enumerate(matches1):
    #     if m.distance < 0.7 * n.distance:
    #         matchesMask1[i] = [1, 0]
    #
    # for i, (m, n) in enumerate(matches2):
    #     if m.distance < 0.7 * n.distance:
    #         matchesMask2[i] = [1, 0]
    #
    # draw_params1 = dict(matchColor=(0, 255, 0),
    #                     singlePointColor=(255, 0, 0),
    #                     matchesMask=matchesMask1,
    #                     flags=0)
    #
    # draw_params2 = dict(matchColor=(0, 255, 0),
    #                     singlePointColor=(255, 0, 0),
    #                     matchesMask=matchesMask2,
    #                     flags=0)
    # if len(matches1) >= len(matches2):
    #     img6 = cv2.drawMatchesKnn(img1, key1, img2, key2, matches1, None, **draw_params1)
    #     cv2.imshow("Image", img6)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    # else:

    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    MIN_MATCH_COUNT = 10

    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([key1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([key2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()
        h, w, d = img1.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, M)
        img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
    else:
        matchesMask = None

    draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                       singlePointColor=None,
                       matchesMask=matchesMask,  # draw only inliers
                       flags=2)

    matching_result = cv2.drawMatches(img1, key1, img2, key2, good, None, **draw_params)
    img = Image.fromarray(cv2.cvtColor(matching_result, cv2.COLOR_BGR2RGB))
    return img


def compare_sift(path):
    img1 = cv2.imread(path)

    sift = cv2.xfeatures2d.SIFT_create()
    key1, des1 = sift.detectAndCompute(img1, None)
    list_data = load_data()
    list_key, list_des = load_key_des()

    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)  # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    list_good = {}
    for i in range(0, len(list_data)):
        matches = flann.knnMatch(des1, list_des[list_data[i]], k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)
        list_good[list_data[i]] = len(good)
    return list_good