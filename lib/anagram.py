class Anagram:

    def __init__(self, string):
        self.string = string

    def match(self, list):
        match_list = []
        for word in list:
            if sorted(self.string) == sorted(word):
                match_list.append(word)
        return match_list
