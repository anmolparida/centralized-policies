import json
import sys

import centralized_policy

if __name__ == "__main__":

    with open("config.json", "r") as f:
        config = json.load(f)
        api_gateway_url = config['api_gateway_url']
        api_access_token = config['api_access_token']

        if all(v is None for v in (api_gateway_url, api_access_token)):
            sys.exit(f"Exiting code, please update the config.json. Values can not be null.")

    print(">>> Report Generation Started <<<")


    # create a policy with rule - QDS Score
    centralized_policy.delete_policy(api_gateway_url, api_access_token, policy_name="mufg")
    centralized_policy.create_policy(api_gateway_url, api_access_token)
    centralized_policy.update_policy(api_gateway_url, api_access_token, policy_name="mufg", active=False)

    print(">>> Report Generation Completed <<<")
