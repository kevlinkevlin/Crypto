import time
from web3 import Web3
import json
abi = ''
with open("./gel.json") as f:
    abi = json.load(f)
web3 = Web3(Web3.HTTPProvider('https://jsonrpc.maiziqianbao.net'))

contract_addr = Web3.toChecksumAddress(
    '0x5898D2aE0745c8d09762Bac50fd9F34A2a95A563')  # 現在為Gelato
# 個人資訊
user_addr = ''
private_key = ''
contract = web3.eth.contract(address=contract_addr, abi=abi)
# 開始時間
start_time = 1631563200
# 購買數量(ETH)
buy_eth = 1.17
nonce = web3.eth.getTransactionCount(user_addr)
singature=''

while True:
    blocktime = web3.eth.get_block('latest').timestamp
    if start_time - blocktime <= 30:
        transaction = contract.functions.buyDolphin(singature).buildTransaction({
            'gas': 600000,
            'gasPrice': web3.toWei('180', 'gwei'),
            'from': user_addr,
            'nonce': web3.eth.getTransactionCount(user_addr),
            'value':buy_eth,
            'chainId': 1, 
        })
        signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
        print(web3.eth.sendRawTransaction(signed_txn.rawTransaction))
        print("完成")
        break
    print("開始時間:{s1}秒, 現在區塊時間:{s2}".format(s1=start_time,s2=blocktime))
    print("市場狀態{s}".format(s=contract.functions.isPoolTwoOpen().call()))