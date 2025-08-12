import re 


def extract_title(markdown):
    
    h1 = re.findall(r"^#(?!#) *(.*?)$",markdown,re.MULTILINE)
    if not h1:
        raise Exception("Couldnt find a title")
    else:
        return h1[0].strip()

