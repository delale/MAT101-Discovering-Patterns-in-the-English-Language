"""
Present your findings from Task 4 graphically with the help of matplotlib. (For a
quick introduction to matplotlib go to: http://matplotlib.org/users/pyplot_
tutorial.html). Illustrate how often the 20 most frequent words occur. Compare
at least 5 novels
"""
import matplotlib.pyplot as plt
from task2 import occurences

# task 2 returns an ordered least of pairs

ttl = ("Wuthering Heights", "Title", "Title", "Title", "Title", "Title") # this will be the titles of the novels

# no need for the variable paths as this can be achieved with string concatenation i.e. Title+'.txt'
# as long as the novels are in the same directory of the script

res = [occurences(t+'.txt') for t in ttl]

# plotting
fig, ax = plt.subplots(2,3) # make a grid of subplot(2 rows, 3 columns)

"""
>>> help(plt.subplots_adjust)
Help on function subplots_adjust in module matplotlib.pyplot:
subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
    Adjust the subplot layout parameters.
    
    Unset parameters are left unmodified; initial values are given by
    :rc:`figure.subplot.[name]`.
    
    Parameters
    ----------
    left : float, optional
        The position of the left edge of the subplots,
        as a fraction of the figure width.
    right : float, optional
        The position of the right edge of the subplots,
        as a fraction of the figure width.
    bottom : float, optional
        The position of the bottom edge of the subplots,
        as a fraction of the figure height.
    top : float, optional
        The position of the top edge of the subplots,
        as a fraction of the figure height.
    wspace : float, optional
        The width of the padding between subplots,
        as a fraction of the average axes width.
    hspace : float, optional
        The height of the padding between subplots,
        as a fraction of the average axes height.
"""

fig.subplots_adjust(wspace=0.3, hspace=0.5, top=0.87)

# loop through all the results, take only the 20 most frequent words, plot
for x in range(len(ttl)):

    Words, Numbers = zip(*res[x][:20]) # extracting 20 most frequent words and their occurences

    ax[x % 2, x % 3].bar(Words, Numbers) # barplot
    ax[x % 2, x % 3].set_ylabel("Occurances", fontsize=7) # y-axis label
    ax[x % 2, x % 3].set_title(ttl[x], fontsize=10) # plot title
    ax[x % 2, x % 3].tick_params(axis="x", labelsize=6, labelrotation=90) # y-axis ticks
    ax[x % 2, x % 3].tick_params(axis="y", labelsize=6) # x-axis ticks

plt.show()

