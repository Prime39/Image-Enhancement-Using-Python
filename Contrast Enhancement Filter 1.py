import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

image_mp = cv2.imread("rahul.jpg")
plt.imshow(image_mp)
plt.show()


r,c,p = image_mp.shape
for k in range (0,p):
    for i in range (0,r):
        for j in range (0,c):
            image_mp[i][j][k] = image_mp[i][j][k]+25
            
cv2.imwrite("enhanced_rahul.jpg", image_mp)
