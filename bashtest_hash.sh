#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle hash_functions.py
assert_no_stdout
run test_style pycodestyle hash_tables.py
assert_no_stdout
run test_style pycodestyle test_hash.py
assert_no_stdout