## Function 2 IdentitySerializer

import json
import base64
import boto3

# import sagemaker
# from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT ="image-classification-2022-12-29-17-50-45-782" ## TODO: fill in
runtime= boto3.client('runtime.sagemaker')


def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["body"]["image_data"]) ## TODO: fill in)

    # # Instantiate a Predictor
    # predictor = sagemaker.predictor.Predictor(endpoint,
    # sagemaker_session=sagemaker.Session(),
    # )## TODO: fill in
    

    # # For this model the IdentitySerializer needs to be "image/png"
    # predictor.serializer = IdentitySerializer("image/png")
    
    # # Make a prediction:
    # inferences = predictor.predict(image, initial_args={'ContentType': 'application/x-image'})## TODO: fill in
    
    # Instantiate a Predictor
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType='application/x-image', Body=image)
    inferences = response['Body'].read().decode('utf-8')
    
    # We return the data back to the Step Function    
    event["body"]["inferences"] = [float(x) for x in inferences[1:-1].split(',')]
    return {
        'statusCode': 200,
        'body': {
            "image_data": event['body']['image_data'],
            "s3_bucket": event['body']['s3_bucket'],
            "s3_key": event['body']['s3_key'],
            "inferences": event['body']['inferences'],
            }
    }