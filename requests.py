from freebible import read_web
web = read_web()

def getverse(book, *args):
    book_name = book.capitalize()
    if book_name not in web.keys():
        return "The book you selected is not in the Bible. Please try again."
    try:
        chapter = args[0]
        verse = args[1]
        print(book, chapter, verse)
        data = web[book_name][chapter][verse]
        print(data)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again.")

if __name__ == "__main__":
    getverse()
