import ticketpy
from tok import secret
import pprint

token = secret()
tm_client = ticketpy.ApiClient(token)
pp = pprint.PrettyPrinter(indent=4)

def tm_api(*args):
    # dictionary keys of argument are the fields we care about
    print(args)
    argument = {}
    argument['startDateTime'] = args[0] + 'T00:00:00Z'
    argument['city'] = args[1]
    argument['keyword']  = args[2]
    argument['radius'] = args[3]
    
    # do something like this...
    # argument["city"] =
    # hardcoded example:
##    argument['city'] = 'San Francisco'
##    argument['startDateTime'] = '2019-12-21T00:00:00Z'
##    argument['keyword'] = 'Sports'
##    argument['radius']  = 50

    print(argument)

    pages = tm_client.events.find(**argument)

    dicts = []
    for page in pages:
        for event in page:
            # pp.pprint(event.json)
            # populate this dictionary with info from the search
            if event.json['name'] and event.json['url'] and \
               event.json['dates']['start']['dateTime'] and \
               event.json['images'][0]:
                dct = {}
                dct['name'] = event.json['name']
                dct['url'] = event.json['url']
                date_time_str = event.json['dates']['start']['dateTime']
                dct['date'] = date_time_str[:date_time_str.index('T')]
                dct['time'] = date_time_str[date_time_str.index('T') +  1:]
                dct['image'] = event.json['images'][0]['url']
            #dct['address'] = event.json['_embedded']['venues'][0]  \
            #                 ['address']['line1']
            #dct['venue name'] = event.json['_embedded']['venues'][0]  \
            #                 ['name']
                #print(dct)
                dicts.append(dct)
            if len(dicts) >= 10:
                break
        break
    #print(dicts)
    return dicts





