#!/usr/bin/python3
import argparse
import datetime
import os
import json
import sys
import yaml
from pathlib import Path

######
# Intended to be used with build_reports.py which generates reports per stage in CI/CD pipeline
# This script aggregates the reports from each stage in CI/CD flow
# generate_reports.py --reports directory-compliance-manifest build-compliance-manifest.json registry-compliance-manifest.json

###### Setup command line parser
def setup_parser():
    parser = argparse.ArgumentParser(description="Tool for aggregate reports")
    parser.add_argument('-d', '--directory', default='artifacts', help='root directory to search for json report files')
    parser.add_argument('-c', '--compliance', default='cis', help='compliance check to evaluate. ex. cis')

    return parser

###### Loads a json input file from a security tool such as Grype or Anchore
def process_input_results_file(input_file):
    # Load results file from tool into dict
    report_input_file_path = input_file

    if os.path.exists(report_input_file_path):
        with open(report_input_file_path, 'r') as stream:
            input_file_dict = json.load(stream)
            return input_file_dict
    else:
        print("Could not find input file")

def create_report(root_directory, compliance_standard):

    current_time = datetime.datetime.now()
    aggregate_report = {}
    aggregate_report["description"] = 'Aggregate compliance report'
    aggregate_report["compliance_standard"] = compliance_standard
    aggregate_report["timestamp"] = current_time.strftime("%c")
    git_sha = os.getenv('GITHUB_SHA')
    aggregate_report["git_sha"] = git_sha
    aggregate_report["git_sha"] = git_sha
    results_list = []
    
    for subdir, dirs, files in os.walk(root_directory):
        for filename in files:
            file_path = os.path.join(subdir, filename)
            if file_path.endswith(".json"):
                input_file = file_path
                results_dict = process_input_results_file(input_file)
                results_list.append(results_dict)

    sorted_results = sorted(results_list, key = lambda k: k['stage_number'])
    aggregate_report["results"] = sorted_results
    
    with open("full-compliance-report.json", "w") as file:
       json.dump(aggregate_report, file)

def main(arg_parser):

    parser = arg_parser
    args = parser.parse_args()
    root_directory = args.directory
    compliance_standard = args.compliance

    # Create report
    create_report(root_directory, compliance_standard)
    
if __name__ == "__main__":
    try:
        arg_parser = setup_parser()
        main(arg_parser)
    except Exception as error:
        print ("\n\nERROR executing script - Exception: {}".format(error))
        sys.exit(1)