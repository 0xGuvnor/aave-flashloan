from brownie import accounts, config, network, interface


def main():
    """
    Runs the get_weth function to get WETH
    """
    get_weth(0.01)


def get_weth(value=1):
    """
    Mints WETH by depositing ETH.
    """
    acct = accounts[0]
    # acct = accounts.add(
    #     config["wallets"]["from_key"]
    # )  # add your keystore ID as an argument to this call
    weth = interface.WethInterface(config["networks"][network.show_active()]["weth"])
    tx = weth.deposit({"from": acct, "value": value * 10**18})
    tx.wait(1)
    print(f"Received {value} WETH")
    return tx
