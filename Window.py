import tkinter as tinker
from tkinter import ttk


class Page(tinker.Tk):
    def __init__(self, *args, **kwargs):
        tinker.Tk.__init__(self, *args, **kwargs)
        container = tinker.Frame(self, width=500, height=500)
        container.pack(side="top", fill="both", expand=False)

        self.frames = {}
        frame = Page1(container, self)
        self.frames[Page1] = frame
        self.show_frame(Page1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Page1(tinker.Frame):
    def __init__(self, parent, controller):
        tinker.Frame.__init__(self, parent)
        title = tinker.Label(self, text="Welcome to the Ratings Trading desktop app!", font=("Helvetica", 22))
        title.pack(pady=10, padx=10)
        # button to next frame
        nextButton = tinker.Button(self, text="Next", command=lambda: controller.show_frame(Page2))
        nextButton.place(x=415, y=450)


class Page2(tinker.Frame):
    def __init__(self, parent, controller):
        tinker.Frame.__init__(self, parent)
        title = tinker.Label(self, text="Please select your brokerage:", font=("Helvetica", 22))
        title.pack(pady=10, padx=10)
        # button to next frame
        nextButton = tinker.Button(self, text="Next", command=lambda: controller.show_frame(Page3))
        nextButton.place(x=415, y=450)
        # button to previous frame
        backButton = tinker.Button(self, text="Back", command=lambda: controller.show_frame(Page1))
        backButton.place(x=50, y=450)


class Page3(tinker.Frame):
    def __init__(self, parent, controller):
        tinker.Frame.__init__(self, parent)
        title = tinker.Label(self, text="Now, select the credit agency you would like to trade ratings off of:",
                             font=("Helvetica", 22))
        title.pack(pady=10, padx=10)
        # button to next frame
        nextButton = tinker.Button(self, text="Next", command=lambda: controller.show_frame(Page4))
        nextButton.place(x=415, y=450)
        # button to previous frame
        backButton = tinker.Button(self, text="Back", command=lambda: controller.show_frame(Page2))
        backButton.place(x=50, y=450)


class Page4(tinker.Frame):
    def __init__(self, parent, controller):
        tinker.Frame.__init__(self, parent)
        title = tinker.Label(self, text="Now, here are the securities and upgrades/downgrades:", font=("Helvetica", 22))
        title.pack(pady=10, padx=10)
        # button to next frame
        nextButton = tinker.Button(self, text="Next", command=lambda: controller.show_frame(Page5))
        nextButton.place(x=415, y=450)
        # button to previous frame
        backButton = tinker.Button(self, text="Back", command=lambda: controller.show_frame(Page3))
        backButton.place(x=50, y=450)


class Page5(tinker.Frame):
    def __init__(self, parent, controller):
        tinker.Frame.__init__(self, parent)
        title = tinker.Label(self, text="Select the amount of shares you'd like to buy/sell:", font=("Helvetica", 22))
        title.pack(pady=10, padx=10)
        # button to next frame
        nextButton = tinker.Button(self, text="Next", command=lambda: controller.show_frame(Page5))
        nextButton.place(x=415, y=450)
        # button to previous frame
        backButton = tinker.Button(self, text="Back", command=lambda: controller.show_frame(Page3))
        backButton.place(x=50, y=450)


app = Page()
app.mainloop()
