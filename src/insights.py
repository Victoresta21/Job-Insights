from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_types = set()
    for job_type in jobs_list:
        jobs_types.add(job_type["job_type"])
    return list(jobs_types)


def filter_by_job_type(jobs, job_type):
    job_job_type = list()
    for type in jobs:
        if type["job_type"] == job_type:
            job_job_type.append(type)
    return job_job_type


def get_unique_industries(path):
    jobs_read = read(path)
    jobs_industry = set()
    for job_industry in jobs_read:
        if len(job_industry["industry"]) != 0:
            jobs_industry.add(job_industry["industry"])
    return list(jobs_industry)


def filter_by_industry(jobs, industry):
    job_industry = list()
    for job in jobs:
        if job["industry"] == industry:
            job_industry.append(job)
    return job_industry


def get_max_salary(path):
    jobs_read = read(path)
    max_salaries = list()
    for job_max_salary in jobs_read:
        if len(job_max_salary['max_salary']) != 0 and \
                job_max_salary['max_salary'] != "invalid":
            max_salaries.append(int(job_max_salary["max_salary"]))
    max_salary = max(max_salaries)
    return max_salary


def get_min_salary(path):
    jobs_read = read(path)
    min_salaries = list()
    for job_min_salary in jobs_read:
        if len(job_min_salary['min_salary']) != 0 and \
                job_min_salary['min_salary'] != "invalid":
            min_salaries.append(int(job_min_salary["min_salary"]))
    min_salary = min(min_salaries)
    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
