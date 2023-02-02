from datetime import datetime
from dateutil.relativedelta import relativedelta


def req_to_list(data):
    from parser.matcher import apply_preprocess
    """
    Convert Dates from request TO
    List of (startDate, endDate)
    """

    exp_dates_list = []
    titles = []
    skills_data = []
    for ex in data["experiences"]:
        startDate = ex["startDate"]
        endDate = ex["endDate"]
        description = ex['description']
        skills = apply_preprocess(description)
        skills_data.append(skills)

        if endDate == 'Present':
            endDate = datetime.now().date()
            endDate = f'{endDate.day}/{endDate.month}/{endDate.year}'
        exp_dates_list.append((startDate, endDate))
        titles.append(ex["jobTitle"])

    return exp_dates_list, titles, skills_data


def dates_to_experience(exp_dates_list, titles):
    """
    Takes list of start and end dates (Generated by `~Exp.req_to_list`) and calculate experience
    """
    # initializing total_exp i.e. creating empty relativedelta with Y=0, M=0 D=0
    total_exp = relativedelta()

    exp_list = {}

    i = 0
    for startDate, endDate in exp_dates_list:
        start = datetime.strptime(startDate, "%d/%m/%Y")
        end = datetime.strptime(endDate, "%d/%m/%Y")
        # Get the interval between two dates
        diff = relativedelta(end, start)
        total_exp = total_exp + diff

        if titles[i] in exp_list:
            exp_list[titles[i]] += diff
        else:
            exp_list[titles[i]] = diff
        i += 1

    return total_exp, exp_list


def exp_correction(exp):
    """
    Takes the exp in relativedelta and return in experience in years.
    Parameters:
        exp (relativedelta): Experience in relativedelta
    Returns:
        new_years(float): return the experience calculated in years.
    """

    years = exp.years
    months = (exp.months,)
    days = exp.days

    new_months = months[0] + days // 30

    new_years = years + new_months // 12

    new_months = new_months % 12

    new_years = new_years + round(new_months / 12, 1)

    return new_years


def get_total_experience(request_query: dict):
    """
    Takes request query (dict) and return total experience.

    Parameters:
        request_query (dict): Request data containing experience information.

    Returns:
        Total experience (float): containing total experience in years
        Relative experience (dict): job titles with respective experience and skills
    """
    if not isinstance(request_query, dict):
        raise AssertionError("input must be dict object")
    x = req_to_list(request_query)

    exp, exp_list = dates_to_experience(x[0], x[1])
    extracted_skills = x[2]

    final_exp = exp_correction(exp)
    for index, job_title in enumerate(exp_list):
        value = {
            'experience': exp_correction(exp_list[job_title]),
            'skills': extracted_skills[index]
        }
        exp_list[job_title] = value

    return final_exp, exp_list
