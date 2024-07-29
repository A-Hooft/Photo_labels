from blabel import LabelWriter
import yaml
import os

STYLESHEETS = {
    'xsmall': "CSS_template/A4_label_style_xsmall.css",
    'small': "CSS_template/A4_label_style_small.css",
    'medium': "CSS_template/A4_label_style_medium.css",
    'large': "CSS_template/A4_label_style_large.css",
    'custom': "CSS_template/A4_label_style_custom.css"
}

# Function to load configuration from a YAML file
def load_config(config_path=os.path.join("Config", "write_labels.yaml")):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Load the configuration
config = load_config()

# Check if all required keys are present in the config
required_keys = ['label_size', 'qr_code', 'scale_bar', 'project_name', 'sequential_labels', 'Prefix', 'Suffix', 'Range', 'filename']
for key in required_keys:
    if key not in config:
        raise KeyError(f"Missing required config key: {key}")

# Access configuration parameters
label_size = config['label_size']
qr_code = config['qr_code']
scale_bar = config['scale_bar']
project_name = config['project_name']
sequential_labels = config['sequential_labels']
Prefix = config['Prefix']
Suffix = config['Suffix']
filename = config['filename']
range_str = config['Range']
rangestart, rangeend = map(int, range_str.split('-'))

# Select the stylesheet based on label size
stylesheet = STYLESHEETS.get(label_size, "CSS&template/A4_label_style_custom.css")

# Initialize the LabelWriter with the template and selected stylesheet
label_writer = LabelWriter(
    "CSS_template/A4_item_template.html", items_per_page=1, default_stylesheets=(stylesheet,)
)

# Define the output directory and ensure it exists
output_dir = "label_sheets/"
os.makedirs(output_dir, exist_ok=True)

# Generate sample IDs based on the specified range, prefix, and suffix
if sequential_labels:
    sample_ids = [f"{Prefix}{str(i)}{Suffix}" for i in range(rangestart, rangeend + 1)]
else:
    sample_ids = config['Labels_list']

# Prepare the records for label writing
records = []
for sample_id in sample_ids:
    record = {
        'sample_id': sample_id,
        'project_label': project_name,
        'sample': sample_id,
        'qr_code': qr_code,
        'scale_bar': scale_bar,
        'label_size': label_size
    }
    if qr_code:
        record['QRValue'] = f"{sample_id};{project_name}"
    records.append(record)

# Write labels to the specified file
label_writer.write_labels(records, target=os.path.join(output_dir, f"{filename}.pdf"))
