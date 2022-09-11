#!/usr/bin/python3

import csv
import datetime
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

def filterPostingMonth(csv_file: str, month: int) -> list:
    filteredTransactions = []
    with open(csv_file, 'r') as f:
        transactions = csv.DictReader(f)
        for transaction in transactions:
            if month == postingMonth(record['Posting Date']):
                filteredTransactions.append(transaction)
    return filteredTransactions

def filterPostingDay(csv_file: str, day: int) -> list:
    filteredTransactions = []
    with open(csv_file, 'r') as f:
        transactions = csv.DictReader(f)
        for transaction in transactions:
            if day == postingDay(record['Posting Date']):
                filteredTransactions.append(transaction)
    return filteredTransactions

def filterPayments(csv_file: str, query: str) -> list:
    payments = []
    with open(csv_file, 'r') as f:
        transactions = csv.DictReader(f)
        for transaction in transactions:
            if query in transaction['Description']:
                payments.append(transaction)
    return payments

def printFilterPayments(financials_list: list, query: str) -> None:
    '''printFilterPayments takes in the same parameters as filterPayments but iterates through the list and prints the transcations that satify the specified query'''
    for record in financials_list:
        if query in record['Description']:
            print(record)




if __name__ == '__main__':
    csv_file = sys.argv[1]
    x = transactions(csv_file)
    date = PostingDate('08/08/2022')
    print(date.year)
    print(date.month)
    print(date.day)
    y = filter_by_year(x, 2022)
    print(y)
