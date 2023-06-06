import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Argument Parsing Example')

# Add arguments
parser.add_argument('--min_instances', type=int, help='minimum number of instances')
parser.add_argument('--max_instances', type=int, help='maximum number of instances')
parser.add_argument('--up_check_interval', type=float, help='interval for checking scaling up')
parser.add_argument('--tasks_in_queue', type=int, help='number of tasks in the queue')
parser.add_argument('--up_next_check_interval', type=float, help='interval for checking scaling up next time')
parser.add_argument('--down_check_interval', type=float, help='interval for checking scaling down')

# Parse the arguments
args = parser.parse_args()

# Access the parsed arguments
min_instances = args.min_instances
max_instances = args.max_instances
up_check_interval = args.up_check_interval
tasks_in_queue = args.tasks_in_queue
up_next_check_interval = args.up_next_check_interval
down_check_interval = args.down_check_interval

# Print the values of the arguments
print('Min instances:', min_instances)
print('Max instances:', max_instances)
print('Up check interval:', up_check_interval)
print('Tasks in queue:', tasks_in_queue)
print('Up next check interval:', up_next_check_interval)
print('Down check interval:', down_check_interval)
