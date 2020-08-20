import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def calcGrayHist(I):
    # Calculate gray histogram
    h, w = I.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    for i in range(h):
        for j in range(w):
            grayHist[I[i][j]] += 1
    return grayHist


def equalHist(img):
    # The height and width of the gray image
    h, w = img.shape[0], img.shape[1]
    # Step 1: Calculate the gray histogram
    grayHist = calcGrayHist(img)
    # Step 2: Calculate the cumulative gray histogram
    zeroCumuMoment = np.zeros([256], np.uint32)
    for p in range(256):
        if p == 0:
            zeroCumuMoment[p] = grayHist[0]
        else:
            zeroCumuMoment[p] = zeroCumuMoment[p - 1] + grayHist[p]
    # Step 3: Obtain the mapping relationship between the input gray level
    # and the output gray level according to the accumulated gray histogram
    outPut_q = np.zeros([256], np.uint8)
    cofficient = 256.0 / (h * w)
    for p in range(256):
        q = cofficient * float(zeroCumuMoment[p]) - 1
        if q >= 0:
            outPut_q[p] = np.floor(q)
        else:
            outPut_q[p] = 0
    # Step 4: Obtain the equalized image of the histogram
    equalHistImage = np.zeros(img.shape, np.uint8)
    for i in range(h):
        for j in range(w):
            equalHistImage[i][j] = outPut_q[img[i][j]]
    return equalHistImage


def main():
    img_name = sys.argv[1]
    img = cv2.cvtColor(cv2.imread(img_name), cv2.COLOR_BGR2RGB)
    # Use your own function to implement
    equa = equalHist(img)

    # plt.hist(equa.ravel(),256,[0,256])
    plt.imshow(equa)
    plt.show()


if __name__ == '__main__':
    main()


# plt.hist(img.ravel(),256,[0,256])
# plt.show()
