import tkinter
from tkinter import *
from tkinter import ttk


# import main


class MovieReccApp:
    def __init__(self):

        # Creating main window
        self.win = tkinter.Tk()
        self.win.geometry("400x300")
        self.win.minsize(400, 300)
        self.win.title("Movie Recommendation")

        # Creating tabs
        self.tabs = ttk.Notebook(self.win)
        tab1 = ttk.Frame(self.tabs)
        tab2 = ttk.Frame(self.tabs)
        tab3 = ttk.Frame(self.tabs)

        tkinter.Tk.grid_rowconfigure(self.win, 0, weight=1)
        tkinter.Tk.grid_columnconfigure(self.win, 0, weight=1)
        tkinter.Tk.grid_columnconfigure(tab1, (1, 2), weight=1)
        tkinter.Tk.grid_columnconfigure(tab2, (1, 2), weight=1)
        tkinter.Tk.grid_columnconfigure(tab3, (1, 2), weight=1)

        # variable that controls start/stop flow of the program
        self.submit_button_clicked = False

        # Tab 1 - Genre
        self.genre = StringVar()

        self.tabs.add(tab1, text="Genre")
        genreLabel = ttk.Label(tab1, text="Select a genre:")
        genreLabel.grid(row=1, column=0)
        genreDescription = ttk.Label(tab1, text="The genre, or specific type of movie to be searched for.")

        genre1 = ttk.Radiobutton(tab1, text="Action", value="action", variable=self.genre, command=self.buttonEnabler)
        genre2 = ttk.Radiobutton(tab1, text="Sci-Fi", value="sci-fi", variable=self.genre, command=self.buttonEnabler)
        genre3 = ttk.Radiobutton(tab1, text="Comedy", value="comedy", variable=self.genre, command=self.buttonEnabler)
        genre4 = ttk.Radiobutton(tab1, text="Thriller", value="thriller", variable=self.genre,
                                 command=self.buttonEnabler)
        genre5 = ttk.Radiobutton(tab1, text="Horror", value="horror", variable=self.genre, command=self.buttonEnabler)

        # Adding the radio buttons to the tab
        genres = [genre1, genre2, genre3, genre4, genre5]
        for each in range(0, 5):
            genres[each].grid(row=each + 2, column=0, sticky="w")

        genreDescription.grid(row=0, column=0, columnspan=3, pady=(10, 5), sticky="n")

        # Tab 2 - Rating
        self.tabs.add(tab2, text="Rating")
        ratingLabel = ttk.Label(tab2, text="Select a rating:")
        ratingLabel.grid(row=1, column=0)
        ratingDescription = ttk.Label(tab2, text="The rating of the movie to be searched for.")

        self.rating = IntVar()

        rating1 = ttk.Radiobutton(tab2, text="1 Star", value=1, variable=self.rating, command=self.buttonEnabler)
        rating2 = ttk.Radiobutton(tab2, text="2 Stars", value=2, variable=self.rating, command=self.buttonEnabler)
        rating3 = ttk.Radiobutton(tab2, text="3 Stars", value=3, variable=self.rating, command=self.buttonEnabler)
        rating4 = ttk.Radiobutton(tab2, text="4 Stars", value=4, variable=self.rating, command=self.buttonEnabler)
        rating5 = ttk.Radiobutton(tab2, text="5 Stars", value=5, variable=self.rating, command=self.buttonEnabler)

        ratings = [rating1, rating2, rating3, rating4, rating5]
        for each in range(0, 5):
            ratings[each].grid(row=each + 2, column=0, sticky="w")

        ratingDescription.grid(row=0, column=0, columnspan=3, pady=(10, 5), sticky="n")

        # Tab 3 - Year (Intervals)

        self.tabs.add(tab3, text="Year")
        yearLabel = ttk.Label(tab3, text="Select a year:")
        yearLabel.grid(row=1, column=0)
        yearDescription = ttk.Label(tab3, text="The year intervals in which the movie released.")

        self.year = IntVar()

        yearGroup1 = ttk.Radiobutton(tab3, text="2020 and beyond", value=5, variable=self.year,
                                     command=self.buttonEnabler)
        yearGroup2 = ttk.Radiobutton(tab3, text="2017 - 2019", value=4, variable=self.year, command=self.buttonEnabler)
        yearGroup3 = ttk.Radiobutton(tab3, text="2015 - 2017", value=3, variable=self.year, command=self.buttonEnabler)
        yearGroup4 = ttk.Radiobutton(tab3, text="2010 - 2015", value=2, variable=self.year, command=self.buttonEnabler)
        yearGroup5 = ttk.Radiobutton(tab3, text="Before 2010", value=1, variable=self.year, command=self.buttonEnabler)

        years = [yearGroup1, yearGroup2, yearGroup3, yearGroup4, yearGroup5]
        for each in range(0, 5):
            years[each].grid(row=each + 2, column=0, sticky="w")

        yearDescription.grid(row=0, column=0, columnspan=3, pady=(10, 5), sticky="n")

        self.tabs.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 0), sticky="nsew")

        # INCLUDED COMMAND = TO TIE BUTTON to running app window
        self.submitButton = ttk.Button(self.win, text="Submit Filters", state="disabled",
                                       command=self.submit_button_pressed())

        self.submitButton.grid(row=1, column=2, padx=10, pady=(0, 10), sticky="e")

    def buttonEnabler(self):
        if str(self.genre.get()) and int(self.rating.get()) != 0 and int(self.year.get()) != 0:
            self.submitButton.config(state="normal")
            self.submit_button_clicked = True  # once all choices are selected, status of button click changed to true

    def submit_button_pressed(self, event=None):
        # if the button is clicked, get the value of each option and put it into list
        if self.submit_button_clicked:
            filters = [self.year.get(), self.rating.get(), self.genre.get()]
            pass
            # access tree and store into child nodes
            # or send to the the database for search
            # will remove once logic implemented: used to avoid errors

    # run function to catch mouse scroll error and be called on by main
    def run(self):
        try:
            # Running Window
            self.win.mainloop()
        except UnicodeDecodeError:  # if error occurs, let user exit the app gui. needs to rerun and try again
            error_msg = "\nPlease re-run the program."
            print(error_msg)
            input("Press any key to exit")
            pass


# used to build the gui and run the move recc app
if __name__ == '__main__':
    app = MovieReccApp()
    app.run()
