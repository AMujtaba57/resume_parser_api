
def certification_similarity(certifications, filter_w, query, certification_weightage_formula, keywords=None):
    keyword_list = ''
    certification_list = [certificate["name"] for certificate in certifications if certificate["name"].lower() in query.lower()]
    if keywords:
        keyword_list = [keys for keys in keywords if keys in certification_list]
    if not certification_list and certifications and keyword_list:
        weightage = filter_w * (certification_weightage_formula/ 100)
    elif certification_list:
        weightage = filter_w
    else:
        weightage = 0

    return weightage
