import time
import random
from datetime import datetime

import numpy as np
import pandas as pd

from web3 import Web3

from config import REPORT_TABLE_NAME, NUMBER_OF_VARIATIONS_BETWEEN_SENDING_AMOUNT, MIN_TIMESLEEP_BETWEEN_TRANSACTIONS, \
    MAX_TIMESLEEP_BETWEEN_TRANSACTIONS
import chain_settings


global_list_for_report = list()


def save_report_to_global_list(chain_name, wallet_address,
                               transaction_type, transaction_status,
                               amount, transaction_explorer_url, error):
    d = dict()
    d['chain_name'] = chain_name
    d['wallet_address'] = wallet_address
    d['transaction_type'] = transaction_type
    d['transaction_status'] = transaction_status
    d['sent_amount'] = amount
    d['transaction_url'] = transaction_explorer_url
    d['date'] = datetime.now().strftime('%d-%m-%Y')
    d['error'] = error

    global global_list_for_report
    global_list_for_report.append(d)


def export_report():
    global global_list_for_report
    df = pd.DataFrame.from_dict(global_list_for_report)
    df.to_csv(REPORT_TABLE_NAME, index=False)


def create_random_value_from_range(min_value, max_value):
    random_value_between_range = random.choice(range(min_value, max_value))

    return random_value_between_range


def create_random_amount_for_sending(min_value_for_sending, max_value_for_sending,
                                     number_of_variations_between_sending_amount):
    random_position = random.choice(range(number_of_variations_between_sending_amount))

    random_amount_for_sending = np.linspace(min_value_for_sending,
                                            max_value_for_sending,
                                            num=number_of_variations_between_sending_amount)[random_position]

    return random_amount_for_sending


def transaction_settings(web3, from_address, to_address, amount):
    amount_wei = web3.to_wei(amount, 'ether')

    gas_price = web3.eth.gas_price

    estimated_gas = web3.eth.estimate_gas({
        'to': to_address,
        'value': amount_wei,
    })

    nonce = web3.eth.get_transaction_count(from_address)

    transaction = {
        'chainId': web3.eth.chain_id,
        'from': from_address,
        'to': to_address,
        'value': amount_wei,
        'nonce': nonce,
        'gasPrice': gas_price,
        'gas': estimated_gas,
    }

    return transaction


def create_sign_send_transaction(web3, from_address, to_address, amount, private_key):
    create_transaction = transaction_settings(
        web3=web3,
        from_address=from_address,
        to_address=to_address,
        amount=amount
    )

    signed_transaction = web3.eth.account.sign_transaction(create_transaction, private_key)

    transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

    return transaction_hash.hex()


def self_transaction(web3, amount, private_key,
                     min_timesleep_between_transactions,
                     max_timesleep_between_transactions,
                     chain_name, explorer_url):

    try:
        timesleep_value = create_random_value_from_range(5, 15)
        time.sleep(timesleep_value)

        transaction_type = 'SELF-transaction'
        print(f'Key {private_key[:6]}...{private_key[-6:]}, {transaction_type} {chain_name}')

        my_address = web3.eth.account.from_key(private_key).address

        transaction_hash = create_sign_send_transaction(web3, my_address, my_address,
                                                        amount, private_key)

        print(f'Hash {transaction_type} {chain_name} {transaction_hash}')

        print(f'Recording data in a report')
        save_report_to_global_list(chain_name, my_address,
                                   transaction_type, 'SUCCESS',
                                   amount, f'{explorer_url}{transaction_hash}', '-')

        timesleep_value = create_random_value_from_range(min_timesleep_between_transactions,
                                                         max_timesleep_between_transactions)
        print(f'Pause {timesleep_value} sec. after {transaction_type} {chain_name} ', '\n')
        time.sleep(timesleep_value)

    except Exception as error:
        print(f'{transaction_type} {chain_name}, error -  {error}', '\n')
        save_report_to_global_list(chain_name, my_address,
                                   transaction_type, 'ERROR',
                                   amount, '-', error)


def random_transaction(web3, amount, private_key,
                       min_timesleep_between_transactions,
                       max_timesleep_between_transactions,
                       chain_name, explorer_url):
    try:
        timesleep_value = create_random_value_from_range(5, 15)
        time.sleep(timesleep_value)

        transaction_type = 'RANDOM-transaction'
        print(f'Key {private_key[:6]}...{private_key[-6:]}, {transaction_type} {chain_name}', '\n')

        account = web3.eth.account.create()
        random_wallet = account.address

        my_address = web3.eth.account.from_key(private_key).address
        prepared_wallet = web3.to_checksum_address(random_wallet)

        transaction_hash = create_sign_send_transaction(web3, my_address, prepared_wallet,
                                                        amount, private_key)

        print(f'Hash {transaction_type} {chain_name} {transaction_hash}' )

        print(f'Recording data in a report')
        save_report_to_global_list(chain_name, my_address,
                                   transaction_type, 'SUCCESS',
                                   amount, f'{explorer_url}{transaction_hash}', '-')

        timesleep_value = create_random_value_from_range(min_timesleep_between_transactions,
                                                         max_timesleep_between_transactions)
        print(f'Pause {timesleep_value} sec. after {transaction_type} {chain_name} ', '\n')
        time.sleep(timesleep_value)

    except Exception as error:
        print(f'{transaction_type} {chain_name}, error -  {error}', '\n')
        save_report_to_global_list(chain_name, my_address,
                                   transaction_type, 'ERROR',
                                   amount, '-', error)


def main_function_make_random_or_self_txns(private_key):
    try:
        for chain in map(chain_settings.__dict__.get, chain_settings.__all__):
            chain_name = chain['name']

            print(f'Process has been launched for {private_key[:6]}...{private_key[-6:]} on the network {chain_name}')

            web3 = Web3(Web3.HTTPProvider(chain['url']))

            if not web3.is_connected():
                print(f'Connection to {chain_name} is not established', '\n')

                my_address = web3.eth.account.from_key(private_key).address
                save_report_to_global_list(chain_name, my_address,
                                           '-', 'ERROR',
                                           '-', '-',
                                           'Connection is not established')
                time.sleep(5)
                continue

            print(f'Connection to {chain_name} was established', '\n')

            transactions_quantity = create_random_value_from_range(chain['min_transactions'],
                                                                   chain['max_transactions'])

            for _ in range(transactions_quantity):
                amount = create_random_amount_for_sending(chain['min_amount_for_sending'],
                                                          chain['max_amount_for_sending'],
                                                          NUMBER_OF_VARIATIONS_BETWEEN_SENDING_AMOUNT)

                random.choice([self_transaction, random_transaction])(web3, amount, private_key,
                                                                      MIN_TIMESLEEP_BETWEEN_TRANSACTIONS,
                                                                      MAX_TIMESLEEP_BETWEEN_TRANSACTIONS,
                                                                      chain_name, chain['explorer_url'])

    except Exception as error:
        print(error, '\n')
        save_report_to_global_list('-', private_key,
                                   '-', 'ERROR',
                                   '-', '-',
                                   'Some system error occurred during the process.')