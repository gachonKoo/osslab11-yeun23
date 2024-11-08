from geo import area, distance

print("Circle area with radius 5:", area.circle_area(5))
print("Rectangle area with width 4 and height 6:", area.rectangle_area(4, 6))
print("Euclidean distance between (1, 2) and (4, 6):", distance.euclidean_distance(1, 2, 4, 6))
print("Manhattan distance between (1, 2) and (4, 6):", distance.manhattan_distance(1, 2, 4, 6))
