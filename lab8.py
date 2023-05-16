from abc import ABC, abstractmethod

class Frequency(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFrequency(self):
        pass

class ListCount(Frequency):
    def calculateFrequency(self):
        frequencies = [0] * 26

        with open(self.address, 'r') as file:
            for line in file:
                for char in line.lower():
                    if char.isalpha():
                        frequencies[ord(char) - ord('a')] += 1

        for i, freq in enumerate(frequencies):
            print(chr(ord('a') + i), '=', freq)


class DictCount(Frequency):
    def calculateFrequency(self):
        frequencies = {}

        with open(self.address, 'r') as file:
            for line in file:
                for char in line.lower():
                    if char.isalpha():
                        frequencies[char] = frequencies.get(char, 0) + 1

        for char, freq in frequencies.items():
            print(char, '=', freq)

file_address = "weirdWords.txt"

list_counter = ListCount(file_address)
print("List Count:")
list_counter.calculateFrequency()

print()

dict_counter = DictCount(file_address)
print("Dictionary Count:")
dict_counter.calculateFrequency()