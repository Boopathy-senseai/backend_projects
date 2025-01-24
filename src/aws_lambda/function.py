import json

def lambda_handler(event, context):
    """
    Lambda function that processes an input event and returns a response.

    Parameters:
    - event: dict, required
        API Gateway Lambda Proxy Input Format
    - context: object, required
        Lambda Context runtime methods and attributes

    Returns:
    - dict: API Gateway Lambda Proxy Output Format
    """
    # Log the received event
    print("Received event:", json.dumps(event, indent=2))

    # Extract input from the event (e.g., name)
    name = event.get("name", "World")
    response_message = f"Hello, {name}!"

    # Return the response
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": response_message,
            "input": event
        })
    }
