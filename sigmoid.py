

def icecream(score,day,temp,match,weather):d
    if day == "saturday" or "sat":
        score == 0

    elif temp > 30:
        score += 4

    elif match == True:
        score += 3

    elif weather == "rain":
        score -= 5

    if score >= 2:
        return score," busy day"
    else:
        return score," slow day"


print(icecream(3,"sat",40,True,"rain"))