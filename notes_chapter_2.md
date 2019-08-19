# Cleaning Data

## Overview
- Variables can be quantitative or categorical.
- Usually, quantitative are expressed in numbers with a scale or measure of some kind
- Categorical could be yes/no or blue/green/red.

- "Kay's Variable organization" example of a "code book" or "Data dictionary" that defines variables and their measures.
| Variable Name | Measure |
| ---- | ---|
| Mass | 10^24 kg|
| Diameter | km |
| Period | days | 

## Organize Data in Spreadsheets
- We need to organize and clean data before using it
- Broman and Woo in "Data Organization in Spreadhseets" (2017) say:
- Make a single big rectangle
    - rows for subjects/observations
    - columns for variables
- Create a data dictionary (that maps variables to the measurement used for them)
- Leave no empty cells
- Save the data in plain text files
- Always be consistent
    - Case or subject identifiers
    - Variable names
    - Consistent codes for categorical 
    - Use the same codes for missing values
    - Use a consistent format for all dates
    - Data layout in multiple files
    - File names

## Tidy Data
- One observation per row
- Each variable is a column