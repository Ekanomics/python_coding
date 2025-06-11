# Plotly Express lib helps creating interactive charts, incl choropleth maps
# A choropleth map is a type of thematic map where geographic areas (like countries..) are colored or shaded according to statistical data values.
import plotly.express as px


country = input("Enter the country name: ")


# Creating a dictionary
data = {
    'Country': [country],           # list with user provided country name
    'Values': [100]                 # list with value 100, whicih will be used to apply color intensity
}



fig = px.choropleth(                                    # Creates a choropleth map using the data
    data,
    locations = 'Country',
    locationmode = 'country names',
    color = "Values",
    color_continuous_scale = 'Inferno',
    title = f'Country Map Highlighting {country}'
)

try:
    fig.show()                                              # Displays interactive map
except Exception as err:
    print("Error occured:", err)


# Output: Country which we entered at the beginning, will be highlighted with the color (value 100)


