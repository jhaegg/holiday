from datetime import datetime

def _match(date, rule):
    date_time = datetime.strptime(date, "%Y-%m-%d")
    result = True
    if 'yearly' in rule:
        result &= _yearly(date_time, rule['yearly'])

    return result

def _yearly(date, rule):
    rule_time = datetime.strptime(rule, "%Y-%m-%d")
    return date.day == rule_time.day and date.month == rule_time.month
