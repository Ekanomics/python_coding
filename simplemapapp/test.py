print("Starting test...")

try:
    print("1. Testing basic imports...")
    import json
    print("✅ json imported")
    
    import plotly.express as px
    print("✅ plotly imported")
    
    print("2. Testing lambda function import...")
    from mapapp_v2_lambda import lambda_handler
    print("✅ lambda_function imported")
    
    print("3. Testing basic functionality...")
    event = {
        'queryStringParameters': {
            'country': 'United States'
        }
    }
    
    result = lambda_handler(event, {})
    print(f"✅ Function executed - Status: {result['statusCode']}")
    
    if result['statusCode'] == 200:
        print("🎉 SUCCESS: Your Lambda function works!")
    else:
        print(f"⚠️  Function returned error: {result['body']}")
        
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Check if all dependencies are installed correctly")
    
except Exception as e:
    print(f"❌ Runtime Error: {e}")
    print("Check your lambda_function.py for syntax errors")

print("Test completed.")