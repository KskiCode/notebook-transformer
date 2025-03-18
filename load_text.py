
# basic load and pre-processing.
with open("./data\source_text.txt", "r", encoding="utf8") as infile, open(r"./data\training-data.txt", "w", encoding="utf8") as outfile:
    for line in infile:
        if line.strip():
            outfile.write(line)
            print(line)