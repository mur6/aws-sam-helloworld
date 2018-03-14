import json

print('Loading function')


def lambda_handler1(event, context):
    print("Received event: " + json.dumps(event))
    return {"body": "handler 1"}


def lambda_handler2(event, context):
    print("Received event: " + json.dumps(event))
    return {"body": "handler 2"}