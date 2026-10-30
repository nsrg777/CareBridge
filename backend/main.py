from tinyfish_service import search_healthcare
from recovery_plan import generate_recovery_plan
from fastapi import FastAPI, UploadFile, File, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from document_processor import extract_text_from_pdf

app = FastAPI(
    title="CareBridge",
    description="AI-Powered Post-Discharge Recovery Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "Welcome to CareBridge!",
        "status": "Running successfully"
    }


@app.get("/health")
def health():

    return {"status": "healthy"}


@app.post("/upload-discharge-summary")
async def upload_discharge_summary(
    file: UploadFile = File(...)
):

    # Validate file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    # Read uploaded file
    file_bytes = await file.read()

    # Limit file size to 10 MB
    if len(file_bytes) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=413,
            detail="File size must be below 10 MB."
        )

    if not file_bytes:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    # Extract PDF text
    result = extract_text_from_pdf(file_bytes)

    if not result["success"]:
        raise HTTPException(
            status_code=422,
            detail=result["message"]
        )

    return {
        "message": "Discharge summary processed successfully!",
        "filename": file.filename,
        "extracted_text": result["text"]
    }
@app.post("/generate-recovery-plan")
async def generate_plan(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    file_bytes = await file.read()

    if len(file_bytes) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=413,
            detail="File exceeds 10 MB"
        )

    result = extract_text_from_pdf(file_bytes)

    if not result["success"]:
        raise HTTPException(
            status_code=422,
            detail=result["message"]
        )

    plan = generate_recovery_plan(result["text"])

    return {
        "message": "Recovery information extracted successfully",
        "recovery_plan": plan
    }
@app.get("/healthcare-resources")
def healthcare_resources(query: str):

    try:

        results = search_healthcare(query)

        return {
            "message": "Healthcare resources retrieved successfully",
            "query": query,
            "total_results": len(results),
            "resources": results
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )