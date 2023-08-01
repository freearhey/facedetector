import numpy as np
import math

def findEuclideanDistance(source_representation, test_representation):
  euclidean_distance = source_representation - test_representation
  euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance))
  euclidean_distance = np.sqrt(euclidean_distance)
  return euclidean_distance

def calc_angle(landmarks):
  eyes_center, mouth_center = landmarks['eyes_center'], landmarks['mouth_center']

  eyes_center_x, eyes_center_y = eyes_center
  mouth_center_x, mouth_center_y = mouth_center

  #-----------------------
  #find rotation direction

  if eyes_center_x < mouth_center_x:
    point_3rd = (mouth_center_x, eyes_center_y)
    direction = -1 #rotate same direction to clock
  else:
    point_3rd = (eyes_center_x, mouth_center_y)
    direction = 1 #rotate inverse direction of clock

  #-----------------------
  #find length of triangle edges

  a = findEuclideanDistance(np.array(mouth_center), np.array(point_3rd))
  b = findEuclideanDistance(np.array(eyes_center), np.array(point_3rd))
  c = findEuclideanDistance(np.array(eyes_center), np.array(mouth_center))

  #-----------------------

  #apply cosine rule

  angle = 0
  if b != 0 and c != 0: #this multiplication causes division by zero in cos_a calculation

    cos_a = (b*b + c*c - a*a)/(2*b*c)
    
    #PR15: While mathematically cos_a must be within the closed range [-1.0, 1.0], floating point errors would produce cases violating this
    #In fact, we did come across a case where cos_a took the value 1.0000000169176173, which lead to a NaN from the following np.arccos step
    cos_a = min(1.0, max(-1.0, cos_a))
    
    
    angle = np.arccos(cos_a) #angle in radian
    angle = (angle * 180) / math.pi #radian to degree

    #-----------------------
    #rotate base image

    if direction == -1:
      angle = 90 - angle

    # if eyes_center[1] > nose[1]:
    #   angle = 180

  #-----------------------

  return direction * angle