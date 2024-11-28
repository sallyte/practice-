# from abc import ABC, abstractmethod


# class Animal(ABC):
#     #추상 메서드 정의(구체적인 구현은 하지 않음)
#     @abstractmethod
#     def make_sound(self):
#         pass

#     def sleep(self):
#         print("The animal is sleeping")

# #추상 클래스를 상속받는 클래스에서 구체적인  구현
# class Dog(Animal):
#     def make_sound(self):
#         print("Bark!")
#     def sleep(self):
#         print("The Dog is sleeping")

# class Cat(Animal):
#     Dog().make_sound()
#     Dog().sleep()
#     # dog.make_sound()

#     def make_sound(self):
#        print("Meow!")

# # 객체 생성 및 구현
# # dog = Dog()
# cat = Cat()

# # dog.make_sound()
# cat.make_sound()

# # dog.sleep()
# cat.sleep()

from typing import Protocol

class Speakable(Protocol):
    def speak(self)-> str:
        ...

class Dog:
    def speak(self)-> str:
        return "Bark"

class Cat:
    def speak(self)-> str:
        return "Meow"

def make_it_speak(animal: Speakable):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_it_speak(dog)
make_it_speak(cat)





# #부모 클래스
# class Animal:
#     def __init__(self, name):
#       self.name = name
    
#     def speak(self):
#         print(f"{self.name} is making a sound.")

# #자식 클래스
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
    
#     def speak(self):
#         print(f"{self.name} the {self.breed} is barking.")

# dog = Dog("Buddy", "Golden Retriever")
# dog.speak()

# class Animal:
#     def eat(self):
#         print("Eating...")

# class Walker:
#     def walk(self):
#         print("Walking...")

# class Dog(Animal, Walker):
#     def bark(self):
#         print("Barking...")

# dog = Dog()
# dog.eat()
# dog.walk()
# dog.bark()


# class  Animal():
#     def speak(a):
#         return "소리를 낸다"

# class Dog(Animal):
#     def speak(a):
#         return "Bark"

# class Lamb(Animal):
#     def speak(a):
#         return "Emna"

# class Cat(Animal):
#     def speak(a):
#         return "Meow"

# class Cow(Animal):
#     def speak(a):
#         return "Moo"

# class Cow(Animal):
#     # speak any="b"
#     def speak(a):
#         return "Moo"

# # def make_animal_speak(animal: Animal):
# #     print(animal.speak())

# dog = Dog()
# cat = Cat()
# cow = Cow()
# lamb = Lamb()
# ani = Animal()
# print(dog.speak())
# # cow.speak()

# # make_animal_speak(dog)
# # make_animal_speak(cat)
# # make_animal_speak(cow)
# # make_animal_speak(lamb)


