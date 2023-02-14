import pytest
from ethereum_client.plugin import ERC20Information
import ethereum_client

def test_provide_erc20_token(cmd):
    erc20_info = ERC20Information(
        erc20_ticker="5a5258",
        addr="0xe41d2489571d322189246dafa5ebde1f4699f498",
        nb_decimals=18,
        chainID=1,
        sign="304402200ae8634c22762a8ba41d2acb1e068dcce947337c6dd984f13b820d396176952302203306a49d8a6c35b11a61088e1570b3928ca3a0db6bd36f577b5ef87628561ff7"
    )

    # Test if return 9000
    try:
        cmd.provide_erc20_token_information(info=erc20_info)
    except:
        raise

def test_provide_erc20_token_goerli(cmd):
    erc20_info = ERC20Information(
        erc20_ticker=b"USDC".hex(),
        addr="0x79542cc915c2a19D1B00409C8B79E8E9E3bB4Bdc",
        nb_decimals=6,
        chainID=5,
        sign="304402202736a1fe050770aa00916f53d90bfee112eea5cb5ad139b8e8829d95cdbdf94602202fb39953c0d6189dd8bb8c69c7e9145a67fb535243fa91e8e82eb38d5edf767f"
    )

    # Test if return 9000
    try:
        cmd.provide_erc20_token_information(info=erc20_info)
    except:
        raise


def test_provide_erc20_token_goerli_with_t(cmd):
    erc20_info = ERC20Information(
        erc20_ticker=b"tUSDC".hex(),
        addr="0x79542cc915c2a19D1B00409C8B79E8E9E3bB4Bdc",
        nb_decimals=6,
        chainID=5,
        sign="304402202736a1fe050770aa00916f53d90bfee112eea5cb5ad139b8e8829d95cdbdf94602202fb39953c0d6189dd8bb8c69c7e9145a67fb535243fa91e8e82eb38d5edf767f"
    )

    # Test if return 9000
    try:
        cmd.provide_erc20_token_information(info=erc20_info)
    except:
        raise


def test_provide_erc20_token_goerli_valid_signature(cmd):
    erc20_info = ERC20Information(
        erc20_ticker=b"USDC".hex(),
        addr="0x79542cc915c2a19D1B00409C8B79E8E9E3bB4Bdc",
        nb_decimals=6,
        chainID=5,
        sign="30440220426f264508cc02682f8d216c3d6358d3d3b170714668c43a39528a1c83d30c9502203dae50943c13f537d98fcef343bb9a18314f4fb172938d96de5e6945529b3494"
    )

    # Test if return 9000
    try:
        cmd.provide_erc20_token_information(info=erc20_info)
    except:
        raise


def test_provide_erc20_token_goerli_with_t_valid_signature(cmd):
    erc20_info = ERC20Information(
        erc20_ticker=b"tUSDC".hex(),
        addr="0x79542cc915c2a19D1B00409C8B79E8E9E3bB4Bdc",
        nb_decimals=6,
        chainID=5,
        sign="30440220426f264508cc02682f8d216c3d6358d3d3b170714668c43a39528a1c83d30c9502203dae50943c13f537d98fcef343bb9a18314f4fb172938d96de5e6945529b3494"
    )

    # Test if return 9000
    try:
        cmd.provide_erc20_token_information(info=erc20_info)
    except:
        raise

def test_provide_erc20_token_error(cmd):
    erc20_info = ERC20Information(
        erc20_ticker="5a5258",
        addr="0xe41d2489571d322189246dafa5ebde1f4699f498",
        nb_decimals=18,
        chainID=1,
        sign="deadbeef"
    )

    with pytest.raises(ethereum_client.exception.errors.UnknownDeviceError) as error:
        cmd.provide_erc20_token_information(info=erc20_info)
        assert error.args[0] == '0x6a80'
