#!/bin/bash

poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 9000
