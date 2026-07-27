# Contributing

This started as a personal learning project for practicing data structures and algorithms, but suggestions and improvements are welcome.

If you'd like to contribute:

1. Fork the repo and create a new branch for your change.
2. Make sure existing tests still pass:
   ```bash
   pip install pytest mypy --break-system-packages
   pytest -v
   mypy *.py
   ```
3. If you add or change behavior, add a test for it in `tests/`.
4. Open a pull request describing what changed and why.

For small fixes (typos, doc clarifications), feel free to open a PR directly without an issue first. For anything larger (new data structures, API changes), open an issue to discuss before doing the work.
