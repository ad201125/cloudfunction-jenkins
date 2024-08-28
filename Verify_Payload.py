import argparse
import json

def verify_payload(expected_file, actual_file):
    with open(expected_file, 'r') as file:
        expected = json.load(file)
    with open(actual_file, 'r') as file:
        actual = json.load(file)
    
    if expected == actual:
        print("Payloads match!")
    else:
        print("Payloads do not match!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--expected_output', required=True)
    parser.add_argument('--actual_output', required=True)
    args = parser.parse_args()

    verify_payload(args.expected_output, args.actual_output)

if __name__ == '__main__':
    main()
