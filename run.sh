#!/bin/bash

# Script to run all test cases in casos_teste_v3 directory

echo "Running all test cases from casos_teste_v3..."
echo "=============================================="

# Loop through all .txt files in casos_teste_v3 directory
for test_file in casos_teste_v3/*.txt; do
    # Extract the filename without path
    filename=$(basename "$test_file")
    # Create output filename
    output_file="output_${filename}"
    
    echo ""
    echo "Running test: $filename"
    echo "Output will be saved to: $output_file"
    
    # Run the Python script with the test case
    python3 trab1.py "$test_file" "$output_file"
    
    if [ $? -eq 0 ]; then
        echo "✓ Test $filename completed successfully"
    else
        echo "✗ Test $filename failed"
    fi
done

echo ""
echo "=============================================="
echo "All tests completed!"