from brownie import Mock, accounts, reverts

ERR_MSG = "Number not greater than 10"

def test_shouldThrow():
	mock = Mock.deploy({ 'from': accounts[0] })
	with reverts(ERR_MSG):
		mock.testShouldThrow(1)


def test_shouldThrowWithoutWithStatement():
	mock = Mock.deploy({ 'from': accounts[0] })
	mock.testShouldThrow(1)
