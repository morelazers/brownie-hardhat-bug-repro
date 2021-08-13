pragma solidity 0.8.7;

import "./impl.sol";

contract Mock is Impl {
	function testShouldThrow (uint256 greaterThanTen) public pure {
		shouldThrow(greaterThanTen);
	}
}