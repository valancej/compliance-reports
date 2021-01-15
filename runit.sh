#!/bin/bash

set -e

./stage_artifacts_generate.py ./stage_outputs > ./stage_outputs/stage_artifacts.json
./final_report_generate.py ./stage_outputs > final_report.json
./final_report_render.py final_report.json
