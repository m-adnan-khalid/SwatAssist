import http.client
import json

conn = http.client.HTTPSConnection("vroozi.zendesk.com")
payload = ''
headers = {
    'authority': 'vroozi.zendesk.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_zendesk_cookie=BAhJIkp7ImRldmljZV90b2tlbnMiOnsiNDAzMjUxODEwNzkxIjoiZDFtVmg3ZXBsTEFuSXhKNGF3ZDVGa1pMRllJd1JIbUMifX0GOgZFVA%3D%3D--e154ab85294732354c146bfc68cb6d245afca09c; _pendo_accountId.df3d609f-14a9-4a77-b441-73602a4aaab2=157286; ajs_group_id=157286; bime_subdomain=vroozi; ajs_group_id=157286; __cfruid=a30331f1aee79e68d39422fdc33debf46ae8eef8-1678692686; _zendesk_authenticated=1; _zdsession_app-market=ba0585dfd4ea5a0ce297e0c50d3b30da; _pendo_guides_blocked.df3d609f-14a9-4a77-b441-73602a4aaab2=0; _zdsession_zendesk-proxy=53f8d8859e3329b9737a3b66d379f271; _bimeio_session=8%2BawndDFyV4Q1B4ooIQWkJhmO%2BO9sSuAu%2FLvNKvs%2F8ZxuoXVar%2FvUWD9rYDvpLnvJpjOJKgexcjoxK48GZ5FyRUDYLOYoq6FjObBtGAmCjG8wUT42kOi%2BPXXQhBypjLWwAb1ewoK7FhH5cyaX06zMj%2BsloGchKJsMo3rvGnq8V7dIjyk2tohwJIGNJiBxUNYwvi1ROOP7Ffj%2B18bTfy7upG0gPF678tXfufu1nppto0S6Rzk6S%2FJdylhDlK71ng%3D--sP152AAtgSSwQum4--nLwhAjD9NN8sD3%2F0tU0RtQ%3D%3D; _ga=GA1.2.792868533.1670926716; _gid=GA1.2.1577258913.1678693476; _ga_GX4ZE3WYYT=GS1.1.1678693476.4.0.1678693502.0.0.0; ajs_user_id=403251810791; ajs_anonymous_id=82eac05f-9a77-4361-9e43-f69d49402649; _pendo_visitorId.df3d609f-14a9-4a77-b441-73602a4aaab2=403251810791; _pendo_meta.df3d609f-14a9-4a77-b441-73602a4aaab2=2306805523; __cf_bm=YNXD3xRWm0tn8eXPILC7utAVzJcRWYDWUrtxfkMYlTg-1678693642-0-AXmKEdwg7GJTV67dJgXq+HkkdL0B05N8VTTNenkTAFihB+HN4YrUWZstJEC+6RUKOz+akcoVUfW0YM/cemvsxD18cnDoMRhlzBWDnkUdmtvA; __cfruid=d385060bc3f551ed46ca54d75b6475f8008605c8-1678693642; _zendesk_shared_session=-S0k5aG5iY3pSRlVUQjNFa29zUWE5RkNzMG1zSzAwS3NWTkYxSDMwL2lyNlA5eFlaR1AraFNndjRaYUlxQ1YvMU1yWkxTdW9pUHNxdENVbEpIS1NjQlNUZjdUZnF3T1ZTc1kzdGs3K1B6OStSVjNLdXVXeVhsV2lRUUxqeW02NHYtLXQ5dUtUVkJvSHRYdHdiSmFhM0tvZFE9PQ%3D%3D--a44bd77f8c2dc9c8097258f7a00d976a21111f2c; _app_market_session=dEZkVmJuUmNKYXlGRXFralYrWUFmR3ZWNlRhUVRRd1NrbzdBRlFlTmJVNTlKV1BWTXhRUVpPaUhxbDd2dEpWVFNFOFdtb3dPSGVaV0ZqR1JRb2FFcTVkWlpMR1dNU3IxT3FzZWRFdFlsc0hhTkN3U0dHNFRaSCthZW10YWtiOUVXVkRRbllsWmNyN0swWVVHN0VKVndnPT0tLXQvQUg4RlpNMG5vSzgrZDBHMzhPM1E9PQ%3D%3D--9fd38c0214d3ffc62f3472daf53eef40734ed7ee; _help_center_session=SzIzdU1TWVcxV0FrajE1bWl0VVE4VkhkM2FpaDJNTnQ4bVpTVmxYY2tlMjZrRUFqV25LTytNR2FxSm16eE5IQXBiVGtYNDh0cGdTQkkrSU5jUmp6S1FVNWRNU00rQ0h6M0tITWVkalYyTUVqS2JHRURQUno3WDl5MFZNYUlrMWxIdEdDMlo4WHlwNDdKeUdoVHYzTnBUcHhka3JKZEJXUTRHaWxFRC9ZNDVrUHhCZnJ5bUdXQ2xhVkJ1T25LUnMyLS13Q3ZOVnlVTTlGeWFxNkxsV0gyVUxBPT0%3D--a89b47c2272da100f4097ec7a17e61e1dc80a66e; __cf_bm=MiwGIJCxb6OnkkWiQj5SywBxq.nODk55gTQMP_0MNFE-1678694101-0-AUk0auKI2Fm4KATjo5yN228h15r7ZTNGpDhfMk+nDfd0rOtOiLsfcvUDnQpMiuUHk53IvNoEXV1OiYd9Zf478UmlsjFOLGgki8P4uspBeCOAXRX82GSjHc5R5Ke7w4NwCg==; _voice_session=cDRkK0tzTkd4Z0xieVlFS1FLSWV6L3pLdW1MbS9JL1p1OHBET21pZDBTUTlIVGpOVkc1QVBOUERKaVNlRjFZbWVBTjFsV3VIYjZtZjdMNXhlTkYyVURzb1NsVFpCdi9sQmZ3MEpFVVJTL1FVZUttMjV4cGQ5eSsyNXJJcDBiai9jeUdVNGxURGcvbmlJSmcwVE54WFRRPT0tLUpMWis3aWFXdUFNTE5oUWVJN29QYkE9PQ%3D%3D--537a95abc8da5524afbec1ca65b16555dc22b6af; _zendesk_session=dW41d0FrdU9ScXhna3I3S2svQStMV2ZCaUZ3WGM0b0YrWHV1OHpXbm42M3dFcFkrYXBtZk5tOTRJZVBHVkpTYmQ0a0tZY1ZQNU5EU3pJbXJQcS9vajRYbWxGQWJEaW5mdmkxemp2b09aWFpNcSt6ZU9yampLcG9kbzNwOFkwR3BjaUR5Wm11dkVvcXc0d3pDMG44VUZISzdqK1UyNEd3SUVrTzhiUFJFTHJpTHcyY3h2cEZOeEdzYlVMZjQzeFlwbTVpQ1ZKZzV5b3pkK0dNSzFYS0pEZDM5cmoyM3B2NmdIRGx4N2JsSDUyYURpMHJ0d0ZMR1V6YWhIdkRDeUhhdy0tbkxGRDBtb2g2RzZ0N0VMZlkvZzZwZz09--3577afef4dcee584f685728c35e6d5defae78593; __cfruid=a8394a2e9fdf6bd4ba6340d47563c00ea17c1aa0-1678693872; _zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307; _zendesk_session=dVpJQkhSRDQ3ck5RMGwvd01YSDlja1hrTlVuV28xUWtTYXA3WmJHT3krQWE2SHdzSUZtbmFEUTAveUxwdHdhZ2lVRUd2dUxNeTQwNmFDNC9KYVhhalRQNi9hL1VXb014RXRsbjFzeTdNeWx5VlhxNUNHSHg1U0xiRmhjZzNVUFF1ejdhTWNZSE1yVE95VFFHUnMzSGhvbFNyOW1ZdVYzbkVYcFpVeWZkNmFMSld3MVhSc1FGZkZPNWhGNHArand6cmxQeXM0TzR4a0JHMUw4VU1WclhxcFhnbjVESkJuNmJZRDQvT0ZTbHVMZ2Q2VE5uSkxTWDFFNXFiazRYY0RFdy0tMkxuWUVjUEhEa0JBTzIxR0xCZVZLUT09--3fb6f11a0bdb4ada7bcf21e98d21aae607738197',
    'if-none-match': 'W/"43e47bfdc979c1a4d3d2ba3b5b3bebd4"',
    'referer': 'https://vroozi.zendesk.com/agent/tickets/163799',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-csrf-token': 'FLA4+7l3hg/9AeVf7hnMdFYh6YmPkEPXBk8p/uFA7y4=',
    'x-zendesk-lotus-feature': 'Ticket/Customer',
    'x-zendesk-lotus-initial-user-id': '403251810791',
    'x-zendesk-lotus-initial-user-role': 'admin',
    'x-zendesk-lotus-tab-id': '573fb79c-d84f-4ef7-bcc2-dfe1e906391c',
    'x-zendesk-lotus-uuid': '1063396e-805d-4ba6-b519-8bed57d69174',
    'x-zendesk-lotus-version': '16925',
    'x-zendesk-originator': 'lotus-react',
    'x-zendesk-radar-socket': '_foWBCgWthx86eZgAEOF',
    'x-zendesk-radar-status': 'activated'
}

# data = response.json()



def getTicketDetail(requester_id, ticketId):
    conn.request("GET",
                 "/api/v2/users/" + str(requester_id) + "/tickets/requested.json?include=comment_count,first_comment,last_comment,users&per_page=10&sort_order=desc&sort_by=id&exclude_archived=true",
                 payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode('utf-8'))
    for ticket in data['tickets']:
        id = ticket['id'];
        if(id==ticketId):
            print(ticket)

