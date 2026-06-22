'''script to count how many words i yapped lol'''

import os

def path(*args):
    return os.listdir(os.path.join(*args))

totalWords = 0
totalChars = 0
for folder in path("updatelogs"):
    if folder=="images" or "." in folder: continue
    for file in path("updatelogs", folder):
        with open(os.path.join("updatelogs", folder, file), "r") as f:
            temp = f.read()
            totalWords += temp.count(" ")
            totalChars += len(temp)

images = 0
for folder in path("updatelogs", "images"):
    images += len(path("updatelogs", "images", folder))

# not sure if correct but good estimate i guess
print("total {} words!".format(totalWords-(2*images)))
print("total {} chars!".format(totalChars-((52-3)*images)))
print("total {} images!".format(images))