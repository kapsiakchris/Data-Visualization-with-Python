from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""

        # Attributes
        self.num_points = num_points

        # All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:

            # Decide the direction to go and how to go in that direction
            x_step = self.get_step()
            y_step = self.get_step(False)

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position relative to last position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self, x_axis=True):
        """Get Distance and Direction"""
        distance = choice(range(0,5))
        x_direction = choice([1, -1])
        y_direction = choice([0, 1])

        if x_axis:
            return x_direction * distance
        else:
            return y_direction * distance
