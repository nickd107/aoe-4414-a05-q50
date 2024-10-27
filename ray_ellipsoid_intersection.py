# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z...
# Finds the intersection point (if it exists) between a ray and the Earth reference ellipsoid


# Parameters: Assumed to be in km for c_l
# d_l_x: x-component of origin-referenced ray direction
# d_l_y: y-component of origin-referenced ray direction
# d_l_z: z-component of origin-referenced ray direction
# c_l_x: x-component offset of ray origin
# c_l_y: y-component offset of ray origin
# c_l_z: z-component offset of ray origin


# Output:
# l_d[0] # x-component of intersection point
# l_d[1] # y-component of intersection point
# l_d[2] # z-component of intersection point


# Written by Nick Dickson

# import Python modules
import math # math module
import sys # argv

# constants
R_E_KM = 6378.137
E_E    = 0.081819221456

#Vector Magnitude
def mag(v):
  sum_of_squares = 0.0
  for i in range(0, len(v)):
    sum_of_squares += v[i]*v[i]
  return math.sqrt(sum_of_squares)

#Scalar Multi multiplication
def smul(s,v):
  sprod=[]
  for i in range(0,len(v)):
    sprod.append(s*v[i])
  return sprod
  #return [s*e for e in v] This does same thing

#Vector Addition
def add(v1,v2):
  if len(v1) != len(v2):
    return None
  else:
    v3=[]
    for i in range(0,len(v1)):
      v3.append(v1[i]+v2[i])
    return v3
#Vetcor Subtraction
def sub(v1,v2):
  if len(v1) != len(v2):
    return None
  else:
    v3=[]
    for i in range(0,len(v1)):
      v3.append(v1[i]-v2[i])
    return v3
  
# dot product
def dot(v1,v2):
  if len(v1) != len(v2):
    return float('nan')
  else:
    dp=0.0
    for i in range(0,len(v1)):
      dp += v1[i]*v2[i]
    return dp

# initialize script arguments
d_l_x = float('nan') 
d_l_y = float('nan') 
d_l_z = float('nan') 
c_l_x = float('nan')
c_l_y = float('nan')
c_l_z = float('nan')

# parse script arguments
if len(sys.argv) == 7:
  d_l_x = float(sys.argv[1])
  d_l_y = float(sys.argv[2])
  d_l_z = float(sys.argv[3])
  c_l_x = float(sys.argv[4])
  c_l_y = float(sys.argv[5])
  c_l_z = float(sys.argv[6])
else:
  print(\
    'Usage: '\
    'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
  )
  exit()

### script below this line ###
## setup vectors
d_l = [d_l_x, d_l_y, d_l_z] #must be a unit vector
c_l = [c_l_x, c_l_y, c_l_z] 

# if mag(d_l) != 1:
#   d_l = [d_l_x/mag(d_l), d_l_y/mag(d_l), d_l_z/mag(d_l)]
#   d_l_x = d_l[0]
#   d_l_y = d_l[1]
#   d_l_z = d_l[2]

# determinant
a = d_l_x**2 + d_l_y**2 + (d_l_z**2)/(1-E_E**2)
b = 2 * (d_l_x * c_l_x + d_l_y * c_l_y + (d_l_z * c_l_z)/(1-E_E**2))
c = c_l_x**2 + c_l_y**2 + (c_l_z**2)/(1-E_E**2) - R_E_KM**2
discr = b*b - 4*a*c 

##solution logic
if discr>=0.0:
  d = (-b-math.sqrt(discr))/(2*a)
if d<0.0:
  d = (-b+math.sqrt(discr))/(2*a)
if d>=0.0:
  l_d = add(smul(d,d_l),c_l)
  print(l_d[0])
  print(l_d[1])
  print(l_d[2])
#If nothing prints, no intersection