import json

THRESHOLD = 0.93


def lambda_handler(event, context):

    # Grab the inferences from the event
    inferences = event.get("inferences")
    inferences = json.loads(inferences)

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = [inference for inference in inferences if inference > THRESHOLD]

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if not meets_threshold:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return {"statusCode": 200, "body": json.dumps(event)}
