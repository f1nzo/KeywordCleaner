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

    def setup(self):
        # imports
        import easygui
        from functools import partial

        global easygui
        global partial

    def clean(self):
        file_path = easygui.fileopenbox()

        output = []
        blacklisted = ["#", "+", "*", "?", '"', "/", "&", "|", "(", ")", "{", "}", "[", "]", ".", ",", "$", "%", "^", "@", "!", "<", ">", ";", ":"] # +* ?"/&|(){}[].,$#%^@!<>;:

        utf8open = partial(open, encoding="UTF-8")

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

                    line = line.replace("  ", " ")

                    line = line.replace("   ", " ")

                    line = line.replace("    ", " ")

                    line = line.replace("     ", " ")

                    for char in blacklisted:
                        line = line.replace(char, "")

                    if len(line) != 0 and line not in output and "amp;" not in line and not line.isdecimal():

                        output.append(line)

                output.sort(key=len)

                for line in output:
                    output_file.write(line + "\n")


    def __init__(self):
        self.setup()
        self.clean()


def main():
    Cleaner()

if __name__ == "__main__":
    main()
