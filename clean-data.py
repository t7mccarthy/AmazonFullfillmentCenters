text_file = open("raw-output.txt", "r")
lines = text_file.read().split(',')
cursor = 0
length = len(lines)
for i in range (length-1,0,-1):
    if "Bounding box - X:" in lines[i]:
        del lines[i]
print lines
for line in lines:
    print(line)
    print("\n")
text_file.close()
