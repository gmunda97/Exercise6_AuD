# Question 1

def transform_to_row(infile, outfile):
    with open(infile, 'r') as reader:
        contents = reader.read()
        content_list = contents.split(',')

    with open(outfile, 'w') as writer:
        for name in content_list:
            writer.write(name)
            writer.write('\n')

# print(transform_to_row('Names.txt', 'outfile.txt'))


# Question 2

def add_greeting(infile, outfile):
    with open(infile, 'r') as reader:
        contents = reader.readlines()
        print(contents)

    with open(outfile, 'w') as writer:
        for name in contents:
            name = "Hello " + name
            writer.write(name)

# print(add_greeting('outfile.txt', 'outfile2.txt'))


# Question 3

def strip_greeting(infile, outfile):
    delete_list = ["Hello "]
    lst = []
    with open(infile, 'r') as reader:
        with open(outfile, 'w') as writer:
            for line in reader:
                for word in delete_list:
                    if word in line:
                        line = line.replace(word, "")
                lst.append(line)
            for line in lst:
                writer.write(line)

# print(strip_greeting("outfile2.txt", "NoHello.txt"))



# Question 4

def combine_files(file1, file2, outfile):
    with open(file1) as x:
        with open(file2) as y:
            with open(outfile, 'w') as z:
                xlines = x.readlines()
                ylines = y.readlines()

                if len(xlines) != len(ylines):
                    raise Exception("Cannot merge files. Only files with the same amount of lines supported")
                else:
                    for i in range(len(xlines)):
                        line = xlines[i].strip() + " " + ylines[i]
                        z.write(line)

# print(combine_files('outfile2.txt', 'Surnames.txt', 'outfile3.txt'))
