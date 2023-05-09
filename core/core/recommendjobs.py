def recommend_jobs(candidate_skills, job_opportunities):
    # Create a list of dictionaries to store the job titles, number of matching skills, matching skills, and additional job information
    matching_jobs = []
    
    # Iterate through each job opportunity and count the number of matching skills
    for job in job_opportunities:
        job_skills = job['company_skills']
        matching = list(set(candidate_skills).intersection(job_skills))
        missing = list(set(job_skills).difference(candidate_skills))
        matching_jobs.append({
            'title': job['job_title'],
            'matching_skills': matching,
            'missing_skills': missing,
            'company_name': job['company_name'],
            'location': job['location'],
            'avg_base_pay_est': job['avg_base_pay_est'],
            'company_rating': job['company_rating'],
            'company_link': job['company_link'],
            'time_since_posted': job['time_since_posted'],
            'company_skills': job['company_skills']
        })
    
    # Sort the jobs based on the number of matching skills in descending order
    sorted_jobs = sorted(matching_jobs, key=lambda x: (len(x['matching_skills']), -len(x['missing_skills'])), reverse=True)
    
    return sorted_jobs