class Cleaner:

    # This cleaner does the following:
    # 1. remove non acii charicters
    # 2. strip each line
    # 3. remove tabs
    # 4. remove + * ?"/&|\() {} [].,$#%
    # 5. removes duplicats
    # 6. replaces large amounts of spaces with a single space
    # 7. removes keyword "amp;" that can mess with dorking
    # 8. replaces - and _ with a space
    # 9. removes lines made up of purely numbers
    # 10. sorts lines from smallest to largest
    # 11. removes lines that are less than 1 word long
    # 12. removes lines that are longer than 3 words
    # 13. removes words that are in the bad word list.
    # 14. Looks for a string of characters that is at least 1 character long and can be up to 20 characters in length

    def setup(self):
        # imports
        import easygui
        from functools import partial
        import regex

        global easygui
        global partial
        global regex

    def clean(self):
        file_path = easygui.fileopenbox()

        output = []
        blacklisted = ["#", "+", "*", "?", '"', "/", "&", "|", "(", ")", "{", "}", "[", "]", ".", ",", "$", "%", "^", "@", "!", "<", ">", ";", ":"] # +* ?"/&|(){}[].,$#%^@!<>;:

        utf8open = partial(open, encoding="UTF-8", errors="ignore")

        with utf8open("keyword_output.txt", "w") as output_file:
            with utf8open(file_path, "r") as input_file:
                for line in input_file:

                    # Remove non ascii
                    line = line.encode("ascii", "ignore").decode()

                    line = line.strip()

                    line = line.replace("\n", "")

                    line = line.replace("\t", "")

                    line = line.replace("_", " ")

                    line = line.replace("-", " ")

                    line = line.replace("\\", "")

                    line = regex.match(r"^(.{1,20}\s?){1,}$", line).group(0)

                    line = regex.sub(r"\s+", " ", line)

                    for char in blacklisted:
                        line = line.replace(char, "")

                    if len(line) != 0 and line not in output and "amp;" not in line and not line.isdecimal():

                        output.append(line)

                output.sort(key=len)

                bad_words = ["http", "www", "com", "002"]
                for line in output:
                    if not any(bad_word in line for bad_word in bad_words):
                        if line.count(" ") > 1 and line.count(" ") < 5:
                            output_file.write(line + "\n")


    def __init__(self):
        self.setup()
        self.clean()


def main():
    Cleaner()

if __name__ == "__main__":
    main()
