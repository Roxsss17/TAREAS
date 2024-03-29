# -*- coding: utf-8 -*-
"""Crear gráficos a partir de un archivo CSV

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fSpg9wMl3YQGHl9Xj2UF_6OT_QykL8ur
"""

import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv("data.csv")
ids = data ["Responder_id"]
lang_responses = data ["LanguagesWorkedWith"]

Language_counter = Counter()

for response in lang_responses:
      Language_counter.update(response.split(";"))

languages = []
popularity = []

for item in Language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.show()