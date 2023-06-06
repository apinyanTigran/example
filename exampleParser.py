import argparse
import json

parser = argparse.ArgumentParser(description='Argument Parsing Example')

# Add arguments
parser.add_argument('--cluster_file', help='path to the JSON file for cluster')
parser.add_argument('--tasks_file', help='path to the JSON file for tasks')
parser.add_argument('--output_file', help='path to the JSON file for output')


args = parser.parse_args()

cluster_file = args.cluster_file
tasks_file = args.tasks_file
output_file = args.output_file

cluster = None
tasks = None
output = None

if cluster_file:
    try:
        with open(cluster_file) as f:
            cluster = json.load(f)
    except FileNotFoundError:
        print(f'Error: JSON file {cluster_file} not found')
    except json.JSONDecodeError:
        print(f'Error: Invalid JSON file {cluster_file}')

if tasks_file:
    try:
        with open(tasks_file) as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print(f'Error: JSON file {tasks_file} not found')
    except json.JSONDecodeError:
        print(f'Error: Invalid JSON file {tasks_file}')

if output_file:
    try:
        with open(output_file) as f:
            output = json.load(f)
    except FileNotFoundError:
        print(f'Error: JSON file {output_file} not found')
    except json.JSONDecodeError:
        print(f'Error: Invalid JSON file {output_file}')


# Print the parsed values
print('Cluster:', cluster)
print('Tasks:', tasks)
print('Output:', output)
