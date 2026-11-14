# Agriculture Monte Carlo Engine

This agriculture-focused Monte Carlo engine allows users to run simulations on crop yields and soil sensor data, providing valuable insights into potential outcomes through the calculation of confidence intervals. Built from scratch in pure Python, this project prioritizes ease of use and customization. With comprehensive testing and documentation in place, users can trust the accuracy and reliability of their results.

## What makes it unique

Combines crop yield and soil sensor data with a Monte Carlo experiment runner with confidence intervals — a niche where few ready-made tools exist.

## Features

- **`agriculture_randomizer/core.py`** — Core Monte Carlo engine logic and data structures
- **`agriculture_randomizer/experiment.py`** — Monte Carlo experiment runner with confidence intervals
- **`agriculture_randomizer/data.py`** — Crop yield and soil sensor data handling and simulation
- **`agriculture_randomizer/utils.py`** — Helper functions for Monte Carlo engine operations
- **`agriculture_randomizer/tests_test_core.py`** — Unit tests for core Monte Carlo engine logic
- **`agriculture_randomizer/models.py`** — data classes for the domain objects

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/agriculture-randomizer.git
cd agriculture-randomizer

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
agriculture-randomizer/
├── agriculture_randomizer/
│   ├── core.py
│   ├── experiment.py
│   ├── data.py
│   ├── utils.py
│   ├── tests_test_core.py
│   ├── models.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **agriculture** · Archetype: **randomizer** ·
Built autonomously by JARVIS on 2026-11-14. MIT licensed.
