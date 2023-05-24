import os

run_number = os.getenv('GITHUB_RUN_NUMBER')
run_id = os.getenv('GITHUB_RUN_ID')
run_attempt = os.getenv('GITHUB_RUN_ATTEMPT')

workflow_info = f"{run_number}-{run_id}-{run_attempt}"
print(workflow_info)
