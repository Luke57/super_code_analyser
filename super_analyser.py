#!/usr/bin/env python3

"""
Code Analyser is een wrapper om veel verschillende opensource SAST
tools om een zo breed mogelijke indruk te krijgen van de code
Author: Tom Kluter
"""

# import modules
#import coverage
#import pytest
import subprocess
import time
import sys
import argparse
from io import StringIO
import pyfiglet
from pylint.lint import Run
from pylint.reporters.text import TextReporter
from mypy import api
from colorama import init as color_init
from color import output_info, output_bad, output_good, output_warning


BANNER = pyfiglet.figlet_format("Super Code Analyser")

def script_banner():
    print(BANNER)
    print("###################################################################\n")
    time.sleep(0.5)
    output_info("Current used tools: pylint, flake8, mypy, bandit, pydocstyle, pytype, pyright, vulture and coverage.py")
    time.sleep(0.5)

def update_packages():
    output_info("Updating packages...")
    subprocess.run(["pip", "install", "--upgrade", "pylint"], capture_output=True, text=True, check=False)
    subprocess.run(["pip", "install", "--upgrade", "flake8"], capture_output=True, text=True, check=False)
    subprocess.run(["pip", "install", "--upgrade", "mypy"], capture_output=True, text=True, check=False)
    subprocess.run(["pip", "install", "--upgrade", "bandit"], capture_output=True, text=True, check=False)
    subprocess.run(["pip", "install", "--upgrade", "pydocstyle"], capture_output=True, text=True, check=False)
    subprocess.run(["pip", "install", "--upgrade", "pytype"], capture_output=True, text=True, check=False)
    subprocess.run(["pip", "install", "--upgrade", "pyright"], capture_output=True, text=True, check=False)
    subprocess.run(["pip", "install", "--upgrade", "vulture"], capture_output=True, text=True, check=False)
    subprocess.run(["pip", "install", "--upgrade", "coverage"], capture_output=True, text=True, check=False)

    output_good("Packages updated!\n")

def script_input():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=BANNER)
    parser.add_argument("-i", "--input", help="File to analyze", required=False, type=str)
    parser.add_argument("-u", "--update", help="Update the used tools", required=False, action="store_true")
    parser.add_argument("-c", "--coverage", help="Measure code coverage of a given file, this is a dynamic check", required=False, action="store_true")
    args = parser.parse_args()
    parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    return args

def file_print():
    output_info(f"The following file will be analysed: {file}")
    time.sleep(1.5)

def begin_warning():
    output_warning("This tool could contain false positives. Always review manually")
    output_info("Indentation style errors are currently disabled")

def pylint_function():
    output_info("Running pylint \n")
    pylint_output = StringIO()
    reporter = TextReporter(pylint_output)
    Run(["--disable=W0311","--max-line-length=150", f"{file}"], reporter=reporter, do_exit=False)
    output_good("Pylint output: \n" + (pylint_output.getvalue()))

def flake8_function():
    output_info("Running flake8 \n")
    time.sleep(1)
    flake8_output = subprocess.run(["flake8", "--ignore=W191,E111,E114","--max-line-length=150", file], capture_output=True, text=True, check=False)
    output_good("Flake8 output: \n" + flake8_output.stdout)
    time.sleep(0.5)

def mypy_function():
    output_info("Running mypy \n")
    mypy_result = api.run([file, "--ignore-missing-imports"])
    if mypy_result[0]:
        output_good("Mypy output: \n" + mypy_result[0])
    elif mypy_result[1]:
        output_bad(mypy_result[1])
    else:
        output_bad("\nExit status:" + str(mypy_result[2]))

def bandit_function():
    output_info("Running Bandit\n")
    time.sleep(1)
    bandit_output = subprocess.run(["bandit", file], capture_output=True, text=True, check=False)
    output_good("Bandit output: \n" + bandit_output.stdout)

def pydocstyle_function():
    output_info("Running pydocstyle \n")
    time.sleep(1)
    pydocstyle_output = subprocess.run(["pydocstyle", file], capture_output=True, text=True, check=False)
    output_good("pydocstyle output: \n" + pydocstyle_output.stdout)

def pyright_function():
    output_info("Running pyright \n")
    pyright_output = subprocess.run(["pyright", file], capture_output=True, text=True, check=False)
    output_good("pyright output: \n" + pyright_output.stdout)

def pytype_function():
    output_info("Running pytype \n")
    pytype_output = subprocess.run(["pytype", file], capture_output=True, text=True, check=False)
    output_good("pytype output: \n" + pytype_output.stdout)

def vulture_function():
    output_info("Running vulture \n")
    time.sleep(1)
    vulture_output = subprocess.run(["vulture", file], capture_output=True, text=True, check=False)
    if vulture_output.returncode == 0:
        output_good("vulture output: \n" + "No dead code found!\n")
    else:
        output_good("vulture output: \n" + vulture_output.stdout)

def coverage_function():
    output_info("Running coverage.py \n")
    time.sleep(1)
    subprocess.run(["coverage", "run", "--branch", file], capture_output=False, text=True, check=False)
    coverage_output = subprocess.run(["coverage", "report", "-i", "-m", file], capture_output=True, text=True, check=False)
    output_good("Coverage.py output: \n" + coverage_output.stdout)

if __name__ == "__main__":
    color_init()

try:
    inputs = script_input()
    if inputs.update:
        script_banner()
        update_packages()
    elif inputs.input and inputs.coverage:
        script_banner()
        begin_warning()
        file = inputs.input
        file_print()
        pylint_function()
        flake8_function()
        mypy_function()
        bandit_function()
        pydocstyle_function()
        pytype_function()
        pyright_function()
        vulture_function()
        coverage_function()
    elif inputs.input:
        script_banner()
        begin_warning()
        file = inputs.input
        file_print()
        pylint_function()
        flake8_function()
        mypy_function()
        bandit_function()
        pydocstyle_function()
        pytype_function()
        pyright_function()
        vulture_function()

except Exception:
        sys.exit(0)
