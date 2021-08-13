pragma solidity 0.8.7;

contract Impl {
	function shouldThrow (uint256 greaterThanTen) public pure {
		require(greaterThanTen > 10, "Number not greater than 10");
	}
}