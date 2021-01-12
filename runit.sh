#!/bin/bash

set -e

./final_report_generate.py ./stage_outputs > final_report.json
./final_report_render.py final_report.json
