Make a directory named venv
mkdir venv

Create a virtual environment in that directory
python3 -m venv venv

Activate virtual environment
source venv/bin/activate

Install pandas
pip install pandas

Install bagpy
pip install bagpy

Open jupyter notebook and run BagToTable.ipynb in the venv. It will generate csv files from the bag data in the /analysis/processed_data directory.




Check the kernel list
jupyter kernelspec list

To reset the kernel
python -m ipykernel install --user --name venv

Remove venv folder
rm -rf venv

Rosbags package
pip install . (instead of the python setup.py install)
