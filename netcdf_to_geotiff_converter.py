import glob
import os
from netCDF4 import Dataset
import ntpath

# This script converts all NetCDF files in the input directory to GeoTIFF files in the output directory
# Make sure to install the netCDF4 and gdal libraries before running this script
# You can install the libraries using the following commands:
# pip install netCDF4
# pip install gdal or conda install gdal (if you are using Anaconda - Preferred) OR use OSGeo4W Terminal (Easiest)

# Specify the directory containing the NetCDF files
input_directory = os.getcwd() + '/input/'

# Specify the output directory for the GeoTIFF files
output_directory = os.getcwd() + '/output/'

# Get a list of all NetCDF files in the directory
nc_files = glob.glob(input_directory + "*.nc")

# Iterate over each NetCDF file
for nc_file_path in nc_files:

    # Open the NetCDF file
    nc = Dataset(nc_file_path, 'r')

    # Get a list of variables in the NetCDF file
    variables = nc.variables.keys()

    # Print the file name and variables
    print(f"NetCDF file: {nc_file_path}")
    print(f"Variables: {variables}")

    # Iterate over each variable in the NetCDF file
    for variable in variables:
        # Get the variable object
        var_obj = nc.variables[variable]

        # Get the variable name
        var_name = var_obj.name

        # Get output file path
        var_out_name = var_name.replace(' ', '_')
        out_file_path = output_directory + ntpath.basename(nc_file_path).replace('.nc', f'_{var_out_name}.tif')

        # Execute the shell script with the nc_file and variable name as arguments
        os.system(f"sh converter.sh {nc_file_path} {var_name} {out_file_path}")

        print(f"Converted : {ntpath.basename(out_file_path)} to GeoTIFF")

    # Close the NetCDF file
    nc.close()
