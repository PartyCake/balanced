from pydantic import BaseModel
import datetime
import pandas as pd
import csv
from typing import Literal


class Transaction(BaseModel):
    date: datetime.date
    first_name: str
    last_name: str
    transaction_id: int
    amount: float
    currency: Literal['USD', 'EUR']


def read_csv(filename):
    array = []

    with open(f'{filename}.csv', encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            Transaction(**row)
            array.append(row)
        return array


def calculation_by_period(start_date, end_date, filename):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    df = pd.DataFrame(read_csv(filename))
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'])

    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    result_list = df.groupby([pd.PeriodIndex(df['date'], freq="M"), 'currency'])['amount'].mean().to_list()
    return result_list
