from numpy import PINF
import pandas as pd
from tabulate import tabulate
import requests
import csv
import functions

ingredient = input('Please type an ingredient: ')
functions.run_script(ingredient)
