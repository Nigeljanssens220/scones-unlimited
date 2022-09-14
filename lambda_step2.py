import base64
import json

import boto3

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2022-09-14-11-56-09-381"
runtime = boto3.client("runtime.sagemaker")


def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event.get("image_data"))

    if not image:
        return {"statusCode": 400, "body": "No image data"}

    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT, ContentType="image/png", Body=image
    )

    # We return the data back to the Step Function
    event["inferences"] = response["Body"].read().decode("utf-8")

    return {"statusCode": 200, "body": json.dumps(event)}
