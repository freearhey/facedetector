from retinaface import RetinaFace
from .utils import (calc_distance, calc_angle, calc_bbox, calc_coords)

def detect(img):
  results = RetinaFace.detect_faces(img, threshold = 0.95, allow_upscaling=False)

  faces = []
  if type(results) != dict:
    return faces

  for face in results.values():
    x1, y1, x2, y2 = face['facial_area']
    landmarks = {}
    for key in face['landmarks']:
      landmarks[key] = tuple(face['landmarks'][key])

    landmarks = add_extra_landmarks(landmarks)

    pivot = landmarks['eyes_center']
    angle = calc_angle(landmarks)
    coords = calc_coords(landmarks, pivot, angle)
    bbox = calc_bbox(coords)
    pivot = landmarks["face_center"]

    faces.append({
      "score": face['score'],
      "angle": angle,
      "pivot": landmarks["face_center"],
      "coordinates": coords,
      "bounding_box": bbox,
      "landmarks": landmarks
    })

  return faces

def add_extra_landmarks(landmarks):
  #left eye is the eye appearing on the left (right eye of the person)
  left_eye_x, left_eye_y = landmarks["right_eye"]
  right_eye_x, right_eye_y = landmarks["left_eye"]
  left_mouth_x, left_mouth_y = landmarks["mouth_right"]
  right_mouth_x, right_mouth_y = landmarks["mouth_left"]
  nose_x, nose_y = landmarks["nose"]

  eyes_center_x, eyes_center_y = (int((left_eye_x + right_eye_x) / 2), int((left_eye_y + right_eye_y) / 2))
  mouth_center_x, mouth_center_y = (int((left_mouth_x + right_mouth_x) / 2), int((left_mouth_y + right_mouth_y) / 2))
  landmarks['eyes_center'] = (eyes_center_x, eyes_center_y)
  landmarks['mouth_center'] = (mouth_center_x, mouth_center_y)
  landmarks['face_center'] = (int((eyes_center_x + mouth_center_x) / 2), int((eyes_center_y + mouth_center_y) / 2))

  return landmarks