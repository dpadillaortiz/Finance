#!/usr/bin/python3

import csv
import sys

class PostingDate:
    def __init__(self, posting_date):
        self.year = self.posting_year(posting_date)
        self.month = self.posting_month(posting_date)
        self.day = self.posting_day(posting_date)

    def posting_year(self, posting_date: str) -> int:
        date_stripped = posting_date.split('/')
        year = int(date_stripped[2])
        return year

    def posting_month(self, posting_date: str) -> int:
        date_stripped = posting_date.split('/')
        month = int(date_stripped[0])
        return month

    def posting_day(self, posting_date: str) -> int:
        date_stripped = posting_date.split('/')
        day = int(date_stripped[1])
        return day


def transactions(csv_file: str) -> list:
    transactions = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader: 
            transactions.append(line)
    return transactions

def filter_by_year(transactions: list, target_year: int) -> list:
    filtered_transactions = []
    for transaction in transactions:
        if target_year == PostingDate(transaction['Posting Date']).year:
            filtered_transactions.append(transaction)
    return filtered_transactions

def filter_by_month(transactions: list, month: int) -> list:
    filtered_transactions = []
    for transaction in transactions:
        if month == PostingDate(transaction['Posting Date']).month:
            filtered_transactions.append(transaction)
    return filtered_transactions

def filter_by_day(transactions: list, day: int) -> list:
    filtered_transactions = []
    for transaction in transactions:
        if day == PostingDate(transaction['Posting Date']).day:
            filtered_transactions.append(transaction)
    return filtered_transactions

def filter_by_description(transactions: list, description: str) -> list:
    filtered_transactions = []
    for transaction in transactions:
        if description in transaction['Description']:
            filtered_transactions.append(transaction)
    return filtered_transactions

def print_transactions(transactions: list) -> None:
    for transaction in transactions:
        print(transaction)




if __name__ == '__main__':
    csv_file = sys.argv[1]
    transactions_list = transactions(csv_file)
    year = filter_by_year(transactions_list, 2022)
    print_transactions(year)
    month = filter_by_month(transactions_list, 8)
    print_transactions(month)
    day = filter_by_day(transactions_list, 13)
    print_transactions(day)
