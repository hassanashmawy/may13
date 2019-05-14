import random

print("************")
print(" Exercise 1")
print("************")
emotions = {
    'fear': 3,
    'happy': 2,
    'sad': 3
}
print(emotions)

print()
print("************")
print(" Exercise 2")
print("************")

class Person:
    
    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def __str__(self):
        return "I am {} feeling a mix of:{}".format(self.name, self.emotions)

    def get_mood(self):
        rand_int = random.randint(1,len(self.emotions) - 1)
        print(rand_int,'rand_int')
        power = 0
        emotion = '-'
        for k,v in enumerate(emotions):
            if rand_int == k:
                power = emotions[v]
                emotion = v
                exit
        
        rank = convert_to_rank(power)
        return '{} feels a random of a {} amount of {}'.format(self.name, rank, emotion)
        



    

persona_a = Person('Hassan', emotions)
print(persona_a)

print()
print("************")
print(" Exercise 3")
print("************")

def convert_to_rank(number):
    rank = 'high' if number == 1 else 'medium' if number == 2 else 'low'
    return rank



print('moood:', persona_a.get_mood())
# print()
# print(emotions[-1])



