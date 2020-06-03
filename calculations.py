import Figures.quadrangles.square as square, circle, triangle

sq = square.Square(5)
print("Field: ", sq.getField(), " Perimeter: ", sq.getCircunference())

tr = triangle.EquilateralTriangle(5)
print("Field: ", tr.getField(), " Perimeter: ", tr.getCircunference())

ci = circle.Circle(5)
print("Field: ", ci.getField(), " Perimeter: ", ci.getCircunference())
