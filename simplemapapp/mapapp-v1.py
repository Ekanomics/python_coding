# Plotly Express lib helps creating interactive charts, incl choropleth maps
# A choropleth map is a type of thematic map where geographic areas (like countries..) are colored or shaded according to statistical data values, or the values we assign.
import plotly.express as px


country = input("Enter the country name: ")


# Creating a dictionary with DataFrame-like structure
data = {
    'Country': [country],           # Indicating location(e.g., country name)
    'Values': [100]                 # list with value 100, which will be used to apply color and color intensity
}


# Creates a choropleth map using the data
fig = px.choropleth(                                    
    data,                                                                           # Parameters
    locations = 'Country',
    locationmode = 'country names',
    color = "Values",
    title = f'Here is the World Map, and you were looking for: {country}'
)

try:
    fig.show()                                              # Displays interactive map
except Exception as err:                                    # fig.show() renders the chart as a full HTML page using Plotly's JavaScript.
    print("Error occured:", err)                            # This is because Plotly Express uses JavaScript-based rendering, and when you run fig.show():

# It creates an HTML file behind the scenes that contains:
# The map (via plotly.js, which is a JavaScript library for plotting).
# The data you gave it.


# Output: Country which we entered at the beginning, will be highlighted with the color (density-100)



