"""
engine.py - your micrograd engine.

This is YOUR file. You'll build the `Value` class here, one milestone at a time,
with the tutor guiding you. Don't worry about filling it all in now - start with
Milestone 1 and let the tutor walk you through it.

"""


class Value:
    def __init__(self, data, _children=()):
        self.data = data
        self.grad = 0.0
        # TODO (Milestone 1): remember this value's children so we can backprop later.

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    # TODO (Milestone 2): __add__ and __mul__
    # TODO (Milestone 3): store the local derivative for each op
    # TODO (Milestone 4): backward()
    # TODO (Milestone 5): tanh()
