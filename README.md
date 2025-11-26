# Hack The River 2025 - Swimming Safety Prediction Team

This repository contains the code developed by the swimming safety prediction team for the Hack The River hackathon organised by UKCEH, Thames21 and The Rivers Trust.

We use data from the Oxford Rivers Portal (https://oxfordrivers.ceh.ac.uk/) to explore the factors which control e. coli polution in Oxford's rivers and wild swimming spots. Because e. coli data is infrquently recorded, and has a two day latency, we use river level and rainfall to predict e. coli levels. A future operational model based upon the work here would enable members of the public to access real-time forecasts of e. coli, promoting safe wild swimming in Oxfordshire.

## Code Organisation

The code is organised as follows:

### app.py

Contains utilities to download data from the Oxford Rivers Portal and reformat the files into user friendly Pandas dataframes.

### EcoliTurbidityInvestigation.py

Explores relationship between e. coli and turbidity at Wolvercote bathing site.

### RainfallInvestigation.ipynb

Explores relationship between e. coli and other potential predictors (rainfall, dissolved organic matter) at Wolvercote bathing site.

### predicting_ecoli.ipynb

Training and testing three machine learning models (Random Forest, LightGBM, XGBoost), aiming to predict e. coli from rainfall and river level.

## Usage

- Download or fork the repository to your machine
- Install pipenv (https://pipenv.pypa.io/en/latest/quick_start.html).
- Run pipenv install in the terminal. This will create a virtual environment on your machine from the piplock file.
- .py scripts can be run using e.g. pipenv run python app.py in the terminal

## Using pipenv

The python environment is managed using pipenv. 
It manages dependencies and virtual environment for us. 
Here is a quick start guide to using pipenv. 
I've done most of the setup for basic dependencies already.
The short of it is to use pipenv to install dependencies and run scripts.

https://pipenv.pypa.io/en/latest/quick_start.html

We might need to install new dependencies e.g., 
```pipenv install pandas```

or run python scripts
```pipenv run python app.py``` (use `python3`) on mac.

## How to use git and github (very quick and dirty)

- Install git onto your machine.
- Create an account for Github and accept my invitation.
- Clone the repository `git clone git@github.com:jeannielynnmoulton/swimming-safety-prediction.git`
- This will put everything in the github repo onto your computer.
- You can create a new branch using `git checkout -b your_branch` and switch between branches `git checkout main`.
- You can push and pull to github using `git push` and `git pull`. 

For example, if you want to make a new branch from main do
- `git pull` on main
- `git checkout -b your_branch` which creates and switches to a new local branch
- Write some code in `your_script.py`
- `git add your script.py`
- `git commit` will store your code in the branch with a message you type (you may need to change your text editor, google it)
- `git push` will push the changes to Github so other people can view and pull.

When we need to start merging our code into main, I can help with that. We can use pull requests to help avoid conflicts.
