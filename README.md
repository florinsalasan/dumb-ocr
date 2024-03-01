# Snip to Clipboard

Turn's out this is a built in functionality of macOS, but the idea is a snipping
tool that then extracts the text and pastes it into your clipboard to be 
pasted into whatever you want. Comes in 3 separate python scripts.\

# snip.py
Creates a fullscreen overlay that allows a user to click and drag to create
a rectangular area that is then snipped and saved to 'ss.png' in the same 
directory as the repo by default.

# ocr.py 
Called with an image that is a valid format type such as png, jpg, or bmp
and then extracts the text with pytesseract and copies the extracted text
to your clipboard.

# main.py
Is a script that uses the functionality of both of the other scripts together
to make the process slightly less tedious, creates the overlay, waits for the
user to select the area, then does the text extraction and copying to 
clipboard in one script.

## Notes:

This has only been tested on macOS and I do not plan on testing on other
platforms mostly because of lack of access to the other platforms.\
Secondly there is a vertical offset in the snip.py script due to weird 
pixel location caused by the notch on my machine. Feel free to remove the
offsets if you have a normal rectangular screen, or if they are not needed
for your use case.

## TODO:

- [] Implement multi monitor usage, currently only works on main monitor\
- [] Allow for more complex ocr, only really tested this on typed content so far\
- [x] Remove the overlaid white canvas on the selected area before generating the screen grab\
- [x] Do something with the extracted text that is more than printing to console, copying to clipboard could be a good start\
- [x] Ensure that the overlay is properly anchored in the top left and covering the entire screen\
- [] Live update the selected area? Unsure if needed or viable but highlighting the current selection would be neat.
