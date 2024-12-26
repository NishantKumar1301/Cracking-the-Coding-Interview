"""QUESTION 5 : Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a 
strictly"first in, first out" basis. People must adopt either the "oldest" (based on arrival time)
of all animals at the shelter, or they can select whether they would prefer a dog or a cat 
(and will receive the oldest animal of that type). They cannot select which specific animal they 
would like. Create the data structures to maintain this system and implement operations such as 
enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list data structure."""

class Node:
    def __init__(self, animal, type):
        self.animal = animal
        self.type = type
        self.next = None

class AnimalShelter:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, animal, type):
        new_animal = Node(animal, type)
        if not self.head:
            self.head = new_animal
            self.tail = new_animal
        else:
            self.tail.next = new_animal
            self.tail = new_animal
    
    def dequeueAny(self):
        if not self.head:
            return None
        animal = self.head.animal
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return animal
    
    def dequeueDog(self):
        if not self.head:
            return None
        
        # If head is a dog
        if self.head.type == "Dog":
            dog = self.head.animal
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return dog
        
        # Search for the first dog
        current = self.head
        while current.next and current.next.type != "Dog":
            current = current.next
        
        if current.next:
            dog = current.next.animal
            current.next = current.next.next
            if not current.next:
                self.tail = current
            return dog
        return None
            
    def dequeueCat(self):
        if not self.head:
            return None
        
        if self.head.type == "Cat":
            cat = self.head.animal
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return cat
        
        curr = self.head
        while curr.next and curr.next.type != "Cat":
            curr = curr.next
            
        if curr.next:
            cat = curr.next.animal
            curr.next = curr.next.next
            if not curr.next:
                self.tail = curr
            return cat
        return None

def test_animal_shelter():
    # Test Case 1: Basic operations
    print("\nTest Case 1: Basic operations")
    shelter = AnimalShelter()
    
    # Test empty shelter
    print("Empty shelter dequeue:", shelter.dequeueAny())  # Should print None
    print("Empty shelter dequeue dog:", shelter.dequeueDog())  # Should print None
    print("Empty shelter dequeue cat:", shelter.dequeueCat())  # Should print None
    
    # Test Case 2: Alternating cats and dogs
    print("\nTest Case 2: Alternating cats and dogs")
    shelter = AnimalShelter()
    shelter.enqueue("Cat1", "Cat")
    shelter.enqueue("Dog1", "Dog")
    shelter.enqueue("Cat2", "Cat")
    shelter.enqueue("Dog2", "Dog")
    
    print("Dequeue any:", shelter.dequeueAny())  # Should print Cat1
    print("Dequeue dog:", shelter.dequeueDog())  # Should print Dog1
    print("Dequeue cat:", shelter.dequeueCat())  # Should print Cat2
    print("Dequeue any:", shelter.dequeueAny())  # Should print Dog2
    
    # Test Case 3: All cats then all dogs
    print("\nTest Case 3: All cats then all dogs")
    shelter = AnimalShelter()
    shelter.enqueue("Cat1", "Cat")
    shelter.enqueue("Cat2", "Cat")
    shelter.enqueue("Cat3", "Cat")
    shelter.enqueue("Dog1", "Dog")
    shelter.enqueue("Dog2", "Dog")
    
    print("Dequeue dog:", shelter.dequeueDog())  # Should print Dog1
    print("Dequeue dog:", shelter.dequeueDog())  # Should print Dog2
    print("Dequeue dog:", shelter.dequeueDog())  # Should print None
    print("Dequeue cat:", shelter.dequeueCat())  # Should print Cat1
    

if __name__ == "__main__":
    test_animal_shelter()