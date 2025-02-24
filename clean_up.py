import json
import os

def strip_execution_count(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    for cell in notebook.get('cells', []):
        if 'execution_count' in cell:
            cell['execution_count'] = None
        for output in cell.get('outputs', []):
            if 'execution_count' in output:
                output['execution_count'] = None

    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

def strip_execution_counts_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.ipynb'):
                strip_execution_count(os.path.join(root, file))

if __name__ == "__main__":
    directory = 'Exercises'
    strip_execution_counts_in_directory(directory)