from print_triangle import ptriangle


def tower():

    choise = int(input("Enter your choise "))

    if choise < 0 or choise > 3:
        return"Invalid Input"
    
    height_width = input("Please enter the height and width  ")
    height = int(height_width.split(' ')[0])
    width = int(height_width.split(' ')[1])

    # while choise!=
    while choise <= 3:
        match(choise):

            case 1:
                print("You chose a rectangular tower ")
                height_width
                if height == width or abs(height - width) > 5:
                    print("The area of the rectangle is ", height*width)
                print("The perimeter of the rectangle is " , 2*(height+width))

            case 2:
                print("You chose a triangular tower")
                height_width
                triangle_chise = int(input("To calculate the perimeter of the triangle press 1 \
                                        To print the triangle press 2 "))
                height = int(height_width.split(' ')[0])
                width = int(height_width.split(' ')[1])

                if triangle_chise == 1:
                    per = pow((height**2 - width**2),0.5)
                    print("The perimeter of the rectangle is ", per)

                elif triangle_chise == 2:

                    if width % 2 == 0 or (width*2 > height):
                        print("This triangle cannot be printed")
                    else:
                        ptriangle(height, width)
            case 3:
                return "good bye"
            

        choise = int(input("Enter your choise "))
        if choise < 0 or choise > 3:
            return "Invalid Input"

print(tower())