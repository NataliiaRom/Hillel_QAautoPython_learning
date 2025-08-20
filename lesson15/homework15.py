class Rhombus:
# a_side >0
#angle_a + angle_b = 180
    def __init__(self,a_side,angle_a):
        self.a_side = a_side
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        # rules for angle_a assignment
        if key == "angle_a":
            if isinstance(value,int):
                if 0 < value < 180:
                    print(f"Setting a new value for {key}...")
                    print(f"Setting a new value for angle_b...\n")
                    super().__setattr__("angle_b", 180 - value)
                else:
                    raise ValueError("angle_a value should be inside (0 to 180) scope")
            else:
                raise TypeError("angle_a value should have INT type")

        # rules for angle_B assignment
        def __setattr__(self, key, value):
            if key == "angle_b":
                if isinstance(value, int):
                    if 0 < value < 180:
                        print(f"Setting a new value for {key}...")
                        print(f"Setting a new value for angle_a...\n")
                        super().__setattr__("angle_a", 180 - value)
                    else:
                        raise ValueError("angle_b value should be inside (0 to 180) scope")
                else:
                    raise TypeError("angle_b value should have INT type")

        # rules for a_side assignment
        if key == "a_side":
            if isinstance(value,int):
                if value < 0:
                    raise ValueError("a_side should have a positive value")
                else:
                    print(f"Setting a new value for {key}...\n")
            else:
                raise TypeError("a_side should have INT type")

        super().__setattr__(key, value)


r = Rhombus(45,67)

print(f"||| Initial values for object Rhombus are: a_side = {r.a_side}, angle_a = {r.angle_a}, "
      f"angle_b = {r.angle_b}\n")

r.a_side = 34
r.angle_a = 179

print(f"||| New values for object Rhombus are: a_side = {r.a_side}, angle_a = {r.angle_a}, "
      f"angle_b = {r.angle_b}\n")

r.angle_b = 30

print(f"||| New values for object Rhombus are: a_side = {r.a_side}, angle_a = {r.angle_a}, "
      f"angle_b = {r.angle_b}\n")
