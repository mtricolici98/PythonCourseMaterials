# Basic on Composition

Create a class that describes a pet.

A pet should have the following properties:

* A name - string
* A type (cat/dog/bird) - string
* A favourite food - string

All the properties above should be initialized in the constructor function, by arguments to the constructor.

When a pet object is printed it should output something like this:

`Cat called Garfield that loves lasagna`
or
`Dog called Kuzea that loves bones`

Also create a new class HumanWithPet:

The HumanWithPet should have the same properties as the Human in the other exercise.

Additionally, the HumanWithPet class should have a list of pets as a instance property.

Add two methods to the HumanWithPet class:

* Adopt new pet - Adds a new pet object to the list of pets
* Give away pet - Removes a pet from the humans list of pets

When printing a HumanWithPet object, the console should output the according to the following examples:

`Marius Tricolici, age 24 with a pet: Cat called Garfield that loves lasagna` - If the human has 1 pets.

`Marius Tricolici, age 24 with 2 pets: Cat called Garfield that loves lasagna, Dog called Kuzea that loves bones` - If
the human has 2 or more pets.
