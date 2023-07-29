from common.Goerli import GoerliToken
from common.TokenL1 import GOERLI_TOKEN
from common.abi import GOERLI_TOKEN_ABI
import os
from brownie import network
from brownie import Contract
from brownie.network import rpc, web3 as brownie_web3
from brownie import accounts
from loguru import logger
from brownie.network.transaction import TransactionReceipt
import requests
import json

def get_signature(wallet, refer):
    

    url = "https://api.karatdao.com/network/action"

    payload = json.dumps({
        "method": "claimer/requestMintClaimerSignature",
        "params": {
            "walletAddress": wallet,
            "validatorTokenId": "8",
            "lieutenantAddr": refer
        }
    })
    headers = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    obj = response.json()
    return obj['result']
