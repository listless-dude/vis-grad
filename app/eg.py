import wrapper as w
import graph as g

a = w.Tensor([[1, 2], [3, 4]])
b = w.Tensor([[1, 2], [3, 4]])
c = w.Tensor([[1,1]])

d = a*b + c
print(d)
g.draw_dot(d)
