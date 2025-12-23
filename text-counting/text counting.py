paragraph = input("Please write a paragraph and hit enter when you're finished: \n")
# paragraph = "hello this is a test function. My name is test. What time is it."


paragraphLength = len(paragraph.split(" "))
sentencesSplit = paragraph.split(". ")
sentencesSplit.pop()

print(paragraph.split(" "))
sentences = len(sentencesSplit)

print(f"\nTotal number of words = {paragraphLength}")
print(f"Total number of sentences = {sentences + 1}")

print(f"\nCapitalized sentences are:")

for x in range(sentences):
    print(sentencesSplit[x][0].upper() + sentencesSplit[x][1:] + ".")