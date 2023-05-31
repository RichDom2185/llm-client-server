# llm-client-server

Testing the client-server model for LLM integration into apps. Ideally, this would be LLM-agnostic.

## Setup

### Python version

Use the version of python specified in the `.tool-versions` file.

### Recommended: Using virtual environments

Install `virtualenv` if you have not done so:

```bash
pip install virtualenv
```

Create a virtual environment:

```bash
virtualenv llm-env
```

Activate the virtual environment:

* On Mac/Linux:

    ```bash
    source llm-env/bin/activate
    ```

* On Windows:

    ```cmd
    llm-env\Scripts\activate
    ```

### Installing required packages

For convenience, the required packages are listed in the `requirements.txt` file. To install them, run:

```bash
pip install -r requirements.txt
```
