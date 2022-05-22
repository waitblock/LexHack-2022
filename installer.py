import subprocess
import sys

def install():
    with open('requirements.txt', 'r') as req:
        requirements = req.readlines()

    for r in requirements:
        requirements[requirements.index(r)] = r.replace('\n', '')

        subprocess.check_call([sys.executable, "-m", "pip", "install", r])