#!/bin/bash

source venv/bin/activate

uvicorn relay.relay:app --host 0.0.0.0 --port 9000 &
uvicorn client.main:app --host 0.0.0.0 --port 8000
