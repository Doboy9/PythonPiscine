# ft_package

ft_package is a simple Python package designed to count occurrences of a specific element in a list. It provides a lightweight utility function that is easy to integrate into your projects.

---

## Installation

1. Clone the repository or download the source code.
2. Build the package:
    ```bash
    python3 setup.py sdist bdist_wheel
    ```
3. Install the package locally:
    ```bash
    pip install dist/ft_package-0.0.1-py3-none-any.whl
    ```

---

## Usage

After installing, you can use the `count_in_list` function in your Python scripts.

### Example:

Create a Python script:

```python
from ft_package import count_in_list

# Test cases
print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0
```

Run the script:
```bash
python3 test_script.py
```

---

## Uninstallation

To uninstall the package after testing:
```bash
pip uninstall ft_package
```

---

## Development and Testing

1. **Verify Installation**:
    After installing, check the package details:
    ```bash
    pip show ft_package
    ```

    Expected output:
    ```
    Name: ft_package
    Version: 0.0.1
    Summary: A sample test package
    Home-page: https://github.com/eagle/ft_package
    Author: eagle
    Author-email: eagle@42.fr
    License: MIT
    Location: /path/to/your/package
    Requires:
    Required-by:
    ```

2. **Optional: Validate with `twine`**:
    Ensure your package meets Python Package Index (PyPI) standards:
    ```bash
    pip install twine
    twine check dist/*
    ```

---

## Metadata

- **Name**: ft_package
- **Version**: 0.0.1
- **Summary**: A sample test package
- **Author**: eagle
- **Author Email**: eagle@42.fr
- **License**: MIT
- **Home Page**: [GitHub Repository](https://github.com/eagle/ft_package)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/eagle/ft_package/issues) or submit a pull request.

---

## Acknowledgements

Special thanks to the Python community for their extensive documentation and support.

