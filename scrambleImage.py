import sys
try:
    import cv2 as cv
    import numpy as np
    cvInstalled = True
    size = 500, 700, 3
    scrambleImg = np.zeros(size, dtype=np.uint8)
    colorAr = []
except:
    print("OpenCV and numpy not installed!")
    cvInstalled = False

class Cube:
    def __init__(self):
        self.cube = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']]

    def faceMove(self, x):
        self.cube[x][0], self.cube[x][6], self.cube[x][4], self.cube[x][2] = self.cube[x][6], self.cube[x][4], self.cube[x][2], self.cube[x][0]
        self.cube[x][1], self.cube[x][7], self.cube[x][5], self.cube[x][3] = self.cube[x][7], self.cube[x][5], self.cube[x][3], self.cube[x][1]
        return
    def faceMovePrime(self, x):
        self.cube[x][0], self.cube[x][2], self.cube[x][4], self.cube[x][6] = self.cube[x][2], self.cube[x][4], self.cube[x][6], self.cube[x][0]
        self.cube[x][1], self.cube[x][3], self.cube[x][5], self.cube[x][7] = self.cube[x][3], self.cube[x][5], self.cube[x][7], self.cube[x][1]
        return

    def swap(self, x1, x2, x3, x4, y1, y2, y3, y4):
        self.cube[x1][y1], self.cube[x2][y2], self.cube[x3][y3], self.cube[x4][y4] = self.cube[x2][y2], self.cube[x3][y3], self.cube[x4][y4], self.cube[x1][y1]

    def printCube(self):
        print(
                                                            "    " + self.cube[0][0] + self.cube[0][1] + self.cube[0][2] + "\n" +
                                                            "    " + self.cube[0][7] + "w" + self.cube[0][3] + "\n" +
                                                            "    " + self.cube[0][6] + self.cube[0][5] + self.cube[0][4] + "\n\n" +
                    self.cube[1][0] + self.cube[1][1] + self.cube[1][2] + " " + self.cube[2][0] + self.cube[2][1] + self.cube[2][2] + " " + self.cube[3][0] + self.cube[3][1] + self.cube[3][2] + " " + self.cube[4][0] + self.cube[4][1] + self.cube[4][2] + "\n" +
                    self.cube[1][7] + "o" + self.cube[1][3] + " " + self.cube[2][7] + "g" + self.cube[2][3] + " " + self.cube[3][7] + "r" + self.cube[3][3] + " " + self.cube[4][7] + "b" + self.cube[4][3] + "\n" +
                    self.cube[1][6] + self.cube[1][5] + self.cube[1][4] + " " + self.cube[2][6] + self.cube[2][5] + self.cube[2][4] + " " + self.cube[3][6] + self.cube[3][5] + self.cube[3][4] + " " + self.cube[4][6] + self.cube[4][5] + self.cube[4][4] + "\n\n" +
                                                            "    " + self.cube[5][0] + self.cube[5][1] + self.cube[5][2] + "\n" +
                                                            "    " + self.cube[5][7] + "y" + self.cube[5][3] + "\n" +
                                                            "    " + self.cube[5][6] + self.cube[5][5] + self.cube[5][4] + "\n"
                )

    def topRow(self, s, pt1, pt2, pt3, x):
        cv.rectangle(scrambleImg, (pt1+x, pt1), (pt1+s+x, pt1+s), self.cube[0][0], -1)
        cv.rectangle(scrambleImg, (pt2+x, pt1), (pt2+s+x, pt1+s), self.cube[0][1], -1)
        cv.rectangle(scrambleImg, (pt3+x, pt1), (pt3+s+x, pt1+s), self.cube[0][2], -1)

        cv.rectangle(scrambleImg, (pt1+x, pt2), (pt1+s+x, pt2+s), self.cube[0][7], -1)
        cv.rectangle(scrambleImg, (pt2+x, pt2), (pt2+s+x, pt2+s), (255,255,255), -1)
        cv.rectangle(scrambleImg, (pt3+x, pt2), (pt3+s+x, pt2+s), self.cube[0][3], -1)

        cv.rectangle(scrambleImg, (pt1+x, pt3), (pt1+s+x, pt3+s), self.cube[0][6], -1)
        cv.rectangle(scrambleImg, (pt2+x, pt3), (pt2+s+x, pt3+s), self.cube[0][5], -1)
        cv.rectangle(scrambleImg, (pt3+x, pt3), (pt3+s+x, pt3+s), self.cube[0][4], -1)
        return

    def middleRow(self, s, pt1, pt2, pt3, sep, x):
        cv.rectangle(scrambleImg, (pt1-sep+x, pt1+sep), (pt1+s-sep+x, pt1+s+sep), self.cube[1][0], -1)
        cv.rectangle(scrambleImg, (pt2-sep+x, pt1+sep), (pt2+s-sep+x, pt1+s+sep), self.cube[1][1], -1)
        cv.rectangle(scrambleImg, (pt3-sep+x, pt1+sep), (pt3+s-sep+x, pt1+s+sep), self.cube[1][2], -1)

        cv.rectangle(scrambleImg, (pt1-sep+x, pt2+sep), (pt1+s-sep+x, pt2+s+sep), self.cube[1][7], -1)
        cv.rectangle(scrambleImg, (pt2-sep+x, pt2+sep),(pt2+s-sep+x, pt2+s+sep),(0,165,225), -1)
        cv.rectangle(scrambleImg, (pt3-sep+x, pt2+sep), (pt3+s-sep+x, pt2+s+sep), self.cube[1][3], -1)

        cv.rectangle(scrambleImg, (pt1-sep+x, pt3+sep), (pt1+s-sep+x, pt3+s+sep), self.cube[1][6], -1)
        cv.rectangle(scrambleImg, (pt2-sep+x, pt3+sep), (pt2+s-sep+x, pt3+s+sep), self.cube[1][5], -1)
        cv.rectangle(scrambleImg, (pt3-sep+x, pt3+sep), (pt3+s-sep+x, pt3+s+sep), self.cube[1][4], -1)

        cv.rectangle(scrambleImg, (pt1+x, pt1+sep), (pt1+s+x, pt1+s+sep), self.cube[2][0], -1)
        cv.rectangle(scrambleImg, (pt2+x, pt1+sep), (pt2+s+x, pt1+s+sep), self.cube[2][1], -1)
        cv.rectangle(scrambleImg, (pt3+x, pt1+sep), (pt3+s+x, pt1+s+sep), self.cube[2][2], -1)

        cv.rectangle(scrambleImg, (pt1+x, pt2+sep), (pt1+s+x, pt2+s+sep), self.cube[2][7], -1)
        cv.rectangle(scrambleImg, (pt2+x, pt2+sep), (pt2+s+x, pt2+s+sep), (0,255,0), -1)
        cv.rectangle(scrambleImg, (pt3+x, pt2+sep), (pt3+s+x, pt2+s+sep), self.cube[2][3], -1)

        cv.rectangle(scrambleImg, (pt1+x, pt3+sep), (pt1+s+x, pt3+s+sep), self.cube[2][6], -1)
        cv.rectangle(scrambleImg, (pt2+x, pt3+sep), (pt2+s+x, pt3+s+sep), self.cube[2][5], -1)
        cv.rectangle(scrambleImg, (pt3+x, pt3+sep), (pt3+s+x, pt3+s+sep), self.cube[2][4], -1)

        cv.rectangle(scrambleImg, (pt1+sep+x, pt1+sep), (pt1+s+sep+x, pt1+s+sep), self.cube[3][0], -1)
        cv.rectangle(scrambleImg, (pt2+sep+x, pt1+sep), (pt2+s+sep+x, pt1+s+sep), self.cube[3][1], -1)
        cv.rectangle(scrambleImg, (pt3+sep+x, pt1+sep), (pt3+s+sep+x, pt1+s+sep), self.cube[3][2], -1)

        cv.rectangle(scrambleImg, (pt1+sep+x, pt2+sep), (pt1+s+sep+x, pt2+s+sep), self.cube[3][7], -1)
        cv.rectangle(scrambleImg, (pt2+sep+x, pt2+sep), (pt2+s+sep+x, pt2+s+sep), (0,0,225), -1)
        cv.rectangle(scrambleImg, (pt3+sep+x, pt2+sep), (pt3+s+sep+x, pt2+s+sep), self.cube[3][3], -1)

        cv.rectangle(scrambleImg, (pt1+sep+x, pt3+sep), (pt1+s+sep+x, pt3+s+sep), self.cube[3][6],-1)
        cv.rectangle(scrambleImg, (pt2+sep+x, pt3+sep), (pt2+s+sep+x, pt3+s+sep), self.cube[3][5],-1)
        cv.rectangle(scrambleImg, (pt3+sep+x, pt3+sep), (pt3+s+sep+x, pt3+s+sep), self.cube[3][4],-1)

        cv.rectangle(scrambleImg, (pt1+(sep*2)+x, pt1+sep), (pt1+s+(sep*2)+x, pt1+s+sep), self.cube[4][0], -1)
        cv.rectangle(scrambleImg, (pt2+(sep*2)+x, pt1+sep), (pt2+s+(sep*2)+x, pt1+s+sep), self.cube[4][1], -1)
        cv.rectangle(scrambleImg, (pt3+(sep*2)+x, pt1+sep), (pt3+s+(sep*2)+x, pt1+s+sep), self.cube[4][2], -1)

        cv.rectangle(scrambleImg, (pt1+(sep*2)+x, pt2+sep), (pt1+s+(sep*2)+x, pt2+s+sep), self.cube[4][7], -1)
        cv.rectangle(scrambleImg, (pt2+(sep*2)+x, pt2+sep), (pt2+s+(sep*2)+x, pt2+s+sep), (255,0,0), -1)
        cv.rectangle(scrambleImg, (pt3+(sep*2)+x, pt2+sep), (pt3+s+(sep*2)+x, pt2+s+sep), self.cube[4][3], -1)

        cv.rectangle(scrambleImg, (pt1+(sep*2)+x, pt3+sep), (pt1+s+(sep*2)+x, pt3+s+sep), self.cube[4][6], -1)
        cv.rectangle(scrambleImg, (pt2+(sep*2)+x, pt3+sep), (pt2+s+(sep*2)+x, pt3+s+sep), self.cube[4][5], -1)
        cv.rectangle(scrambleImg, (pt3+(sep*2)+x, pt3+sep), (pt3+s+(sep*2)+x, pt3+s+sep), self.cube[4][4], -1)

        return

    def bottomRow(self, s, pt1, pt2, pt3, sep, x):
        cv.rectangle(scrambleImg, (pt1+x, pt1+sep), (pt1+s+x, pt1+s+sep), self.cube[5][0], -1)
        cv.rectangle(scrambleImg, (pt2+x, pt1+sep), (pt2+s+x, pt1+s+sep), self.cube[5][1], -1)
        cv.rectangle(scrambleImg, (pt3+x, pt1+sep), (pt3+s+x, pt1+s+sep), self.cube[5][2], -1)

        cv.rectangle(scrambleImg, (pt1+x, pt2+sep), (pt1+s+x, pt2+s+sep), self.cube[5][7], -1)
        cv.rectangle(scrambleImg, (pt2+x, pt2+sep), (pt2+s+x, pt2+s+sep), (0,255,255), -1)
        cv.rectangle(scrambleImg, (pt3+x, pt2+sep), (pt3+s+x, pt2+s+sep), self.cube[5][3], -1)

        cv.rectangle(scrambleImg, (pt1+x, pt3+sep), (pt1+s+x, pt3+s+sep), self.cube[5][6], -1)
        cv.rectangle(scrambleImg, (pt2+x, pt3+sep), (pt2+s+x, pt3+s+sep), self.cube[5][5], -1)
        cv.rectangle(scrambleImg, (pt3+x, pt3+sep), (pt3+s+x, pt3+s+sep), self.cube[5][4], -1)

        return

    def image(self, scr):
        for y in range(6):
            for z in range(8):
                if(self.cube[y][z] == 'w'):
                    self.cube[y][z] = (255,255,255)
                elif(self.cube[y][z] == 'o'):
                    self.cube[y][z] = (0,165,255)
                elif(self.cube[y][z] == 'g'):
                    self.cube[y][z] = (0,255,0)
                elif(self.cube[y][z] == 'r'):
                    self.cube[y][z] = (0,0,255)
                elif(self.cube[y][z] == 'b'):
                    self.cube[y][z] = (255,0,0)
                elif(self.cube[y][z] == 'y'):
                    self.cube[y][z] = (0,255,255)

        x = 100
        s = 30
        pt1 = 50
        pt2 = pt1+s+5
        pt3 = pt2+s+5

        # print(cube)

        self.topRow(s, pt1, pt2, pt3, x)
        self.middleRow(s, pt1, pt2, pt3, pt3, x)
        self.bottomRow(s, pt1, pt2, pt3, pt3*2, x)

        cv.putText(scrambleImg, scr, (25, 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), lineType=cv.LINE_AA)
        cv.imshow("Scrambler", scrambleImg)
        cv.waitKey(0)
        cv.destroyAllWindows()


# print(cube.cube)

def move(cube, m, x):
    #Need to do 3 swaps based on the move
    if(m == 'U'):
        cube.faceMove(x)
        cube.swap(1,2,3,4,0,0,0,0)
        cube.swap(1,2,3,4,1,1,1,1)
        cube.swap(1,2,3,4,2,2,2,2)
    elif(m == "U'"):
        cube.faceMovePrime(x)
        cube.swap(1,4,3,2,0,0,0,0)
        cube.swap(1,4,3,2,1,1,1,1)
        cube.swap(1,4,3,2,2,2,2,2)
    elif(m == 'U2'):
        move(cube, 'U', x)
        move(cube, 'U', x)
    elif(m == 'D'):
        cube.faceMove(x)
        cube.swap(1,4,3,2,4,4,4,4)
        cube.swap(1,4,3,2,5,5,5,5)
        cube.swap(1,4,3,2,6,6,6,6)
    elif(m == "D'"):
        cube.faceMovePrime(x)
        cube.swap(1,2,3,4,4,4,4,4)
        cube.swap(1,2,3,4,5,5,5,5)
        cube.swap(1,2,3,4,6,6,6,6)
    elif(m == 'D2'):
        move(cube, 'D', x)
        move(cube, 'D', x)
    elif(m == 'R'):
        cube.faceMove(x)
        cube.swap(0,2,5,4,2,2,2,6)
        cube.swap(0,2,5,4,3,3,3,7)
        cube.swap(0,2,5,4,4,4,4,0)
    elif(m == "R'"):
        cube.faceMovePrime(x)
        cube.swap(0,4,5,2,2,6,2,2)
        cube.swap(0,4,5,2,3,7,3,3)
        cube.swap(0,4,5,2,4,0,4,4)
    elif(m == 'R2'):
        move(cube, 'R', x)
        move(cube, 'R', x)
    elif(m == 'L'):
        cube.faceMove(x)
        cube.swap(0,4,5,2,6,2,6,6)
        cube.swap(0,4,5,2,7,3,7,7)
        cube.swap(0,4,5,2,0,4,0,0)
    elif(m == "L'"):
        cube.faceMovePrime(x)
        cube.swap(0,2,5,4,6,6,6,2)
        cube.swap(0,2,5,4,7,7,7,3)
        cube.swap(0,2,5,4,0,0,0,4)
    elif(m == 'L2'):
        move(cube, 'L', x)
        move(cube, 'L', x)
    elif(m == 'F'):
        cube.faceMove(x)
        cube.swap(0,1,5,3,4,2,0,6)
        cube.swap(0,1,5,3,5,3,1,7)
        cube.swap(0,1,5,3,6,4,2,0)
    elif(m == "F'"):
        cube.faceMovePrime(x)
        cube.swap(0,3,5,1,4,6,0,2)
        cube.swap(0,3,5,1,5,7,1,3)
        cube.swap(0,3,5,1,6,0,2,4)
    elif(m == 'F2'):
        move(cube, 'F', x)
        move(cube, 'F', x)
    elif(m == 'B'):
        cube.faceMove(x)
        cube.swap(0,3,5,1,0,2,4,6)
        cube.swap(0,3,5,1,1,3,5,7)
        cube.swap(0,3,5,1,2,4,6,0)
    elif(m == "B'"):
        cube.faceMovePrime(x)
        cube.swap(0,1,5,3,0,6,4,2)
        cube.swap(0,1,5,3,1,7,5,3)
        cube.swap(0,1,5,3,2,0,6,4)
    elif(m == 'B2'):
        move(cube, 'B', x)
        move(cube, 'B', x)

def scramble(scr, len):
    cube = Cube()
    moves = ['U', 'L', 'F', 'R', 'B', 'D']
    for x in scr:
        move(cube, str(x[0])+str(x[1]), moves.index(x[0]))

    scr = ''.join(str(scr[x][0]) + str(scr[x][1]) + ' ' for x in range(len)) + "[" + str(len) + "]"
    if('-cv' in sys.argv or cvInstalled == True):
        cube.image(scr)
    else:
        cube.printCube()