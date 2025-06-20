import json
import plotly.express as px
import plotly.graph_objects as go


def lambda_handler(event, context):
    try:
        # Extract country from API request
        if 'queryStringParameters' in event and event['queryStringParameters']:
            country = event['queryStringParameters'].get('country', '')
        else:
            body = json.loads(event.get('body', '{}'))
            country = body.get('country', '')
        
        if not country:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Country parameter is required'})
            }
        
        # Create the choropleth map
        data = {
            'Country': [country],
            'Values': [100]
        }
        
        fig = px.choropleth(
            data,
            locations='Country',
            locationmode='country names',
            color="Values",
            title=f'Here is the World Map, and you were looking for: {country}'
        )
        
        # Convert to HTML for web display
        html_content = fig.to_html(include_plotlyjs='cdn')
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
                'Access-Control-Allow-Origin': '*'
            },
            'body': html_content
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
    

