from freebible import read_web
web = read_web()
book = "John"
chapter = "3"
verse = "16"
print(len(web[book][chapter]["*"]))