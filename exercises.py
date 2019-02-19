"""
Exercise 1
Create an emotions dict, where the keys are the names of different human emotions and the values are the degree to which the
emotion is being felt on a scale from 1 to 3.
"""

emotions = {
    'anger': 2,
    'happiness': 3,
    'fear': 1,
    'joy': 2,
    'sadness': 1
}


"""
Exercise 2
Write a Person class with the following characteristics:
    name (string)
    emotions (dict)

Initialize an instance of Person using your emotions dict from exercise 1.
"""

class Person:
    def __init__(self,name,emotions):
        self.name = name
        self.emotions = emotions

jeff = Person("Jeff",emotions)
print(jeff)
