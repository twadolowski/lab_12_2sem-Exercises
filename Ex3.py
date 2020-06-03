def countLines(file):
    lines = file.readlines()
    numLines = len(lines)
    return(numLines)

def countWordsPerLine(file):
    lines = file.readlines()
    words = []
    for i in lines:
        words.append(len(i.split()))
    return(words)

def countVowelsPerLine(file):
    lines = file.readlines()
    vowels = []
    for i in lines:
        count = i.lower().count("a")
        count += i.lower().count("e")
        count += i.lower().count("i")
        count += i.lower().count("o")
        count += i.lower().count("u")
        vowels.append(count)
    return(vowels)

def capitalizeVowels(file):
    lines = file.readlines()
    line = ""
    newLines = []
    vowels = 'aeiou'
    for i in lines:
        for j in i:
            if j in vowels:
                line += j.upper()
            else:
                line += j
        newLines.append(line)
        line = ""
    return(newLines)

file = open("test.txt", "r")   
print(countLines(file))
file = open("test.txt", "r")  
print(countWordsPerLine(file))
file = open("test.txt", "r")
print(countVowelsPerLine(file))
file = open("test.txt", "r")
print(capitalizeVowels(file))
