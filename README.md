# Pipelines 4 All - From Data Engineering to Machine Learning
==============================

### Date: November 19th from 13:00 to 15:00 Thailand Time

## PyCon APAC 2021

Welcome to **Pipelines 4 All - From Data Engineering to Machine Learning**, a PyCon APAC 2021 tutorial where we will be learning about how to create data engineering and machine learning pipelines.

To go over the tutorial, please use the Binder button below.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ramonpzg/pycon-apac21-pipelines/master)


## Description

Pipelines are useful tools for data professionals at all levels and within different industries. From analysts who want to build processes to automate their analyses, to data engineers building extract, transform, and load pipelines, or even data scientists building models that require that a series of steps occur on the data needed before making a prediction (e.g. tokenization, scaling, or one of the many feature engineering techniques available). With this in mind, the goal of this tutorial is to help data professionals from diverse fields and at diverse levels build pipelines that can move and transform data as well as make useful predictions given different sets of inputs.

The tutorial will emphasize both methodology and frameworks through a top-down approach. Several of the open source libraries included are Prefect, MLFlow, Scikit-Learn, XGBoost, FastAPI, pandas, and the HoloViz suite of libraries.  In addition, the tutorial covers important concepts regarding data engineering, data analytics, and machine learning. Participants will learn concepts from the fields where the datasets came from as well, and build a foundation on how to reverse engineer data pipelines and other processes they find in the wild.

## Outline for the Tutorial

The time budgeted for this tutorial is about 3.5 hours including breaks. We will follow, as best as possible, the following schedule.

1. **Data Engineering Pipelines Part 1 - pandas (~45 minutes)**
3. **7-minute break**
4. **Data Engineering Pipelines Part 2 - Prefect (~45 minutes)**
5. **7-minute break**
6. **Machine Learning Pipelines (~45 minutes)**
5. **7-minute break**
6. **Machine Learning Experiments (~45 minutes)**

## Prerequisites (P) and Good To Have's (GTH)

- **(P)** Attendees for this tutorial are expected to be familiar with Python (1 year of coding). 
- **(P)** Participants should be comfortable with loops, functions, lists comprehensions, and if-else statements.
- **(GTH)** While it is not necessary to have knowledge of Prefect, MLFlow, Scikit-Learn, XGBoost, FastAPI, pandas, and the HoloViz suite of libraries, a bit of experience with these libraries would be very beneficial throughout this tutorial.
- **(P)** Participants should have at least 5 GB of free space in their computers.
- **(GTH)** While it is not required to have experience with an integrated development environment like Jupyter Lab, this would be very beneficial for the session.


## Setup

You should first make sure you have [Anaconda](https://www.anaconda.com/products/individual#download-section) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed. This will allow you to have most of the packages you will need for this tutorial already installed once you open up Jupyter Lab.

Here is one of the ways in which you can get the setup for the tutorial ready.

#### First Step

Open up your terminal and navigate to a directory of your choosing in your computer. Once there, run the following command.

```sh
 git clone https://github.com/ramonpzg/pycon-apac21-pipelines
```

Conversely, you can click on the green `download` button at the top and donwload all files to your desired folder/directory. Once you download it, unzip it and move on to the second step.

#### Second Step

To get all dependancies, packages and everything else that would be useful in this tutorial, you can recreate the environment by first going into the directory for today

```sh
cd pycon-apac21-pipelines
```

and then running

```sh
conda env create -f environment.yml
```

#### Third Step

Then you will need to activate your environment using the following command.

```sh
conda activate pipelines
```

#### Fourth Step

Open up Jupyter Lab and you should be ready to go.

```sh
jupyter lab
```