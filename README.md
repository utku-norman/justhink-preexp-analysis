# JUSThink Pre-experiment Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Overview


**Keywords:** human-robot interaction, mutual understanding, collaborative learning, computational thinking


### License <a name="license"></a>

The whole package is under MIT License, see [LICENSE](LICENSE).

Classes under the [tools/effsize](tools/effsize) package were taken from project [DABEST](https://acclab.github.io/DABEST-python-docs/index.html), Copyright 2016-2020 Joses W. Ho. These classes are licensed under the BSD 3-Clause Clear License. See [tools/effsize/LICENSE](tools/effsize/LICENSE) for additional details.

The package has been tested under Python 3.8 on Ubuntu 20.04.
This is research code, expect that it changes often and any fitness for a particular purpose is disclaimed.


### Publications

If you use this work in an academic context, please cite the following publication:

* Norman, U., Chin, A., Bruno, B., & Dillenbourg, P. (2022). **Efficacy of a ‘Misconceiving’ Robot to Improve Computational Thinking in a Collaborative Problem Solving Activity: A Pilot Study.** 2022 31st IEEE International Conference on Robot & Human Interactive Communication (RO-MAN). ([PDF](https://infoscience.epfl.ch/record/294825))

        @inproceedings{norman_efficacy_2022,
            title       = {Efficacy of a 'Misconceiving' Robot to Improve Computational Thinking in a Collaborative Problem Solving Activity: A Pilot Study},
            booktitle   = {2022 31st {IEEE} International Conference on Robot \& Human Interactive Communication ({RO}-{MAN})},
            author      = {Norman, Utku and Chin, Alexandra and Bruno, Barbara and Dillenbourg, Pierre},
            month       = aug,
            year        = {2022},
            url         = {https://infoscience.epfl.ch/record/294825},
            urldate     = {2022-07-01},
        }



### Installation

#### Dependencies

* [justhink_world](https://github.com/utku-norman/justhink_world) to represent an activity as a world/problem with a state (that depends on [pomdp_py](https://h2r.github.io/pomdp-py/html/), [networkx](https://networkx.org/), [pyglet](https://pyglet.readthedocs.io/en/latest/), [importlib_resources](https://importlib-resources.readthedocs.io/en/latest/), and [pqdict](https://pypi.org/project/pqdict/))
* [effsize](tools/effsize) tool to compute estimators of effect size.
We specifically use it to compute Cliff's Delta, which quantifies the amount difference between two groups of observations, by computing the Cliff's Delta statistic. It is from project [DABEST](https://acclab.github.io/DABEST-python-docs/index.html) (see [License](#license)).

## Installation

1) Clone this ([justhink-preexp-analysis]) repository:
```
git clone https://github.com/utku-norman/justhink-preexp-analysis.git
```

2) Create a new [virtual environment](https://docs.python.org/3/tutorial/venv.html) and activate it (can do so in the same folder. Note that the folder name `venv` is [git-ignored](https://git-scm.com/docs/gitignore)):
```
cd justhink-preexp-analysis

python3 -m venv .venv --prompt JUSThink-preexp-env

source .venv/bin/activate
```

3) Install the dependency [justhink_world] Python package inside this virtual environment:
```
# Get the source code.
git clone --branch v0.2.0 https://github.com/utku-norman/justhink_world.git .venv/justhink_world


# Activate the virtual environment.
source .venv/bin/activate

# Install the package.
pip install -e .venv/justhink_world
```


4) Install the remaining dependencies:
```
pip install -r analysis/requirements.txt
```

For any issues while installing the [justhink_world] package, refer to its README.


5) Install a Jupyter kernel for the virtual environment.
```
python -m ipykernel install --user --name justhink-preexp-env --display-name "Python (JUSThink-preexp)" 
```

6) Done! Run the notebooks in [tools/] with: 
```
jupyter notebook
```


### Usage

In the [tools/] folder, there are Jupyter notebook that generate process the data in [data/].



### Other useful commands

Check the kernel list:
```
jupyter kernelspec list
```

Remove an installed kernel:
```
jupyter kernelspec remove justhink-preexp-env
```



[ROS]: http://www.ros.org
[justhink_world]: https://github.com/utku-norman/justhink_world
[justhink-preexp-analysis]: https://github.com/utku-norman/justhink-preexp-analysis