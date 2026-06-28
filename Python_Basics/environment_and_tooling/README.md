# Environment and Tooling

When writing real-world Python applications, you will need to install external packages, manage project environments, and write code in suitable editors.

---

## 1. PIP (Package Installer for Python)

PIP is the standard package manager for Python. It allows you to download and install packages from PyPI (Python Package Index).

- **Check if PIP is installed:**
    ```bash
    pip --version
    ```
- **Install a package:**
    ```bash
    pip install package_name
    ```
- **List installed packages:**
    ```bash
    pip list
    ```
- **Uninstall a package:**
    ```bash
    pip uninstall package_name
    ```

---

## 2. VENV (Virtual Environments)

Virtual environments are self-contained directory trees that contain a copy of Python and standard tools, isolating your project dependencies from other projects on your computer.

### Step-by-Step Workflow

#### Step 1: Create the Virtual Environment

Navigate to your project directory in the terminal and run:

```bash
python -m venv myenv
```

#### Step 2: Activate the Virtual Environment

- **On Windows (PowerShell):**
    ```powershell
    .\myenv\Scripts\Activate.ps1
    ```
- **On macOS/Linux:**
    ```bash
    source myenv/bin/activate
    ```

#### Step 3: Install Packages and Deactivate

Once activated, any `pip install` commands run exclusively inside this environment. To exit, type:

```bash
deactivate
```

---

## 3. Dependency Management: `requirements.txt`

To share your project with others or deploy it, you need to document the packages it uses.

- **Generate `requirements.txt` (freeze current environment packages):**
    ```bash
    pip freeze > requirements.txt
    ```
- **Install dependencies from `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```

### Modern Standard: `pyproject.toml`

In modern Python packaging, `pyproject.toml` (defined in PEP 518) is the standardized configuration file for build tools, dependencies, and code formatter settings (like Black, Ruff, or Flake8).

---

## 4. Popular Python IDEs

To write Python code efficiently, it is recommended to use a dedicated Integrated Development Environment (IDE) or text editor:

1. **Visual Studio Code (VS Code)**: A lightweight, powerful editor with excellent Python support via the official Microsoft Python extension.
2. **PyCharm**: A full-featured IDE developed by JetBrains specifically for Python development.

---

## Further Reading

- [Official Python Docs — Installing Python Modules](https://docs.python.org/3/installing/index.html)
- [Official Python Docs — Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)
