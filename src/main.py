import sys
from ocr_module import *

def main():
    # write in the script to properly process the ocr to get the info 
    # from the tables and write the info to csvs

    if len(sys.argv) != 3:
        sys.exit('Usage: python main.py datasheet.pdf output_path')
    

if __name__ == '__main__':
    main()

