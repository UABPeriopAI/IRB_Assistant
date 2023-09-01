#!/bin/bash

cd /workspaces/IRB_Assistant/src
pip install --upgrade pip setuptools wheel\
	    && pip install -e ".[dev]"
