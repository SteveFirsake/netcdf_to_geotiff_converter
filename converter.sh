#!/bin/bash

# Make sure to make this script executable with 
# chmod +x converter.sh

# This script converts a NetCDF file to a GeoTIFF file
# using the gdal_translate command
# The script takes three arguments:
# 1. The input NetCDF file
# 2. The variable name to extract
# 3. The output GeoTIFF file

# Check if all three arguments are provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 <input_file> <variable_name> <output_file>"
    exit 1
fi

# Assign the arguments to variables
input_file="$1"
variable_name="$2"
output_file="$3"

# Run gdal_translate command
gdal_translate "NETCDF:\"$input_file\":$variable_name" "$output_file"