import random


class NameGenerator(object):

    def __init__(self):
        self.vowels = ["a", "e", "i", "o", "u", "y"]
        self.consonants = ["b", "c", "d", "f", "g", "h", "j", "k",
                           "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

    def get_vowel(self):
        return random.choice(self.vowels)

    def get_consonant(self):
        return random.choice(self.consonants)

    def get_first_name(self):
        name = []
        counter = 0
        for element in range(5):
            if counter % 2 == 0:
                if counter == 0:
                    name.append(self.get_consonant().capitalize())
                    counter += 1
                else:
                    name.append(self.get_consonant())
                    counter += 1
            elif counter % 2 == 1:
                name.append(self.get_vowel())
                counter += 1
        return ''.join(name)

    def get_last_name(self):
        name = []
        counter = 1
        for element in range(7):
            if counter % 2 == 0:
                name.append(self.get_vowel())
                counter += 1
            elif counter % 2 == 1:
                if counter == 1:
                    name.append(self.get_consonant().capitalize())
                    counter += 1
                else:
                    name.append(self.get_consonant())
                    counter += 1

        return ''.join(name)

    def get_full_names(self, num):
        names = []
        for element in range(num):
            names.append("{} {}".format(
                self.get_first_name(), self.get_last_name()))
        return names


gen = NameGenerator()
names = gen.get_full_names(10)
for name in names:
    print(name)
