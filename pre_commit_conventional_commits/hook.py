import re
import sys
import argparse

# Define default conventional types
CONVENTIONAL_TYPES = ["feat", "fix"]

# Define default types
DEFAULT_TYPES = [
    "build",
    "chore",
    "ci",
    "docs",
    "feat",
    "fix",
    "perf",
    "refactor",
    "revert",
    "style",
    "test",
]

RESULT_SUCCESS = 0
RESULT_FAIL = 1


def main(argv=[]):
    # Allow additiional params to be passed in configuration
    parser = argparse.ArgumentParser(
        prog="pre-commit-conventional-commits", description="Check a git commit message for Conventional Commits formatting."
    )
    parser.add_argument("types", type=str, nargs="*", default=DEFAULT_TYPES, help="Optional list of types to support")
    parser.add_argument("input", type=str, help="A file containing a git commit message")

    if len(argv) < 1:
        argv = sys.argv[1:]

    try:
        args = parser.parse_args(argv)
    except SystemExit:
        return RESULT_FAIL

    # Read the actual commit message
    with open(args.input, encoding="utf-8") as f:
        message = f.read()

    # Define the regex pattern for Conventional Commits
    pattern = r"^(\w+)(\(([\w\s-]+)\))?: ([\w\s-]+)$"

    # Check if the message matches the pattern
    if re.match(pattern, message):
        return RESULT_SUCCESS
    else:
        print("Your commit message is incorrect")


def regex_types(types):
    """
    Join types with the "|" to form or chain for regex
    """
    return "|".join(types)


def regex_scope():
    """
    Regex for an optional scope
    """
    return r"(\([\w \/:-]+\))?"


def regex_delimiter():
    """
    Regex string for colon and/or breaking change delimiter
    """
    return r"!?:"


def regex_subject():
    """
    Regex for body, footer and subject
    """
    return r" .+"


def convnetional_types_list(types=[]):
    """
    Returns a final list of Convetional Commits types that is merged from passed types and CONVENTIONAL_TYPES
    """

    if set(types) and set(CONVENTIONAL_TYPES) == set():
        return CONVENTIONAL_TYPES + types

    return types


def is_commit_conventional(input, types=DEFAULT_TYPES):
    """
    Checks if commit message follows Conventional Commits formatting.
    """

    types = convnetional_types_list(types)
    pattern = f"^({regex_types(types)}){regex_scope()}{regex_delimiter()}{regex_subject()}$"
    regex = re.compile(pattern, re.DOTALL)

    return bool(regex.match(input))


if __name__ == "__main__":
    raise SystemExit(main())
