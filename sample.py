import random
import os
import filecmp

def generate():
    with open("input.txt", mode = "w") as input_file:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        input_file.write(f"{b} {c}\n")

        s = []
        length = random.randint(1, 100)
        for i in range(length):
            s.append(chr(random.randint(ord("a"), ord("z"))))
        s = "".join(s)
        input_file.write(f"{s}\n")
    return


def is_same():
    # if not os.path.isfile("main.exe"):
    #     os.system("g++ main.cpp -o main")
        
    # if not os.path.isfile("simple.exe"):
    #     os.system("g++ simple.cpp -o simple")
        
    os.system("./main < input.txt > out1.txt")
    os.system("./simple < input.txt > out2.txt")
    
    if filecmp.cmp("out1.txt","out2.txt"):
        return True
    else:
        return False

def main():
    while True:
        generate()
        if not is_same():
            break


if __name__ == '__main__':
    main()


