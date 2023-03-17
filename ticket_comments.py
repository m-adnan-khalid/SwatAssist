import http.client
import json

conn = http.client.HTTPSConnection("vroozi.zendesk.com")
payload = ''
headers = {
    'authority': 'vroozi.zendesk.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '_zendesk_cookie=BAhJIkp7ImRldmljZV90b2tlbnMiOnsiMzgyMzcxODA4NDUyIjoiOGlOZU5ITjFPQzVKbXJRbUhkZkVvZm9FNWh3RFlHN3YifX0GOgZFVA%3D%3D--c5d0cb3cacdf3edfa4eef133f129183c6e94cbb3; _zdsession_app-market=ba0585dfd4ea5a0ce297e0c50d3b30da; ajs_anonymous_id=3dde3653-5faf-4c23-b8cb-dcad3e7dd79d; ajs_user_id=382371808452; ajs_group_id=157286; _pendo_visitorId.df3d609f-14a9-4a77-b441-73602a4aaab2=382371808452; _pendo_accountId.df3d609f-14a9-4a77-b441-73602a4aaab2=157286; bime_subdomain=vroozi; _bimeio_session=Y4FdPb64uG0Ao1daiGdn31GbT02cN1fPkuWlO%2FEJd8qYSBaq25WGEI0hOd4xTCEXemEZ3IDPqaCZURrryyWy4zA1DxslJxMCe00oyZlROjhUqRT3CvXdeKQpAf4iIcd64Pfnj4A5toMPDjQRg%2FaGR84lU7YH6rgeZco6jk07S959BRTr2ELkldfuzD0FCBCmevv%2Bg6Oi7hr5PNIWfjCFHnznQLSW2XX8dltQMuV6xlUVc%2Fs0wcDgwV31AnrseFA%3D--8pTs67evNy4t5IRu--ZFuiaAyfyHzQGliBK3QyeQ%3D%3D; __cfruid=6c96f6476601b15eba85476946f0e54c31764c1c-1678708090; _ga=GA1.1.1229509753.1678708377; _ga_GX4ZE3WYYT=GS1.1.1678708377.1.1.1678710343.0.0.0; _zdsession_zendesk-proxy=53f8d8859e3329b9737a3b66d379f271; _pendo_meta.df3d609f-14a9-4a77-b441-73602a4aaab2=592995165; __cf_bm=.SKEDEUykwX_DPRcIOUEzAJSdPyAPL0c0a1hSOQ7tfU-1679029019-0-AWzRDSi2GbdWi4ZgLqD9jx9+o8yeEfJtu91f86/mAaWy7CTzp1Vj1RrP0Hx78VFaHmGJIXQrVBtzZDpNtcqXt/OxFgmhX8iDeNZ3QXUiqyS1/L8QNnmCkwhr8dHcBClJpQ==; _zendesk_shared_session=-WEg3R25EWXB0dHVOUURvODQzdlFjWlhjZ3lzbi9KcnI1VEJrYmZxcXlPTENIVHAxYzVDOHB4emRqeE15Q3M0MFRKQ2JGaUk4RlNsaS9nNkxSeSt1Um5UMVYzYmMyamZFSlZab2lBQldxMlBzZ3dwTG5SUVdLM3pJVE1NdVNtd2ItLUZyOVhGVzM0VkVRejVhQ3RObFphQlE9PQ%3D%3D--d05c38a3ee2f1113a7a565d79c953a8c75db66d2; _zendesk_authenticated=1; _app_market_session=ZW9vV3FUTFJRWW5yZ1Nyc1JnZ2Nsdlk2NFJtbVNndEpmak5hM3ZUNjRKOEhQKytOVk10T3J2V0kydDhPZEYwQUxacFdVWmN1NXdUWTlTeWkxZkxlMVoxUWNzbzFjOTVjNW9PZnRqWFQ0SE9VQ3VXKzRYNldmSmMwUURUeUxFeXQ3YUpnR1h4SzMra2Y4R0hIeXMrMnRBPT0tLWwyalNlblIvcWFIZ1RSQnBsOUJIeGc9PQ%3D%3D--5ba5a4960323857f97704d09f4c879937de5fc8b; _voice_session=UnVOUGVSaEJSOU1yWCs0U1RLZytEOGpuK0tqcVNuVytYeUxnUzhhZ3VZZU4zRGNPSlV6S3BVa3VubGxDVGNvRFRaM1pCK0lTeVFEN2J6aEc3NTRhbm1sWlBRcTg3c2o0WTJ6QWc1UGg2R01jREZlVitxNkZSQTIzNHNPcm1IekJoQmIyNUxvMlpNaDFhMUhiVWFsbmZRPT0tLTVIWnZCMHJjSkgzM21Xa256ck16SXc9PQ%3D%3D--f98d264f9275dc3c06e236d1ebb869d37ccba01f; _pendo_guides_blocked.df3d609f-14a9-4a77-b441-73602a4aaab2=0; __cfruid=f1b5d3c53ebd496abebed5e433ee253a2f18ec7c-1679029042; _zendesk_session=MS9zS1YxWFN2akpXS1MrVENxM0dXMURQQXR0TzlYVzQzaGFERmNVRy82OUtDTS94VVFVbVN4c21TekptektmSmd4KzVJZGp5KzFPNlFsQ0ZuRjNOSDRudmdrQVpFc3VCclkwc1h4RTFjTTI1YkxXZW9aVzNOVGdTMmNYTWNmWWlQODRpQjkxSXpCSmpWR2RYOWt5NUE1NDErWWhYOXU1eVY1YTk4ckxhWDdpcGkrSk4vSUtmYm40SDg2bzMwRnN0ekp4UVdka1JPNkVCQjlNc2RNaHNncSszQ3hOekRvV09ua1lPb1MyWGU2ZE5uTmJzSHdUckw2elpsVWxzaXpLci0tOWpPVWM3c0ZpUEp2ZUUrZnh0NGdNQT09--b448f69b83bfee367c90f27e96d319251e617a0c; _help_center_session=d2FQWUJHdFkzMmZZOFNhRkFVNTVpREtvK1dUdWJpL1o4d0REaHZYZzJ0M2EyL2pWMStvcnpOTXdOdGRRZGVnbm8zSmNkMndWMmlHNUlwbXFjcGdtem5aTjNXSFRZa2d4L01GVFVzOURDYmlQbFd2SXZhclVvY0xPQnlLSlVmWCtVT0V2Ylhwdm5Hdk9tUUl2MUF1VE5FUGRkQU9Bczl4dnBCazFKMkVUazRBQ20wa29meWt3RUpxcUJ6ajhlbERhOEJIbFo1b1pmSisrU3d2dVZJbFQ3UT09LS1xdGtLbGxFMkI2bk5VKzNTU3VOc21BPT0%3D--bdfd8a60993e61f06b70034d46182f6bc14e0cc8; __cfruid=a484a2cceb535c82081c68aa565b115c4054e4ed-1679029094; _zendesk_authenticated=1; _zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307; _zendesk_session=UnRtdkx5QW90M3MyeGNDWnhKUUUvMkZBd1hwRExiTThyNnlLaVY1eUs2SjhmdWVkYXBZanF1OTE2YlA2S1FLdmtUcktmL3h0MXk3R3RQTGhhNkkyMVRLUnJBU0tCK2RucXArQkVuQ1lJM0p3ZHpXWHh4OUV1bVZkdEcyVWdSY0h4blYzSlJ2VG95VkJDSDhHc1NRS3RBNkdhZjM1Y3JRaFRUN255WFhpNXB2SU5BTXFTMktud2hKOEFtcHN3QkFHamtuN3ZuNlI2Wkw0VVAyWElQbU9KYzVrNFVZWm9BYWR2a0pjVHh6NHRrZmlkcDZLMmlmV1BkSmVjaE5lOHZRYi0tRUVOYWNVa1h2SVN5bEU1alcvQzhFdz09--37e55a186f423747e500528ed697e44636e037ae; _zendesk_shared_session=-QUxhOGYrNmdDcVpQWFhTOXFBTkRjN3JGUHRaN3hIZUNTMjRkcC9zekdVUmhvb29lcEVaSzcyYzJHbXM3djhmMnlQeXRYQkp1aGxDTGs0cTd3bGdma2xzMmY2SmVRYW9Ba2ZIbGxFZFVaSnRSemY5a3AvZ2JxTFk5N21aL2lnQW0xWGFzQ09oRk1ZUTZiZlVXcENzbEFRPT0tLTYwNFF5bFM5Yjk4OXBlRDE2TTRXSWc9PQ%3D%3D--54b922defc4acec32052d04032bde94454b4f28f',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}


def getTicketComments(ticketId):
    conn.request("GET", "/agent/tickets/" + str(ticketId), payload, headers)
    response = conn.getresponse()
    content = response.read()

    # Decode the response content as a string
    html = content.decode("utf-8")

    # Find the script tag containing the conversations data
    start_tag = '<script type="text/preload" charset="utf-8" data-preload-id="/api/lotus/tickets/' + str(
        ticketId) + '/conversations.json?include=users&sort_order=desc">'
    end_tag = '</script>'
    start_index = html.find(start_tag) + len(start_tag)
    end_index = html.find(end_tag, start_index)
    json_data = html[start_index:end_index]

    # Parse the JSON data
    data = json.loads(json_data)

    # Get the conversations data from the JSON data
    conversations = data["conversations"]
    comments = [];
    for conversation in conversations:
        # print("processing....")
        body = conversation['body'];
        comments.append(body);
    return comments;
