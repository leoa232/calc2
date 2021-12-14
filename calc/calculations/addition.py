"""This is the addition calculation that is being inherits the value A and value B from calculation class"""
# this is called a namespace is is lime files and folders the classes are files and the folders organize the classes
# It looks like a folder and file path but is is sort of a virtual representation of how the program is organized

from calc.calculation import Calculation


# This is how you extend the Addition class with the Calculation

class Addition(Calculation):
    """The addition class has one method to get the result of the calculator A and B come from the calculation parent"""
    def get_result(self):
        """get the addition results"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values