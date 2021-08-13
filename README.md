# Brownie Hardhat Bug Reproduction

To reproduce the bug (assumes Yarn and Brownie are installed):

```
yarn
brownie test
brownie test --network hardhat
```

You should see that with the first instance of `brownie test`, one of the tests succeeds (as expected).

With `brownie test --network hardhat`, both tests fail.
