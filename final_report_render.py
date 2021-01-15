#!/usr/bin/env python3

import json
import sys
from prettytable import PrettyTable, PLAIN_COLUMNS, ALL


def get_compliance_result_grype_cis(data, compliance_sections):
    ret = []

    # this would go through each input compliance section and determine, from the tool output data, if the section was pass/fail.  elements of the return look like this:
    #el = {
    #    "section": "4.1",
    #    "summary": "summary",
    #    "status": "pass"
    #    }
    grype_vuln_matches = data['matches']
    severity_threshold = 'High'
    vuln_status = 'Pass'
    
    for match in grype_vuln_matches:
        if match['vulnerability']['severity'] == severity_threshold:
            vuln_status = 'Fail'

    for compliance_section in compliance_sections:
        section = compliance_section.get('name')
        summary = compliance_section.get('description')

        # here is where each section would be implement a check against the grype output in 'data', for now hardcode pass
        if compliance_section.get('name') == "4.4":
            status = vuln_status                                   
        else:
            status = 'not_performed'
        el = {
            'section': section,
            'summary': summary,
            'status': status
        }
        ret.append(el)
    return(ret)

def get_compliance_result_anchore_enterprise_cis(data, compliance_sections):
    ret = []
    for compliance_section in compliance_sections:
        section = compliance_section.get('name')
        summary = compliance_section.get('description')

        # here is where each section would be implement a check against the grype output in 'data', for now hardcode pass
        if compliance_section.get('name') == "4.1":
            status = 'Pass'
        elif compliance_section.get('name') == "4.2":
            status = 'Pass'
        elif compliance_section.get('name') == "4.3":
            status = 'Pass'
        elif compliance_section.get('name') == "4.4":
            status = 'Pass'
        elif compliance_section.get('name') == "4.5":
            status = 'Pass'
        elif compliance_section.get('name') == "4.6":
            status = 'Pass'
        elif compliance_section.get('name') == "4.7":
            status = 'Pass'
        elif compliance_section.get('name') == "4.8":
            status = 'Pass'
        elif compliance_section.get('name') == "4.9":
            status = 'Pass' 
        elif compliance_section.get('name') == "4.10":
            status = 'Pass' 
        elif compliance_section.get('name') == "5.8":
            status = 'Pass'                                               
        else:
            status = 'not_performed'
        el = {
            'section': section,
            'summary': summary,
            'status': status
        }
        ret.append(el)
    return(ret)

def get_compliance_result_kube_bench_cis(data, compliance_sections):
    ret = []
    kube_bench_section_3_tests = data[0]['tests']
    section_3_1 = next((item for item in kube_bench_section_3_tests if item["section"] == "3.1"), False)
    section_3_2 = next((item for item in kube_bench_section_3_tests if item["section"] == "3.2"), False)
    if section_3_1.get("fail") == False:
        section_3_1_status = 'Pass'

    if section_3_2.get("fail") == False:
        section_3_2_status = 'Pass'
    
    for compliance_section in compliance_sections:
        section = compliance_section.get('name')
        summary = compliance_section.get('description')

        # here is where each section would be implement a check against the grype output in 'data', for now hardcode pass
        if compliance_section.get('name') == "1":
            status = "Skipped. EKS Control Plane access required"
        elif compliance_section.get('name') == "2":
            status = "Skipped. EKS Control Plane access required"
        elif compliance_section.get('name') == "3.1.1":
            status = section_3_1_status
        elif compliance_section.get('name') == "3.1.2":
            status = section_3_1_status
        elif compliance_section.get('name') == "3.1.3":
            status = section_3_1_status
        elif compliance_section.get('name') == "3.1.4":
            status = section_3_1_status
        elif compliance_section.get('name') == "3.2.1":
            status = section_3_2_status
        elif compliance_section.get('name') == "3.2.2":
            status = section_3_2_status
        elif compliance_section.get('name') == "3.2.3":
            status = section_3_2_status
        elif compliance_section.get('name') == "3.2.4":
            status = section_3_2_status
        elif compliance_section.get('name') == "3.2.5":
            status = section_3_2_status
        elif compliance_section.get('name') == "3.2.6":
            status = section_3_2_status
        elif compliance_section.get('name') == "3.2.7":
            status = section_3_2_status
        elif compliance_section.get('name') == "3.2.8":
            status = section_3_2_status
        elif compliance_section.get('name') == "3.2.9":
            status = section_3_2_status
        elif compliance_section.get('name') == "3.2.10":
            status = section_3_2_status
        elif compliance_section.get('name') == "3.2.11":
            status = section_3_2_status                                
        else:
            status = 'not_performed'
        el = {
            'section': section,
            'summary': summary,
            'status': status
        }
        ret.append(el)
    return(ret)

def get_compliance_result_anchore_cis_bench(data, compliance_sections):
    ret = []
    
    for compliance_section in compliance_sections:
        section = compliance_section.get('name')
        summary = compliance_section.get('description')

        # here is where each section would be implement a check against the grype output in 'data', for now hardcode pass
        if compliance_section.get('name') == "1.1.1-1.2.12":
            status = "Skipped. Host access required"
        elif compliance_section.get('name') == '2.1':
            status = data['cis_daemon_checks']['2.1'].get('status')
        elif compliance_section.get('name') == '2.2':
            status = data['cis_daemon_checks']['2.2'].get('status')
        elif compliance_section.get('name') == '2.3':
            status = data['cis_daemon_checks']['2.3'].get('status')
        elif compliance_section.get('name') == '2.4':
            status = data['cis_daemon_checks']['2.4'].get('status')
        elif compliance_section.get('name') == '2.5':
            status = data['cis_daemon_checks']['2.5'].get('status')
        elif compliance_section.get('name') == '2.6':
            status = data['cis_daemon_checks']['2.6'].get('status')
        elif compliance_section.get('name') == '2.7':
            status = data['cis_daemon_checks']['2.7'].get('status')
        elif compliance_section.get('name') == '2.8':
            status = data['cis_daemon_checks']['2.8'].get('status')
        elif compliance_section.get('name') == '2.9':
            status = data['cis_daemon_checks']['2.9'].get('status')
        elif compliance_section.get('name') == '2.10':
            status = data['cis_daemon_checks']['2.10'].get('status')
        elif compliance_section.get('name') == '2.11':
            status = data['cis_daemon_checks']['2.11'].get('status')
        elif compliance_section.get('name') == '2.12':
            status = data['cis_daemon_checks']['2.12'].get('status')
        elif compliance_section.get('name') == '2.13':
            status = data['cis_daemon_checks']['2.13'].get('status')
        elif compliance_section.get('name') == '2.14':
            status = data['cis_daemon_checks']['2.14'].get('status')
        elif compliance_section.get('name') == '2.15':
            status = data['cis_daemon_checks']['2.15'].get('status')
        elif compliance_section.get('name') == '2.16':
            status = data['cis_daemon_checks']['2.16'].get('status')
        elif compliance_section.get('name') == '2.17':
            status = data['cis_daemon_checks']['2.17'].get('status')
        elif compliance_section.get('name') == "3.1-3.22":
            status = "Skipped. Host access required"
        elif compliance_section.get('name') == "5.1":
            status = data['container']['cis_runtime_checks']['5.1'].get('status')
        elif compliance_section.get('name') == "5.2":
            status = data['container']['cis_runtime_checks']['5.2'].get('status')
        elif compliance_section.get('name') == "5.3":
            status = data['container']['cis_runtime_checks']['5.3'].get('status')
        elif compliance_section.get('name') == "5.4":
            status = data['container']['cis_runtime_checks']['5.4'].get('status')
        elif compliance_section.get('name') == "5.5":
            status = data['container']['cis_runtime_checks']['5.5'].get('status')
        elif compliance_section.get('name') == "5.6":
            status = data['container']['cis_runtime_checks']['5.6'].get('status')
        elif compliance_section.get('name') == "5.7":
            status = data['container']['cis_runtime_checks']['5.7'].get('status')
        elif compliance_section.get('name') == "5.8":
            status = data['container']['cis_runtime_checks']['5.8'].get('status')
        elif compliance_section.get('name') == "5.9":
            status = data['container']['cis_runtime_checks']['5.9'].get('status')
        elif compliance_section.get('name') == "5.10":
            status = data['container']['cis_runtime_checks']['5.10'].get('status')
        elif compliance_section.get('name') == "5.11":
            status = data['container']['cis_runtime_checks']['5.11'].get('status')
        elif compliance_section.get('name') == "5.12":
            status = data['container']['cis_runtime_checks']['5.12'].get('status')
        elif compliance_section.get('name') == "5.13":
            status = data['container']['cis_runtime_checks']['5.13'].get('status')
        elif compliance_section.get('name') == "5.14":
            status = data['container']['cis_runtime_checks']['5.14'].get('status')
        elif compliance_section.get('name') == "5.15":
            status = data['container']['cis_runtime_checks']['5.15'].get('status')
        elif compliance_section.get('name') == "5.16":
            status = data['container']['cis_runtime_checks']['5.16'].get('status')
        elif compliance_section.get('name') == "5.17":
            status = data['container']['cis_runtime_checks']['5.17'].get('status')
        elif compliance_section.get('name') == "5.18":
            status = data['container']['cis_runtime_checks']['5.18'].get('status')
        elif compliance_section.get('name') == "5.19":
            status = data['container']['cis_runtime_checks']['5.19'].get('status')
        elif compliance_section.get('name') == "5.20":
            status = data['container']['cis_runtime_checks']['5.20'].get('status')
        elif compliance_section.get('name') == "5.21":
            status = data['container']['cis_runtime_checks']['5.21'].get('status')
        elif compliance_section.get('name') == "5.22":
            status = data['container']['cis_runtime_checks']['5.22'].get('status')
        elif compliance_section.get('name') == "5.23":
            status = data['container']['cis_runtime_checks']['5.23'].get('status')
        elif compliance_section.get('name') == "5.24":
            status = data['container']['cis_runtime_checks']['5.24'].get('status')
        elif compliance_section.get('name') == "5.25":
            status = data['container']['cis_runtime_checks']['5.25'].get('status') 
        elif compliance_section.get('name') == "5.26":
            status = data['container']['cis_runtime_checks']['5.26'].get('status')
        elif compliance_section.get('name') == "5.27":
            status = data['container']['cis_runtime_checks']['5.27'].get('status')
        elif compliance_section.get('name') == "5.28":
            status = data['container']['cis_runtime_checks']['5.28'].get('status')
        elif compliance_section.get('name') == "5.29":
            status = data['container']['cis_runtime_checks']['5.29'].get('status')
        elif compliance_section.get('name') == "5.30":
            status = data['container']['cis_runtime_checks']['5.30'].get('status')
        elif compliance_section.get('name') == "5.31":
            status = data['container']['cis_runtime_checks']['5.31'].get('status')
        elif compliance_section.get('name') == "6.1":
            status = "Skipped"
        elif compliance_section.get('name') == "6.2":
            status = "Skipped"                     
        else:
            status = 'not_performed'
        el = {
            'section': section,
            'summary': summary,
            'status': status
        }
        ret.append(el)
    return(ret)

def plain_column_table(header, align='l'):
    table = PrettyTable(header)
    #table.set_style(PLAIN_COLUMNS)
    table.align = align
    return table

result_file = sys.argv[1]

with open(result_file, 'r') as FH:
    result = json.loads(FH.read())

report_timestamp = result.get('timestamp')
report_id = result.get('report_id')
report_origin_stage = result.get('origin_stage')
report_final_status = 'pass'
report_compliance_type = result.get('compliance_type')
report_compliance_standards = result.get('compliance_standards')
registry_image = result.get('pipeline_ids').get('registry').get('metadata')[0].get('name')
registry_sha = result.get('pipeline_ids').get('registry').get('metadata')[1].get('name')
stages_passed = []
stages_failed = []
    
header = ['Stage', 'Type', 'ID']
t = plain_column_table(header)
for stage in result.get('pipeline_ids').keys():
    
    for id_record in result.get('pipeline_ids', {}).get(stage, {}).get('metadata', []):
        row = [stage, id_record.get('type'), id_record.get('name')]
        t.add_row(row)
        
artifact_table = t.get_string()

if report_compliance_type:
    standard = report_compliance_type + " Standard"
else:
    standard = "Standard"

header = ['Stage', standard, 'Section', 'Detail', 'Status']
t = plain_column_table(header)

total_stages_passed = 0
total_stages_failed = 0
total_stages_skipped = 0

for stage in result.get('results').keys():
   
    stage_passed = True
    tool_info = result.get('results').get(stage).get('tool')
    compliance_info = result.get('results').get(stage).get('compliance')
    tool_output = result.get('results').get(stage).get('tool_result_data')


    if tool_info and compliance_info and tool_output:
        if tool_info.get('name') == 'anchore-grype':
            if compliance_info.get('name') == 'cis':
                standard = report_compliance_standards.get('docker')
                cis_eval_results = get_compliance_result_grype_cis(tool_output, compliance_info.get('sections'))
                for cis_eval_result in cis_eval_results:
                    row = [stage, standard, cis_eval_result.get('section'), cis_eval_result.get('summary'), cis_eval_result.get('status')]
                    t.add_row(row)
                    if cis_eval_result.get('status') == 'Fail':
                        total_stages_failed += 1
                        stage_passed = False
                    elif cis_eval_result.get('status') == 'Pass':
                        total_stages_passed += 1
                    else:
                        total_stages_skipped += 1
        
        elif tool_info.get('name') == 'anchore-enterprise':
            if compliance_info.get('name') == 'cis':
                standard = report_compliance_standards.get('docker')
                cis_eval_results = get_compliance_result_anchore_enterprise_cis(tool_output, compliance_info.get('sections'))
                for cis_eval_result in cis_eval_results:
                    row = [stage, standard, cis_eval_result.get('section'), cis_eval_result.get('summary'), cis_eval_result.get('status')]
                    t.add_row(row)
                    if cis_eval_result.get('status') == 'Fail':
                        total_stages_failed += 1
                        stage_passed = False
                    elif cis_eval_result.get('status') == 'Pass':
                        total_stages_passed += 1
                    else:
                        total_stages_skipped += 1
        
        elif tool_info.get('name') == 'kube-bench':
            if compliance_info.get('name') == 'cis':
                standard = report_compliance_standards.get('kubernetes')
                cis_eval_results = get_compliance_result_kube_bench_cis(tool_output, compliance_info.get('sections'))
                for cis_eval_result in cis_eval_results:
                    row = [stage, standard, cis_eval_result.get('section'), cis_eval_result.get('summary'), cis_eval_result.get('status')]
                    t.add_row(row)
                    if cis_eval_result.get('status') == 'Fail':
                        total_stages_failed += 1
                        stage_passed = False
                    elif cis_eval_result.get('status') == 'Pass':
                        total_stages_passed += 1
                    else:
                        total_stages_skipped += 1
        
        elif tool_info.get('name') == 'anchore-cis-bench':
            if compliance_info.get('name') == 'cis':
                standard = report_compliance_standards.get('docker')
                cis_eval_results = get_compliance_result_anchore_cis_bench(tool_output, compliance_info.get('sections'))
                for cis_eval_result in cis_eval_results:
                    row = [stage, standard, cis_eval_result.get('section'), cis_eval_result.get('summary'), cis_eval_result.get('status')]
                    t.add_row(row)
                    if cis_eval_result.get('status') == 'Fail':
                        total_stages_failed += 1
                        stage_passed = False
                    elif cis_eval_result.get('status') == 'Pass':
                        total_stages_passed += 1
                    else:
                        total_stages_skipped += 1
        
    else:
        row = [stage, 'N/A', 'N/A', 'N/A', 'N/A']
    #t.add_row(row)
    # set up some global results along the way
    if stage_passed:
        stages_passed.append(stage)
    else:
        stages_failed.append(stage)
        # if any one stage fails, global status is fail
        report_final_status = 'fail'

            
result_table = t.get_string()
#print("results", result_table)


print("Compliance Report\n---------------\n")
print("Time: {}".format(report_timestamp))
print("Report ID: {}".format(report_id))
print("Origin Stage: {}".format(report_origin_stage))
print("Status: {}".format(report_final_status))
print("Compliance Type: {}".format(report_compliance_type))
print("Compliance Standards: {}".format(report_compliance_standards))
print("Stages Passed: {}".format(stages_passed))
print("Stages Failed: {}".format(stages_failed))

print("\nArtifacts\n----------------\n")
print(artifact_table)

print("\nResults\n----------------\n")
print(result_table)
print("\nTotals\n----------------\n")
print("Stages failed: {}".format(total_stages_failed))
print("Stages passed: {}".format(total_stages_passed))
print("Stages skipped: {}".format(total_stages_skipped))
