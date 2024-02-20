import subprocess
import sys

run_snip = subprocess.run(['python', 'snip.py'], capture_output=True,
                          text=True)

if not run_snip.returncode == 0:
    sys.exit("Could not capture the selected area")

run_ocr = subprocess.run(['python', 'ocr.py'], capture_output=True,
                         text=True)

if not run_ocr.returncode == 0:
    sys.exit("Something went wrong in the OCR process")
