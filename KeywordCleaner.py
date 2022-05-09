class Cleaner:

    # This cleaner does the following:
    # 1. remove non acii charicters
    # 2. strip each line
    # 3. remove tabs
    # 4. remove + * ?"/&| () {} [].,$#%
    # 5. removes duplicates
    # 6. sorts by length

    def setup(self):
        # imports
        import easygui

        global easygui

    def clean(self):
        file_path = easygui.fileopenbox()

        output = []
        blacklisted = """+* ?"/&|(){}[].,$#%^@!"""

        with open("keyword_output.txt", "w") as output_file:
            with open(file_path, "r") as input_file:
                for line in input_file:

                    # Remove non ascii
                    line = line.encode("ascii", "ignore").decode()

                    line = line.strip()

                    line = line.replace("\n", "")

                    line = line.replace("\t", "")

                    line = line.replace("_", " ")

                    line = line.replace("-", " ")

                    for char in blacklisted.split():
                        line = line.replace(char, "")

                    if len(line) != 0 and line not in output:

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
