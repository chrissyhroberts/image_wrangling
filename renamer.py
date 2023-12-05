#!/usr/bin/env python3
"""
Script Name: renamer.py
Description: This script renames and watermarks images based on information from a CSV file.
             It requires the pandas and Pillow libraries.

Usage:
- To rename files based on a CSV file, use:
  python3 renamer.py -f <path_to_csv_file> -i <column_for_input_IDs> -r <column_for_renaming>

- To watermark images, use:
  python3 renamer.py -f <path_to_csv_file> -i <column_for_input_IDs> -w <column_names_for_watermark>

- To rename and watermark images, combine the flags as needed.

License: MIT License

The script uses the Roboto font under the Apache License, Version 2.0.
Roboto font license: http://www.apache.org/licenses/LICENSE-2.0
"""

import argparse
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

def watermark_image(image_path, output_path, watermark_data, font_size=100, font_color=(255, 255, 255)):
    """
    Add watermark text to an image, with each variable on a new line.
    :param image_path: Path to the input image
    :param output_path: Path to save the watermarked image
    :param watermark_data: Dictionary of variable names and their values
    :param font_size: Size of the watermark font
    :param font_color: Color of the watermark font in RGB
    """
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)

        # Load the Roboto font. Replace 'font/Roboto-Black.ttf' with the correct path if necessary.
        font = ImageFont.truetype('font/Roboto-Black.ttf', font_size)

        # Create the watermark text, each key-value pair on a new line.
        text = "\n".join([f"{key}: {value}" for key, value in watermark_data.items()])

        # Calculate text bounding box and position the text at the top left corner.
        text_bbox = draw.multiline_textbbox((0, 0), text, font=font)
        x, y = 20, 20  # Margin from the top left corner

        draw.multiline_text((x, y), text, font=font, fill=font_color)
        img.save(output_path)

def process_files(csv_file, id_column, rename_column=None, watermark_columns=None):
    """
    Process files based on the CSV file for renaming and watermarking.
    :param csv_file: Path to the CSV file
    :param id_column: Column name for input file IDs
    :param rename_column: Column name for renaming files
    :param watermark_columns: List of column names for watermark text
    """
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        input_file = f"in/{row[id_column]}"
        output_file = f"out/{row[rename_column]}" if rename_column else f"out/{row[id_column]}"

        if watermark_columns:
            watermark_data = {col: row[col] for col in watermark_columns}
            watermark_image(input_file, output_file, watermark_data)
        else:
            with Image.open(input_file) as img:
                img.save(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename and watermark images based on a CSV file.")
    parser.add_argument("-f", "--file", required=True, help="Path to the CSV file")
    parser.add_argument("-i", "--id", required=True, help="Column name for input file IDs")
    parser.add_argument("-r", "--rename", help="Column name for renaming files")
    parser.add_argument("-w", "--watermark", nargs='+', help="Column names for watermark text")

    args = parser.parse_args()

    process_files(args.file, args.id, args.rename, args.watermark)

# MIT License
# Copyright (c) 2023 [Chrissy h Roberts, chrissy.roberts@lshtm.ac.uk]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
