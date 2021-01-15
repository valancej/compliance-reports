#!/usr/bin/env python3

import json
import uuid
import time
import sys

input_dir = sys.argv[1]

stages = ['source', 'build', 'registry', 'deploy', 'k8s']

ds = {
    'report_id': str(uuid.uuid4()),
    'timestamp': time.time(),
    'origin_stage': 'source',
    'compliance_type': 'CIS',
    'compliance_standards': {
        "docker": "Docker 1.2",
        "kubernetes": "EKS 1.0.0"
    }, 
    'pipeline_ids': {},
    'results': {}
}

with open("{}/stage_artifacts.json".format(input_dir), 'r') as FH:
    ds['pipeline_ids'] = json.loads(FH.read())

for stage in stages:
    with open("{}/{}.json".format(input_dir, stage), 'r') as FH:
        ds['results'][stage] = json.loads(FH.read())
    
print (json.dumps(ds, indent=4))
        

