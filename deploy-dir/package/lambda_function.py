import json                                                                      # For encoding/decoding JSON data (used for API request/response)
import plotly.graph_objects as go                                                # For creating Plotly visualizations, like choropleth maps


def lambda_handler(event, context):                                              # entrypoint for AWS Lambda function
    try:                                                                            # event: contains request data
        # Extract country from API request                                          # context: Contains runtime info about the Lambda invocation
        if 'queryStringParameters' in event and event['queryStringParameters']:
            country = event['queryStringParameters'].get('country', '')             # checks if the event has query string parameter
        else:                                                                       ## If the query string wasn't present, the code assumes the country might be sent in the request body
            body = json.loads(event.get('body', '{}'))                              # converts JSON string to Python dict; gets the body or defults to empty JSON, 
            country = body.get('country', '')                                       # tries to extract the country
                                                                                    
        if not country:                                                             # if no country was provided, return a 400 Bad Request
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',                             # indicates it's returning JSON
                    'Access-Control-Allow-Origin': '*'                              # allows cross-origin browser access (CORS)
                },
                'body': json.dumps({'error': 'Country parameter is required'})
            }
        
        # Create the choropleth map using graph_objects
        fig = go.Figure(data=go.Choropleth(
            locations=[country],                                                # Pass country as a list
            locationmode='country names',                                       # format of the location data
            z=[100],                                                           # Color values
            colorscale='Blues',                                                # Color scheme
            showscale=False                                                    # Hide color scale bar
        ))
        
        # Update layout with title
        fig.update_layout(
            title=f'Here is the World Map, and you were looking for: {country}',
            geo=dict(showframe=False, showcoastlines=True)
        )
        
        # Convert fig to HTML for web display
        html_content = fig.to_html(include_plotlyjs='cdn')                      # loading also Plotly JS from a CDN
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',                                    # indicates HTML is returned
                'Access-Control-Allow-Origin': '*'                              # allows CORS access
            },
            'body': html_content                                                # contains the actual HTML with the Plotly map created
        }
        
    except Exception as e:                                                      # Handling errors, in case they happen
        return {
            'statusCode': 500,                                                  # Internal server error
            'headers': {                                                        # JSON error message showing what went wrong, useful foe further debugging
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }