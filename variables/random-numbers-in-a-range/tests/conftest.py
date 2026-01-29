import os
import sys

# Add the challenge directory to the path so we can import from paceCParser
challenge_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, challenge_dir)
