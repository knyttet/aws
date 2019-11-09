import boto3
import jsbeautifier


def create_api_key(client, name):
    create_key = client.create_api_key(name=name)
    return create_key


def create_usage_plan(client, name):
    create_usage_plan = client.create_usage_plan(name=name)
    return create_usage_plan


def create_api(client, name):
    create_api = client.create_rest_api(name=name)
    return create_api
    

def list_api_keys(client):
    keys = [x['id'] for x in client.get_api_keys()['items']]
    return keys


def list_apis(client):
    list_apis = client.get_rest_apis()
    return list_apis


def delete_usage_plans(client):
    responses = []
    for plan in client.get_usage_plans()['items']:
        response = client.delete_usage_plan(usagePlanId=plan['id'])
        responses.append(response)
    return responses


def delete_api_keys(client):
    responses = []
    for key in list_api_keys(client):
        response = client.delete_api_key(apiKey=key)
        responses.append(response)
    return responses


api = boto3.client('apigateway')
print(jsbeautifier.beautify(str(list_apis(api))))
