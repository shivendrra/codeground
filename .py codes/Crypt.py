alpha_low = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':34, 'H':35, 'I':36, 'J':37, 'K':38, 'L':39, 'M':40, 'N':41, 'O':42, 'P':43, 'Q':44, 'R':45, 'S':46, 'T':47, 'U':48, 'V':49, 'W':50, 'X':51, 'Y':52, 'Z':53}

input_data = 'Harsh'
encrWord = 0
output_corpus = []
for i in range(len(input_data)):
    ltr = input_data[i]
    def check(inp):
        letter = alpha_low[inp]
        return letter
    ltrIdx = check(ltr)
    encrWord = encrWord + ltrIdx
print(encrWord)