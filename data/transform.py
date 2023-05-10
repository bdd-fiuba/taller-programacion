from json import loads as json_loads, dumps as json_dumps


def iterador_tweets():
    with open("tweets.json", "r", encoding="utf-8") as f:
        yield from (json_loads(l) for l in f)


def fix_dollar_signs(d):
    return {
        k.replace("$", ""): (v if not isinstance(v, dict) else fix_dollar_signs(v))
        for k, v in d.items()
    }

def change_created_at(d):
    d['created_at'] = d['created_at']['date']
    return d

def remove_id_str_in_retweeted_status(d):
    retw = d['retweeted_status']
    if retw is not None:
        retw['id'] = retw['id_str']
        del retw['id_str']
    return d

def main():
    with open('out.json', 'w', encoding='utf-8') as f:
        for tweet in iterador_tweets():
            if tweet['place'] is not None:
                place = tweet['place']
                if '_id' in place:
                    place['id'] = place['_id']
                    del place['_id']
            f.write(json_dumps(tweet) + '\n')
        

if __name__ == "__main__":
    main()
