import subprocess
import sys
from pip._internal.operations import freeze

def install():
    with open('requirements.txt', 'r') as req:
        requirements = req.readlines()
    
    # installed = freeze.freeze()

    for r in requirements:
        subprocess.check_call([sys.executable, "-m", "pip", "install", r])
        # subprocess.Popen([sys.executable, "-m", "pip", "install", r], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

    #     for i in installed:
    #         if r in i:
    #             pass
    #         else:
    #             requirements[requirements.index(r)] = r.replace('\n', '')
    #             subprocess.check_call([sys.executable, "-m", "pip", "install", r])