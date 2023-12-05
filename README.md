# image_wrangling

Description: This script renames and watermarks images based on information from a CSV file.
             It requires the pandas and Pillow libraries.

Usage:
- To rename files based on a CSV file, use:
  python3 renamer.py -f <path_to_csv_file> -i <column_for_input_IDs> -r <column_for_renaming>

- To watermark images, use:
  python3 renamer.py -f <path_to_csv_file> -i <column_for_input_IDs> -w <column_names_for_watermark>

- To rename and watermark images, combine the flags as needed.
