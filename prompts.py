from langchain_core.prompts import PromptTemplate

json_prompt = PromptTemplate.from_template("""
You are an AI Resume Screening System.

Return STRICT JSON:

{
  "score": number,
  "matched_skills": [],
  "missing_skills": [],
  "reason": ""
}

Resume:
{resume}

Job Description:
{jd}
""")