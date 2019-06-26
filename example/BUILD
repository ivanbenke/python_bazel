py_binary(
    name="example_class",
    srcs=["example_class.py"],
    python_version = "PY2",
)

py_test(
    name = "example_class_test",
    srcs = ["example_class_test.py"],
    deps = [":example_class"],
    size = "small",
    python_version = "PY2",
)