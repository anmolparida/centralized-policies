import requests
from request_body import create_policy_request_body_mufg


def get_all_policies(base_url, access_token,):
    url = f"{base_url}/csapi/v1.3/centralizedPolicy"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers,verify=False)
    all_policies = response.json()
    assert response.status_code == 200, f"Policy retrieval failed with status code {response.status_code}."
    return all_policies


def get_policy_uuid(base_url, access_token, policy_name):
    # find the policy name in the dict
    all_policies = get_all_policies(base_url, access_token)
    policy_uuid = next((policy.get('uuid') for policy in all_policies.get('data', [])
                        if policy.get('policyName') == policy_name), None)
    if policy_uuid:
        print(f"Policy [{policy_name}] found. Policy UUID: {policy_uuid}")
    else:
        print(f"Policy {policy_name} not found.")
    return policy_uuid


def delete_policy(base_url, access_token, policy_name):
    policy_uuid = get_policy_uuid(base_url, access_token, policy_name)
    if policy_uuid:
        url = f"{base_url}/csapi/v1.3/centralizedPolicy/{policy_uuid}"
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.delete(url, headers=headers,verify=False)
        if response.status_code == 200:
            print(f"Policy {policy_name} deleted successfully.")
        else:
            print(f"Policy {policy_name} deletion failed with status code {response.status_code}.")


def create_policy(base_url, access_token):
    # # create_policy_request_body_mufg
    # cluster = "banking-cluster-us2"
    # cluster_uuid = "8b0d0561-993a-45a7-a511-cad5651e7502"
    #
    # # get namespace uuid dynamically
    # namespace = "nginx-trurisk-app"
    # namespace_uuid = "d6a01904-7b8f-4980-9522-f842fe7b542d"

    url = f"{base_url}/csapi/v1.3/centralizedPolicy"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.post(url, headers=headers, json=create_policy_request_body_mufg,verify=False)
    assert response.status_code == 200, f"Policy creation failed with status code {response.status_code}."


def update_policy(base_url, access_token, policy_name, active):
    policy_uuid = get_policy_uuid(base_url, access_token, policy_name)
    url = f"{base_url}/csapi/v1.3/centralizedPolicy/{policy_uuid}/mode"
    headers = {'Authorization': f'Bearer {access_token}'}
    payload = {"policyMode": "ACTIVE" if active else "INACTIVE"}
    response = requests.put(url, headers=headers, json=payload,verify=False)
    assert response.status_code == 200, f"Policy {policy_name} update failed with status code {response.status_code}."
