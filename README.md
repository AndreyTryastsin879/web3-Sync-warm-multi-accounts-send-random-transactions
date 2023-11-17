RU

Подробное описание работы со скриптом:
https://crypto-py.com/13-avtomatizatsiya-akkauntov/85-progrev-akkauntov-v-evm-setyakh-self-tranzaktsii-i-tranzaktsii-na-sluchajnye-adresa-c-pomoshchyu-web3-py

Такое же подробное описание в файле web3-warm-multi-accounts-send-random-transactions.ipynb

Репозиторий с асинхронной версией:
https://github.com/AndreyTryastsin879/web3-async-warm-multi-accounts-send-random-transactions

Что делает этот скрипт
Идея скрипта @S7miles. Сообщества https://t.me/sybilders и https://t.me/shitbilders. Купить готовый софт http://t.me/sybilders_bot.

Для работы используются:
- txt файл с приватными ключалми от кошельков, для которых будут осуществляться транзакции,
- модуль chain_settings.py в котором задаются настройки для сетей, в которых будут осуществляться транзакции.

Используются два вида транзакций:
- SELF - отправка идет на свой адрес,
- RANDOM - генерируется случайный адрес, на него отправляется некоторое количество монет.
Для каждого кошелька из списка берется сеть, определяется рандомное количество транзакций, в рамках этого количества рандомно выбирается вид транзакции. Например, в сети BSC будет совершено 12 транзакций, из них 3 будет SELF, а 9 - RANDOM и т.п. После каждой транзакции процесс засыпает на время, которое определяется рандомно.

После завершения всех транзакций для всех адресов, экспортируется отчет в csv.

===========================================================================================================================================================

EN

Detailed description of working with the script:
https://crypto-py.com/13-automating-accounts/85-warming-accounts-in-evm-networks-self-transactions-and-transactions-to-random-addresses-with-web3-py

The same detailed description is available in the file web3-warm-multi-accounts-send-random-transactions.ipynb

Repository with the asynchronous version:
https://github.com/AndreyTryastsin879/web3-async-warm-multi-accounts-send-random-transactions

What this script does
The script idea is from @S7miles, communities https://t.me/sybilders and https://t.me/shitbilders. Buy ready-made software at http://t.me/sybilders_bot.

Used for operation:

txt file with private keys from wallets for which transactions will be made,
module chain_settings.py where settings for networks in which transactions will be made are specified.
Two types of transactions are used:

SELF - the sending goes to one's own address,
RANDOM - a random address is generated, and a certain amount of coins is sent to it.
For each wallet from the list, a network is taken, a random number of transactions is determined, and within this number, the type of transaction is randomly chosen. For example, in the BSC network, 12 transactions will be made, 3 of which will be SELF, and 9 will be RANDOM, and so on. After each transaction, the process sleeps for a randomly determined time.
After completing all transactions for all addresses, a report is exported to CSV.

