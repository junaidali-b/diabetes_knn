#!/bin/bash

cd ~/Projects/Diabetes_KNN/Data

sqlite3 diabetes.db <<EOF
.mode csv
.import diabetes.csv raw_data
.schema raw_data
EOF
