import re
import os
import turtle
from PIL import Image


class Homework1:
    def __init__(self):
        self.axim = None
        self.newf = None
        self.newb = None
        self.level = None
        self.output = ""
        self.Run()

    def Run(self):
        axim = input("Input axim:")
        newf = input("Input newf:")
        newb = input("Input newb:")
        level = int(input("Input level:"))
        output = ""

        for i in range(level):
            for char in axim:
                if char == "+":
                    output += "+"
                elif char == "[":
                    output += "["
                elif char == "]":
                    output += "]"
                elif char == "-" or char == "_":
                    output += "-"
                elif char == "F" or char == "f":
                    output += newf
                elif char == "b" or char == "b":
                    output += newb

            print("level", i + 1, ":", output)


class Homework2:
    def __init__(self):
        self.axim = ""
        self.newF = ""
        self.newB = ""
        self.angle = 0
        self.level = 0
        self.Input()
        self.Fractal()

    def CheckChar(self):
        if self.axim != None:
            subString = re.sub("[^FfBb+-_]", "", self.axim)
            if subString != self.axim:
                return False

        if self.newF != None:
            subString = re.sub("[^FfBb+-_]", "", self.newF)
            if subString != self.newF:
                return False

        if self.newB != None:
            subString = re.sub("[^Bb]", "", self.newB)
            if subString != self.newB:
                return False

        return True

    def Input(self):
        while True:
            self.axim = input("Input axim: ")
            if self.CheckChar():
                break
            else:
                print("axim is not a correct string !\n")

        while True:
            self.newF = input("Input newF: ")
            if self.CheckChar():
                break
            else:
                print("newF is not a correct string !\n")

        while True:
            self.newB = input("Input newB: ")
            if self.CheckChar():
                break
            else:
                print("newB is not a correct string !\n")

        while True:
            try:
                self.angle = int(input("Input angle: "))
                break

            except ValueError:
                print("Angle is not a integer !\n")

        while True:
            try:
                self.level = int(input("Input level: "))
                break

            except ValueError:
                print("Level is not a integer !\n")

    def SaveToPNG(self, level):
        img = Image.open(str(level) + ".eps")
        img.save("level_" + str(level + 1) + ".png")
        os.remove(os.getcwd() + "/" + str(level) + ".eps")

    def DrawResult(self, level):
        window = turtle.Screen()
        window.setup(1080, 720)
        window.bgcolor("white")
        pen = turtle.Turtle()
        pen.pensize(1)
        pen.hideturtle()
        pen.color("black")
        pen.penup()
        pen.setpos(0, 0)
        pen.speed(0)

        for letter in self.axim:
            if letter == "F" or letter == "f":
                pen.pendown()
                pen.forward(3)

            if letter == "B" or letter == "b":
                pen.penup()
                pen.forward(3)

            if letter == "+":
                pen.left(self.angle)

            if letter == "-":
                pen.right(self.angle)

        pen.getscreen().getcanvas().postscript(file=str(level) + ".eps")
        pen.clear()

    def PrintResult(self, level):
        print("Level", level + 1, ": ", self.axim)

    def Calculate(self):
        newWord = "\0"
        for letter in self.axim:
            if letter == "F" or letter == "f":
                newWord = newWord + self.newF
            if letter == "B" or letter == "b":
                newWord = newWord + self.newB
            if letter == "+":
                newWord = newWord + "+"
            if letter == "-":
                newWord = newWord + "-"
        self.axim = newWord
        newWord = "\0"

    def Fractal(self):
        for i in range(self.level):
            self.Calculate()
            self.PrintResult(i)
            self.DrawResult(i)
            self.SaveToPNG(i)


if __name__ == "__main__":
    hw = int(input("hw1 or hw2:"))

    if hw == 1:
        Homework1()
    elif hw == 2:
        Homework2()
