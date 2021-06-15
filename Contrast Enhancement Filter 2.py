import matplotlib.image as mpimg
import cv2

def main():
    image_mp= cv2.imread("rahul.jpg")
    r,c,p= image_mp.shape
    for k in range (0,p):
        for i in range (0,r):
            for j in range (0,c):
                if image_mp[i][j][k]>=255//2:
                    image_mp[i][j][k] = image_mp[i][j][k]-50
                else:
                    image_mp[i][j][k] = image_mp[i][j][k]+50 
    cv2.imwrite("enhanced2_rahul.jpg",image_mp)


if __name__=="__main__":
    main()