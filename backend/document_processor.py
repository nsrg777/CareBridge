import fitz


def extract_text_from_pdf(file_bytes):

    try:
        # Open PDF from uploaded bytes
        pdf = fitz.open(
            stream=file_bytes,
            filetype="pdf"
        )

        extracted_text = ""

        # Extract text from every page
        for page in pdf:

            text = page.get_text()

            extracted_text += text + "\n"

        pdf.close()

        if not extracted_text.strip():
            return {
                "success": False,
                "message": "No readable text found. This PDF may be scanned."
            }

        return {
            "success": True,
            "text": extracted_text
        }

    except Exception:
        return {
            "success": False,
            "message": "Unable to read this PDF."
        }