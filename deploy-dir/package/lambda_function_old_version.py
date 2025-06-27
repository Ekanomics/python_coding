# import json                                                                      # For encoding/decoding JSON data (used for API request/response)
# import plotly.express as px                                                      # For creating Plotly visualizations, like choropleth maps


# def lambda_handler(event, context):                                              # entrypoint for AWS Lambda function
#     try:                                                                            # event: contains request data
#         # Extract country from API request                                          # context: Contains runtime info about the Lambda invocation
#         if 'queryStringParameters' in event and event['queryStringParameters']:
#             country = event['queryStringParameters'].get('country', '')             # checks if the event has query string parameter
#         else:                                                                       ## If the query string wasn't present, the code assumes the country might be sent in the request body
#             body = json.loads(event.get('body', '{}'))                              # converts JSON string to Python dict; gets the body or defults to empty JSON, 
#             country = body.get('country', '')                                       # tries to extract the country
                                                                                    
#         if not country:                                                             # if no country was provided, return a 400 Bad Request
#             return {
#                 'statusCode': 400,
#                 'headers': {
#                     'Content-Type': 'application/json',                             # indicates it's returning JSON
#                     'Access-Control-Allow-Origin': '*'                              # allows cross-origin browser access (CORS)
#                 },
#                 'body': json.dumps({'error': 'Country parameter is required'})
#             }
        
        
#         data = {                                                                # Creating dataset for highlighting the country on the map
#             'Country': [country],
#             'Values': [100]
#         }
        
        
#         fig = px.choropleth(                                                    # Create the choropleth map
#             data,
#             locations='Country',                                                # Using country name from the dataset
#             locationmode='country names',                                       # format of the location data
#             color="Values",                                                     # Colors the country using the value from "Values"
#             title=f'Here is the World Map, and you were looking for: {country}' # Setting the chart title with dynamic country name inside
#         )
        
#         # Convert fig to HTML for web display
#         html_content = fig.to_html(include_plotlyjs='cdn')                      # loading also Plotly JS from a CDN
        
#         return {
#             'statusCode': 200,
#             'headers': {
#                 'Content-Type': 'text/html',                                    # indicates HTML is returned
#                 'Access-Control-Allow-Origin': '*'                              # allows CORS access
#             },
#             'body': html_content                                                # contains the actual HTML with the Plotly map created
#         }
        
#     except Exception as e:                                                      # Handling errors, in case they happen
#         return {
#             'statusCode': 500,                                                  # Internal server error
#             'headers': {                                                        # JSON error message showing what went wrong, useful foe further debugging
#                 'Content-Type': 'application/json',
#                 'Access-Control-Allow-Origin': '*'
#             },
#             'body': json.dumps({'error': str(e)})
#         }
    

# This code used DataFrames, which required installing additional packages like Pandas
# Because of the complexity and a big weight of the dependencies, we decided to refactor the code and make it with 
# graph_objects code (No pandas)

# Plotly Graph Objects (plotly.graph_objects) is a powerful alternative to Plotly Express — and importantly, 
# it doesn't require pandas or numpy. This makes it ideal for AWS Lambda or minimal environments.

#  1. What is plotly.graph_objects?
# It’s the low-level, fully customizable Plotly API.
# You create each element of the chart manually (traces, layout, etc.).
# Works well with plain Python types like lists and dicts.

# Best for:

# Full control over chart layout
# Minimal dependencies
# Environments where pandas is not available

