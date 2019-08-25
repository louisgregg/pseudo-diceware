# pseudo-diceware
A password generator for lazy, paranoid people.  
In fact, even calling this pseudo-diceware is a stretch. It's more like a random word selector.   
You can find an *evil, password stealing implementation* of this code here: 
https://www.ocf.berkeley.edu/~fin/flasky/diceware

## Random Number Generation
Random numbers generated by an instance of the SystemRandom class in the random library.   
https://pynative.com/cryptographically-secure-random-data-in-python/  
I chose to use this instead of the secrets library (available from Python 3.6 onwards) for backwards compatibility.  
The documentation for random recommends using the SystemRandom class for crypto applications. See here:  
https://docs.python.org/2/library/random.html  
Read more about actual dice implementation here:  
https://www.eff.org/dice  

## Sources
EFF Long wordlist taken from the EFF website.  
https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt  
Moby Dick and the Bible taken from the Project Gutenberg website.  
https://www.gutenberg.org/files/2701/old/moby10b.txt  
https://www.gutenberg.org/ebooks/10.txt.utf-8  

## Usage Example
```
python pseudo-diceware.py bible.txt 10 
```

Example Output:
There are 12893 unique words in the file.
reproach bleating wait sheva araunah tyre zerah closets ransom jeshebeab
