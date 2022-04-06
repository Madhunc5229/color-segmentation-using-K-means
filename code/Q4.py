import cv2
import numpy as np
import random
import copy

#Function to calucate mean of one group of points
def meanOfPoints(group):

    column_average = [int((sum(sub_list) / len(sub_list))) for sub_list in zip(*group)]

    return column_average

#K-means algorithm function
def kMeans(image):
    #copy image
    img = copy.deepcopy(image)

    #assigning random colors from img as starting points
    k1 = list(img[random.randint(0,img.shape[0]),random.randint(0,img.shape[1])])
    k2 = list(img[random.randint(0,img.shape[0]),random.randint(0,img.shape[1])])
    k3 = list(img[random.randint(0,img.shape[0]),random.randint(0,img.shape[1])])
    k4 = list(img[random.randint(0,img.shape[0]),random.randint(0,img.shape[1])])

    #loop start
    while True:
        group_1_points = []
        group_1_ind = []
        group_2_points = []
        group_2_ind = []
        group_3_points = []
        group_3_ind = []
        group_4_points = []
        group_4_ind = []

        #Looping through the image
        for x in range(0,img.shape[1]):
            for y in range(0,img.shape[0]):

                #Calculating euclidean distance of the points from mean value
                dist_from_1 = np.linalg.norm(k1-img[y,x])
                dist_from_2 = np.linalg.norm(k2-img[y,x])
                dist_from_3 = np.linalg.norm(k3-img[y,x])
                dist_from_4 = np.linalg.norm(k4-img[y,x])

                #check which group does the point belong to
                close_to_group_1 = dist_from_1 < dist_from_2 and dist_from_1 < dist_from_3 and dist_from_1 < dist_from_4
                close_to_group_2 = dist_from_2 < dist_from_1 and dist_from_2 < dist_from_3 and dist_from_2 < dist_from_4
                close_to_group_3 = dist_from_3 < dist_from_1 and dist_from_3 < dist_from_2 and dist_from_3 < dist_from_4
                close_to_group_4 = dist_from_4 < dist_from_1 and dist_from_4 < dist_from_2 and dist_from_4 < dist_from_3

                
                if close_to_group_1:
                    group_1_points.append(img[y,x])
                    group_1_ind.append([y,x])

                if close_to_group_2:
                    group_2_points.append(img[y,x])
                    group_2_ind.append([y,x])

                if close_to_group_3:
                    group_3_points.append(img[y,x])
                    group_3_ind.append([y,x])

                if close_to_group_4:
                    group_4_points.append(img[y,x])
                    group_4_ind.append([y,x])

        #calculate average of the groups and assign as new means
        new_k1 = meanOfPoints(group_1_points)
        new_k2 = meanOfPoints(group_2_points)
        new_k3 = meanOfPoints(group_3_points)
        new_k4 = meanOfPoints(group_4_points)

        #check if the mean is not changing and break the loop
        if k1 == new_k1 and k2 == new_k2 and k3 == new_k3 and k4 == new_k4:

            print("the 4 colors are:..")
            print(k1)
            print(k2)
            print(k3)
            print(k4)

            break

        else:
            print("clustering again...")
            k1 = new_k1
            k2 = new_k2
            k3 = new_k3
            k4 = new_k4
    
    #assign the 4 colors according to groups
    for ind in group_1_ind:
        img[ind[0],ind[1]] = (k1[0],k1[1],k1[2])
    for ind in group_2_ind:
        img[ind[0],ind[1]] = (k2[0],k2[1],k2[2])
    for ind in group_3_ind:
        img[ind[0],ind[1]] = (k3[0],k3[1],k3[2])
    for ind in group_4_ind:
        img[ind[0],ind[1]] = (k4[0],k4[1],k4[2])

    return img



if __name__ == '__main__':

    #reading the image
    img = cv2.imread('Q4image.png')

    #calling the K means function
    color_segmented = kMeans(img)

    cv2.imshow('original',img)
    cv2.imshow('color segmented using K-means',color_segmented)
    cv2.waitKey(0)