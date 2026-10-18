# import fitz # install pumypdf <The `fitz` API is deprecated>
import pymupdf 

# Open the PDF file
pdf_document = "pythonbook.pdf"  # Replace with your file
doc = pymupdf.open(pdf_document)

# Extract text and save it to a file
with open("output.txt", "w", encoding="utf-8") as fhand:
   for page in doc:
       fhand.write(page.get_text())
       fhand.write("\n" + "-"*80 + "\n")  # Add separator between pages

print("PDF converted to text successfully!")


count = 0
with open("output.txt", "r", encoding="utf-8") as fhand:
    for line in fhand:
        cleaned_line = line.strip()
        if cleaned_line.startswith('Exercise'):
            print(cleaned_line)
            count = count + 1
        
print(f"Total exercises found: {count}")
    

        



































