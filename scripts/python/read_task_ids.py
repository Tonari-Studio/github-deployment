import json
import os

with open('task_ids.json', 'r') as file:
    data = json.load(file)

task_ids = ','.join(data['task_ids'])
print(f"TASK_IDS={task_ids}")

with open(os.getenv('GITHUB_ENV'), 'a') as env_file:
    env_file.write(f"TASK_IDS={task_ids}\n")
