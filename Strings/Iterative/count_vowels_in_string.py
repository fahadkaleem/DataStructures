# http://www.geeksforgeeks.org/program-count-vowels-string-iterative-recursive/

class countVowels():

    def __init__(self):
        self.vowels = ['a','e','i','o','u']

    def isVowel(self,v):
        return v in self.vowels

    def countVowels(self,givenString):
        count = 0
        for i in givenString:
            if self.isVowel(i):
                count+=1
        return count

if __name__ == "__main__":
    givenString = 'Hello World'
    c = countVowels()
    print("There are {} vowels in {}".format(c.countVowels(givenString),givenString))






