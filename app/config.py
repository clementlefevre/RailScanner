URL = "https://www.voyages-sncf.com/proposition/rest/search-travels/outward"

# headers = {
#     'accept': "application/json, text/plain, */*",
#     'accept-encoding': "gzip, deflate, br",
#     'accept-language': "en-US,en;q=0.8,de;q=0.6,fr;q=0.4",
#     'connection': "keep-alive",
#     'content-length': "1049",
#     'content-type': "application/json;charset=UTF-8",
#     'cookie': "x-vsc-correlation-id=2ff51743-e061-4ffd-a878-950a1d8f61f0; x-vsc-app-version-3000=ACTIVATED; VSL_city=SDN_PRD7; _cs_v=0; dydu.lastvisitfor=IjIwMTctMDgtMDZUMTg6MDk6NDUuMzYwWiI%3D; AMCVS_F3F4148954F730780A4C98BC%40AdobeOrg=1; vsct_policy_compliance=1; i18next=fr_FR; HYPDEC=; ab_test_id=opt1_ebillet_v1; s_vi=[CS]v1|2CC3AF6B053125EB-60000103E00001B1[CE]; SESS5058f1af8388633f609cadb75a75dc9d=h0mi5e14q6476t7lcahlblf376; VSCCACHE=vslpibp7var; CSCSESSIONENG=csctrep11eng; CMSSESSION=vslcalp22cms; CCLSESSION=cclagdp71; s_cp_persist=T_LSP_53074FACD8C84; s_cpm=%5B%5B%27T_LSP_53074FACD8C84%27%2C%271502047665804%27%5D%5D; VSASESSION=vsaliep61; va_ic=42961f8252752031fbb7b1bd468b8a36a84d5d7b%3A1502048993390; x-vsc-correlation-id=2ff51743-e061-4ffd-a878-950a1d8f61f0; _cs_cvars=%7B%221%22%3A%5B%22pageType%22%2C%22web%2Ftrain%2Fapresvente%2Fmonvoyage%22%5D%2C%222%22%3A%5B%22is_connected%22%2C%220%22%5D%2C%223%22%3A%5B%22langue%22%2C%22fr%22%5D%2C%224%22%3A%5B%22pays%22%2C%22fr%22%5D%7D; ck_chStak=%5B%5B%27Liens%2520Sponsos%2520Train%2520Hors%2520Marque%27%2C%271502046580912%27%5D%2C%5B%27SEO%2520Inconnu%27%2C%271502046587258%27%5D%2C%5B%27Liens%2520Sponsos%2520Train%2520Hors%2520Marque%27%2C%271502047665806%27%5D%2C%5B%27Sites%2520Groupe%27%2C%271502047696737%27%5D%2C%5B%27SEO%2520Inconnu%27%2C%271502050593668%27%5D%5D; _cs_id=70f51450-2d6c-ac67-af60-5d46a7b3a891.1502043034.3.1502050751.1502050738.1.1536207034643; AGGREGSESSION=vslnicp71agr; _ga=GA1.2.1839451703.1502048573; _gid=GA1.2.2057658956.1502048573; AMCV_F3F4148954F730780A4C98BC%40AdobeOrg=2096510701%7CMCIDTS%7C17385%7CMCMID%7C21295866883441942143768664583583281125%7CMCAAMLH-1502647786%7C6%7CMCAAMB-1502706101%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1502108501s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17392%7CvVersion%7C2.0.0; c_m=www.google.frNatural%20Search; VSLPRD7Session=583690866DF3538B87D63076311CE13D; VSCSESSION=vslcamp71vsl; SCDEC=; has_js=1; dydu.sidebar=eyJ0aXRsZSI6IiIsImNvbnRlbnQiOiIiLCJ1cmwiOiIiLCJjb250ZW50U3R5bGUiOnt9LCJmcmFtZVN0eWxlIjp7fSwiY29udGFpbmVyU3R5bGUiOnt9LCJzaG93IjpmYWxzZSwiYm90dG9tIjowLCJyaWdodCI6MTAsImlnbm9yZUNvbmZpZ3VyZWREaW1lbnNpb25zIjpmYWxzZX0%3D; ABTasty=uid%3D17080620093325122%26fst%3D1502042973634%26pst%3D1502090898175%26cst%3D1502101284121%26ns%3D3%26pvt%3D57%26pvis%3D4%26th%3D135889.189547.226.10.3.1.1502042973643.1502101353128.1_140811.195995.3.0.3.0.1502043934164.1502044042515.1_149835.207779.2.0.3.0.1502043858174.1502043905048.1_181545.250357.2.0.3.0.1502043857885.1502043904629.1_192372.264031.1.0.3.0.1502044127227.1502044127227.1_198984.0.60.1.3.0.1502043006878.1502101351329.1_199746.274239.4.1.3.0.1502048569751.1502101284133.1_212381.290359.139.3.3.0.1502046575194.1502101351335.1; dydu.session=IntcImNsaWVudElEXCI6XCJ2VWV4am5ITTA5TzAwQzJcIixcImNvbnRleHRzXCI6W10sXCJjb250YWN0c1wiOltdLFwic3RhdGVzXCI6e1widGVhc2VyXCI6ZmFsc2UsXCJkaWFsb2dcIjpmYWxzZSxcInNpZGViYXJcIjpmYWxzZX19Ig%3D%3D; dydu.teaser=eyJ0eXBlIjoiY2xhc3NpYyIsInRpbWVvdXQiOi0xLCJhY3Rpb24iOm51bGwsInJld29yZCI6bnVsbCwic2hvdyI6ZmFsc2V9; dydu.popin=eyJib3R0b20iOjAsInJpZ2h0IjoxMCwic2hvdyI6ZmFsc2V9; dydu.push=eyJyX3BhZ2VzVmlld2VkIjp7ImNvdW50Ijo0OH0sInJfbGFzdHBhZ2Vsb2FkZWQiOnt9fQ%3D%3D; ABTastySession=referrer%3Dhttps%3A//www.google.fr/__landingPage%3Dhttps%3A//www.voyages-sncf.com/__referrerSent%3Dtrue; ry_ry-g6d9xe0l_realytics=eyJpZCI6InJ5X0U5M0Q4RDJCLUFCNkEtNDcwNi1CMjNGLTUxMjAzMEJFREFDNiIsImNpZCI6bnVsbH0%3D; ry_ry-g6d9xe0l_so_realytics=eyJpZCI6InJ5X0U5M0Q4RDJCLUFCNkEtNDcwNi1CMjNGLTUxMjAzMEJFREFDNiIsImNpZCI6bnVsbCwib3JpZ2luIjpmYWxzZSwicmVmIjpudWxsLCJjb250IjpudWxsfQ%3D%3D; _cs_ex=1; RT=\"\"; va_prov=VSD; VSCPRDDEC=requestedDate%3D1502103600000%7C; va_first_visit=1; va_iv=7ca87ccb-3bd9-4a00-a7a9-869beb3d6809; va_s_getNewRepeat=1502101357324-Repeat; s_cc=true; country_code=FR; ck_dir=1; s_sq=voyagessncfcomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DPropositionAllerNew%2526link%253DRECHERCHER%2526region%253Dmain-form-panel%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DPropositionAllerNew%2526pidt%253D1%2526oid%253DRECHERCHER%2526oidt%253D3%2526ot%253DSUBMIT; rfrr=PropositionAllerNew_body_FORM-; merchTrck=%23",
#     'host': "www.voyages-sncf.com",
#     'origin': "https://www.voyages-sncf.com",
#     'referer': "https://www.voyages-sncf.com/proposition?clientId=b38b61a3-9448-4866-b485-1d47455ca7c5&language=fr&country=FR",
#     'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
#     'x-vsd-locale': "fr_FR",
#     'x-vsd-smart-guy-guard': "DqjrxvdlqN3:3;534:T4QQRZD\\",
#     'cache-control': "no-cache",
#     'postman-token': "c7245c1f-0937-f88a-586e-abe2bc40e58a"
#}

# headers = {
#     'accept': "application/json, text/plain, */*",
#     'accept-encoding': "gzip, deflate, br",
#     'accept-language': "en-US,en;q=0.8,de;q=0.6,fr;q=0.4",
#     'connection': "keep-alive",
#     'content-length': "1049",
#     'content-type': "application/json;charset=UTF-8",
#     'host': "www.voyages-sncf.com",
#     'origin': "https://www.voyages-sncf.com",
#     'referer': "https://www.voyages-sncf.com/proposition?clientId=b38b61a3-9448-4866-b485-1d47455ca7c5&language=fr&country=FR",
#     'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
#     'x-vsd-locale': "fr_FR",
#     'x-vsd-smart-guy-guard': "DqjrxvdlqN3:3;534:T4QQRZD\\",
#     'cache-control': "no-cache",
#     'postman-token': "c7245c1f-0937-f88a-586e-abe2bc40e58a"
# }

headers = {
    'accept': "application/json, text/plain, */*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8,de;q=0.6,fr;q=0.4",
    'connection': "keep-alive",
    'content-length': "1049",
    'content-type': "application/json;charset=UTF-8",
    'host': "www.voyages-sncf.com",
    'origin': "https://www.voyages-sncf.com",

    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    'x-vsd-locale': "fr_FR",

    'cache-control': "no-cache",

}

DB_NAME = 'sncf_trips.db'
