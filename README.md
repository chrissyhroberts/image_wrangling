# Image wrangling

Description: This script renames and watermarks images based on information from a CSV file.
             It requires the pandas and Pillow libraries.

Usage:
- To rename files based on a CSV file, use:
  python3 renamer.py -f <path_to_csv_file> -i <column_for_input_IDs> -r <column_for_renaming>

- To watermark images, use:
  python3 renamer.py -f <path_to_csv_file> -i <column_for_input_IDs> -w <column_names_for_watermark>

- To rename and watermark images, combine the flags as needed.


## Example

Your CSV file `data.csv` probably looks like this

|ID|NEWID|Class|Score|State|Blah|
|--|-----|-----|-----|-----|----|
PXL_20231125_165105778.jpg|0002.jpg|People|1|Overcrowded|Wah
PXL_20231125_170447451.jpg|0003.jpg|People|Level 10000|Awesome|Quack
PXL_20231128_012043067.jpg|0004.jpg|Pets|10|Asleep|Quack
PXL_20231130_091145587.jpg|0006.jpg|Pets|2|Keen|Wah
PXL_20231201_101108180.jpg|0007.jpg|Things|10|Lifebringer|Quack

Your files might be called 

```
in/PXL_20231125_165105778.jpg
in/PXL_20231125_170447451.jpg
in/PXL_20231128_012043067.jpg
in/PXL_20231130_091145587.jpg
in/PXL_20231201_101108180.jpg
```

As you can see, column **ID** has the current filenames, whilst column **NEWID** has the names you want

To change the filenames you would run this command
`python3 renamer.py -f data.csv -i ID -r NEWID`

This has the effect of changing all the filenames to match the NEWID column


```
in/PXL_20231125_165105778.jpg > out/0002.jpg
in/PXL_20231125_170447451.jpg > out/0003.jpg
in/PXL_20231128_012043067.jpg > out/0004.jpg
in/PXL_20231130_091145587.jpg > out/0006.jpg
in/PXL_20231201_101108180.jpg > out/0007.jpg
```
To change the filenames AND add watermarks from columns **Class**, **Score** and **State** you would run this command
`python3 renamer.py -f data.csv -i ID -r NEWID -w Class Score State`

<img src="./out/0003.jpg" width=30% height=30%>
![0003](https://github.com/chrissyhroberts/image_wrangling/assets/31275801/f5b33334-7db2-438d-84d9-9a04d571a89f,width=200)


