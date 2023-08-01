import math

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

def distance(points):
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