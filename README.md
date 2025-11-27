# Hack The River 2025 - Swimming Safety Prediction Team

This repository contains the code developed by the swimming safety prediction team for the Hack The River hackathon organised by UKCEH, Thames21 and The Rivers Trust.

We use data from the Oxford Rivers Portal (https://oxfordrivers.ceh.ac.uk/) to explore the factors which control E. coli 
pollution in Oxford's rivers and wild swimming spots. Because E. coli data is infrequently recorded, and has a two-day 
latency, we use river level and rainfall to predict E. coli levels, as well as investigate other potential predictors for which
there is currently not enough data. A future operational model based upon the work here would enable 
members of the public to access real-time forecasts of E. coli, promoting safe wild swimming in Oxfordshire.

## Code Organisation

The code is organised as follows:

### app.py

Contains utilities to download data from the Oxford Rivers Portal and reformat the files into user-friendly Pandas dataframes.
The utilities ensure that data is stored locally once called and the API of the rivers portal
is only accessed when local data is not available. Further work on these utilities could include
testing, refreshing when new data is available, further refinement of useful utilities, etc.

### EcoliTurbidityInvestigation.py

Examines a potential relationship between E. coli and turbidity at Wolvercote bathing site.
There is not much data and the results are inconclusive.

### RainfallInvestigation.ipynb

Investigates any relationship between E. coli and other potential predictors, e.g. rainfall, dissolved organic matter) at Wolvercote bathing site.
The rainfall data is further examined in predicting_ecoli.ipynb. Dissolved organic matter is further investigated in
EcoliFDOMInvestigation.ipynb

### predicting_ecoli.ipynb

Training and testing three machine learning models (Random Forest, LightGBM, XGBoost), aiming to predict E. coli from rainfall and river level.

### EcoliFDOMInvestigation.ipynb
Examines time series and correlation relationship between Dissolved organic matter (FDOM) and E. coli at Wolvercote bathing site.
There is not enough data to say conclusively whether FDOM is a good predictor of E. coli, but the initial
results look promising.

## Usage

- Download or fork the repository to your machine
- Install pipenv (https://pipenv.pypa.io/en/latest/quick_start.html).
- Run `pipenv install` in the terminal. This will create a virtual environment on your machine from the Pipfile.
- .py scripts can be run using e.g. `pipenv run python app.py` in the terminal

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

You can activate the shell with
```pipenv shell```

## How to use git and github (very quick and dirty)

- Install git onto your machine.
- Create an account for Github and accept my invitation.
- Clone the repository `git clone git@github.com:jeannielynnmoulton/swimming-safety-prediction.git`
- This will put everything in the github repo onto your computer.
- You can create a new branch using `git checkout -b your_branch` and switch between branches `git checkout main`.
- You can push and pull to github using `git push` and `git pull`. 

For example, if you want to make a new branch from main do
- `git checkout main`
- `git pull` on main
- `git checkout -b your_branch` which creates and switches to a new local branch
- Write some code in `your_script.py`
- `git add your_script.py`
- `git commit -m "Describe your changes"` will store your code in the branch with a message you type.
- `git push -u origin your_branch` for the first push.
- `git push` for the subsequent pushes.
- To merge code onto `main`, open a pull request on Github. This will help manage conflicts.