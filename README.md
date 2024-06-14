# FunnyJsonExplorer_2
For this task, using the code from the first Funny Json Explorer project as the basis, modify it so that it uses the iterator(迭代器)+strategy(访问者) or the iterator(迭代器)+visitor(策略) design pattern.

## UML Diagram

## Design pattern
Here in our code, we use the iterator(迭代器)+strategy(访问者) design pattern
 
### Iterator (迭代器)
The Iterator design pattern is used to provide a way to access elements of a collection object sequentially without exposing its underlying representation.
#### Iterator Interface: Iterator()
The base Iterator class provides the interface for the iterator. It includes:
- An initializer (__init__) that sets up the initial state (index).
- An abstract method has_next() that should return a boolean indicating if there are more elements to iterate over.
- An abstract method next() that should return the next element in the collection.

a. Concrete Iterator Class: ContainerIterator(Iterator)

The Concrete Iterator class inherits from Iterator and provides a concrete implementation of the iterator for a specific collection. The client code uses the ContainerIterator to        traverse the children. It plays a crucial role in the draw method by managing the traversal of the container's children, , ensuring that the Container can easily iterate over its       children and draw them in the correct sequence. 

### Strategy (访问者)
The strategy design pattern is used to define a family of algorithms, encapsulate each one, and make them interchangeable. 
#### Strategy Interface : StyleStrategy()
The Container class uses a Style Strategy to draw itself and its children, whether it uses Tree Style Strategy or Rectangle Style Strategy. The strategy design pattern allows for flexible and interchangeable drawing strategies for containers and leaves. 
a. Concrete Strategy Class: TreeStyleStrategy(StyleStrategy) & RectangleStyleStrategy(StyleStrategy)
These classes provide specific implementations of the drawing methods. Each class provides its own way to draw containers and leaves, allowing for different visual representations.



## Output
Using the test cases from example.json file

#### Style=Tree style, icon=poker-face
#### Style=Tree style, icon=moon-sun
#### Style=Rectangle style, icon=poker-face
#### tyle=Rectangle style, icon=moon-sun
