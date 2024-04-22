import os

commands = [
    not os.system('/bin/bash -c flake8 practice/day2_dvc/src/models'),
    not os.system('pip freeze > requirements.txt'),
    not os.system('git add requirements.txt'),
    not os.system('pip check')
]
print(commands)
if all(commands):
    print("All commands executed successfully.")
else:
    print("Some commands failed. Please check the output.")
