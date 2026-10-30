# CareBridge

### Your Companion Beyond Hospital Discharge

**Upload it. Understand it. Talk to it.**

CareBridge is an AI-assisted post-discharge recovery companion designed to help patients organize, understand, and manage their recovery journey after leaving the hospital.

It provides a centralized platform for managing discharge information, medication reminders, recovery milestones, healthcare resources, and daily recovery check-ins.

---

## 1. Problem Statement

Hospital discharge does not mean that a patient's recovery journey is complete.

After leaving the hospital, patients often receive lengthy discharge summaries containing medical instructions, medication schedules, follow-up appointments, and recovery guidelines.

However, patients and caregivers may struggle to understand these instructions, remember medications, track appointments, and monitor recovery progress.

This lack of organized post-discharge support can lead to confusion, missed medications, and difficulties managing recovery at home.

## 2. Our Solution

CareBridge bridges the gap between hospital discharge and home recovery through a centralized digital platform.

It helps patients organize discharge information, maintain medication schedules, track recovery milestones, explore healthcare resources, and record daily recovery progress.

The platform focuses on making post-discharge information more accessible and easier to manage.

---

## 3. Key Features

### 3.1 Discharge Summary Upload

* Upload hospital discharge summaries in PDF format.
* Extract text from uploaded documents.
* Process available discharge information for further organization.

### 3.2 Recovery Plan Generation

* Organize extracted discharge information into a structured recovery plan.
* Present available recovery instructions in a readable format.
* Help patients access important discharge information.

### 3.3 Medication Reminder

* Add prescribed medication names and dosages.
* Set medication reminder times.
* Mark medications as taken.
* Manage and delete medication entries.
* Browser-based notification support.

### 3.4 Recovery Timeline

* Add important recovery milestones.
* Schedule follow-up appointments.
* Add descriptions to recovery activities.
* Track milestones using upcoming and completed statuses.

### 3.5 Healthcare Resources

* Search for healthcare-related information.
* Retrieve external search results using the TinyFish integration.
* Display relevant resource titles, descriptions, and links.

### 3.6 Daily Recovery Check-in

* Record daily recovery status.
* Report symptoms and personal observations.
* Add additional recovery notes.
* Save and review previous check-ins.

---

## 4. Technology Stack

| Category                    | Technologies                 |
| --------------------------- | ---------------------------- |
| Frontend                    | React.js, Vite               |
| Styling                     | CSS                          |
| Backend                     | Python, FastAPI              |
| Document Processing         | PyMuPDF                      |
| External Search Integration | TinyFish Python SDK          |
| Database                    | SQLite (development backend) |
| Browser Storage             | LocalStorage                 |
| API Communication           | REST API                     |

---

## 5. System Architecture

CareBridge follows a frontend-backend architecture.

```text
                USER
                  |
                  v
          REACT FRONTEND
                  |
        ---------------------
        |         |         |
        v         v         v
     Upload    Medication  Recovery
     Document  Reminder    Timeline
        |
        v
      FASTAPI BACKEND
        |
   -------------------------
   |           |           |
   v           v           v
 PDF Text   Recovery    Healthcare
 Extraction  Plan       Resource Search
             Logic          |
                            v
                         TINYFISH
                            |
                            v
                    External Resources

        REACT FRONTEND
               |
               v
       LOCAL STORAGE
               |
        ----------------
        |              |
        v              v
    Check-ins      Medication &
                   Timeline Data
```

---

## 6. Project Workflow

1. The patient opens the CareBridge application.
2. The patient uploads a discharge summary in PDF format.
3. The backend extracts available text from the document.
4. The extracted information is organized into a recovery plan.
5. The patient adds medication reminders based on prescribed instructions.
6. Important recovery milestones and follow-up appointments are added to the timeline.
7. Patients can search for relevant healthcare resources through TinyFish.
8. Daily check-ins allow patients to record their recovery progress.
9. Previous check-ins can be reviewed through the application.

---

## 7. Project Structure

```text
CareBridge/
│
├── backend/
│   ├── main.py
│   ├── document_processor.py
│   ├── recovery_plan.py
│   ├── tinyfish_service.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── package.json
│   └── index.html
│
├── .gitignore
├── README.md
└── .env.example
```

*Note: The structure above represents the main project components. Additional files may be present in the actual implementation.*

---

## 8. Installation and Setup

### Prerequisites

Install the following:

* Python 3.10 or later
* Node.js and npm
* Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/CareBridge.git
```

```bash
cd CareBridge
```

### Step 2: Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Configure the required environment variables in a `.env` file in the project root.

Example:

```env
TINYFISH_API_KEY=your_api_key_here
```

Start the backend:

```bash
python -m uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### Step 3: Frontend Setup

Open another terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:5173
```

---

## 9. TinyFish Integration

CareBridge integrates TinyFish through its Python SDK to support the Healthcare Resources feature.

### How It Works

1. The user enters a healthcare-related search query.
2. The React frontend sends the query to the FastAPI backend.
3. The backend invokes the TinyFish search service.
4. TinyFish retrieves external search results.
5. The backend processes the returned titles, URLs, and descriptions.
6. The frontend displays the results to the user.

TinyFish is used for external resource discovery and does not perform medical diagnosis or make clinical decisions.

---

## 10. Future Enhancements

We aim to extend CareBridge with the following capabilities:

* Voice-based interaction for patients.
* AI-powered conversational recovery assistance.
* Caregiver dashboard for family members.
* Multilingual support for regional accessibility.
* Secure cloud-based patient data storage.
* Advanced medication notification support.
* Personalized recovery tracking based on verified clinical instructions.

---

## 11. Project Impact

CareBridge aims to make post-discharge recovery more organized and accessible by bringing important recovery information into one platform.

It supports patients in managing their discharge instructions, medication schedules, appointments, and daily recovery records.

By focusing on the transition from hospital to home, CareBridge addresses an important stage of the healthcare journey that often receives less attention.

---

## 12. Medical Disclaimer

CareBridge is an educational prototype designed to support the organization of post-discharge information.

It is not a substitute for professional medical advice, diagnosis, or treatment. Medication schedules, dosages, and recovery instructions must always be verified against the instructions provided by qualified healthcare professionals.

---

## 13. Contributors

Developed as a hackathon project.

**Project Name:** CareBridge

**Tagline:** Upload it. Understand it. Talk to it.

---

**CareBridge – Because recovery deserves support beyond hospital discharge.**
