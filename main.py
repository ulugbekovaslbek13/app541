import os
import sys

def run_core_pipeline():
    print('[INFO] Executing main microservice processing runtime...')
    env_status = os.getenv('APP_ENV', 'production')
    print(f'[STATUS] Environment profile identified as: {env_status}')

if __name__ == '__main__':
    run_core_pipeline()