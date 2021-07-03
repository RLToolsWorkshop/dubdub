# DubDub

A toy programming language the group is writing in **Python**, **Rust**, then eventually **TVM**. The main goal of the language is to learn from the [interpreters book](https://www.craftinginterpreters.com/). By writing the language we'll increase our mean knowledge in data structures and symbolic programming.

This will make for a more effective programmer that will be able to execute on all further developments. In order to ensure we're running the code with consistency we'll enforce typing onto the codebase using a combination of dataclasses and pydantic.

By the end of the project, each person in the group that participates should have a strong understanding of the structure of languages. This, in fact, will improve every aspect of the data scientist's skill. Here's how:

1. Understand how frameworks work (including Jax & Pytorch).
2. Will be able to know how to construct complex recursive and stack-based applications.
3. Understanding transpiler technology (relavent to understand JAX and other tech)
4. Can better create environments and gyms that represent their problem set.
5. Will help with creating RL algorithms that require things like buffers or dataflows.


## Getting Started

Follow these instructions to get started.

### Pre-requisites

To ensure you have all of the right dependencies ensure to install:

1. Pyenv - Python version manager. It has an [autoinstaller](https://github.com/pyenv/pyenv-installer).
2. Poetry - This is the package manager we're using. It has [install instructions on its introduction page.](https://python-poetry.org/docs/)

### Install and Run Project

In order to run the project you have to install all of the dependencies. This might take some time at first. In the root folder run the command:

```bash
poetry install
```

Once done you have to activate the virtual environment:

```bash
poetry shell
```

There should be an indicator that looks a little like `dubdub/.venv/bin/activate` indicating that you're in the project.