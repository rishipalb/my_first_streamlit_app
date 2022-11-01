import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)
st.code(
''' 
x_limit = 

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

st.subheader('Scatter plot')
#Question 3: Change 1
x_limit = st.number_input('Pick x-axis limit', 0,100, value=100)+1
x_axis = np.arange(0, x_limit, 1)
#st.write(x_axis)
y_data = np.random.randn(x_limit)
df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)
st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)
st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

scatter = alt.Chart(df).mark_point().encode(x='x',y='y')
#st.altair_chart(scatter, use_container_width=True)

scatter = alt.Chart(df).mark_circle().encode(x='x',y='y', size='y', color='y', tooltip=['x','y'])
#st.altair_chart(scatter, use_container_width=True)



# Interactive
st.subheader('Slider')
#Question 3: Change 2
x1_limit = (st.slider('Adjust x-axis limit', 0, x_limit-1, x_limit-1))
x1_axis = np.arange(0, x1_limit, 1)
#st.write('x1_axis:', x1_axis)

#Question 3: Change 3
y1_data = np.random.randn(x1_limit)
if st.button('Refresh y-axis random values'): y1_data = np.random.randn(x1_limit)

df1 = pd.DataFrame({'x1': x1_axis,
                     'y1': y1_data})
scatter1 = alt.Chart(df1).mark_circle().encode(x='x1',y='y1', size='y1', color='y1', tooltip=['x1','y1'])
st.altair_chart(scatter1, use_container_width=True)


#Question 3: Change 4
st.subheader('Concatenate')
if st.checkbox('Vertical Concatenate'):
        #Question 3: Change 5
        color = st.color_picker('Pick A Color', '#00f900')
        st.write('The current color is', color)
        area = alt.Chart(df1).mark_area(color=color).encode(x='x1', y='y1')
        obj = alt.vconcat(scatter1, area) #Vertical Concatenation
        st.altair_chart(obj)

else:
        st.write('End of Questions 1 to 3.')

st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Change 1: Used 'st.number_input' to set x_limit
- Change 2: Used 'st.slider' to adjust x-axis
- Change 3: Used 'st.button' to refresh y-axis
- Change 4: Used 'st.checkbox' to convert scatter plot to vertical concatenated area plot
- Change 5: Inserted 'st.color_picker' option to change the color of the area under the plot
""")

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("""
The 2 changes I made were:
- Change 1: Used 'st.checkbox' to chose either vertical or horizontal bar plot
- Change 2: Used 'st.checkbox' to select or de-select 'normalize' the plot option
"""
)
source = pd.read_json('barley.json')
st.write(source)

st.header('Bar Chart')
st.write ('Select the parameters for the bar graph')
Vertical = st.checkbox('Vertical')

Normal = st.checkbox('Normalize')
#Question 4: Change 1
if Vertical:
    if not Normal:
        a=alt.Chart(source).mark_bar().encode(
        x='variety',
        y='sum(yield)',
        color='site'
    )
        st.altair_chart(a, use_container_width=True)
#Question 3: Change 1
    if Normal:
        a=alt.Chart(source).mark_bar().encode(
        x='variety',
        y=alt.Y('sum(yield)', stack="normalize"),
        color='site'
        )
        st.altair_chart(a, use_container_width=True)


if not Vertical:
    if not Normal:
        a=alt.Chart(source).mark_bar().encode(
        x='sum(yield)',
        y='variety',
        color='site'
    )
        st.altair_chart(a, use_container_width=True)
    if Normal:
        a=alt.Chart(source).mark_bar().encode(
        x=alt.X('sum(yield)', stack="normalize"),
        y='variety',
        color='site'
        )
        st.altair_chart(a, use_container_width=True)
