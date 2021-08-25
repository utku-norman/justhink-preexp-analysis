### Installation

Activate the virtual environment of [justhink_world]
```
source venv/bin/activate
```

Install the dependencies.
```
pip install ipykernel bagpy pandas autopep8
```
Install a Jupyter kernel for the virtual environment.
```
python -m ipykernel install --user --name venv
```

### Usage


Open jupyter notebook and run BagToTable.ipynb in the venv. 
It will generate csv files from the bag data in the /analysis/processed_data directory.


### Misc

Check the kernel list
```
jupyter kernelspec list
```

Create a virtual environment in that directory
```
python3 -m venv venv
```


Remove venv folder
```
rm -rf venv
```

Rosbags package
```
pip install .    # (instead of the python setup.py install)
```

[ROS]: http://www.ros.org
[justhink_world]: https://github.com/utku-norman/justhink_world
[justhink_app]: https://github.com/utku-norman/justhink_app
[justhink_robot]: https://github.com/utku-norman/justhink_robot
[justhink_msgs]: https://github.com/utku-norman/justhink_msgs
