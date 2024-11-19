from freebible import read_web
web = read_web()

def getverse(book, chapter, verse):
    buk = book.capitalize()

    if buk == "List":
        return web.keys()

    if buk not in web.keys():
        return "The book you selected is not in the Bible. Please try again."
    
    try:
        data = web[f"{buk}"][chapter][verse]
        print(data)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again.")

if __name__ == "__main__":
    getverse()
