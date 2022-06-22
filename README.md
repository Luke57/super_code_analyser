# Super Code Analyser

Super Code Analyser is a wrapper around the following tools: flake8, mypy, bandit, pydocstyle, pytype, pyright, vulture and coverage.py the tool combines te strength of all the mentioned tools to give a broad overview of the quality of the tested python code 

## Usage

```
usage: super_analyser.py [-h] [-i INPUT] [-u] [-c]

 ____                           ____          _      
/ ___| _   _ _ __   ___ _ __   / ___|___   __| | ___ 
\___ \| | | | '_ \ / _ \ '__| | |   / _ \ / _` |/ _ \
 ___) | |_| | |_) |  __/ |    | |__| (_) | (_| |  __/
|____/ \__,_| .__/ \___|_|     \____\___/ \__,_|\___|
            |_|                                      
    _                _                     
   / \   _ __   __ _| |_   _ ___  ___ _ __ 
  / _ \ | '_ \ / _` | | | | / __|/ _ \ '__|
 / ___ \| | | | (_| | | |_| \__ \  __/ |   
/_/   \_\_| |_|\__,_|_|\__, |___/\___|_|   
                       |___/               

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        File to analyze
  -u, --update          Update the used tools
  -c, --coverage        Measure code coverage of a given file, this is a dynamic check
```

## Setup
Run ```pip3 install -r requirements.txt``` from the command line to install the required dependencies.
