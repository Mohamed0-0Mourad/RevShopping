import requests

def access_dict(analysis: dict, key: str, value: int):
    try:   
        analysis[key] += value
    except KeyError: 
        analysis[key] = value  

def assign_scr(score: int, negatives: set, sent:str, words:set, drop:set, analysis:dict):
    if score >= 7:
        for ne in negatives:
            if ne not in sent:
                for pos in words:
                    if pos in drop:
                        continue
                    else:
                        access_dict(analysis, pos, 1)
            else:
                for neg in words:
                    if neg in drop:
                        continue
                    else:
                        access_dict(analysis, neg, -1.5)

    elif score >= 4:
        for ne in negatives:
            if ne not in sent:
                for pos in words:
                    if pos in drop:
                        continue
                    else:
                        access_dict(analysis, pos, 0.25)
            else:
                for neg in words:
                    if neg in drop:
                        continue
                    else:
                        access_dict(analysis, neg, -0.25)
    elif score >= 0 :
        for ne in negatives:
            if 'but' in sent:
                for pos in words:
                    if pos in drop:
                        continue
                    else:
                        access_dict(analysis, pos, 1.5)
            else:
                for neg in words:
                    if neg in drop:
                        continue
                    else:
                        access_dict(analysis, neg, -1)


def analys(js2dict: dict) -> dict:           # -----------------------------------------> MAAAAAINNN
    analysis = dict()
    while True:
        reviews = js2dict['reviews']

        # scores = []
        drop = {'he', 'had', 'not', 'and', 'a', 'the', 'you', 'have',"i'm", 'this', 'these', 'that', 'so', 'be', 'am', 'on', 'is', 'to', 'i', 'my', 'me', 'it', 'of', 'in', 'for', 'was', "hate", "dislike", 'but', 'do', 'not', "don't", 'like', 'love', 'greates', 'fan', 'myself', 'from', 'one', 'few', 'diffrent', 'thing', 'things', '', 'any', "can't", 'see', 'at', 'it'}
        negatives = {"hate", "dislike", 'but',"i don't like", "i do not like"}

        for rev in reviews:
            score = rev['score']
            # scores.append(score)
            txt = rev['extract'].lower().split('.')
            for sent in txt:
                words = sent.split(" ")
                assign_scr(score, negatives, sent, words, drop, analysis)
                                      
        try:
            link = js2dict['next-page-url']
            r2 = requests.get(link)
            js2dict = r2.json()
        except KeyError:
            break
    return analysis