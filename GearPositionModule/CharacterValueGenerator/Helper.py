from tkinter import *


class alphanumericDisplayValue:

    def __init__(self):
        self.value = 0

        self.i = self.h = self.f = self.g1 = self.e = self.m = self.d = self.l = self.k = self.c = self.dp = self.g2 = self.b = self.j = self.a = True


        top = Tk(className="Helper")

        self.label = Label(top, text=hex(self.value))

        self.label.pack()

        self.w = Canvas(top, width=400, height=600)
        # a
        self.w.create_line(100, 100, 300, 100, width=10)
        # d
        self.w.create_line(100, 520, 300, 520, width=10)
        # f
        self.w.create_line(100, 120, 100, 320, width=10)
        # b
        self.w.create_line(300, 120, 300, 320, width=10)

        # g1
        self.w.create_line(120, 320, 180, 320, width=10)
        # g2
        self.w.create_line(220, 320, 280, 320, width=10)

        # e
        self.w.create_line(100, 340, 100, 500, width=10)
        # c
        self.w.create_line(300, 340, 300, 500, width=10)
        # i
        self.w.create_line(200, 120, 200, 320, width=10)
        # l
        self.w.create_line(200, 340, 200, 500, width=10)

        # h
        self.w.create_line(120, 120, 180, 280, width=10)
        # j
        self.w.create_line(280, 120, 220, 280, width=10)

        # m
        self.w.create_line(180, 340, 120, 500, width=10)

        # k
        self.w.create_line(220, 340, 280, 500, width=10)

        self.w.bind("<Button-1>", self.callback)
        self.w.pack()
        Button(top, text="generate", command=self.generate, width=30).pack()
        Button(top, text="clear", command=self.clear, width=30).pack()

        top.mainloop()


    def generate(self):

        listifySegments = []
        # i is least significant bit
        listifySegments.append(self.i)
        listifySegments.append(self.h)
        listifySegments.append(self.f)
        listifySegments.append(self.g1)
        listifySegments.append(self.e)
        listifySegments.append(self.m)
        listifySegments.append(self.d)
        listifySegments.append(self.l)
        listifySegments.append(self.k)
        listifySegments.append(self.c)
        listifySegments.append(self.dp)
        listifySegments.append(self.g2)
        listifySegments.append(self.b)
        listifySegments.append(self.j)
        listifySegments.append(self.a)

        #i is most significant bit
        listifySegments = listifySegments[::-1]

        sum = 0

        for i, val in enumerate(listifySegments):
            sum += val*2**i

        #add 16th value because of we use 2 8-bit shift registers

        sum += 2**15

        #print(sum,'-' , hex(sum))
        self.label.configure(text=hex(sum))

    def callback(self, event):

        if (90 < event.x < 110 ):
            if (120 < event.y <320):
                self.f = not self.f
            elif(340< event.y < 500):
                self.e = not self.e


        if (290 < event.x < 310 ):
            if (120 < event.y <320):
                self.b = not self.b
            elif(340< event.y < 500):
                self.c = not self.c

        if ( 90 <event.y <110):
            if ( 100< event.x < 500):
                self.a = not self.a

        if ( 480 <event.y <550):
            if ( 100< event.x < 500):
                self.d = not self.d

        if (190 < event.x < 210 ):
            if (120 < event.y <320):
                self.i = not self.i
            elif(340< event.y < 500):
                self.l = not self.l

        if ( 290 <event.y <350):
            if ( 100< event.x < 200):
                self.g1 = not self.g1
            elif(220 < event.x< 500):
                self.g2 = not self.g2

        if (125 < event.y < 280):
            if (110 < event.x < 180):
                self.h = not self.h
            elif (215 < event.x < 280):
                self.j = not self.j

        if (335 < event.y < 500):
            if (110 < event.x < 180):
                self.m = not self.m
            elif (215 < event.x < 280):
                self.k = not self.k

        self.reDraw()

    def clear(self):
        self.i = self.h = self.f = self.g1 = self.e = self.m = self.d = self.l = self.k = self.c = self.dp = self.g2 = self.b = self.j = self.a = True
        self.reDraw()

    def reDraw(self):
        self.w.delete('all')

        # a
        self.w.create_line(100, 100, 300, 100, width=10, fill='black' if self.a else 'red')
        # d
        self.w.create_line(100, 520, 300, 520, width=10, fill='black' if self.d else 'red')
        # f
        self.w.create_line(100, 120, 100, 320, width=10, fill='black' if self.f else 'red')
        # b
        self.w.create_line(300, 120, 300, 320, width=10, fill='black' if self.b else 'red')

        # g1
        self.w.create_line(120, 320, 180, 320, width=10, fill='black' if self.g1 else 'red')
        # g2
        self.w.create_line(220, 320, 280, 320, width=10, fill='black' if self.g2 else 'red')

        # e
        self.w.create_line(100, 340, 100, 500, width=10, fill='black' if self.e else 'red')
        # c
        self.w.create_line(300, 340, 300, 500, width=10, fill='black' if self.c else 'red')
        # i
        self.w.create_line(200, 120, 200, 320, width=10, fill='black' if self.i else 'red')
        # l
        self.w.create_line(200, 340, 200, 500, width=10, fill='black' if self.l else 'red')

        # h
        self.w.create_line(120, 120, 180, 280, width=10, fill='black' if self.h else 'red')
        # j
        self.w.create_line(280, 120, 220, 280, width=10, fill='black' if self.j else 'red')

        # m
        self.w.create_line(180, 340, 120, 500, width=10, fill='black' if self.m else 'red')

        # k
        self.w.create_line(220, 340, 280, 500, width=10, fill='black' if self.k else 'red')





alphanumericDisplayValue()