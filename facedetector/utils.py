import numpy as np
import math

def calc_coords(landmarks, pivot, angle):
  eye_line = [landmarks['left_eye'], landmarks['right_eye']]
  face_line = [landmarks['eyes_center'], landmarks['mouth_center']]
  face_line_length = calc_distance(face_line)
  eye_line_length = calc_distance(eye_line)
  max_length = max(face_line_length, eye_line_length)
  bbox_size = int(max_length / .5)
  bbox_offset_x = int(bbox_size / 2)
  bbox_offset_y = int(bbox_size * .55)
  coords = [(0-bbox_offset_x,0-bbox_offset_y),(bbox_size-bbox_offset_x,0-bbox_offset_y),(bbox_size-bbox_offset_x,bbox_size-bbox_offset_y),(0-bbox_offset_x,bbox_size-bbox_offset_y)]
  coords = move(coords, (pivot[0], pivot[1]+face_line_length/2))
  coords = rotate(coords, pivot, angle)

  return coords

def find_euclidean_distance(source_representation, test_representation):
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

  a = find_euclidean_distance(np.array(mouth_center), np.array(point_3rd))
  b = find_euclidean_distance(np.array(eyes_center), np.array(point_3rd))
  c = find_euclidean_distance(np.array(eyes_center), np.array(mouth_center))

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

def rotate(points, origin, deg):
  angle = math.radians(deg)
  pts = []
  for point in points:
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    pts.append((int(qx), int(qy)))
  
  return pts

def calc_distance(points):
  p1x, p1y = points[0]
  p2x, p2y = points[1]

  return math.sqrt((p1x-p2x)**2 + (p1y-p2y)**2)

def move(points, origin):
  pts = []
  for point in points:
    ox, oy = origin
    px, py = point

    qx = px + ox
    qy = py + oy

    pts.append((int(qx), int(qy)))

  return pts

def calc_bbox(points):
  minx, miny = float("inf"), float("inf")
  maxx, maxy = float("-inf"), float("-inf")
  for x, y in points:
    if x < minx:
      minx = x
    if y < miny:
      miny = y
    if x > maxx:
      maxx = x
    elif y > maxy:
      maxy = y

  width = maxx - minx
  height = maxy - miny

  return {
    'x': minx,
    'y': miny,
    'width': width,
    'height': height
  }