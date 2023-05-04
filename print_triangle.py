from math import floor as round


def ptriangle(height, width):

    odd_numbers = [x for x in range(2,width-1) if x%2!=0]
    same_rows = round((height-2)/len(odd_numbers))
    remaind = (height-2) % len(odd_numbers)

    # print the first *
    print(" " * (round(width/2)), end="")
    print("*")

    # print the remain rows
    for i in range(remaind):
        print(" " * (round(width/2)-1), end="")
        print("***")
    
    # print the inner rows
    for i in odd_numbers:
        j = same_rows
        while j > 0:
            print(" " * ( round(width/2)-1-odd_numbers.index(i)), end="")
            print("*" * i)
            j = j - 1
    
    # print the last row
    print("*"*width)

ptriangle(4,5)