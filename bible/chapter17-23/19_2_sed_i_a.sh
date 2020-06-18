#!/bin/bash

echo "1.test i - insert"

echo "Test Line 2" | sed 'i\Test Line 1'

echo "1.test a - append"

echo "Test Line 2" | sed 'a\Test Line 1'
