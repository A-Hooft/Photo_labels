from blabel import LabelWriter
import yaml
import os

# Initialize the LabelWriter with the template and stylesheets
label_writer = LabelWriter(
    "A4_item_template.html", items_per_page=1, default_stylesheets=("A4_label_style.css",)
)

# Function to load configuration from a YAML file
def load_config(config_path='config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Load the configuration
config = load_config()

# Check if all required keys are present in the config
required_keys = ['label_size', 'qr_code', 'scale_bar', 'Project_name', 'sequential_labels', 'Prefix', 'Suffix', 'Range', 'filename']
for key in required_keys:
    if key not in config:
        raise KeyError(f"Missing required config key: {key}")

# Access configuration parameters
label_size = config['label_size']
qr_code = config['qr_code']
scale_bar = config['scale_bar']
project_name = config['Project_name']
sequential_labels = config['sequential_labels']
prefix = config['Prefix']
suffix = config['Suffix']
range_end = config['Range']
filename = config['filename']

# Define the output directory and ensure it exists
output_dir = "label_sheets/"
os.makedirs(output_dir, exist_ok=True)

# Generate sample IDs based on the specified range, prefix, and suffix
sample_ids = [f"{prefix}{i}{suffix}" for i in range(range_end)]

# Prepare the records for label writing
records = []
for sample_id in sample_ids:
    record = {
        'sample_id': sample_id,
        'project_label': project_name,
        'sample': sample_id
    }
    if qr_code:
        record['QRValue'] = f"{sample_id};{project_name}"
    records.append(record)

# Write labels to the specified file
label_writer.write_labels(records, target=os.path.join(output_dir, f"{filename}.pdf"))
