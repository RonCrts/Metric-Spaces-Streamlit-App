# Metric-Spaces-Streamlit-App
I have created this repository because of my interest in studying metric spaces, so I have built a whole interactive application in Python using Streamlit to learn more about it.

For my study I have started the video series of "The Bright Side Of Mathematics" channel on Youtube, mainly this project is a consequence of what I learned in the first video of the series called "Functional Analysis - Part 1 - Metric Space".

A metric space is a set of points for which the distances between all pairs of points are defined.
         
    -The distance between two points is a real number, and is always positive or zero.
         
    -The distance between a point and itself is zero.
         
    -The distance between two different points is positive.
         
    -The distance between two points is the same regardless of the order of the two points.
         
    -The distance between two points is less than or equal to the sum of the distances from the first point to a third point and from the 
     third point to the second point.

    In mathematical notation, these rules are expressed as follows:

    - For all x, y in X, d(x, y) >= 0.
    - For all x, y in X, d(x, y) = 0 if and only if x = y.
    - For all x, y in X, d(x, y) = d(y, x).
    - For all x, y, z in X, d(x, y) + d(y, z) >= d(x, z).

Attached is the first video of the series.

[![Alt text](https://img.youtube.com/vi/yDdxFBcvSGw/0.jpg)](https://www.youtube.com/watch?v=yDdxFBcvSGw)

In summary, this is a Python application that creates an interactive Streamlit interface for creating and visualizing metric spaces. once the user has selected the values, the application plots the metric space and checks if the distance matrix meets the rules of a metric space. If the distance matrix is a metric space, the application saves the metric space in a database along with its name, number of points and range of values. The application also allows the user to visualize all the metric spaces in the database in a Pandas data frame. The application is written in Python and uses several modules, including Streamlit, NumPy and Pandas, as well as several custom modules that define functions for creating and plotting metric spaces and for interacting with a database.

