from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal

# Parse Layout Function
def parse_layout(layout):
    """Function to recursively parse the layout tree."""
    for lt_obj in layout:
        print(lt_obj.__class__.__name__)
        print(lt_obj.bbox)
        if isinstance(lt_obj, LTTextBoxHorizontal) or isinstance(lt_obj, LTTextLine):
            print(lt_obj.get_text())
        elif isinstance(lt_obj, LTFigure):
            parse_layout(lt_obj)  # Recursive
# End of Function

# Open a PDF file
fp = open('pdftest.pdf', 'rb')
#fp = open('E-AdmitCard.pdf', 'rb')
# Create a PDF parser object associated with file object
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
document = PDFDocument(parser)
# Check if the documentallows text extraction. If not, abort.
if not document.is_extractable:
	raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Set parameter for Analysis
laparams = LAParams()
# Create Pdf device object
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
# Create a pdf interpreter object
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in document
for page in PDFPage.create_pages(document):
	interpreter.process_page(page)
	# Receive the LTPage object for the page
	layout = device.get_result()
	print(type(layout))
	parse_layout(layout)
#	for element in layout:
#		if isinstance(element, LTTextLineHorizontal):
#			print(element.get_text())
#outlines = document.get_outlines()
#for (level,title,dest,a,se) in outlines:
#	print(level, title)


#If you are interested in the location of individual LTChar objects, 
#you can recursively parse into the child layout objects of LTTextBox 
#and LTTextLine just like what is done with LTFigure in the above example.

