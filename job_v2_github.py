from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional

from etherscan import Etherscan

API = 'YourEtherScanAPI'
eth = Etherscan(API)

bs = 20 #Batch Search   

 
Find = 0
Count = 0

while Find == 0:
    Wallet_List = []
    MNEMONIC_List = []  
    for txn in range(bs):
        #'''
        # Generate english mnemonic words
        MNEMONIC: str = generate_mnemonic(language="english", strength=128)
        # Secret passphrase/password for mnemonic
        PASSPHRASE: Optional[str] = None  # "meherett"
        
        # Initialize Ethereum mainnet BIP44HDWallet
        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
        # Get Ethereum BIP44HDWallet from mnemonic
        bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, language="english", passphrase=PASSPHRASE)
        # Clean default BIP44 derivation indexes/paths
        bip44_hdwallet.clean_derivation()
        
        # Get Ethereum BIP44HDWallet information's from address index
    
        for address_index in range(1): #wallet address shown
            # Derivation from Ethereum BIP44 derivation path
            bip44_derivation: BIP44Derivation = BIP44Derivation(
                cryptocurrency=EthereumMainnet, account=0, change=False, address=address_index
            )
            # Drive Ethereum BIP44HDWallet
            bip44_hdwallet.from_path(path=bip44_derivation)
            # Print address_index, path, address and private_key
            #print(f"({address_index}) {bip44_hdwallet.path()} {bip44_hdwallet.address()} 0x{bip44_hdwallet.private_key()}")
            address_temp = bip44_hdwallet.address()
            #print(address_temp)
            # Clean derivation indexes/paths
            bip44_hdwallet.clean_derivation()
        
            Wallet_List.append(address_temp)
            MNEMONIC_List.append(MNEMONIC)

    B_List = eth.get_eth_balance_multiple(Wallet_List)
    
    BB_List = [i['balance'] for i in B_List]
    
    if BB_List.count('0') == bs:
        print('Trying @', Count)

        Count = Count + 1
    else:
        print('Find One')
        print('##############################################################')
        print(B_List)
        print('##############################################################')
        print(MNEMONIC_List)
        Find = 1