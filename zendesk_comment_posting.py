import http.client
import json

conn = http.client.HTTPSConnection("vroozi.zendesk.com")

headers = {
    'authority': 'vroozi.zendesk.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': '_zendesk_cookie=BAhJIkp7ImRldmljZV90b2tlbnMiOnsiMzgyMzcxODA4NDUyIjoiOGlOZU5ITjFPQzVKbXJRbUhkZkVvZm9FNWh3RFlHN3YifX0GOgZFVA%3D%3D--c5d0cb3cacdf3edfa4eef133f129183c6e94cbb3; _zdsession_app-market=ba0585dfd4ea5a0ce297e0c50d3b30da; ajs_anonymous_id=3dde3653-5faf-4c23-b8cb-dcad3e7dd79d; ajs_user_id=382371808452; ajs_group_id=157286; _pendo_visitorId.df3d609f-14a9-4a77-b441-73602a4aaab2=382371808452; _pendo_accountId.df3d609f-14a9-4a77-b441-73602a4aaab2=157286; bime_subdomain=vroozi; _bimeio_session=Y4FdPb64uG0Ao1daiGdn31GbT02cN1fPkuWlO%2FEJd8qYSBaq25WGEI0hOd4xTCEXemEZ3IDPqaCZURrryyWy4zA1DxslJxMCe00oyZlROjhUqRT3CvXdeKQpAf4iIcd64Pfnj4A5toMPDjQRg%2FaGR84lU7YH6rgeZco6jk07S959BRTr2ELkldfuzD0FCBCmevv%2Bg6Oi7hr5PNIWfjCFHnznQLSW2XX8dltQMuV6xlUVc%2Fs0wcDgwV31AnrseFA%3D--8pTs67evNy4t5IRu--ZFuiaAyfyHzQGliBK3QyeQ%3D%3D; __cfruid=6c96f6476601b15eba85476946f0e54c31764c1c-1678708090; _ga=GA1.1.1229509753.1678708377; _ga_GX4ZE3WYYT=GS1.1.1678708377.1.1.1678710343.0.0.0; _zdsession_zendesk-proxy=53f8d8859e3329b9737a3b66d379f271; __cf_bm=.SKEDEUykwX_DPRcIOUEzAJSdPyAPL0c0a1hSOQ7tfU-1679029019-0-AWzRDSi2GbdWi4ZgLqD9jx9+o8yeEfJtu91f86/mAaWy7CTzp1Vj1RrP0Hx78VFaHmGJIXQrVBtzZDpNtcqXt/OxFgmhX8iDeNZ3QXUiqyS1/L8QNnmCkwhr8dHcBClJpQ==; _zendesk_shared_session=-WEg3R25EWXB0dHVOUURvODQzdlFjWlhjZ3lzbi9KcnI1VEJrYmZxcXlPTENIVHAxYzVDOHB4emRqeE15Q3M0MFRKQ2JGaUk4RlNsaS9nNkxSeSt1Um5UMVYzYmMyamZFSlZab2lBQldxMlBzZ3dwTG5SUVdLM3pJVE1NdVNtd2ItLUZyOVhGVzM0VkVRejVhQ3RObFphQlE9PQ%3D%3D--d05c38a3ee2f1113a7a565d79c953a8c75db66d2; _zendesk_authenticated=1; _pendo_guides_blocked.df3d609f-14a9-4a77-b441-73602a4aaab2=0; _app_market_session=Q3l0aW56Rm1qY1EyeFdTZ24xZDJBcFdHZ0Fld3NsVXhYV0VvdkNSK2dwVWJVQVZNVk9yNXl3Yi9UeUhCaHlRU0VtUFg4dlp3alBnNEFUaStGWWxQeURaM01mME5VM3pWTnlERitwcGg4TXZlc29yYzEvUG5ONktFSGNpeXhjSkdpb2pESWI0Zy9odXRqNnBqbHNwTFB3PT0tLW5tb3Ezdlpucmh1S2NkYUh0MStTV3c9PQ%3D%3D--44c1c0bf6ea695a67f9476a9b4b6eabcaa3b842f; _help_center_session=aTVCbldIWGRRUjlQbnFaNThjYnhKYlVucFdJWWVoOWtPWHdoVmNYWC8xUkVNV1E0YWZXTjd5QTNBNi9qNkdSWUxnVWVVRjk1SXBDZ2R0ei9GZ1Z6QWJJTGNGUDJTWkJ4R2dpNFJORjVpVHFJSkt1NlhkYU5vcGZreGNSOE0xeFZmNGRlekppVTV5OU9JODNOM2ZyZ2VqeURkOEhBSmxrYTAwWmFZZXFOOFkrNTRJRzFRbUJRWXNIaUM3MlhIUGhHZXkzcTdZZXdDZFFTOVdDbkpvYXc5dz09LS00dXBHaGhDM0pDejdXY3lTVUgwSHN3PT0%3D--7704602afe58c89e3fef603fd1bd9e985819ee73; _voice_session=c1lpVXBoODZoUWlpOEpKc29QcFVaUnVzNE92MWVlaXgxb0JjMnhtY1dyaVZGQkI1UDNTemROM3lUZWREYVluYktXU0RFWThVTk9mSFJRdzN6UWpySHpmZmpKT1NPR2pxOTRQOXJ5TzJPalkwVDA3R3I4ZGRMc3V2OTVPdGpTWVZJYk9RdHdVcHVSQjdseWpuTjJNcDNRPT0tLVFHc3pDZmdkWGhuQTdIa2J6bU9uY1E9PQ%3D%3D--9e4ecece99722e7ddf7563b16509b9aec8a70c17; _pendo_meta.df3d609f-14a9-4a77-b441-73602a4aaab2=2444561493; _zendesk_session=WjlIbnJsOGhhS09GNkxvSDRCT1ByaHlaMnNGQnNOYStOVC9JVEtaZkRSZlU4N2liTFV1QmZrSzVscSt3MmJkKy9kY2cvWEtVZFNkamVDaFI4NVN1elBDNEJCUWI5SE9QMWF0NURadzlGa3JIV1pSdWY4VGliUFk4c3I2dG8xUHE3M2orR3RsVEVKejZxazBrUTgrb0lPWXdkRXZnYUZFd0M3cmJVdGFzeDN2c29QblIyRE9VaklDc3pTUEc5U040SkZmcW5KczNoVFU5bWo0cjB2UkMrQXNMSWZhQTdjMVkwSlk3MXpRdGEzbkYyTkMrbDlBU2hlN1ZtNTVuZUovVC0tcTNXNVZWS0lkWmIwU1FzMURxak5hQT09--f39bd4477cc02d6451a9a4ef5ebea8ce0606f56e; __cfruid=78d5dde6bf54fe350dbd648090132e514767d7e8-1679029073; __cfruid=4114b5d6300ae4271f6eae6a8099b7f55343d8d0-1679029189; _zendesk_authenticated=1; _zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307; _zendesk_session=bW1iMUJWbXMydXRUSy81ZGROK2xZOEozSHRWcDJuTXFwR0dWZU05WnVOdEF1b0Rqb2xYRmNxU1VzMVJNRnJlQXMzMXh1TndscHhNdGdIM3FFS0xIcmRuem1YWG9QWWRwbzdsZVpSOE4vT01RcWJHKzdRZkNjcVloVnFIOVNkUnVyOGJ2WHVsVDNyUzBZSC9Jcjd4bVpLVnBRNWUwL1loVTJhZy9jT20raHJuWGFERHZ2eDdSWUREcGxNS1hLNDRJd0xzR0ZzTlB2UklQTXhFWjROV1NkVXJyMXNUMGZFU0YvY2wrenBTNk85YktBcmxsc01pL20yTHZVblV2WjFCUS0teU9oVFV1clJQcjU4MTBZNjR5eUtDQT09--6cdb6bf3a5cea02111274f6354eb0792b88bf324; _zendesk_shared_session=-QUxhOGYrNmdDcVpQWFhTOXFBTkRjN3JGUHRaN3hIZUNTMjRkcC9zekdVUmhvb29lcEVaSzcyYzJHbXM3djhmMnlQeXRYQkp1aGxDTGs0cTd3bGdma2xzMmY2SmVRYW9Ba2ZIbGxFZFVaSnRSemY5a3AvZ2JxTFk5N21aL2lnQW0xWGFzQ09oRk1ZUTZiZlVXcENzbEFRPT0tLTYwNFF5bFM5Yjk4OXBlRDE2TTRXSWc9PQ%3D%3D--54b922defc4acec32052d04032bde94454b4f28f',
    'origin': 'https://vroozi.zendesk.com',
    'referer': 'https://vroozi.zendesk.com/agent/tickets/163831',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-csrf-token': 'Z40nk9rIxPhruI5Co046lFzsyumsEAaAo2bO6boxPNY=',
    'x-requested-with': 'XMLHttpRequest',
    'x-zendesk-lotus-feature': 'Ember',
    'x-zendesk-lotus-initial-user-id': '382371808452',
    'x-zendesk-lotus-initial-user-role': 'admin',
    'x-zendesk-lotus-tab-id': '08f269ba-27d6-4437-b18a-36d4744c700f',
    'x-zendesk-lotus-uuid': 'f979691c-3484-43b2-a750-511c8229b31b',
    'x-zendesk-lotus-version': '16979',
    'x-zendesk-radar-socket': 'Occ_sAnLl1zMVQWbANBl',
    'x-zendesk-radar-status': 'interrupted'
}


def post_answer(answer, ticket_form_id):
    payload = json.dumps({
        "ticket": {
            "tags": [
                "acknowledged"
            ],
            "via": {
                "channel": "Web form"
            },
            "recipient": "support@vroozi.zendesk.com",
            "safe_update": False,
            "comment": {
                "public": False,
                "uploads": [],
                "html_body": answer,
                "add_short_url": "0",
                "channel_back": "false"
            },
            "ticket_form_id": ticket_form_id,
        }
    });
    conn.request("PUT", "/api/v2/tickets/163831", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("Answer is Posted !!!!1");
