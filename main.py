import json
import requests
from web3 import Web3
from PyQt5 import uic,QtWidgets


app = QtWidgets.QApplication([])
error_dialog = QtWidgets.QErrorMessage()

#carrega a tela do pyqt5
form = uic.loadUi("web3.ui")

<<<<<<< HEAD
#conexão na infura 
=======
#conecta na infura 
infura_url = 'Utilize o seu link da infura mainet para se conectar com a blockchain'
web3 =  Web3(Web3.HTTPProvider(infura_url))

#verifica se a conexão foi concluida
connection = web3.isConnected()
#carrega a tela
form.show()

def main():
    #verifica se a conexão na blockchain está funcionando
    if not connection:
        return error_dialog.showMessage('Verifique se você está conectado com o link da infura')

    #pega o endereço da carteira
    you_adress = form.lineEdit.text()
    print(type(you_adress))
    #remove os espaços
    you_adress = you_adress.strip()
    try:
    #verificar a quantidade de ether na carteira
        check_sum = web3.toChecksumAddress(you_adress)
        balance = web3.eth.get_balance(check_sum)
        
        #converte o valor em ether
        ether_balance  = web3.fromWei(balance, 'ether')
        ether_balance = ether_balance = f'{ether_balance:,.2f}'
        form.lineEdit_2.setText(str(ether_balance))

        #pega a cotação atual do ether em dolar na api json e multiplica pela quantidade
        
        link_request = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
        dic_cotacoes = link_request.json()
        value_eth = float(dic_cotacoes['price'])
        saldo = float(ether_balance) * value_eth
        saldo = f'{saldo:,.2f}'
        form.lineEdit_3.setText(str(saldo))

        #pega o ultimo bloco gerado na blockchain
        latest_block = web3.eth.block_number        
        form.lineEdit_6.setText(str(latest_block))

    except:
        error_dialog.showMessage('Verifique se o endereço da carteira está correto')

form.pushButton.clicked.connect(main)
app.exec()
