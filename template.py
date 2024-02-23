import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = 'InvestmentProject'

list_of_files = [
f'src/{project_name}/__init__.py',
f'src/{project_name}/components/__init__.py',
f'src/{project_name}/components/data_ingestion.py',
f'src/{project_name}/components/data_transformation.py',
f'src/{project_name}/components/model_training.py',
f'src/{project_name}/components/model_monitoring.py',

f'src/{project_name}/pipeline/__init__.py',
f'src/{project_name}/pipeline/training_pipeline.py',
f'src/{project_name}/pipeline/prediction_pipeline.py',

f'src/{project_name}/utils.py',
f'src/{project_name}/exception.py',
f'src/{project_name}/logging.py',

'app.py',
'DockerFile',
'requirements.txt',
'setup.py'

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
    logging.info(f'file directory created: {filedir} and file name created: {filename}')

    if (not os.path.exists(filepath) or os.path.getsize(filepath ) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'empty file has created {filepath}')

    else:
        logging.info(f'{filename} aready exists')          

