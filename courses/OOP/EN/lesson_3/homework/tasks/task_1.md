# More Shapes

## Part 1

Using your classes for **Shape**, **Circle**, **Rectangle** and **Square**.

Implement the necessary methods to:

* Get the area of the shape (Circle, Rectangle, Square), as a property. Except for Shape (shape can't have an area)
* Be able to compare shapes (only shapes of the same type can be compared)
    * Only shapes of the same type can be compared:
        * I should be able to compare a Circle with another circle
        * I should not be able to compare a Circle with a Square
    * I should be able to compare a Square and a Rectangle, because they have the same properties.
    * When comparing Rectangles, compare the area of the rectangle (not the width and length)
* Be able to perform addition, subtraction and multiplication of shapes (for example _rectangle1 + rectangle2_)
    * When performing such operations, perform the operations on the common properties of the 2 objects (
      width/length/radius)
    * When performing subtraction, the value of properties of a shape should not be less than 0.
    * Only shapes with the same properties can have the operations performed (ex: Circle and Square can not be added,
      Square and Rectangles can). You can use the isinstance and issubclass checks to perform the checks.
    * When performing multiplication, also allow to multiply the object with a number.
        * Example: Rectangle(2,4) * 2 = Rectangle(4,8)

## Part 2

Create a Shape service.

The methods inside shape service should all be staticmethods.

The Shape service should have the following properties as class properties:

DEFAULT_INNER_COLOR, DEFAULT_OUTER_COLOR - You can choose any string default values

The Shape service should have the following methods:

* create_default_circle(radius) - creates and returns a Circle object, with properties for colors form the defaults.
* create_default_rectangle(width, length) - creates and returns a Rectangle object, with properties for colors form the
  defaults.
* create_default_square(side_length) - creates and returns a Square object, with properties for colors from defaults.
* color_shapes(list_of_shapes, inner_color, border_color) - set's the colors of all the shapes in the list to the colors
  from the arguments.
