# Conventional Commits pre-commit hook

A [`pre-commit`](https://pre-commit.com) hook to check commit messages for [Conventional Commits](https://conventionalcommits.org) formatting.

## Usage
Add the following entry into your `.pre-commit-config.yaml` file:
```
repos:
  # - repo: ...

  - repo: https://github.com/igorhrcek/pre-commit-conventional-commits
    rev: v1.0.0
    hooks:
      - id: pre-commit-conventional-commits
        stages: [commit-msg]
        args: [] # optional: list of Conventional Commits types to allow e.g. [feat, fix, ci, chore, test]
```

Install the script:
```
pre-commit install --hook-type commit-msg
```
