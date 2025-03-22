# FOSSEE LaTeX Report Generator

![FOSSEE Banner](FOSSEE_BANNER.PNG)

## Overview
The **FOSSEE LaTeX Report Generator** is a streamlined solution for automating the creation of well-structured, professionally formatted reports using LaTeX. Developed for the **FOSSEE Summer Fellowship** as a screening task, this tool ensures consistency in document formatting, including tables, sections, and typography enhancements.

## Features
- Automated LaTeX report generation with structured templates  
- Pre-configured document formatting for professional presentation  
- Support for well-formatted tables using `booktabs` and `multirow`  
- Customizable margins with the `geometry` package  
- Error-free LaTeX compilation with dependency management  

## User Workflow
1. **Prepare Input Data**: The user organizes the necessary text and table data in a structured format.
2. **Execute the Script**: Run the Python script (`gui.py`) to process the input data.
3. **Generate LaTeX File**: The script creates a `.tex` file with structured LaTeX code.
4. **Compile LaTeX Document**: The generated `.tex` file is compiled into a `.pdf` using `pdflatex`.
5. **Review and Use the Output**: The final PDF is reviewed and used as needed.

## Installation

### Prerequisites
Ensure that the following dependencies are installed on your system:  
- Python 3.x  
- MiKTeX or TeX Live (for LaTeX compilation)  
- Required LaTeX packages:  
  - `geometry`  
  - `booktabs`  
  - `multirow`  
  - `xcolor`  
  - `colortbl`  

### Setup Instructions
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/FOSSEE-LaTeX-Report-Generator.git
   cd FOSSEE-LaTeX-Report-Generator
   ```
2. Verify the installation of MiKTeX or TeX Live:
   ```bash
   pdflatex --version
   ```
3. Install any missing LaTeX packages using the package manager of your LaTeX distribution.

## How to Run
1. **Modify the `filtered_report.tex` file** as needed.
2. **Run the Python script to compile the LaTeX document:**
   ```bash
   python gui.py
   ```
3. **The compiled PDF will be available in the `output/` directory.**

## Troubleshooting
- If missing package errors occur, update MiKTeX using:
  ```bash
  miktex-console
  ```
  Then navigate to the package manager and install the required dependencies.
- If cross-references or labels appear incorrect, re-run the LaTeX compilation to resolve them.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
Developed as part of the FOSSEE Summer Fellowship as a screening task, this tool aims to simplify and standardize LaTeX-based report generation.

