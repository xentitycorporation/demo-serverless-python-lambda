import app
import argparse
import json

parser = argparse.ArgumentParser(description='Test Lambda locally')
parser.add_argument('--event', metavar="file", type=str, required=True, help='Event JSON file. ie. events/test01.json')
args = parser.parse_args()

data = json.load(open(args.event))

app.handler(data, {})
