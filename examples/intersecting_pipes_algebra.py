from build123d import *
from ocp_vscode import show

pipes = Rot(10, 20, 30) * Box(10, 10, 10)

for plane in [Plane(f) for f in pipes.faces()]:
    pipe = plane * Circle(4)
    pipes -= extrude(pipe, amount=-5)
    pipe = plane * Circle(4.5)
    pipe -= plane * Circle(4)

    last = pipes.edges()
    pipes += extrude(pipe, amount=10)
    pipes = fillet(pipes.edges() - last, 0.2)

show(pipes, names=["intersecting pipes"])
