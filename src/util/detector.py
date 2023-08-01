from retinaface import RetinaFace

def detect_faces(path):
  results = RetinaFace.detect_faces(path, threshold = 0.95, allow_upscaling=False)

  faces = []
  if type(results) != dict:
    return faces

  for face in results.values():
    x1, y1, x2, y2 = face['facial_area']
    bbox = [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]
    landmarks = {}
    for key in face['landmarks']:
      landmarks[key] = tuple(face['landmarks'][key])

    landmarks = add_extra_landmarks(landmarks)

    faces.append((face['score'], bbox, landmarks))

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