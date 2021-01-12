#!/usr/bin/env python3

import json
import uuid
import time
import sys

input_dir = sys.argv[1]

stages = ['source', 'build', 'registry', 'k8s', 'deploy']

ds = {
    'report_id': str(uuid.uuid4()),
    'timestamp': time.time(),
    'origin_stage': 'source',
    'compliance_type': 'cis',
    'pipeline_ids': {},
    'results': {}
}

with open("{}/stage_artifacts.json".format(input_dir), 'r') as FH:
    ds['pipeline_ids'] = json.loads(FH.read())

for stage in stages:
    with open("{}/{}.json".format(input_dir, stage), 'r') as FH:
        ds['results'][stage] = json.loads(FH.read())
    
print (json.dumps(ds, indent=4))
        

