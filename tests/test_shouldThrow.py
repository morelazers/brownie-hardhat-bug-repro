from brownie import Impl, accounts, reverts

ERR_MSG = "Number not greater than 10"

def test_shouldThrow():
	impl = Impl.deploy({ 'from': accounts[0] })
	with reverts(ERR_MSG):
		impl.shouldThrow(1)


def test_shouldThrowWithoutWithStatement():
	impl = Impl.deploy({ 'from': accounts[0] })
	impl.shouldThrow(1)
