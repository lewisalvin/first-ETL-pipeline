import requests
import re

cookies = {
    'ak_bmsc': '3C92AC3D8E6769B4A8569EA4FEABC9DE~000000000000000000000000000000~YAAQj+stF1GMmGyVAQAABnIOeBuoue5DPBOvOl5e30TiVVqw2cFwhE4BasKzDs8scgQcvV6bBv+KdQ3uCvXgJlIfQVcskttkz/wa4EPKeibiaxZK0PSmd+BJotnslnmiRUILP8zxCF+xpEd9XTdxs2Y3UMta12tgdn8yWnbfBlZ7u0fB89zbdiUYUKmES1Fdn3mFuR8ZYPEe8xs2sik4sI6P1Dp9+NZEWgglqpw02cssww3ExOau8vAPZ47k6ssiXhLIqN5V3gK7IoiXeATnGKsTXUkwy4FwV5mJBIFA6mbnjI8HphiFQMJEYlMMkllHxvkGc8dEBXImcSJFzu8NlWjoawiRQbOiUk9tclcciISzog7th5tb4/n/pfn0x8bwc9bQ6uZ2vMm4tfTf6vqzoiDmFkBmdh8i8IWmAOUIqoRpOSL/DoP9JJ/fc6eqV0nAevgX7s4HeR+T61B6xSlo7zp4VEI4l3AfmTyaFg5lmoe14JJT',
    'nbatag_main__sn': '1',
    'nbatag_main__se': '1^%^3Bexp-session',
    'nbatag_main__ss': '1^%^3Bexp-session',
    'nbatag_main__st': '1741477766760^%^3Bexp-session',
    'nbatag_main_ses_id': '1741475966760^%^3Bexp-session',
    'nbatag_main__pn': '1^%^3Bexp-session',
    'AMCV_248F210755B762187F000101^%^40AdobeOrg': '179643557^%^7CMCMID^%^7C18537307016530662303827156340449654014^%^7CMCAID^%^7CNONE^%^7CMCOPTOUT-1741483168s^%^7CNONE^%^7CMCAAMLH-1742080768^%^7C7^%^7CMCAAMB-1742080768^%^7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI^%^7CMCSYNCSOP^%^7C411-20163^%^7CvVersion^%^7C5.5.0',
    'AMCVS_248F210755B762187F000101^%^40AdobeOrg': '1',
    's_ppv': 'home^%^253Amain^%^2C19^%^2C19^%^2C919^%^2C1^%^2C5',
    's_ips': '919',
    's_tp': '4761',
    's_cc': 'true',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Mar+08+2025+18^%^3A19^%^3A31+GMT-0500+(Eastern+Standard+Time)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=efdff7d5-a84a-410b-be90-2fa1ce9bfbd6&interactionCount=1&isAnonUser=1&landingPath=https^%^3A^%^2F^%^2Fwww.wnba.com^%^2F&GPPCookiesCount=1&groups=OSSTA_BG^%^3A1^%^2CNBAad^%^3A1^%^2Cpad^%^3A1^%^2Cpap^%^3A1^%^2Ccad^%^3A1^%^2Cdsh^%^3A1^%^2Cdsl^%^3A1^%^2Cven^%^3A1^%^2CBG349^%^3A1^%^2Cdlk^%^3A1^%^2Creq^%^3A1^%^2Csec^%^3A1^%^2Cgld^%^3A1^%^2Cmap^%^3A1^%^2Ccos^%^3A1^%^2Cdid^%^3A1^%^2Ctdc^%^3A1^%^2Cdsa^%^3A1^%^2Cpcd^%^3A1^%^2Cmcp^%^3A1^%^2Csid^%^3A1^%^2Cpcp^%^3A1^%^2Cmra^%^3A1^%^2CNBAmt^%^3A1^%^2Cpdd^%^3A1',
    'OTGPPConsent': 'DBABLA~BVQqAAAACgA.QA',
    '__gads': 'ID=fb0e5a0fec7a82e6:T=1741475969:RT=1741475969:S=ALNI_MYXe5Pbq2Gf7v-xIccMFQXp2Gxikw',
    '__gpi': 'UID=00000f1748d6a73d:T=1741475969:RT=1741475969:S=ALNI_Ma5donSVs6KnluC7_dY7oMavAWhYQ',
    '__eoi': 'ID=8385a0f695efbf42:T=1741475969:RT=1741475969:S=AA-AfjYbkzxw0fHRzocpegRvN7Re',
    'bm_sv': 'A859606234EFBE40ABDCA7AE9DD929F6~YAAQkCABF6g5FlaVAQAA6x4keBvTDSoi01AShgKWPcUVkF4rmemwjsu8SMg6u5zuum59d4UzV9XSIOhonUMkNthMXAtNxD1FO6JCiNBVEFoI+K11tGLNDZQnS6y6VjR3w0XrUDLgcs4AixyH087jrJBtqN7Wq4IQq5whCovgPtnSvARhU3fR9LtY5cQ0YL+2XPKelMDAE15KbLITw5SvpyxbH6PJU4Gy8itYji1d+ErEb8HNUSAkmWVuS7goKA==~1',
    '_ga': 'GA1.2.1376169723.1741475972',
    '_gid': 'GA1.2.936848189.1741475972',
    '_ga_GELQE9ZCTK': 'GS1.2.1741475972.1.1.1741477387.0.0.0',
    '_gat': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Connection': 'keep-alive',
    'Referer': 'https://stats.wnba.com/leaders/',
    # 'Cookie': 'ak_bmsc=3C92AC3D8E6769B4A8569EA4FEABC9DE~000000000000000000000000000000~YAAQj+stF1GMmGyVAQAABnIOeBuoue5DPBOvOl5e30TiVVqw2cFwhE4BasKzDs8scgQcvV6bBv+KdQ3uCvXgJlIfQVcskttkz/wa4EPKeibiaxZK0PSmd+BJotnslnmiRUILP8zxCF+xpEd9XTdxs2Y3UMta12tgdn8yWnbfBlZ7u0fB89zbdiUYUKmES1Fdn3mFuR8ZYPEe8xs2sik4sI6P1Dp9+NZEWgglqpw02cssww3ExOau8vAPZ47k6ssiXhLIqN5V3gK7IoiXeATnGKsTXUkwy4FwV5mJBIFA6mbnjI8HphiFQMJEYlMMkllHxvkGc8dEBXImcSJFzu8NlWjoawiRQbOiUk9tclcciISzog7th5tb4/n/pfn0x8bwc9bQ6uZ2vMm4tfTf6vqzoiDmFkBmdh8i8IWmAOUIqoRpOSL/DoP9JJ/fc6eqV0nAevgX7s4HeR+T61B6xSlo7zp4VEI4l3AfmTyaFg5lmoe14JJT; nbatag_main__sn=1; nbatag_main__se=1^%^3Bexp-session; nbatag_main__ss=1^%^3Bexp-session; nbatag_main__st=1741477766760^%^3Bexp-session; nbatag_main_ses_id=1741475966760^%^3Bexp-session; nbatag_main__pn=1^%^3Bexp-session; AMCV_248F210755B762187F000101^%^40AdobeOrg=179643557^%^7CMCMID^%^7C18537307016530662303827156340449654014^%^7CMCAID^%^7CNONE^%^7CMCOPTOUT-1741483168s^%^7CNONE^%^7CMCAAMLH-1742080768^%^7C7^%^7CMCAAMB-1742080768^%^7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI^%^7CMCSYNCSOP^%^7C411-20163^%^7CvVersion^%^7C5.5.0; AMCVS_248F210755B762187F000101^%^40AdobeOrg=1; s_ppv=home^%^253Amain^%^2C19^%^2C19^%^2C919^%^2C1^%^2C5; s_ips=919; s_tp=4761; s_cc=true; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Mar+08+2025+18^%^3A19^%^3A31+GMT-0500+(Eastern+Standard+Time)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=efdff7d5-a84a-410b-be90-2fa1ce9bfbd6&interactionCount=1&isAnonUser=1&landingPath=https^%^3A^%^2F^%^2Fwww.wnba.com^%^2F&GPPCookiesCount=1&groups=OSSTA_BG^%^3A1^%^2CNBAad^%^3A1^%^2Cpad^%^3A1^%^2Cpap^%^3A1^%^2Ccad^%^3A1^%^2Cdsh^%^3A1^%^2Cdsl^%^3A1^%^2Cven^%^3A1^%^2CBG349^%^3A1^%^2Cdlk^%^3A1^%^2Creq^%^3A1^%^2Csec^%^3A1^%^2Cgld^%^3A1^%^2Cmap^%^3A1^%^2Ccos^%^3A1^%^2Cdid^%^3A1^%^2Ctdc^%^3A1^%^2Cdsa^%^3A1^%^2Cpcd^%^3A1^%^2Cmcp^%^3A1^%^2Csid^%^3A1^%^2Cpcp^%^3A1^%^2Cmra^%^3A1^%^2CNBAmt^%^3A1^%^2Cpdd^%^3A1; OTGPPConsent=DBABLA~BVQqAAAACgA.QA; __gads=ID=fb0e5a0fec7a82e6:T=1741475969:RT=1741475969:S=ALNI_MYXe5Pbq2Gf7v-xIccMFQXp2Gxikw; __gpi=UID=00000f1748d6a73d:T=1741475969:RT=1741475969:S=ALNI_Ma5donSVs6KnluC7_dY7oMavAWhYQ; __eoi=ID=8385a0f695efbf42:T=1741475969:RT=1741475969:S=AA-AfjYbkzxw0fHRzocpegRvN7Re; bm_sv=A859606234EFBE40ABDCA7AE9DD929F6~YAAQkCABF6g5FlaVAQAA6x4keBvTDSoi01AShgKWPcUVkF4rmemwjsu8SMg6u5zuum59d4UzV9XSIOhonUMkNthMXAtNxD1FO6JCiNBVEFoI+K11tGLNDZQnS6y6VjR3w0XrUDLgcs4AixyH087jrJBtqN7Wq4IQq5whCovgPtnSvARhU3fR9LtY5cQ0YL+2XPKelMDAE15KbLITw5SvpyxbH6PJU4Gy8itYji1d+ErEb8HNUSAkmWVuS7goKA==~1; _ga=GA1.2.1376169723.1741475972; _gid=GA1.2.936848189.1741475972; _ga_GELQE9ZCTK=GS1.2.1741475972.1.1.1741477387.0.0.0; _gat=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

params = {
    'LeagueID': '10',
    'PerMode': 'PerGame',
    'Scope': 'S',
    'Season': '2024',
    'SeasonType': 'Regular Season',
    'StatCategory': 'PTS',
}

response = requests.get('https://stats.wnba.com/stats/leagueLeaders', params=params, cookies=cookies, headers=headers)

# Get ids that match the pattern below
l = re.findall('\[\d+\,', response.text)

# Isolate ids into list
ids = [int(re.findall('\d+',str_)[0]) for str_ in l]


print(ids)