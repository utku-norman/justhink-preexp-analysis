# JUSThink Pre-experiment Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository contains the **data** and the **analysis** used in our paper [[1]](#references):

* Norman, U., Chin, A., Bruno, B., & Dillenbourg, P. (2022). **Efficacy of a ‘misconceiving’ robot to improve computational thinking in a collaborative problem solving activity: a pilot study.** 2022 31st IEEE International Conference on Robot & Human Interactive Communication (RO-MAN). Available: [https://infoscience.epfl.ch/record/294825](https://infoscience.epfl.ch/record/294825)

The **[data](#dataset)** results from a pre-experimental pilot study conducted remotely with 9 school children, aged 10-12 years old. It contains the logs of the children interacting with a humanoid robot ([QTrobot](https://luxai.com/)) within a learning activity (a human-robot version of the [JUSThink activity](https://www.epfl.ch/labs/chili/index-html/research/animatas/justhink/) [[2,3]](#references)), that aims to improve their computational thinking skills by applying abstract and algorithmic reasoning to solve a problem on networks (the minimum spanning tree problem). The activity is in a pedagogical scenario that consists of individual (e.g. as in a test for assessment) and collaborative (with an artificial agent i.e. a physically embodied robot in our case) activities. In the collaborative activities, the human and the robot take turns in making suggestions on what to do, and agreeing or disagreeing with each other, to construct a shared solution to the problem.

In the **[analysis](#notebooks)**, we investigate the [research questions and hypotheses](#rqs_hs) as reported in [[1]](#references), on whether the interaction results in positive learning outcomes, how the collaboration evolves, and how these relate to each other. Please see [the paper](https://infoscience.epfl.ch/record/294825) for further information.

For the [ROS] packages to govern the human-robot interaction scenario, see the repository [justhink-ros]. The activities are implemented in the repository [justhink_world]. The activity and the scenario is a part of the [JUSThink project](https://www.epfl.ch/labs/chili/index-html/research/animatas/justhink/), at the [CHILI Lab](https://www.epfl.ch/labs/chili) at EPFL.

If you use this work in an academic context, please cite this publication:

        @inproceedings{norman_efficacy_2022,
            title       = {Efficacy of a 'misconceiving' robot to improve computational thinking in a collaborative problem solving activity: a pilot study},
            pages       = {1413--1420},
            booktitle   = {2022 31st {IEEE} International Conference on Robot and Human Interactive Communication ({RO}-{MAN})},
            author      = {Norman, Utku and Chin, Alexandra and Bruno, Barbara and Dillenbourg, Pierre},
            month       = aug,
            year        = {2022},
            doi         = {10.1109/RO-MAN53752.2022.9900775},
        }


**Keywords:** human-robot interaction, mutual understanding, collaborative learning, computational thinking

## Table of Contents
1. [Installation](#installation)
2. [Research Questions and Hypotheses](#rqs_hs) in [[1]](#references)
3. [Content](#content)
    1. [Jupyter Notebooks](#notebooks) (in [tools/](analysis/tools/))
    2. [External Tools](#additional_tools) (in [tools/](analysis/tools/))
    3. [The Dataset](#dataset) (in [data/](data/))
    4. [The Processed Data](#processed_data) (generated at [processed_data/](analysis/processed_data/))
    5. [The Figures](#figures) (generated at [figures/](analysis/figures/))
4. [Acknowledgements](#acknowledgements)
4. [License](#license)


## 1. Installation <a name="installation"></a>

1) Clone this ([justhink-preexp-analysis]) repository:

```
git clone https://github.com/utku-norman/justhink-preexp-analysis.git
```
    
2) Create a new [virtual environment](https://docs.python.org/3/tutorial/venv.html) and activate it (can do so in the same folder. Note that the folder name `.venv` is [git-ignored](https://git-scm.com/docs/gitignore)):

```
cd justhink-preexp-analysis
python3 -m venv .venv --prompt JUSThink-preexp-env
source .venv/bin/activate
```
    
3) Install the dependency [justhink_world] Python package inside this virtual environment:

```
git clone --branch v0.2.0 https://github.com/utku-norman/justhink_world.git .venv/justhink_world

source .venv/bin/activate

pip install -e .venv/justhink_world
```

4) Install the remaining dependencies:

```
pip install -r analysis/requirements.txt
```

For any issues while installing the [justhink_world] package, refer to its README.

5) Install a Jupyter kernel for the virtual environment:

```
python -m ipykernel install --user --name justhink-preexp-env --display-name "Python (JUSThink-preexp)" 
```

6) Done! You can now run the notebooks in [analysis/tools/](analysis/tools/) with:

```
jupyter notebook
```

### Other useful commands

Check the list of installed Jupyter kernels:
```
jupyter kernelspec list
```

Remove the installed kernel:
```
jupyter kernelspec remove justhink-preexp-env
```

## 2. Research Questions and Hypotheses <a name="rqs_hs"></a>

Here are the research question and the hypotheses evaluated in [[1]](#references):

* __RQ1__:  How are the learning outcomes after collaborating with the robot?
    * __H1.1__: A participant provides a valid solution more in the post-test than the pre-test.
    * __H1.2__: A participant provides a correct solution more in the post-test than the pre-test.
    * __H1.3__: A participant provides a better solution (closer to a correct solution) more in the post-test than the pre-test.

* __RQ2__: How does performance in the task evolve during collaboration with the robot?
    * __H2.1__: A participant submits better solutions (closer to a correct solution) later than earlier.
    * __H2.2__: A participant suggests correct actions more later than earlier.
    * __H2.3__: A participant (dis)agrees more with (in)correct robot suggestions later than earlier.
    
* __RQ3__: How does the evolution of performance in the task link to the learning outcomes?
    * __H3.1__: The more a participant’s submissions improve, the better are the learning outcomes.
    * __H3.2__: The more a participant’s suggestions improve, the better are the learning outcomes.
    * __H3.3__: The more a participant’s (dis)agreements improve, the better are the learning outcomes.

The RQs and Hs are addressed in [the Jupyter notebooks](#notebooks): in the dedicated [notebook for RQ1](analysis/tools/3_RQ1_analyze_learning_outcomes.ipynb), [for RQ2](analysis/tools/4_RQ2_analyze_performance_over_time.ipynb), and [for RQ3](analysis/tools/5_RQ3_link_performance_and_learning_outcomes.ipynb).

## 3. Content <a name="content"></a>

The tools provided in this repository consist of 5 Jupyter Notebooks written in Python 3, and an additional external tool utilized by the notebooks.

### 3.1. Jupyter Notebooks <a name="notebooks"></a>

The [tools/](analysis/tools/) folder contains the [Jupyter notebooks](https://jupyter.org/) that process the [dataset](#dataset), to generate the [processed_data](#processed_data) and the [figures](#figures). Results of statistical tests to evaluate the [hypotheses](#rqs_hs) are in the corresponding notebooks.

1. [Convert the raw logs (in rosbag format) to log tables](analysis/tools/1_convert_ROS_bags_to_log_tables.ipynb):
Converts the logs in [`rosbag` format](http://wiki.ros.org/rosbag) that were used to log the events in the application and robot actions to tables in CSV data format. Tables are organized as per event type (i.e. per ROS topic) and per participant, and exported to CSV files.
2. [Construct in interaction histories as state transitions from the log tables](analysis/tools/2_construct_transition_data_from_log_tables.ipynb):
Constructs state and action objects from the log tables, and exports them as transition tables and lists in [pickle](https://docs.python.org/3/library/pickle.html) format.
3. [Address RQ1 on the learning outcomes](analysis/tools/3_RQ1_analyze_learning_outcomes.ipynb)
4. [Address RQ2 on the evolution of performance in the task](analysis/tools/4_RQ2_analyze_performance_over_time.ipynb)
5. [Address RQ3 on the link between the evolution of performance in the task and the learning outcomes](analysis/tools/5_RQ3_link_performance_and_learning_outcomes.ipynb)

### 3.2. External Tools <a name="additional_tools"></a>

* [effsize](tools/effsize) <a name="effsize"></a> tool to compute estimators of effect size.
We specifically use it to compute Cliff's Delta, which quantifies the amount difference between two groups of observations, by computing the Cliff's Delta statistic.
It is from the [DABEST](https://acclab.github.io/DABEST-python-docs/index.html) project (see [License](#license)).

### 3.3. The Dataset (JUSThink Human-Robot Pre-experiment Dataset) <a name="dataset"></a>

The folder [data/](data/) contains the *JUSThink Human-Robot Pre-experiment Dataset* in [`rosbag` format](http://wiki.ros.org/rosbag) format, with the interaction logs of N=9 children: it is converted with [the Jupyter Notebooks](#notebooks) to a history of state transitions for each participant regarding how they constructed their solutions in each activity: individually in the tests and together with the robot in the collaborative activities.

### 3.4. The Processed Data <a name="processed_data"></a>

The folder [processed_data/](analysis/processed_data/) contains the processed version of the [dataset](#dataset), the intermediate content that is used to obtain the results and [the figures](#figures) in [[1]](#references).

### 3.5. The Figures <a name="figures"></a>

The folder [figures/](analysis/figures/) contains the figures that are presented in [[1]](#references), and produced by [the Jupyter Notebooks](#notebooks).

## Acknowledgements <a name="acknowledgements"></a>
This project has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No [765955](https://cordis.europa.eu/project/id/765955). Namely, the [ANIMATAS Project](https://www.animatas.eu/).

## License <a name="license"></a>

The whole package is under MIT License, see [LICENSE](LICENSE).

Classes under the [effsize](analysis/tools/effsize) package were taken from project [DABEST](https://acclab.github.io/DABEST-python-docs/index.html), Copyright 2016-2020 Joses W. Ho. These classes are licensed under the BSD 3-Clause Clear License. See [effsize/LICENSE](analysis/tools/effsize/LICENSE) for additional details.

The package has been tested under Python 3.8 on Ubuntu 20.04.
This is research code, expect that it changes often and any fitness for a particular purpose is disclaimed.


## References <a name="references"></a>

[1] U. Norman, A. Chin, B. Bruno, and P. Dillenbourg, “Efficacy of a ‘misconceiving’ robot to improve computational thinking in a collaborative problem solving activity: a pilot study,” in 2022 31st IEEE International Conference on Robot and Human Interactive Communication (RO-MAN), Aug. 2022, pp. 1413–1420. doi: [10.1109/RO-MAN53752.2022.9900775](https://doi.org/10.1109/RO-MAN53752.2022.9900775)

[2] J. Nasir\*, U. Norman\*, B. Bruno, and P. Dillenbourg, "When positive perception of the robot has no effect on learning," in 2020 29th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN), Aug. 2020, pp. 313–320. \*Contributed equally to this work. doi: [10.1109/RO-MAN47096.2020.9223343](https://doi.org/10.1109/RO-MAN47096.2020.9223343)

[3] J. Nasir, U. Norman, B. Bruno, and P. Dillenbourg, "You tell, i do, and we swap until we connect all the gold mines!," ERCIM News, vol. 2020, no. 120, 2020, [Online]. Available: [https://ercim-news.ercim.eu/en120/special/you-tell-i-do-and-we-swap-until-we-connect-all-the-gold-mines](https://ercim-news.ercim.eu/en120/special/you-tell-i-do-and-we-swap-until-we-connect-all-the-gold-mines)

[ROS]: http://www.ros.org
[justhink_world]: https://github.com/utku-norman/justhink_world
[justhink-ros]: https://github.com/utku-norman/justhink-ros
[justhink-preexp-analysis]: https://github.com/utku-norman/justhink-preexp-analysis