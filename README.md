# NetCDF to GeoTIFF Converter

This repository contains scripts to convert NetCDF variables to GeoTIFF files. It includes a Python script (`netcdf_to_geotiff_converter.py`) to automate the conversion process for all NetCDF files in a specified directory and a shell script (`converter.sh`) to handle the actual conversion using `gdal_translate`.

## Requirements

Make sure to install the following libraries before running the scripts:

- [netCDF4](https://pypi.org/project/netCDF4/)
- [GDAL](https://pypi.org/project/GDAL/)

You can install these libraries using `pip` or `conda`:

```sh
pip install netCDF4
pip install gdal
```

Or, if you are using Anaconda (preferred):

```sh
conda install gdal
```

Alternatively, you can use the OSGeo4W Terminal (easiest).

## Scripts

### `netcdf_to_geotiff_converter.py`

This script converts all NetCDF files in the input directory to GeoTIFF files in the output directory.

#### Usage
1. Specify the directory containing the NetCDF files by setting the input_directory variable.
2. Specify the output directory for the GeoTIFF files by setting the output_directory variable.
3. Run the script:

```sh
python netcdf_to_geotiff_converter.py
```

### `converter.sh`

This script converts a NetCDF file to a GeoTIFF file using the `gdal_translate` command. It takes three arguments: 
the input NetCDF file, the variable name to extract, and the output GeoTIFF file.

#### Usage
Make sure the script is executable:

```sh
chmod +x converter.sh
```

## Directory Structure

Ensure your directory structure looks like this:

```lua
project_root/
│
├── input/
│   ├── your_netcdf_file1.nc
│   ├── your_netcdf_file2.nc
│   └── ...
│
├── output/
│   └── (GeoTIFF files will be saved here)
│
├── netcdf_to_geotiff_converter.py
└── converter.sh
```

## Attribution
This project utilizes the following libraries and resources:

- [netCDF4](https://pypi.org/project/netCDF4/) for reading NetCDF files.
- [GDAL](https://gdal.org/) for converting NetCDF files to GeoTIFF files.

If you use this code in your project, please give credit by linking back to this repository and mentioning the original author [Steve Firsake](https://github.com/SteveFirsake).


## Notes
-Make sure that the `converter.sh` script is executable by running `chmod +x converter.sh`.
-Adjust the `input_directory` and `output_directory` variables in the `netcdf_to_geotiff_converter.py` script as needed.
-Ensure that GDAL is properly installed and accessible from your command line.

Happy converting!