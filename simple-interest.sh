#!/bin/bash

echo "Enter the principal amount:"
read principal

echo "Enter the annual interest rate (in %):"
read rate

echo "Enter the time (in years):"
read time

interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)

echo "The simple interest is: $interest"
