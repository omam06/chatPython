def summarise_amounts(raw_values):
    total = 0          #Defect1 - rejected not initialized
    rejected = 0
    for raw in raw_values:
        try:
           # total += int(raw)   #2 - total will catch even -3 
            num = int(raw)
            if num >= 0:
                total += num          #ool increase total by 1
            else:
                rejected += 1
        except ValueError:       #catch expected error, not bare excpt co its risky
            rejected += 1

    return {'total': total, 'rejected': rejected} #3 - rejected hardcoded to 0
print(summarise_amounts(["10", ' 5 ', 'bad', '-3', '0', ""]))

assert summarise_amounts(["10", ' 5 ', 'bad', '-3', '0', ""]) == {'total': 15, 'rejected': 3}, 'Mixed example failed'
assert summarise_amounts([]) == {'total': 0, 'rejected': 0}, 'Empty list didnt work as expected'
assert summarise_amounts(['gyd', '', 'tyuyh']) == {'total': 0, 'rejected': 3}, 'All rejected inputs not correct'
assert summarise_amounts([0]) == {'total': 0, 'rejected': 0}, 'Valid zero bugging'