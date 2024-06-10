import math
import setuptools

def euclideanDistance(point1, point2):
  """
  İki nokta arasındaki Öklid mesafesini hesaplar.

  Args:
    point1: (x1, y1) şeklinde bir demet.
    point2: (x2, y2) şeklinde bir demet.

  Returns:
    İki nokta arasındaki Öklid mesafesi.
  """
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def minimumDistance(points):
  """
  Bir nokta listesindeki minimum Öklid mesafesini hesaplar.

  Args:
    points: 2D uzaydaki noktaları temsil eden demetlerin bir listesi.

  Returns:
    Minimum Öklid mesafesi.
  """
  distances = []
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      distance = euclideanDistance(points[i], points[j])
      distances.append(distance)

  minimumDistance = min(distances)
  return minimumDistance

# Noktaları tanımlayın
points = [(1, 2), (4, 5), (3, 1), (7, 6)]

# Minimum mesafeyi hesaplayın
minimumDistance = minimumDistance(points)

# Sonucu yazdırın
print("Minimum Öklid mesafesi:", minimumDistance)
