import PyPDF2

# Load resume PDF and extract text
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text.lower()

# Define keywords expected in resume (edit this list as needed)
keywords_required = [
    "python", "java", "c++", "html", "css", "javascript",
    "machine learning", "deep learning", "data analysis", 
    "sql", "django", "flask", "git", "problem solving"
]

# Check for keyword matches
def check_resume(resume_text, keywords):
    matches = []
    for keyword in keywords:
        if keyword in resume_text:
            matches.append(keyword)
    return matches

# Main
resume_path = "BB resume.pdf"  # change this to your file path

resume_text = extract_text_from_pdf(resume_path)
matched_keywords = check_resume(resume_text, keywords_required)
missing_keywords = list(set(keywords_required) - set(matched_keywords))
score = (len(matched_keywords) / len(keywords_required)) * 100

# Output results
print("✅ Resume Analysis Completed")
print("------------------------------")
print("Matched Keywords:", matched_keywords)
print("Missing Keywords:", missing_keywords)
print(f"Resume Score: {score:.2f}%")
