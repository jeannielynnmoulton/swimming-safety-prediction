# swimming-safety-prediction

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
