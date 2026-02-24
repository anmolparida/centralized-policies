create_policy_request_body_mufg = {
    "policyName": "mufg-anparida",
    "description": "",
    "centralizedPolicyRules": [
        {
            "name": "Limit Vulnerability using CVSS",
            "type": "IMAGESCAN_VULN_CVSSV3_SEVERITYCOUNT",
            "isEnabled": True,
            "stopProcessing": False,
            "order": 0,
            "kind": "IMAGE_SECURITY",
            "metaData": {
                "value": "CRITICAL",
                "operator": "GREATER_THAN",
                "threshold": 1
            },
            "action": "FAIL"
        },
        {
            "name": "Limit Vulnerability using Severity",
            "type": "IMAGESCAN_VULN_SEVERITYCOUNT",
            "isEnabled": True,
            "stopProcessing": False,
            "order": 0,
            "kind": "IMAGE_SECURITY",
            "metaData": {
                "operator": "GREATER_THAN",
                "severityLevel": 1,
                "threshold": 1
            },
            "action": "FAIL"
        }
    ],
    "exclusionPolicyRules": [],
    "policyMode": "ACTIVE",
    "policyType": "K8S_ADMISSION_CONTROLLER",
    "isDefault": False,
    "tagIds": [],
    "k8sFilters": [
        {
            "cluster": None,
            "namespace": {
                "_update_this_section": "to be updated",
                "clusterUid": "8b0d0561-993a-45a7-a511-cad5651e7502",
                "namespaceValue": "nginx-trurisk-app"
            }
        }
    ]
}

create_policy_request_body_default = {
    "policyName": "string",
    "description": "string",
    "policyType": "CICD / K8S_ADMISSION_CONTROLLER",
    "centralizedPolicyRules": [
        {
            "name": "string",
            "isEnabled": False,
            "type": "IMAGESCAN_VULN_SEVERITYCOUNT",
            "kind": "IMAGE_SECURITY",
            "metaData": {
                "operator": "GREATER_THAN / GREATER_THAN_OR_EQUAL",
                "threshold": 5,
                "severityLevel": 5
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "IMAGESCAN_VULN_CVSSV3_SEVERITYCOUNT",
            "kind": "IMAGE_SECURITY",
            "metaData": {
                "operator": "GREATER_THAN / GREATER_THAN_OR_EQUAL",
                "threshold": 5,
                "value": "LOW /MEDIUM/ HIGH/ CRITICAL"
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "IMAGESCAN_VULN_SECRETS_SEVERITYCOUNT",
            "kind": "IMAGE_SECURITY",
            "metaData": {
                "operator": "GREATER_THAN / GREATER_THAN_OR_EQUAL",
                "threshold": 5,
                "value": "LOW /MEDIUM/ HIGH/ CRITICAL"
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "IMAGESCAN_VULN_RESTRICTED_CVES",
            "kind": "IMAGE_SECURITY",
            "metaData": {
                "values": [
                    "CVE-2014-34521",
                    "CVE-2023-45673"
                ]
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "IMAGESCAN_VULN_RESTRICTED_QIDS",
            "kind": "IMAGE_SECURITY",
            "metaData": {
                "values": [
                    34521,
                    45638
                ]
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "IMAGESCAN_VULN_QDS_SEVERITY",
            "kind": "IMAGE_SECURITY",
            "metaData": {
                "value": "LOW / HIGH / MEDIUM / CRITICAL"
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "IMAGESCAN_VULN_RESTRICTED_SOFTWARES",
            "kind": "IMAGE_SECURITY",
            "metaData": {
                "values": [
                    "openjdk8-jre"
                ]
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "IMAGESCAN_VULN_RESTRICTED_IMAGES",
            "kind": "IMAGE_SECURITY",
            "metaData": {
                "values": [
                    ".*/amazon-ecs-pause."
                ]
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "IMAGESCAN_VULN_RESTRICTED_OLDER_IMAGES",
            "kind": "IMAGE_SECURITY",
            "metaData": {
                "value": 45
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "IMAGESCAN_VULN_RESTRICTED_MALWARE_IMAGES",
            "kind": "IMAGE_SECURITY",
            "metaData": {}
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "PODSECURITY",
            "kind": "POD_SECURITY",
            "metaData": {
                "options": [
                    {
                        "id": "rw_hostpath",
                        "enabled": True
                    },
                    {
                        "id": "container_hostport",
                        "enabled": True
                    },
                    {
                        "id": "hostPid_hostIpc",
                        "enabled": True
                    },
                    {
                        "id": "host_process",
                        "enabled": True
                    },
                    {
                        "id": "privileged_containers",
                        "enabled": True
                    },
                    {
                        "id": "non_default_procMount",
                        "enabled": True
                    },
                    {
                        "id": "insecure_capabilites",
                        "enabled": True
                    },
                    {
                        "id": "root_container",
                        "enabled": True
                    },
                    {
                        "id": "privilege_escalation",
                        "enabled": True
                    }
                ]
            }
        }
    ],
    "exclusionPolicyRules": [
        {
            "name": "string",
            "isEnabled": False,
            "type": "EX_IMAGESCAN_VULN_QID_AGE",
            "kind": "EXCLUSION",
            "metaData": {
                "value": 45
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "EX_IMAGESCAN_VULN_PATCH_NOT_AVAILABLE",
            "kind": "EXCLUSION",
            "metaData": {}
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "EX_IMAGESCAN_VULN_QIDS",
            "kind": "EXCLUSION",
            "metaData": {
                "values": [
                    34521,
                    45638
                ]
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "EX_IMAGESCAN_VULN_IMAGES",
            "kind": "EXCLUSION",
            "metaData": {
                "values": [
                    ".*/amazon-ecs-pause.*"
                ]
            }
        },
        {
            "name": "string",
            "isEnabled": False,
            "type": "EX_NAMESPACES",
            "kind": "EXCLUSION",
            "metaData": {
                "values": [
                    "qualys",
                    "default"
                ]
            }
        }
    ],
    "policyMode": "ACTIVE",
    "isDefault": True,
    "tagIds": [
        "ae866788-742f-45c5-a212-f96af173a62c",
        "66ba613f-12b3-430f-8e73-a7b6d8b7a03f",
        "0c4c96ca-df91-4954-adbd-ed55cc0b7a3f"
    ],
    "k8sFilters": [
        {
            "cluster": {
                "clusterUid": "string",
                "clusterName": "string"
            },
            "namespace": {
                "namespaceUuid": "string",
                "namespaceValue": "string",
                "clusterUid": "string"
            }
        }
    ]
}
