from chains.pipeline import run_pipeline

jd = "Looking for Data Scientist with Python, ML, SQL"

resume = "2 years experience. Python and SQL."

result = run_pipeline(resume, jd)

print(result)