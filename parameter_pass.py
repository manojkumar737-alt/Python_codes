import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name', required=True, help="your name")
parser.add_argument('--age', type=int, default=18, help="your age")
args = parser.parse_args()
print(f"hello, {args.name}. age:{args.age}")

'''python3 .\script.py --name "Manoj" --age 28'''