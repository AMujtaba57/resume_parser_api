from api.models import QueryIndustryDataset


def load_dataset():
    model = QueryIndustryDataset.objects.all()
    return model


def industry_classifer(query_industry, resume_industry):
    if len(query_industry) > 0 and len(resume_industry) > 0:
        industry = query_industry.intersection(resume_industry)
        if industry:
            return list(industry)[0]
        else:
            return list(resume_industry)[0]
    elif len(query_industry) == 0 and len(resume_industry) != 0:
        return list(resume_industry)[0]
    elif len(query_industry) != 0 and len(resume_industry) == 0:
        return list(query_industry)[0]
    else:
        return ''
