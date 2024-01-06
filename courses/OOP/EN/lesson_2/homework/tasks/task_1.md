# Some Shapes

Create the classes listed below. Use Inheritance.

For all the properties, use underscores inside the class to hide the properties (example self._inner_color), and declare
get and set methods (example set_inner_color).

Create a Class that describes a **Shape**

The shape class should have the following properties:

* inner color
* border color

Create another class **Circle** which extends **Shape**.

The circle class should have the following additional properties.

* radius

Create another class **Rectangle** which also extends **Shape**

The rectangle class should have the following additional properties.

* width
* length

Create another class **Square** that extends **Rectangle**

The Square class should make sure that the width and length are equal when one of them is set. For example if I set
square.set_length(4), square.get_width() should also be 4.
