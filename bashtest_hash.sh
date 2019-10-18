#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle hash_functions.py
assert_no_stdout
run test_style pycodestyle hash_tables.py
assert_no_stdout
run test_style pycodestyle unittest_hash_functions.py
assert_no_stdout
run test_style pycodestyle scatter.py
assert_no_stdout

run test_hash_functions python hash_functions.py --input rand_words.txt --hash_method ascii
assert_exit_code 0
run test_hash_functions python hash_functions.py --input non_rand_words.txt --hash_method ascii
assert_exit_code 0
run test_hash_functions python hash_functions.py --input rand_words.txt --hash_method rolling
assert_exit_code 0
run test_hash_functions python hash_functions.py --input non_rand_words.txt --hash_method rolling
assert_exit_code 0

run bad_input python hash_functions.py --input none.txt --hash_method ascii
assert_exit_code 1
assert_stdout "Failure to open file"
run bad_input python hash_functions.py --input _rand_words.txt --hash_method _ascii
assert_exit_code 1
assert_stdout "Invalid Hash Method"
run bad_input python hash_tables.py --size 10000 --hash_method rolling --collision_strategy linear --input _rand_words.txt --key_nums 1000 --search_nums 100
assert_exit_code 1
assert_no_stdout

for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method rolling --collision_strategy linear --input rand_words.txt --key_nums $M --search_nums 100 > test_rolling_linear_rand.$M.txt
done

grep add test_rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file rolling_linear_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file rolling_linear_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt

for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method ascii --collision_strategy linear --input rand_words.txt --key_nums $M --search_nums 100 > test_ascii_linear_rand.$M.txt
done

grep add test_ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file ascii_linear_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file ascii_linear_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt

for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method rolling --collision_strategy chain --input rand_words.txt --key_nums $M --search_nums 100 > test_rolling_chain_rand.$M.txt
done

grep add test_rolling_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file rolling_chain_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_rolling_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file rolling_chain_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt

for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method ascii --collision_strategy chain --input rand_words.txt --key_nums $M --search_nums 100 > test_ascii_chain_rand.$M.txt
done

grep add test_ascii_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file ascii_chain_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_ascii_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file ascii_chain_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt

python hash_functions.py --input rand_words.txt --hash_method ascii | python scatter.py --out_file ascii_hash_function_rand.png --x_label "Hashed Word" --y_label "Hashed Value"

python hash_functions.py --input non_rand_words.txt --hash_method ascii | python scatter.py --out_file ascii_hash_function_non_rand.png --x_label "Hashed Word" --y_label "Hashed Value"

python hash_functions.py --input rand_words.txt --hash_method rolling | python scatter.py --out_file rolling_hash_function_rand.png --x_label "Hashed Word" --y_label "Hashed Value"

python hash_functions.py --input non_rand_words.txt --hash_method rolling | python scatter.py --out_file rolling_hash_function_non_rand.png --x_label "Hashed Word" --y_label "Hashed Value"

for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method rolling --collision_strategy linear --input rand_words.txt --key_nums $M --search_nums 100 > test_rolling_linear_rand.$M.txt
done
grep add test_rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file rolling_linear_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file rolling_linear_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt

for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method ascii --collision_strategy linear --input rand_words.txt --key_nums $M --search_nums 100 > test_ascii_linear_rand.$M.txt
done
grep add test_ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file ascii_linear_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file ascii_linear_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt

for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method rolling --collision_strategy chain --input rand_words.txt --key_nums $M --search_nums 100 > test_rolling_chain_rand.$M.txt
done
grep add test_rolling_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file rolling_chain_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_rolling_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file rolling_chain_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt

for M in $(seq 1000 1000 10000); do
    python hash_tables.py --size 10000 --hash_method ascii --collision_strategy chain --input rand_words.txt --key_nums $M --search_nums 100 > test_ascii_chain_rand.$M.txt
done
grep add test_ascii_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file ascii_chain_add_time.png --x_label "Load Factor" --y_label "Insert Time"
grep search test_ascii_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file ascii_chain_search_time.png --x_label "Load Factor" --y_label "Search Time"
rm test_*.txt