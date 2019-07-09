py_library(
    name = "example_class",
    srcs = ["example_class.py"],
    visibility = ["//visibility:public"],
)

py_test(
    name = "example_class_test_first",
    srcs = ["example_class_test_first.py"],
    deps = [":example_class"],
    size = "small",
    python_version = "PY2",
)

py_test(
    name = "example_class_test_second",
    srcs = ["example_class_test_second.py"],
    deps = [":example_class"],
    size = "small",
    python_version = "PY2",
)

py_test(
    name = "example_class_test_third",
    srcs = ["example_class_test_third.py"],
    deps = [":example_class"],
    size = "small",
    python_version = "PY2",
)