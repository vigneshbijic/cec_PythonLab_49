calculate_square= lambda side_length: side_length ** 2

calculate_rectangle= lambda length, width: length * width

calculate_triangle= lambda base, height: 0.5 * base * height
sqs = int(input("Enter the side of the square: "))

print("Enter the base and height of the triangle:")

ht = int(input("Height: "))
bs = int(input("Base: "))

print("Enter the length and breadth of the rectangle:")

l = int(input("Length: "))
b = int(input("Breadth: "))

square_area = calculate_square(sqs)
print("Area of the square:", square_area)

triangle_area = calculate_triangle(bs, ht)
print("Area of the triangle:", triangle_area)

rectangle_area = calculate_rectangle(bs, ht)
print("Area of the rectangle:", rectangle_area)
