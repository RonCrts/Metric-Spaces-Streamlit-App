import streamlit as st
import numpy as np
from functions import define_metric_space, is_metric_space, plot_metric_space
from db import save_metric_space, get_metric_spaces
import pandas as pd



st.set_option('deprecation.showPyplotGlobalUse', False)


# Creating an interactive streamlit application.
st.title('Metric Spaces')
st.write('''
    A metric space is a set of points for which the distances between all pairs of points are defined.
         
    -The distance between two points is a real number, and is always positive or zero.
         
    -The distance between a point and itself is zero.
         
    -The distance between two different points is positive.
         
    -The distance between two points is the same regardless of the order of the two points.
         
    -The distance between two points is less than or equal to the sum of the distances from the first point to a third point and from the third point to the second point.

    In mathematical notation, these rules are expressed as follows:

    - For all x, y in X, d(x, y) >= 0.
    - For all x, y in X, d(x, y) = 0 if and only if x = y.
    - For all x, y in X, d(x, y) = d(y, x).
    - For all x, y, z in X, d(x, y) + d(y, z) >= d(x, z).
''')

# Creating a sidebar.
st.sidebar.title('Create a Metric Space')
st.sidebar.write('''
    Choose a set of points and define a metric space.
''')

name = st.sidebar.text_input('Name of the metric space')

# Creating a slider to choose the number of points.
n = st.sidebar.slider('Number of points', 2, 10, 5)

# Creating a slider to choose the minimum value of the points.
min_value = st.sidebar.slider('Minimum value', -10.0, 0.0, -5.0)

# Creating a slider to choose the maximum value of the points.
max_value = st.sidebar.slider('Maximum value', 0.0, 10.0, 5.0)



# Creating a button to create the metric space.
if st.sidebar.button('Create'):
    # Creating a set of points.
    X = np.random.uniform(min_value, max_value, n)

    # Defining the metric space.
    D = define_metric_space(X)

    # Plotting the metric space.
    plot_metric_space(D)
    
    if is_metric_space(D):
            st.write('The distance matrix is a metric space.')
            save_metric_space(name, n, min_value, max_value, str(D))
    else:
        st.write('The distance matrix is not a metric space.')

if st.sidebar.button('Show metric spaces in the database'):
    metric_spaces_df = get_metric_spaces()
    st.dataframe(metric_spaces_df)


    