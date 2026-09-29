import calculator_ops
from shapes import circle, square

add_result = calculator_ops.add(2, 5)
sub_result = calculator_ops.sub(2, 5)
mul_result = calculator_ops.mul(2, 5)
div_result = calculator_ops.div(2, 5)

results = (add_result, sub_result, mul_result, div_result)
print(results)

print(circle.area(5))
print(square.area(4))