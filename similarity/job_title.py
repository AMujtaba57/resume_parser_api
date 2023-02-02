import math


def job_title_similarity(data, _factor):
    _mean = 0
    _sum = 0
    main_title = data['jobTitle'].lower().split(" ")

    for i in range(0, len(data['experiences'])):
        experience_title = data["experiences"][i]["jobTitle"].lower().split(" ")
        score = len(set(main_title).intersection(set(experience_title)))
        _sum += score / len(main_title)
    return math.ceil(
            float("%.2f" % (_sum / len(data['experiences']))))
