# python_bazel

An example to familiarize myself with building with Bazel, more specifically, building and testing Python scripts with Bazel.


To run all tests in a package use: bazel test $(bazel query 'kind(test, deps(//example:all))').

This command functions properly on the condition that the test scripts contain "test" in their names and that the BUILD script contains "py_test(...)" for each test script.
