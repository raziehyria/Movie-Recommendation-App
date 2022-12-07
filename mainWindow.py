
import tkinter
from tkinter import *
from tkinter import ttk

# Creating main window
win = tkinter.Tk()
win.geometry("400x300")
win.minsize(400, 300)
win.title("Movie Recommendation")


def buttonEnabler():
    if str(genre.get()) and int(rating.get()) != 0 and int(year.get()) != 0:
        submitButton.config(state="normal")


# Creating tabs
tabs = ttk.Notebook(win)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tab3 = ttk.Frame(tabs)

tkinter.Tk.grid_rowconfigure(win, 0, weight=1)
tkinter.Tk.grid_columnconfigure(win, 0, weight=1)
tkinter.Tk.grid_columnconfigure(tab1, (1, 2), weight=1)
tkinter.Tk.grid_columnconfigure(tab2, (1, 2), weight=1)
tkinter.Tk.grid_columnconfigure(tab3, (1, 2), weight=1)


# Tab 1 - Genre
genre = StringVar()

tabs.add(tab1, text="Genre")
genreLabel = ttk.Label(tab1, text="Select a genre:")
genreLabel.grid(row=1, column=0)
genreDescription = ttk.Label(tab1, text="The genre, or specific type of movie to be searched for.")

genre1 = ttk.Radiobutton(tab1, text="Action", value="action", variable=genre, command=buttonEnabler)
genre2 = ttk.Radiobutton(tab1, text="Sci-Fi", value="sci-fi", variable=genre, command=buttonEnabler)
genre3 = ttk.Radiobutton(tab1, text="Comedy", value="comedy", variable=genre, command=buttonEnabler)
genre4 = ttk.Radiobutton(tab1, text="Thriller", value="thriller", variable=genre, command=buttonEnabler)
genre5 = ttk.Radiobutton(tab1, text="Horror", value="horror", variable=genre, command=buttonEnabler)

# Adding the radio buttons to the tab
genres = [genre1, genre2, genre3, genre4, genre5]
for each in range(0, 5):
    genres[each].grid(row=each+2, column=0, sticky="w")

genreDescription.grid(row=0, column=0, columnspan=3, pady=(10, 5), sticky="n")


# Tab 2 - Rating

tabs.add(tab2, text="Rating")
ratingLabel = ttk.Label(tab2, text="Select a rating:")
ratingLabel.grid(row=1, column=0)
ratingDescription = ttk.Label(tab2, text="The rating of the movie to be searched for.")


rating = IntVar()

rating1 = ttk.Radiobutton(tab2, text="1 Star", value=1, variable=rating, command=buttonEnabler)
rating2 = ttk.Radiobutton(tab2, text="2 Stars", value=2, variable=rating, command=buttonEnabler)
rating3 = ttk.Radiobutton(tab2, text="3 Stars", value=3, variable=rating, command=buttonEnabler)
rating4 = ttk.Radiobutton(tab2, text="4 Stars", value=4, variable=rating, command=buttonEnabler)
rating5 = ttk.Radiobutton(tab2, text="5 Stars", value=5, variable=rating, command=buttonEnabler)

ratings = [rating1, rating2, rating3, rating4, rating5]
for each in range(0, 5):
    ratings[each].grid(row=each+2, column=0, sticky="w")

ratingDescription.grid(row=0, column=0, columnspan=3, pady=(10, 5), sticky="n")


# Tab 3 - Year (Intervals)

tabs.add(tab3, text="Year")
yearLabel = ttk.Label(tab3, text="Select a year:")
yearLabel.grid(row=1, column=0)
yearDescription = ttk.Label(tab3, text="The year intervals in which the movie released.")

year = IntVar()

yearGroup1 = ttk.Radiobutton(tab3, text="2020 and beyond", value=5, variable=year, command=buttonEnabler)
yearGroup2 = ttk.Radiobutton(tab3, text="2017 - 2019", value=4, variable=year, command=buttonEnabler)
yearGroup3 = ttk.Radiobutton(tab3, text="2015 - 2017", value=3, variable=year, command=buttonEnabler)
yearGroup4 = ttk.Radiobutton(tab3, text="2010 - 2015", value=2, variable=year, command=buttonEnabler)
yearGroup5 = ttk.Radiobutton(tab3, text="Before 2010", value=1, variable=year, command=buttonEnabler)

years = [yearGroup1, yearGroup2, yearGroup3, yearGroup4, yearGroup5]
for each in range(0, 5):
    years[each].grid(row=each+2, column=0, sticky="w")

yearDescription.grid(row=0, column=0, columnspan=3, pady=(10, 5), sticky="n")

tabs.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 0), sticky="nsew")

submitButton = ttk.Button(win, text="Submit Filters", state="disabled")
submitButton.grid(row=1, column=2, padx=10, pady=(0, 10), sticky="e")
