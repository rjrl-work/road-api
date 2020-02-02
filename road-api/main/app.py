import json
import csv

def read_data(local_authority_id, road_name):
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        answer = []
        for row in reader:
            if row['local_authority_id'] == local_authority_id and \
               row['road_name'] == road_name:
                answer.append(row)
        return answer
    
def lambda_handler(event, context):
    _, local_authority_id, road_name = event['path'].split('/')
    return_data = read_data(local_authority_id, road_name)
    return {
        "statusCode": 200,
        "body": json.dumps(return_data),
    }
