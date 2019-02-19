# Exercise 1
# Create an emotions dict, where the keys are the names of different human emotions and the values are the degree to which the
# emotion is being felt on a scale from 1 to 3.

emotions = {
    'anger': 2,
    'happiness': 3,
    'fear': 1,
    'joy': 2,
    'sadness': 1
}

# Exercise 2
# Write a Person class with the following characteristics:
#     name (string)
#     emotions (dict)
#
# Initialize an instance of Person using your emotions dict from exercise 1.

class Person:
    """This class represents a person. It has a name and a dictionary of emotions"""
    def __init__(self,name,emotions):
        self.name = name
        self.emotions = emotions

    def __str__(self):
        return "Hi, I'm {}!".format(self.name)

# Add an instance method to your class that displays a message describing how the person is feeling. Substitute the words
# "high", "medium", and "low" for the emotion levels 1, 2, and 3.

    #Function to figure out the high/medium/low string based off a number
    def emotion_rating(self,rating):
        if rating == 1:
            return "low"
        elif rating == 2:
            return "medium"
        elif rating == 3:
            return "high"

    #Function to print out a statement about how the person is feeling for each emotion in their dict
    def feeling(self):
        for emotion, rating in self.emotions.items():
            print("{} is feeling a {} level of {}.".format(self.name,self.emotion_rating(rating),emotion))



jeff = Person("Jeff",emotions)
print(jeff)
jeff.feeling()
