```
python -m venv arcenv
source arcenv/bin/activate
pip install -r requirements.txt
```

```
poetry config http-basic.pypi __token__ <your_pypi_token>
OR
poetry config pypi-token.pypi <your-api-token>
```

```
pip install poetry
poetry new arcplot # for creating desired package structure
poetry init # to initialize package
poetry install # to install dependencies
poetry build # to build pacakge
poetry publish # to publish package
```

```
# if encountering following error on Debian based Linux: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
# the problem might be missing tkinter dependencies, try:
sudo apt-get install python3-tk
```