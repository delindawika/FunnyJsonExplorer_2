# FunnyJsonExplorer_2
For this task, using the code from the first Funny Json Explorer project as the basis, modify it so that it uses the iterator(迭代器)+strategy(访问者) or the iterator(迭代器)+visitor(策略) design pattern.

## UML Diagram

## Design pattern
Here in our code, we use the **iterator(迭代器)+strategy(访问者)** design pattern.
 
### Iterator (迭代器)
The Iterator design pattern is used to provide a way to access elements of a collection object sequentially without exposing its underlying representation.
#### a. Iterator Interface: Iterator()
The base Iterator class provides the interface for the iterator. It includes:
(i) An initializer (__init__) that sets up the initial state (index).
(ii) An abstract method has_next() that should return a boolean indicating if there are more elements to iterate over.
(iii) An abstract method next() that should return the next element in the collection.

##### - Concrete Iterator Class: ContainerIterator(Iterator)

The Concrete Iterator class inherits from Iterator and provides a concrete implementation of the iterator for a specific collection. The client code uses the ContainerIterator to        traverse the children. It plays a crucial role in the draw method by managing the traversal of the container's children, ensuring that the Container can easily iterate over its       children and draw them in the correct sequence. 

### Strategy (访问者)
The strategy design pattern is used to define a family of algorithms, encapsulate each one, and make them interchangeable. 
#### a. Strategy Interface : StyleStrategy()
The Container class uses a Style Strategy to draw itself and its children, whether it uses Tree Style Strategy or Rectangle Style Strategy. The strategy design pattern allows for flexible and interchangeable drawing strategies for containers and leaves. 

##### - Concrete Strategy Class: TreeStyleStrategy(StyleStrategy) & RectangleStyleStrategy(StyleStrategy)

These classes provide specific implementations of the drawing methods. Each class provides its own way to draw containers and leaves, allowing for different visual representations.

## Output
Using the test cases from example.json file
<img width="1069" alt="Screenshot 2024-06-15 at 02 38 24" src="https://github.com/delindawika/FunnyJsonExplorer_2/assets/65715881/a11ccf5c-1339-42a3-b7d1-99fb3eb2ff15">

#### Style=Tree style, icon=poker-face
<img width="690" alt="Screenshot 2024-06-15 at 02 35 16" src="https://github.com/delindawika/FunnyJsonExplorer_2/assets/65715881/5c4859f3-68d0-4722-9dc3-12d258265b13">

#### Style=Tree style, icon=moon-sun
<img width="673" alt="Screenshot 2024-06-15 at 02 35 45" src="https://github.com/delindawika/FunnyJsonExplorer_2/assets/65715881/c287d7b1-0edd-4ef3-883c-8873af8b8231">

#### Style=Rectangle style, icon=poker-face
<img width="723" alt="Screenshot 2024-06-15 at 02 36 09" src="https://github.com/delindawika/FunnyJsonExplorer_2/assets/65715881/6372a586-ed0f-44bf-9662-95d56fc611b6">

#### Style=Rectangle style, icon=moon-sun
<img width="714" alt="Screenshot 2024-06-15 at 02 36 30" src="https://github.com/delindawika/FunnyJsonExplorer_2/assets/65715881/efabb84c-728a-4f86-9860-c44512b222b6">
