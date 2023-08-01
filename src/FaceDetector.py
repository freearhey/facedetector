from .util import ( detector, align, geometry )

def detect(img):
  output = []
  faces = detector.detect_faces(img)
  for face in faces:
    score, orig_bbox, landmarks = face
    pivot = landmarks['eyes_center']
    angle = align.calc_angle(landmarks)

    eye_line = [landmarks['left_eye'], landmarks['right_eye']]
    face_line = [landmarks['eyes_center'], landmarks['mouth_center']]
    face_line_length = geometry.distance(face_line)
    eye_line_length = geometry.distance(eye_line)
    max_length = max(face_line_length, eye_line_length)

    bbox_size = int(max_length / .30)
    bbox_offset_x = int(bbox_size / 2)
    bbox_offset_y = int(bbox_size * .55)
    bbox = [(0-bbox_offset_x,0-bbox_offset_y),(bbox_size-bbox_offset_x,0-bbox_offset_y),(bbox_size-bbox_offset_x,bbox_size-bbox_offset_y),(0-bbox_offset_x,bbox_size-bbox_offset_y)]
    bbox = geometry.move(bbox, (pivot[0], pivot[1]+face_line_length/2))
    bbox = geometry.rotate(bbox, pivot, angle)

    output.append({
      "score": score,
      "angle": angle,
      "size": bbox_size,
      "pivot": landmarks["face_center"],
      "bounding_box": bbox,
      "landmarks": landmarks
    })

  return output