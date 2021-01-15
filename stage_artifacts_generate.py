#!/usr/bin/env python3

import json
import uuid
import time
import sys

input_dir = sys.argv[1]

stages = ['source', 'build', 'registry', 'deploy', 'k8s']

content = {}

for stage in stages:
    content[stage] = {
        'metadata': []
    }
    with open("{}/{}.json".format(input_dir, stage), 'r') as FH:
        stage_data = json.loads(FH.read())
        if stage == 'source':
            content[stage]['metadata'] = [
                {
                    "type": "source_repository",
                    "name": stage_data['manifest_info']['name']
                },
                {
                    "type": "commit_hash",
                    "name": stage_data.get('git_sha')
                }
            ]
        elif stage == 'build':
            content[stage]['metadata'] = [
                {
                    "type": "container_digest",
                    "name": stage_data['tool_result_data']['source']['target']['digest']
                }
            ]
        elif stage == 'registry':
            content[stage]['metadata'] = [
                {
                    "type": "full_tag",
                    "name": stage_data['manifest_info']['image_name'] + ':' + stage_data['git_sha']
                },
                {
                    "type": "container_digest",
                    "name": list(stage_data['tool_result_data'][0].keys())[0]
                }
            ]    
        elif stage == 'deploy':
            content[stage]['metadata'] = [
                {
                    "type": "container_id",
                    "name": stage_data['tool_result_data']['container']['container_id']
                },
                {
                    "type": "k8s_pod_id",
                    "name": "example-pod-name"
                }
            ]
        elif stage == 'k8s':
            content[stage]['metadata'] = [
                {
                    "type": "k8s_endpoint",
                    "name": "example_k8s.deployment.com"
                }
            ]
        else:
            print("stage not found")

print(json.dumps(content, indent=4))
