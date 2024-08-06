import re

# reformat lines that are in all caps
def handle_caps(text):
    lines = text.split('\n')
    normalized_lines = []

    for line in lines:
        if line.isupper():
            words = line.split()
            capitalized_words = [word.capitalize() for word in words]
            normalized_lines.append(' '.join(capitalized_words))
        else:
            normalized_lines.append(line)
    text = '\n'.join(normalized_lines)
    
    return text

# remove unnecessary newlines 
def merge_lines(text):
    # version 4
    lines = text.split('\n')
    reformatted_text = []
    buffer = ""

    # detect possibl split lines
    possible_split = re.compile(r'^[a-z0-9]')

    for line in lines:
        # if current line is a possible continuation of previous line
        if buffer and possible_split.match(line):
            buffer += " " + line.strip()
        else:
            if buffer:
                reformatted_text.append(buffer)
            buffer = line.strip()

    # add remaining text in buffer
    if buffer:
        reformatted_text.append(buffer)
    return "\n".join(reformatted_text)
