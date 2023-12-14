# myapp
The myapp is generic python console application.

---
## Command
- myapp run --command empdata --date YYYYMMDD
- myapp email --command empdata --date YYYYMMDD
- myapp cleanup --command empdata --date YYYYMMDD
---
## Build
- python setup.py bdist_wheel
- python -m pip uninstall myapp
- python -m pip install dist/myapp-1.0.0-py3-none-any.whl
- python -m pip install --upgrade --force-reinstall --no-deps --target $HOME/.local/lib/python3.12/site_packages/ dist/myapp-1.0.0-py3-none-any.whl
--- 
