
import random
#getting systemRandom instance out of random class
systemRandom = random.SystemRandom()
'''
https://pynative.com/cryptographically-secure-random-data-in-python/
'''
#SystemRandom.randrange()
randomNumber = systemRandom.randrange(50,100)
#print("Secure random number within range using SystemRandom class is ", randomNumber)

alist = ['a','b','g','h']
print(len(alist))
random_index = systemRandom.randrange(0,len(alist))
# both the beginning and ending elements are printed by this. 
print(alist[random_index])
