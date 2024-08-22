def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()

	words = len(file_contents.split())
	characters = {}
	conv_characters = []
	
	for char in file_contents.lower():
		if char.isalpha():
			if char in characters:
				characters[char] += 1
			else:
				characters[char] = 1

	for char in characters:
		conv_characters.append({
			"name": char,
			"count": characters[char]
			})
	
	conv_characters.sort(reverse=True, key=sort_on)

	print(conv_characters)

	print(f"--- Begin report of books/frankfenstein.txt ---")
	print(f"There are {words} words in the document")
	for item in conv_characters:
		print(f"The '{item['name']}' character was found {item['count']} times")

def sort_on(dict):
	return dict["count"]
main()
