cube = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']]

def faceMove(x):
    temp = cube[x][0]
    cube[x][0] = cube[x][6]
    cube[x][6] = cube[x][4]
    cube[x][4] = cube[x][2]
    cube[x][2] = temp

    temp = cube[x][1]
    cube[x][1] = cube[x][7]
    cube[x][7] = cube[x][5]
    cube[x][5] = cube[x][3]
    cube[x][3] = temp
    return

def faceMovePrime(x):
    temp = cube[x][0]
    cube[x][0] = cube[x][2]
    cube[x][2] = cube[x][4]
    cube[x][4] = cube[x][6]
    cube[x][6] = temp

    temp = cube[x][1]
    cube[x][1] = cube[x][3]
    cube[x][3] = cube[x][5]
    cube[x][5] = cube[x][7]
    cube[x][7] = temp
    return

def uMove(move):
    if(move == "U"):
        faceMove(0)

        temp = cube[1][0]
        cube[1][0] = cube[2][0]
        cube[2][0] = cube[3][0]
        cube[3][0] = cube[4][0]
        cube[4][0] = temp

        temp = cube[1][1]
        cube[1][1] = cube[2][1]
        cube[2][1] = cube[3][1]
        cube[3][1] = cube[4][1]
        cube[4][1] = temp

        temp = cube[1][2]
        cube[1][2] = cube[2][2]
        cube[2][2] = cube[3][2]
        cube[3][2] = cube[4][2]
        cube[4][2] = temp
    elif(move == "U'"):
        faceMovePrime(0)

        temp = cube[1][0]
        cube[1][0] = cube[4][0]
        cube[4][0] = cube[3][0]
        cube[3][0] = cube[2][0]
        cube[2][0] = temp

        temp = cube[1][1]
        cube[1][1] = cube[4][1]
        cube[4][1] = cube[3][1]
        cube[3][1] = cube[2][1]
        cube[2][1] = temp

        temp = cube[1][2]
        cube[1][2] = cube[4][2]
        cube[4][2] = cube[3][2]
        cube[3][2] = cube[2][2]
        cube[2][2] = temp
    elif(move == "U2"):
        uMove("U")
        uMove("U")
    return

def dMove(move):
    if(move == "D"):
        faceMove(5)

        temp = cube[1][6]
        cube[1][6] = cube[4][6]
        cube[4][6] = cube[3][6]
        cube[3][6] = cube[2][6]
        cube[2][6] = temp

        temp = cube[1][5]
        cube[1][5] = cube[4][5]
        cube[4][5] = cube[3][5]
        cube[3][5] = cube[2][5]
        cube[2][5] = temp

        temp = cube[1][4]
        cube[1][4] = cube[4][4]
        cube[4][4] = cube[3][4]
        cube[3][4] = cube[2][4]
        cube[2][4] = temp
        return
    elif(move == "D'"):
        faceMovePrime(5)

        temp = cube[1][6]
        cube[1][6] = cube[2][6]
        cube[2][6] = cube[3][6]
        cube[3][6] = cube[4][6]
        cube[4][6] = temp

        temp = cube[1][5]
        cube[1][5] = cube[2][5]
        cube[2][5] = cube[3][5]
        cube[3][5] = cube[4][5]
        cube[4][5] = temp

        temp = cube[1][4]
        cube[1][4] = cube[2][4]
        cube[2][4] = cube[3][4]
        cube[3][4] = cube[4][4]
        cube[4][4] = temp
        return
    elif(move == "D2"):
        dMove("D")
        dMove("D")
    return

def rMove(move):
    if(move == "R"):
        faceMove(3)

        temp = cube[0][4]
        cube[0][4] = cube[2][4]
        cube[2][4] = cube[5][4]
        cube[5][4] = cube[4][0]
        cube[4][0] = temp

        temp = cube[0][3]
        cube[0][3] = cube[2][3]
        cube[2][3] = cube[5][3]
        cube[5][3] = cube[4][7]
        cube[4][7] = temp

        temp = cube[0][2]
        cube[0][2] = cube[2][2]
        cube[2][2] = cube[5][2]
        cube[5][2] = cube[4][6]
        cube[4][6] = temp
        return
    elif(move == "R'"):
        faceMovePrime(3)

        temp = cube[0][4]
        cube[0][4] = cube[4][0]
        cube[4][0] = cube[5][4]
        cube[5][4] = cube[2][4]
        cube[2][4] = temp

        temp = cube[0][3]
        cube[0][3] = cube[4][7]
        cube[4][7] = cube[5][3]
        cube[5][3] = cube[2][3]
        cube[2][3] = temp

        temp = cube[0][2]
        cube[0][2] = cube[4][6]
        cube[4][6] = cube[5][2]
        cube[5][2] = cube[2][2]
        cube[2][2] = temp
        return
    elif(move == "R2"):
        rMove("R")
        rMove("R")
    return

def lMove(move):
    if(move == "L"):
        faceMove(1)

        temp = cube[0][0]
        cube[0][0] = cube[4][4]
        cube[4][4] = cube[5][0]
        cube[5][0] = cube[2][0]
        cube[2][0] = temp

        temp = cube[0][7]
        cube[0][7] = cube[4][3]
        cube[4][3] = cube[5][7]
        cube[5][7] = cube[2][7]
        cube[2][7] = temp

        temp = cube[0][6]
        cube[0][6] = cube[4][2]
        cube[4][2] = cube[5][6]
        cube[5][6] = cube[2][6]
        cube[2][6] = temp
        return
    elif(move == "L'"):
        faceMovePrime(1)

        temp = cube[0][0]
        cube[0][0] = cube[2][0]
        cube[2][0] = cube[5][0]
        cube[5][0] = cube[4][4]
        cube[4][4] = temp

        temp = cube[0][7]
        cube[0][7] = cube[2][7]
        cube[2][7] = cube[5][7]
        cube[5][7] = cube[4][3]
        cube[4][3] = temp

        temp = cube[0][6]
        cube[0][6] = cube[2][6]
        cube[2][6] = cube[5][6]
        cube[5][6] = cube[4][2]
        cube[4][2] = temp
        return
    elif(move == "L2"):
        lMove("L")
        lMove("L")
    return

def fMove(move):
    if(move == "F"):
        faceMove(2)

        temp = cube[0][6]
        cube[0][6] = cube[1][4]
        cube[1][4] = cube[5][2]
        cube[5][2] = cube[3][0]
        cube[3][0] = temp

        temp = cube[0][5]
        cube[0][5] = cube[1][3]
        cube[1][3] = cube[5][1]
        cube[5][1] = cube[3][7]
        cube[3][7] = temp

        temp = cube[0][4]
        cube[0][4] = cube[1][2]
        cube[1][2] = cube[5][0]
        cube[5][0] = cube[3][6]
        cube[3][6] = temp
        return
    elif(move == "F'"):
        faceMovePrime(2)

        temp = cube[0][6]
        cube[0][6] = cube[3][0]
        cube[3][0] = cube[5][2]
        cube[5][2] = cube[1][4]
        cube[1][4] = temp

        temp = cube[0][5]
        cube[0][5] = cube[3][7]
        cube[3][7] = cube[5][1]
        cube[5][1] = cube[1][3]
        cube[1][3] = temp

        temp = cube[0][4]
        cube[0][4] = cube[3][6]
        cube[3][6] = cube[5][0]
        cube[5][0] = cube[1][2]
        cube[1][2] = temp
        return
    elif(move == "F2"):
        fMove("F")
        fMove("F")
    return

def bMove(move):
    if(move == "B"):
        faceMove(4)

        temp = cube[0][2]
        cube[0][2] = cube[3][4]
        cube[3][4] = cube[5][6]
        cube[5][6] = cube[1][0]
        cube[1][0] = temp

        temp = cube[0][1]
        cube[0][1] = cube[3][3]
        cube[3][3] = cube[5][5]
        cube[5][5] = cube[1][7]
        cube[1][7] = temp

        temp = cube[0][0]
        cube[0][0] = cube[3][2]
        cube[3][2] = cube[5][4]
        cube[5][4] = cube[1][6]
        cube[1][6] = temp
        return
    elif(move == "B'"):
        faceMovePrime(4)

        temp = cube[0][2]
        cube[0][2] = cube[1][0]
        cube[1][0] = cube[5][6]
        cube[5][6] = cube[3][4]
        cube[3][4] = temp

        temp = cube[0][1]
        cube[0][1] = cube[1][7]
        cube[1][7] = cube[5][5]
        cube[5][5] = cube[3][3]
        cube[3][3] = temp

        temp = cube[0][0]
        cube[0][0] = cube[1][6]
        cube[1][6] = cube[5][4]
        cube[5][4] = cube[3][2]
        cube[3][2] = temp
        return
    elif(move == "B2"):
        bMove("B")
        bMove("B")
    return

def scramble(scr, len):
    x=0
    for x in range(len):
        if(scr[x][0] == "U"):
            uMove(scr[x][0]+scr[x][1])
        elif(scr[x][0] == "D"):
            dMove(scr[x][0]+scr[x][1])
        elif(scr[x][0] == "R"):
            rMove(scr[x][0]+scr[x][1])
        elif(scr[x][0] == "L"):
            lMove(scr[x][0]+scr[x][1])
        elif(scr[x][0] == "F"):
            fMove(scr[x][0]+scr[x][1])
        elif(scr[x][0] == "B"):
            bMove(scr[x][0]+scr[x][1])


    # print(
    #                                             "    " + cube[0][0] + cube[0][1] + cube[0][2] + "\n" +
    #                                             "    " + cube[0][7] + "w" + cube[0][3] + "\n" +
    #                                             "    " + cube[0][6] + cube[0][5] + cube[0][4] + "\n\n" +
    #     cube[1][0] + cube[1][1] + cube[1][2] + " " + cube[2][0] + cube[2][1] + cube[2][2] + " " + cube[3][0] + cube[3][1] + cube[3][2] + " " + cube[4][0] + cube[4][1] + cube[4][2] + "\n" +
    #     cube[1][7] + "o" + cube[1][3] + " " + cube[2][7] + "g" + cube[2][3] + " " + cube[3][7] + "r" + cube[3][3] + " " + cube[4][7] + "b" + cube[4][3] + "\n" +
    #     cube[1][6] + cube[1][5] + cube[1][4] + " " + cube[2][6] + cube[2][5] + cube[2][4] + " " + cube[3][6] + cube[3][5] + cube[3][4] + " " + cube[4][6] + cube[4][5] + cube[4][4] + "\n\n" +
    #                                             "    " + cube[5][0] + cube[5][1] + cube[5][2] + "\n" +
    #                                             "    " + cube[5][7] + "y" + cube[5][3] + "\n" +
    #                                             "    " + cube[5][6] + cube[5][5] + cube[5][4] + "\n"
    # )
    #
    return cube



import cv2 as cv
import numpy as np

size = 500, 700, 3
scrambleImg = np.zeros(size, dtype=np.uint8)

colorAr = []

for y in range(6):
    for z in range(8):
        if(cube[y][z] == 'w'):
            cube[y][z] = (255,255,255)
        elif(cube[y][z] == 'o'):
            cube[y][z] = (0,165,255)
        elif(cube[y][z] == 'g'):
            cube[y][z] = (0,255,0)
        elif(cube[y][z] == 'r'):
            cube[y][z] = (0,0,255)
        elif(cube[y][z] == 'b'):
            cube[y][z] = (255,0,0)
        elif(cube[y][z] == 'y'):
            cube[y][z] = (0,255,255)

def topRow(s, pt1, pt2, pt3, x):
    cv.rectangle(scrambleImg, (pt1+x, pt1), (pt1+s+x, pt1+s), cube[0][0], -1)
    cv.rectangle(scrambleImg, (pt2+x, pt1), (pt2+s+x, pt1+s), cube[0][1], -1)
    cv.rectangle(scrambleImg, (pt3+x, pt1), (pt3+s+x, pt1+s), cube[0][2], -1)

    cv.rectangle(scrambleImg, (pt1+x, pt2), (pt1+s+x, pt2+s), cube[0][7], -1)
    cv.rectangle(scrambleImg, (pt2+x, pt2), (pt2+s+x, pt2+s), (255,255,255), -1)
    cv.rectangle(scrambleImg, (pt3+x, pt2), (pt3+s+x, pt2+s), cube[0][3], -1)

    cv.rectangle(scrambleImg, (pt1+x, pt3), (pt1+s+x, pt3+s), cube[0][6], -1)
    cv.rectangle(scrambleImg, (pt2+x, pt3), (pt2+s+x, pt3+s), cube[0][5], -1)
    cv.rectangle(scrambleImg, (pt3+x, pt3), (pt3+s+x, pt3+s), cube[0][4], -1)
    return

def middleRow(s, pt1, pt2, pt3, sep, x):
    cv.rectangle(scrambleImg, (pt1-sep+x, pt1+sep), (pt1+s-sep+x, pt1+s+sep), cube[1][0], -1)
    cv.rectangle(scrambleImg, (pt2-sep+x, pt1+sep), (pt2+s-sep+x, pt1+s+sep), cube[1][1], -1)
    cv.rectangle(scrambleImg, (pt3-sep+x, pt1+sep), (pt3+s-sep+x, pt1+s+sep), cube[1][2], -1)

    cv.rectangle(scrambleImg, (pt1-sep+x, pt2+sep), (pt1+s-sep+x, pt2+s+sep), cube[1][7], -1)
    cv.rectangle(scrambleImg, (pt2-sep+x, pt2+sep),(pt2+s-sep+x, pt2+s+sep),(0,165,225), -1)
    cv.rectangle(scrambleImg, (pt3-sep+x, pt2+sep), (pt3+s-sep+x, pt2+s+sep), cube[1][3], -1)

    cv.rectangle(scrambleImg, (pt1-sep+x, pt3+sep), (pt1+s-sep+x, pt3+s+sep), cube[1][6], -1)
    cv.rectangle(scrambleImg, (pt2-sep+x, pt3+sep), (pt2+s-sep+x, pt3+s+sep), cube[1][5], -1)
    cv.rectangle(scrambleImg, (pt3-sep+x, pt3+sep), (pt3+s-sep+x, pt3+s+sep), cube[1][4], -1)

    cv.rectangle(scrambleImg, (pt1+x, pt1+sep), (pt1+s+x, pt1+s+sep), cube[2][0], -1)
    cv.rectangle(scrambleImg, (pt2+x, pt1+sep), (pt2+s+x, pt1+s+sep), cube[2][1], -1)
    cv.rectangle(scrambleImg, (pt3+x, pt1+sep), (pt3+s+x, pt1+s+sep), cube[2][2], -1)

    cv.rectangle(scrambleImg, (pt1+x, pt2+sep), (pt1+s+x, pt2+s+sep), cube[2][7], -1)
    cv.rectangle(scrambleImg, (pt2+x, pt2+sep), (pt2+s+x, pt2+s+sep), (0,255,0), -1)
    cv.rectangle(scrambleImg, (pt3+x, pt2+sep), (pt3+s+x, pt2+s+sep), cube[2][3], -1)

    cv.rectangle(scrambleImg, (pt1+x, pt3+sep), (pt1+s+x, pt3+s+sep), cube[2][6], -1)
    cv.rectangle(scrambleImg, (pt2+x, pt3+sep), (pt2+s+x, pt3+s+sep), cube[2][5], -1)
    cv.rectangle(scrambleImg, (pt3+x, pt3+sep), (pt3+s+x, pt3+s+sep), cube[2][4], -1)

    cv.rectangle(scrambleImg, (pt1+sep+x, pt1+sep), (pt1+s+sep+x, pt1+s+sep), cube[3][0], -1)
    cv.rectangle(scrambleImg, (pt2+sep+x, pt1+sep), (pt2+s+sep+x, pt1+s+sep), cube[3][1], -1)
    cv.rectangle(scrambleImg, (pt3+sep+x, pt1+sep), (pt3+s+sep+x, pt1+s+sep), cube[3][2], -1)

    cv.rectangle(scrambleImg, (pt1+sep+x, pt2+sep), (pt1+s+sep+x, pt2+s+sep), cube[3][7], -1)
    cv.rectangle(scrambleImg, (pt2+sep+x, pt2+sep), (pt2+s+sep+x, pt2+s+sep), (0,0,225), -1)
    cv.rectangle(scrambleImg, (pt3+sep+x, pt2+sep), (pt3+s+sep+x, pt2+s+sep), cube[3][3], -1)

    cv.rectangle(scrambleImg, (pt1+sep+x, pt3+sep), (pt1+s+sep+x, pt3+s+sep), cube[3][6],-1)
    cv.rectangle(scrambleImg, (pt2+sep+x, pt3+sep), (pt2+s+sep+x, pt3+s+sep), cube[3][5],-1)
    cv.rectangle(scrambleImg, (pt3+sep+x, pt3+sep), (pt3+s+sep+x, pt3+s+sep), cube[3][4],-1)

    cv.rectangle(scrambleImg, (pt1+(sep*2)+x, pt1+sep), (pt1+s+(sep*2)+x, pt1+s+sep), cube[4][0], -1)
    cv.rectangle(scrambleImg, (pt2+(sep*2)+x, pt1+sep), (pt2+s+(sep*2)+x, pt1+s+sep), cube[4][1], -1)
    cv.rectangle(scrambleImg, (pt3+(sep*2)+x, pt1+sep), (pt3+s+(sep*2)+x, pt1+s+sep), cube[4][2], -1)

    cv.rectangle(scrambleImg, (pt1+(sep*2)+x, pt2+sep), (pt1+s+(sep*2)+x, pt2+s+sep), cube[4][7], -1)
    cv.rectangle(scrambleImg, (pt2+(sep*2)+x, pt2+sep), (pt2+s+(sep*2)+x, pt2+s+sep), (255,0,0), -1)
    cv.rectangle(scrambleImg, (pt3+(sep*2)+x, pt2+sep), (pt3+s+(sep*2)+x, pt2+s+sep), cube[4][3], -1)

    cv.rectangle(scrambleImg, (pt1+(sep*2)+x, pt3+sep), (pt1+s+(sep*2)+x, pt3+s+sep), cube[4][6], -1)
    cv.rectangle(scrambleImg, (pt2+(sep*2)+x, pt3+sep), (pt2+s+(sep*2)+x, pt3+s+sep), cube[4][5], -1)
    cv.rectangle(scrambleImg, (pt3+(sep*2)+x, pt3+sep), (pt3+s+(sep*2)+x, pt3+s+sep), cube[4][4], -1)

    return

def bottomRow(s, pt1, pt2, pt3, sep, x):
    cv.rectangle(scrambleImg, (pt1+x, pt1+sep), (pt1+s+x, pt1+s+sep), cube[5][0], -1)
    cv.rectangle(scrambleImg, (pt2+x, pt1+sep), (pt2+s+x, pt1+s+sep), cube[5][1], -1)
    cv.rectangle(scrambleImg, (pt3+x, pt1+sep), (pt3+s+x, pt1+s+sep), cube[5][2], -1)

    cv.rectangle(scrambleImg, (pt1+x, pt2+sep), (pt1+s+x, pt2+s+sep), cube[5][7], -1)
    cv.rectangle(scrambleImg, (pt2+x, pt2+sep), (pt2+s+x, pt2+s+sep), (0,255,255), -1)
    cv.rectangle(scrambleImg, (pt3+x, pt2+sep), (pt3+s+x, pt2+s+sep), cube[5][3], -1)

    cv.rectangle(scrambleImg, (pt1+x, pt3+sep), (pt1+s+x, pt3+s+sep), cube[5][6], -1)
    cv.rectangle(scrambleImg, (pt2+x, pt3+sep), (pt2+s+x, pt3+s+sep), cube[5][5], -1)
    cv.rectangle(scrambleImg, (pt3+x, pt3+sep), (pt3+s+x, pt3+s+sep), cube[5][4], -1)

    return

def image(scr):
    x = 100
    s = 30
    pt1 = 50
    pt2 = pt1+s+5
    pt3 = pt2+s+5

    # print(cube)

    topRow(s, pt1, pt2, pt3, x)
    middleRow(s, pt1, pt2, pt3, pt3, x)
    bottomRow(s, pt1, pt2, pt3, pt3*2, x)

    cv.putText(scrambleImg, scr, (25, 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), lineType=cv.LINE_AA)
    cv.imshow("Scrambler", scrambleImg)
    cv.waitKey(0)
    cv.destroyAllWindows()
