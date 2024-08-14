#
# WINDOWS
#

# Install the required library
# pip3 install docx2pdf

# Import library
from docx2pdf import convert

# Converting documents
convert(input_path='file.docx', output_path='output.pdf')

#
# LINUX
#

# Import libraries
import os
import subprocess

# Convert DOCX to PDF using LibreOffice
subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', 'file.docx', '--outdir', 'tmp'], check=True)

# Rename the converted PDF to the desired output file name
os.rename(src='tmp/file.pdf', dst='output.pdf')