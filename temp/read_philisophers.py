
def main():
    infile = open("philosophers.txt", 'r')
    file_contents = infile.read()
    print(file_contents)
    infile.close()
main()