def determineArticle(word):
    article = "an" if word[0].lower() in "aeioh" else "a"
    return f"{article} {word}"

print(determineArticle("university"))
