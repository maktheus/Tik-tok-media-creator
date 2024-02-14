
import string

def clean_filename(title):
    title = title.lower()
    title = title.translate(str.maketrans("", "", string.punctuation))
    title = title.replace(" ", "_")
    return title
