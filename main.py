import subprocess
import pyperclip
import sys

run_snip = subprocess.run(['python', 'snip.py'], capture_output=True,
                          text=True)

if not run_snip.returncode == 0:
    sys.exit("Could not capture the selected area")

run_ocr = subprocess.run(['python', 'ocr.py', 'ss.png'], capture_output=True,
                         text=True)

if not run_ocr.returncode == 0:
    sys.exit("Something went wrong in the OCR process")

# Now that we have the text from tesseract place it in users clipboard
pyperclip.copy(run_ocr.stdout)
