import re


def extract_exp(s):

    if s.endswith('.'):
        s = s[:-1]
    s = s.replace("(", "")
    s = s.replace(")", "")
    res = re.split(" ", s.lower())

    res = [i for i in res if i]

    for i in (0, len(res) - 1):
        if res[i].lower() == 'year':
            res[i] = 'years'
    try:
        data = ''
        years = None
        range = None
        flag = False
        if 'years' not in res:
            return "0 years"
        else:
            while res:
                if 'years' in res:
                    if flag == True:
                        data += " and "
                    years = res.index('years')
                    flag = True
                    if 'minimum' in res:
                        range = res.index('minimum')
                        if range < years:
                            data += ' '.join(map(str, res[range:years + 1]))
                    if 'least' in res:
                        range = res.index('least')
                        if range < years:
                            data += " at " + ' '.join(map(str, res[range:years + 1]))
                    if 'over' in res:
                        range = res.index('over')
                        if range < years:
                            data += ' '.join(map(str, res[range:years + 1]))
                    if 'maximum' in res:
                        range = res.index('maximum')
                        if range < years:
                            data += ' '.join(map(str, res[range:years + 1]))
                    if 'equal' in res:
                        range = res.index('equal')
                        if range < years:
                            data += ' '.join(map(str, res[range:years + 1]))
                    if 'most' in res:
                        range = res.index('most')
                        if range < years:
                            data += "at " + ' '.join(map(str, res[range:years + 1]))
                    if range is None:
                        data += ' '.join(map(str, res[years - 1:years + 1]))

                del res[:years + 1]
        return data

    except Exception as e:
        print(e)


def check_result(years, data):
    res = data.split(' ')
    flag = False
    if 'years' in res:
        year = res.index('years')
        num = float(res[year - 1])
        if 'minimum' in res or 'least' in res:
            if num <= years:
                flag = True
        if 'over' in res:
            if num < years:
                flag = True
        if 'maximum' in res or 'most' in res:
            if num >= years:
                flag = True
        if num == years:
            flag = True
    return flag
