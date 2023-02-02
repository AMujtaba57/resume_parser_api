from itertools import chain


def compare_job_title(data, _factors):
    """
    Get data
    """
    title = _factors["job_title"]["name"]
    f_title = title.split(' ')
    f_weightage = _factors["job_title"]["weightage"]
    avg_weightage = 0
    exp_str = []
    """
    compare each experience in data
    """
    for i in range(0, len(data["experiences"])):
        ex_title = data["experiences"][i]["jobTitle"].lower()
        exp_title = []
        expr_title = ex_title.split('/')
        for j in expr_title:
            j = j.split(' ')
            exp_title.append(j)
        expr_title = list(set(chain.from_iterable(exp_title)))

        weightage = 0
        if len(expr_title) <= len(f_title):
            assign_weightage = round(f_weightage / len(f_title),2)
            for t in f_title:
                if t in expr_title:
                    weightage += assign_weightage
            avg_weightage += weightage

        else:
            assign_weightage = round(f_weightage / len(expr_title),2)
            for t in expr_title:
                if t in f_title:
                    weightage += assign_weightage
            avg_weightage += weightage

    weightage = round(avg_weightage/2, 2)
    return weightage

