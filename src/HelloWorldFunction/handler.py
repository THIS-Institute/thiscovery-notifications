import json
from http import HTTPStatus
def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))

    return {"statusCode": HTTPStatus.OK,
            "body": "Hello World!"
            }
