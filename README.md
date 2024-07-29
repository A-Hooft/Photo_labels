# Label Generator

This project is designed to automate the creation of uniform labels for various purposes, and originally designed for producing labels for in photos of biolgoical speciemens. It utilizes the `blabel` library to generate PDF labels based on a given configuration file. labels can be generated based on a sequenctial numerical identifier or list. optionally an automatically rendered QRcode can be included to allow for automatic content classifcation of photos. A scale bar and 4 preset sizes are defined, but all CSS elements and labels contents are in theory customisable


## Installation

To set up the project and install the necessary dependencies, follow these steps:

### 1) Clone the repository:

`git clone git@github.com:A-Hooft/Photo_labels.git`

### 2) Navigate to the project directory:

cd Photo_labels

### 3) Install the required packages using pip:

pip install -r requirements.txt

their may be issues with the weasyprint package, in that case consult weasyprint installation steps https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation


## Configuration File

The configuration file `Config/write_labels.yaml` includes several parameters;

- `label_size`: Size of labels (xsmall/small/medium/large/custom)
- `qr_code`: Enable or disable QR code generation
- `scale_bar`: Enable or disable scale bar
- `Project_name`: Name of the project - included in top right hand corner of label
- `filename`: Name of the output file - 
- `sequential_labels`: Enable or disable sequential label generation
- `Prefix`: Optional prefix for all specimen numbers
- `Suffix`: Optional suffix for all specimen numbers
- `Range`: Specimen number range (used if `sequential_labels` is true)
- `Labels_list`: List of labels (used if `sequential_labels` is false)


## Generate labels

To generate the labels, execute the following command to run the python script:

python write_labels.py

This will read the configuration from write_labels.yaml, generate the labels according to the specified parameters, and save the output as a PDF file.
