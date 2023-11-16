polygon_testnet = {
    'name': 'Polygon',
    'url': 'https://endpoints.omniatech.io/v1/matic/mumbai/public',
    'min_amount_for_sending': 0.0001,
    'max_amount_for_sending': 0.001,
    'min_transactions': 5,
    'max_transactions': 13,
    'explorer_url': 'https://mumbai.polygonscan.com/tx/'
}

bsc_testnet = {
    'name': 'Binance Smart Chain',
    'url': 'https://bsc-testnet.blockpi.network/v1/rpc/public',
    'min_amount_for_sending': 0.0001,
    'max_amount_for_sending': 0.001,
    'min_transactions': 12,
    'max_transactions': 40,
    'explorer_url': 'https://testnet.bscscan.com/tx/'
}

avalanche_testnet = {
    'name': 'Avalanche',
    'url': 'https://endpoints.omniatech.io/v1/avax/fuji/public',
    'min_amount_for_sending': 0.0001,
    'max_amount_for_sending': 0.001,
    'min_transactions': 5,
    'max_transactions': 10,
    'explorer_url': 'https://testnet.snowtrace.io/tx/'
}

__all__ = ['bsc_testnet', 'polygon_testnet']
