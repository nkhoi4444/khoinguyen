import requests
import os,sys
import re
import base64
import uuid
import json
import time
from datetime import date
from datetime import datetime
from time import sleep
import random
from random import randint
from pystyle import Add, Center, Anime, Colors, Colorate,Write, System
end="\033[0m"
black="\033[0;30m"
blackb="\033[1;30m"
white="\033[0;37m"
whiteb="\033[1;37m"
red="\033[0;39m"
redb="\033[1;31m"
green="\033[0;32m"
greenb="\033[1;32m"
yellow="\033[0;33m"
yellowb="\033[1;33m"
syan="\033[1;36m"
blue="\033[0;34m"
blueb="\033[1;34m"
purple="\033[0;35m"
purpleb="\033[1;35m"
lightblue="\033[0;36m"
lightblue="\033[1;35m"
lightblueb="\033[1;36m"
maunenhong= "\033[1;41;33m"
red = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
cam = "\033[38;5;208m"
tim = "\033[1;35m"
lam = "\033[1;36m"
trang = "\033[1;37m"
thanh_dep = f'{redb}[{whiteb}=.={redb}]{whiteb} => '
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
ip = requests.get("http://kiemtraip.com/raw.php").text
class Facebook_api(object):
  def __init__(self,cookie):
    self.cookie = cookie
    self.headers = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cache-control': 'max-age=0','cookie': cookie,'dpr': '1.75','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"','sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Linux"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36','viewport-width': '980'}
  def getdata(self):
    req = requests.get('https://www.facebook.com',headers=self.headers).text
    try:
      actor_id = re.findall("userID.*?,",req)[0].split(":")[1].split(",")[0]
      dtsg = re.findall('dtsg":.*?,',req)[0].split('"token":"')[1].split('",')[0]
      return actor_id,dtsg
    except Exception as e:
      return False
  def getinfo(self):
    req = requests.get('https://www.facebook.com/me',headers=self.headers).text
    try:
      name = req.split('<title>')[1].split('</title>')[0]
      self.user_id = self.cookie.split('c_user=')[1].split(';')[0]
      return name,self.user_id
    except Exception as e:
      return False
  def reaction(self,actor_id,dtsg,id,rec):
    camxuc = [1635855486666999,1678524932434102,613557422527858,115940658764963,478547315650144,908563459236466,444813342392137]
    index = camxuc[0] if rec == "LIKE" else camxuc[1] if rec == "LOVE" else camxuc[2] if rec == "CARE" else camxuc[3] if rec == "HAHA" else camxuc[4] if rec == "WOW" else camxuc[5] if rec == "SAD" else camxuc[6] if rec == "ANGRY" else camxuc[0]
    headers = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/x-www-form-urlencoded','cookie': self.cookie,'origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"','sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Linux"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36','x-asbd-id': '359341','x-fb-friendly-name': 'CometUFIFeedbackReactMutation','x-fb-lsd': 'H9e-B8CIRZW1WXR31fG8zP'}
    idpost = 'feedback:'+id
    idfb = str(base64.b64encode(bytes(idpost,"UTF-8"))).split("b'")[1].split("'")[0]
    data = {
      'av': actor_id,
      'fb_dtsg': dtsg,
      'fb_api_caller_class': 'RelayModern',
      'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
      'variables': '{"input":{"attribution_id_v2":"CometHomeRoot.react,comet.home,via_cold_start,1753962481029,162100,4748854339,,","feedback_id":"'+idfb+'","feedback_reaction_id":"'+str(index)+'","feedback_source":"NEWS_FEED","is_tracking_encrypted":true,"tracking":[],"session_id":"4886b2a8-2e9f-45d8-bd62-26212190be74","actor_id":"'+actor_id+'","client_mutation_id":"1"},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}',
      'server_timestamps': 'true',
      'doc_id': '24034997962776771',
    }
    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    if '{"data":{"feedback_react":{"feedback":{"id":' in response.text:
      return True
    else:
      return False
  def reactioncmt(self,actor_id,dtsg,rec,id):
    camxuc = [1635855486666999,1678524932434102,613557422527858,115940658764963,478547315650144,908563459236466,444813342392137]
    index = camxuc[0] if rec == "LIKE" else camxuc[1] if rec == "LOVE" else camxuc[2] if rec == "CARE" else camxuc[3] if rec == "HAHA" else camxuc[4] if rec == "WOW" else camxuc[5] if rec == "SAD" else camxuc[6] if rec == "ANGRY" else camxuc[0]
    headers = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/x-www-form-urlencoded','cookie': self.cookie,'origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/be.thoa.56769/posts/pfbid0kTQmzSMHo55LpkA8KYbQgpVM8nZuXcjpYsABfKVuYMAoJ7MpBoisG7qrF2LJuFoJl','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"','sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Linux"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36','x-asbd-id': '359341','x-fb-friendly-name': 'CometUFIFeedbackReactMutation','x-fb-lsd': 'klmkSpBO_sVRubexU8TjB7'}
    idcmt = 'feedback:'+id
    idcmt_enc = str(base64.b64encode(bytes(idcmt,"UTF-8"))).split("b'")[1].split("'")[0]
    data = {
      'av': actor_id,
      'fb_dtsg': dtsg,
      'fb_api_caller_class': 'RelayModern',
      'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
      'variables': '{"input":{"attribution_id_v2":"CometSinglePostDialogRoot.react,comet.post.single_dialog,unexpected,1753966046795,895315,,,;CometHomeRoot.react,comet.home,via_cold_start,1753966016204,298837,4748854339,,","feedback_id":"'+idcmt_enc+'","feedback_reaction_id":"'+str(index)+'","feedback_source":"OBJECT","is_tracking_encrypted":true,"tracking":[],"session_id":"1256e4f8-ed71-4255-a0aa-aa8cd0204f82","actor_id":"'+actor_id+'","client_mutation_id":"1"},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}',
      'server_timestamps': 'true',
      'doc_id': '24034997962776771',
    }
    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    if '{"data":{"feedback_react":{"feedback":{"id":' in response.text:
      return True
    else:
      return False
  def Sharepost(self,actor_id,dtsg,id):
    headers = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/x-www-form-urlencoded','cookie': self.cookie,'origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/be.thoa.56769/posts/pfbid0kTQmzSMHo55LpkA8KYbQgpVM8nZuXcjpYsABfKVuYMAoJ7MpBoisG7qrF2LJuFoJl?comment_id=1411867323426473','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"','sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Linux"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36','x-asbd-id': '359341','x-fb-friendly-name': 'ComposerStoryCreateMutation','x-fb-lsd': '8735-eNXwKi2XTqMgEfHVJ'}
    data = {
      'av': actor_id,
      'fb_dtsg': dtsg,
      'fb_api_caller_class': 'RelayModern',
      'fb_api_req_friendly_name': 'ComposerStoryCreateMutation',
      'variables': '{"input":{"composer_entry_point":"share_modal","composer_source_surface":"feed_story","composer_type":"share","idempotence_token":"'+str(uuid.uuid4())+'_FEED","source":"WWW","attachments":[{"link":{"share_scrape_data":"{\\"share_type\\":22,\\"share_params\\":['+id+']}"}}],"reshare_original_post":"RESHARE_ORIGINAL_POST","audience":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}},"is_tracking_encrypted":true,"tracking":["AZXBJI2AIiV6Q90vOItbE3SAeaK2B9YvEh8URdzLdtMyvPvj-G3k6emZCmO5XobMnNm9AaOSzxGKrPiFv_ZUTThZ0R-v1ioTfyU1S995L1JroJXt_XVSA1XPd9CneKWhFcjGpPEtcqepcG1dhhkbBUcz8H01ItmM2R9Iu6dRIkug-4451X-1dGEIEc2AWyz65oQf4t9Ifse0Ep3iDQ31cPWrOdsxei42VngTkUVbKERcPoUOruAWk2Gf7X_v-P_QY9oG5qKkvYdBeRF-I1yDbvBlmuojVKNtB6RpTW1HkZPixf7hvvn2KutKjwMfZY_68ORZwHi4JCw2UdagxsmkViN4mMSG7dlyRbJJ6tulpCjxaFKCCwlQehafgUYMenNNSdrUmediqgo2CPhcddPDz4iOEJ1X9GY3gOiCuBPZD_eqrKuvW_F6KFvRclOLPzQfG_0ybuTWMI5lDJ82kA94MkqQ_psqMAoQa0l-WN2tjCinOnSWQwpr6XLr0BKFXVGa9N3CyrRyY2xCGs6Z43HV_aA7BXP_elvSeyZdaBC6dz_UOI2uH1wp0T1JGABEt6xZIc_5of1EEDI-AO8SvG8O7OhVEaTd4v-X28_GnFe9ZX3DzGG-yNG-Sh_jGvskwt3TxK2vrIzJclWjfjm3qkq6KQsQR4wkTccIYnCVwNK6FMEsO-GBDsderWSWFQUGsyVpDvEECViLu3ZXgu4HYGoRTf4_t2LeH5FeMR9pHbJM1BkQuHqLSXEpmAbcIXSLB_btyxEYjamQxchXTy6-xCpEgBEq_cTwgGMLNm-Kw0DMq5nxlJmz-VlznRe1egI-oPBQpvxxJ_P-k9ImvdqNOLtz9Ffmg1pAl8kdg--ArG5oQJ2AL3JNmnVb6AVgsREGaIAfBcVPkoNEfhziZna4X6uqU6EIScL9hNMN0qLT1dbadQQFUZlpTwi8wPyPKf8oqRBcFQvhjdwV584xkSDp0bbYxi90BeKfCwJalHhkFNBf8lU0J-vHxCA4tx8GuGE-CM0Yb1ELZhfKAro4wlNb29SOQrRGDf5grqPUFtwqzihNKr7s-2b-6soIcnBNBT0qVLZS1dKhh7rY-cNL4xEsWPvkJmRJb3uuZ50CyRnTr73xMfZ5ffzpJAbGGYc5SWy9LfYirOI",null],"message":{"ranges":[],"text":""},"logging":{"composer_session_id":"'+str(uuid.uuid4())+'"},"navigation_data":{"attribution_id_v2":"CometSinglePostDialogRoot.react,comet.post.single_dialog,via_cold_start,1754008431936,563126,,,"},"event_share_metadata":{"surface":"newsfeed"},"actor_id":"'+actor_id+'","client_mutation_id":"1"},"feedLocation":"NEWSFEED","feedbackSource":1,"focusCommentID":null,"gridMediaWidth":null,"groupID":null,"scale":3,"privacySelectorRenderLocation":"COMET_STREAM","checkPhotosToReelsUpsellEligibility":false,"renderLocation":"homepage_stream","useDefaultActor":false,"inviteShortLinkKey":null,"isFeed":true,"isFundraiser":false,"isFunFactPost":false,"isGroup":false,"isEvent":false,"isTimeline":false,"isSocialLearning":false,"isPageNewsFeed":false,"isProfileReviews":false,"isWorkSharedDraft":false,"hashtag":null,"canUserManageOffers":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":true,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__CometUFI_dedicated_comment_routable_dialog_gkrelayprovider":true,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__FBReels_deprecate_short_form_video_context_gkrelayprovider":true,"__relay_internal__pv__FeedDeepDiveTopicPillThreadViewEnabledrelayprovider":false,"__relay_internal__pv__FBReels_enable_view_dubbed_audio_type_gkrelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":true,"__relay_internal__pv__FBReelsIFUTileContent_reelsIFUPlayOnHoverrelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredAuctionDistanceFieldNamerelayprovider":true}',
      'server_timestamps': 'true',
      'doc_id': '24410273238626866',
    }
    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    if '"errors"' not in response.text:
      return True
    else:
      return False
  def cmt(self,actor_id,dtsg,text,id):
    headers = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/x-www-form-urlencoded','cookie': self.cookie,'origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/permalink.php?story_fbid=pfbid0EWyEqFhpZKWPRZiuAEnps2medHxK5yvmbpQey5QJbYi5q7jnXqSGzw122VB5Tn2Zl&id=100016060129436','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"','sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Linux"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36','x-asbd-id': '359341','x-fb-friendly-name': 'useCometUFICreateCommentMutation','x-fb-lsd': 'h3aS1Jzv8ZrdkqQDm9H-1-'}
    idcmt = 'feedback:'+id
    idpost = str(base64.b64encode(bytes(idcmt,"UTF-8"))).split("b'")[1].split("'")[0]
    data = {
      'av': actor_id,
      'fb_dtsg': dtsg,
      'fb_api_caller_class': 'RelayModern',
      'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation',
      'variables': '{"feedLocation":"POST_PERMALINK_DIALOG","feedbackSource":2,"groupID":null,"input":{"client_mutation_id":"6","actor_id":"'+actor_id+'","attachments":null,"feedback_id":"'+idpost+'","formatting_style":null,"message":{"ranges":[],"text":"'+text+'"},"attribution_id_v2":"CometSinglePostDialogRoot.react,comet.post.single_dialog,unexpected,1754012132159,792799,,,;CometHomeRoot.react,comet.home,via_cold_start,1754011867258,589907,4748854339,,","vod_video_timestamp":null,"is_tracking_encrypted":true,"tracking":["{\\"assistant_caller\\":\\"comet_above_composer\\",\\"conversation_guide_session_id\\":\\"'+str(uuid.uuid4())+'\\",\\"conversation_guide_shown\\":null}"],"feedback_source":"OBJECT","idempotence_token":"client:'+str(uuid.uuid4())+'","session_id":"'+str(uuid.uuid4())+'"},"inviteShortLinkKey":null,"renderLocation":null,"scale":3,"useDefaultActor":false,"focusCommentID":null,"__relay_internal__pv__IsWorkUserrelayprovider":false}',
      'server_timestamps': 'true',
      'doc_id': '10095031393927624',
    }
    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    if '"errors"' not in response.text:
      return True
    else:
      return False
  def follow(self,actor_id,dtsg,id):
    headers = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/x-www-form-urlencoded','cookie': self.cookie,'origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/profile.php?id=100075710632376','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"','sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Linux"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36','x-asbd-id': '359341','x-fb-friendly-name': 'CometUserFollowMutation','x-fb-lsd': 'vxQ8GXdxhcoqxuHEfZzN8t'}
    data = {
        'av': actor_id,
        'fb_dtsg': dtsg,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'CometUserFollowMutation',
        'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1754015506168,685478,250100865708545,,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"'+id+'","tracking":null,"actor_id":"'+actor_id+'","client_mutation_id":"1"},"scale":3}',
        'server_timestamps': 'true',
        'doc_id': '24538877859049758',
    }
    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    if '"subscribe_status":"IS_SUBSCRIBED"' in response.text:
      return True
    else:
      return False
  def likepage(self,actor_id,dtsg,id):
    headers = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/x-www-form-urlencoded','cookie': self.cookie,'origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/danang.entertainment','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"','sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Linux"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36','x-asbd-id': '359341','x-fb-friendly-name': 'CometProfilePlusLikeMutation','x-fb-lsd': 'y4rhSCfyFi1ABkKJK0PNc4'}
    data = {
      'av': actor_id,
      'fb_dtsg': dtsg,
      'fb_api_caller_class': 'RelayModern',
      'fb_api_req_friendly_name': 'CometProfilePlusLikeMutation',
      'variables': '{"input":{"is_tracking_encrypted":false,"page_id":"'+id+'","source":null,"tracking":null,"actor_id":"'+actor_id+'","client_mutation_id":"4"},"scale":3}',
      'server_timestamps': 'true',
      'doc_id': '10062329867123540',
    }
    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    if '"subscribe_status":"IS_SUBSCRIBED"' in response.text:
      return True
    else:
      return False
def getcookie(token):
  req = requests.post('https://tuongtaccheo.com/logintoken.php', headers={'Content-type':'application/x-www-form-urlencoded'}, data={'access_token':token})
  cookie = 'PHPSESSID='+(req.cookies)['PHPSESSID']
  return cookie
def getlikevipcheo(cookie):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': cookie,
    'referer': 'https://tuongtaccheo.com/kiemtien/likepostvipcheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  response = requests.get('https://tuongtaccheo.com/kiemtien/likepostvipcheo/getpost.php', headers=headers)
  return response
def getlikethuong(cookie):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': cookie,
    'referer': 'https://tuongtaccheo.com/kiemtien/likepostvipre/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  response = requests.get('https://tuongtaccheo.com/kiemtien/likepostvipre/getpost.php', headers=headers)
  return response
def getcamxucvip(cookie):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': cookie,
    'referer': 'https://tuongtaccheo.com/kiemtien/camxucvipcheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  response = requests.get('https://tuongtaccheo.com/kiemtien/camxucvipcheo/getpost.php', headers=headers)
  return response
def getcamxucthuong(cookie):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': cookie,
    'referer': 'https://tuongtaccheo.com/kiemtien/camxucvipre/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  response = requests.get('https://tuongtaccheo.com/kiemtien/camxucvipre/getpost.php', headers=headers)
  return response
def getcamxuccmt(cookie):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': cookie,
    'referer': 'https://tuongtaccheo.com/kiemtien/camxuccheobinhluan/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  response = requests.get('https://tuongtaccheo.com/kiemtien/camxuccheobinhluan/getpost.php', headers=headers)
  return response
def getcmtpost(cookie):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': cookie,
    'referer': 'https://tuongtaccheo.com/kiemtien/cmtcheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  response = requests.get('https://tuongtaccheo.com/kiemtien/cmtcheo/getpost.php', headers=headers)
  return response
def getfollowcheo(cookie):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': cookie,
    'referer': 'https://tuongtaccheo.com/kiemtien/subcheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  response = requests.get('https://tuongtaccheo.com/kiemtien/subcheo/getpost.php', headers=headers)
  return response
def getchiasepost(cookie):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': cookie,
    'referer': 'https://tuongtaccheo.com/kiemtien/sharecheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  response = requests.get('https://tuongtaccheo.com/kiemtien/sharecheo/getpost.php', headers=headers)
  return response
def getlikepagecheo(cookie):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': cookie,
    'referer': 'https://tuongtaccheo.com/kiemtien/likepagecheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  response = requests.get('https://tuongtaccheo.com/kiemtien/likepagecheo/getpost.php', headers=headers)
  return response
def datnick(cookie,iddat):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://tuongtaccheo.com',
    'referer': 'https://tuongtaccheo.com/cauhinh/facebook.php',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  data = {
    'iddat[]': iddat,
    'loai': 'fb',
  }
  response = requests.post('https://tuongtaccheo.com/cauhinh/datnick.php', headers=headers, data=data).text
  return response
def getxuttc(cookie):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': cookie,
    'referer': 'https://tuongtaccheo.com/cauhinh/facebook.php',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
  }
  response = requests.get('https://tuongtaccheo.com/home.php', headers=headers).text
  try:
    xu = response.split('id="soduchinh">')[1].split('<')[0]
    return xu
  except Exception as e:
    return False
def nhanxulikevip(cookie,idpost):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://tuongtaccheo.com',
    'referer': 'https://tuongtaccheo.com/kiemtien/likepostvipcheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  data = {
    'id': idpost,
  }
  response = requests.post(
    'https://tuongtaccheo.com/kiemtien/likepostvipcheo/nhantien.php',
    headers=headers,
    data=data,
  ).json()
  return response
def nhanxulikethuong(cookie,idpost):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://tuongtaccheo.com',
    'referer': 'https://tuongtaccheo.com/kiemtien/likepostvipre/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  data = {
    'id': idpost,
  }
  response = requests.post(
    'https://tuongtaccheo.com/kiemtien/likepostvipre/nhantien.php',
    headers=headers,
    data=data,
  ).json()
  return response
def nhanxucamxucvip(cookie,idpost,loaicx):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://tuongtaccheo.com',
    'referer': 'https://tuongtaccheo.com/kiemtien/camxucvipcheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  data = {
    'id': idpost,
    'loaicx': loaicx,
  }
  response = requests.post(
    'https://tuongtaccheo.com/kiemtien/camxucvipcheo/nhantien.php',
    headers=headers,
    data=data,
  ).json()
  return response
def nhanxucamxucthuong(cookie,idpost,loaicx):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://tuongtaccheo.com',
    'referer': 'https://tuongtaccheo.com/kiemtien/camxucvipre/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  data = {
    'id': idpost,
    'loaicx': loaicx,
  }
  response = requests.post('https://tuongtaccheo.com/kiemtien/camxucvipre/nhantien.php', headers=headers, data=data).json()
  return response
def nhanxucamxuccmt(cookie,id,loaicx):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://tuongtaccheo.com',
    'referer': 'https://tuongtaccheo.com/kiemtien/camxuccheobinhluan/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  data = {
    'id': id,
    'loaicx': loaicx,
  }
  response = requests.post(
    'https://tuongtaccheo.com/kiemtien/camxuccheobinhluan/nhantien.php',
    headers=headers,
    data=data,
  ).json()
  return response
def nhanxucmt(cookie,id):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://tuongtaccheo.com',
    'referer': 'https://tuongtaccheo.com/kiemtien/cmtcheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  data = {
    'id': id,
  }
  response = requests.post('https://tuongtaccheo.com/kiemtien/cmtcheo/nhantien.php', headers=headers, data=data).json()
  return response
def nhanxufollow(cookie,id):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://tuongtaccheo.com',
    'referer': 'https://tuongtaccheo.com/kiemtien/subcheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  data = {
    'id': id,
  }
  response = requests.post('https://tuongtaccheo.com/kiemtien/subcheo/nhantien.php', headers=headers, data=data).json()
  return response
def nhanxusharepost(cookie,id):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://tuongtaccheo.com',
    'referer': 'https://tuongtaccheo.com/kiemtien/sharecheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  data = {
    'id': id,
  }
  response = requests.post('https://tuongtaccheo.com/kiemtien/sharecheo/nhantien.php', headers=headers, data=data).json()
  return response
def nhanxulikepage(cookie,id):
  headers = {
    'authority': 'tuongtaccheo.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://tuongtaccheo.com',
    'referer': 'https://tuongtaccheo.com/kiemtien/likepagecheo/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }
  data = {
    'id': id,
  }
  response = requests.post(
    'https://tuongtaccheo.com/kiemtien/likepagecheo/nhantien.php',
    headers=headers,
    data=data,
  ).json()
  return response
def banner():
  os.system("cls" if os.name == "nt" else "clear")
  banner = f"""
\033[1;31m██╗░░██╗██╗░░██╗░█████╗░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;34m██║░██╔╝██║░░██║██╔══██╗██║ ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;33m█████═╝░███████║██║░░██║██║ ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;32m██╔═██╗░██╔══██║██║░░██║██║ ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;35m██║░╚██╗██║░░██║╚█████╔╝██║ ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;36m╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝ ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
\033[1;97mTool By: \033[1;32mkhoi nguyen          \033[1;97mPhiên Bản: \033[1;32mV1    
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;95m \033[1;31mTOOL TTC VIP
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;95m BOX Tele\033[1;31m : \033[1;36mhttps://t.me/+WVAiTiVrELZlYmM1
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;32m ADMIN\033[1;31m : \033[1;95mKHOINGUYEN
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;32m ADMIN TELE\033[1;31m : \033[1;33mkhoinguyen566
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;32m ADMIN DISCORD\033[1;32m : \033[1;33mkhoinguyen566
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;36m IP CỦA BẠN : \033[1;33m{ip}
\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;31m HÔM NAY LÀ: \033[1;34mTHỨ {thu} NGÀY {ngay_hom_nay} THÁNG {thang_nay} NĂM {nam_}
\033[97m════════════════════════════════════════════════  
"""
  for X in banner:
    sys.stdout.write(X)
    sys.stdout.flush() 
    time.sleep(0.00219)
def delay(value):
	while not(value <= 1):
		value -= 0.123
		print(f'''\033[1;39m[\033[1;36mKHOINGUYEN\033[1;39m] [\033[1;36mDELAY\033[1;39m] [\033[1;36m{str(value)[0:5]}\033[1;39m] [\033[1;33mX   \033[1;39m ]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mKHOINGUYEN\033[1;39m] [\033[1;36mDELAY\033[1;39m] [\033[1;36m{str(value)[0:5]}\033[1;39m] [\033[1;33m X   \033[1;39m]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mKHOINGUYEN\033[1;39m] [\033[1;36mDELAY\033[1;39m] [\033[1;36m{str(value)[0:5]}\033[1;39m] [\033[1;33m  X  \033[1;39m]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mKHOINGUYEN\033[1;39m] [\033[1;36mDELAY\033[1;39m] [\033[1;36m{str(value)[0:5]}\033[1;39m] [\033[1;33m   X \033[1;39m]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mKHOINGUYEN\033[1;39m] [\033[1;36mDELAY\033[1;39m] [\033[1;36m{str(value)[0:5]}\033[1;39m] [\033[1;33m    X\033[1;39m]''', '               ', end = '\r')
		sleep(0.025)
def delayblock(delaybl):
  for i in range(delaybl,-1,-1):
    print(f'{yellowb}Delay Block Đang Dược kích Họat Chờ {i} Giây',end='\r');sleep(1); print('                                                        ', end = '\r')
def bongoc(so):
	a= f"{redb}────"*so
	print(a)
def Nhap_cookie():
  demnick = 0
  listnick = []
  while True:
    demnick += 1
    cookiefb = input(f'{thanh_dep}{greenb}Nhập Cookie Facebook Thứ {demnick}: {yellowb}')
    if cookiefb == '' and demnick > 1:
      break
    fb = Facebook_api(cookiefb)
    name = fb.getinfo()
    if name == False:
      print(f'{thanh_dep}{redb}Cookie Facebook Die, Vui Lòng Nhập lại !!!')
      print('\033[1;31m────────────────────────────────────────────────────────────')
      demnick -= 1
    else:
      print('\033[1;31m────────────────────────────────────────────────────────────')
      print(f'{thanh_dep}{redb}Tên Facebook:{greenb} {name[0]}')
      listnick.append(cookiefb)
      print('\033[1;31m────────────────────────────────────────────────────────────')
  return listnick
def main():
  dem = 0
  khoitool = 0
  banner()
  while True:
    if os.path.exists('configttc_khoi.txt'):
      with open('configttc_khoi.txt', 'r') as f:
        token = f.read()
      req = requests.post('https://tuongtaccheo.com/logintoken.php', headers={'Content-type':'application/x-www-form-urlencoded'}, data={'access_token':token})
      if req.json()['status'] == 'success':
        cookie = getcookie(token)
        user = req.json()['data']['user']
        print(f'{thanh_dep}{greenb}Nhập 1 Giữ Tài Khoản {user}')
        print(f'{thanh_dep}{redb}Nhập 2 Nhập access_token TTC Mới')
        chon = input(f'{thanh_dep}{greenb}Nhập Lựa Chọn Của Bạn:{yellowb} ')
        if chon == '2':
          os.remove('configttc_khoi.txt')
        elif chon == '1':
          pass
        else:
          print(f'{redb}Lựa chọn không xác định !!!')
          continue
      else:
        os.remove('configttc_khoi.txt')
    if not os.path.exists('configttc_khoi.txt'):
      token = input(f'{thanh_dep}{greenb}Nhập Access_token TTC:{yellowb} ')
      with open('configttc_khoi.txt', 'w') as f:
        f.write(token)
    with open('configttc_khoi.txt', 'r') as f:
      token = f.read()
    req = requests.post('https://tuongtaccheo.com/logintoken.php', headers={'Content-type':'application/x-www-form-urlencoded'}, data={'access_token':token})
    if req.json()['status'] == 'success':
      cookie = getcookie(token)
      user = req.json()['data']['user']
      sodu = req.json()['data']['sodu']
      print(f'{thanh_dep}{yellowb}Trạng Thái Token : {whiteb}[{greenb}LIVE{whiteb}]\n{thanh_dep}{yellowb}Tuongtaccheo.com :{greenb} Đăng nhập Thành Công !!!')
      break
    else:
      print(f'{thanh_dep}{yellowb}Trạng Thái Token : {whiteb}[{redb}DIE{whiteb}]\n{thanh_dep}{yellowb}Tuongtaccheo.com :{redb} Đăng nhập Thất Bại !!!')
      os.remove ('configttc.txt')
      continue
  bongoc(12)
  while True:
    if os.path.exists('CookieFB_khoi.txt'):
      print(f'{thanh_dep}{vang}[{trang}1{vang}] {cam}Sử Dụng Cookie Facebook Đã Lưu')
      print(f'{thanh_dep}{vang}[{trang}2{vang}] {cam}Nhập Cookie Facebook Mới')
      chon = input(f'{thanh_dep}{greenb}Nhập Lựa Chọn Của Bạn:{yellowb} ')
      if chon == '1':
        print('\033[38;5;208mĐang Lấy Dữ Liệu Đã Lưu')
        sleep(1)
        with open('CookieFB_khoi.txt', 'r') as f:
          listnick = json.loads(f.read())
          break
      elif chon == '2':
        print(f"{red}════════════════════════════════════════════════════")
        os.remove('CookieFB_khoi.txt')
      else:
        print(f'{red}Lựa Chọn Không Xác Định.')
        continue
    if not os.path.exists('CookieFB_khoi.txt'):
      listnick = Nhap_cookie()
      with open('CookieFB_khoi.txt', 'w') as f:
        json.dump(listnick, f)
        break
  banner()
  print(f'{thanh_dep}{greenb}Tên Tài Khoản: {yellowb}{user}')
  print(f'{thanh_dep}{redb}XU TTC HIỆN TẠI: {str(format(int(sodu),","))}')
  print(f'{thanh_dep}{purpleb}LIST COOKIE FACEBOOK: {len(listnick)}')
  bongoc(15)
  print(f'{thanh_dep}{greenb}Nhập {yellowb}[{redb}1{yellowb}] {greenb}Làm job LIKEVIPCHEO')
  print(f'{thanh_dep}{greenb}Nhập {yellowb}[{redb}2{yellowb}] {greenb}Làm job LIKETHUONGCHEO')
  print(f'{thanh_dep}{greenb}Nhập {yellowb}[{redb}3{yellowb}] {greenb}Làm job CAMXUCVIPCHEO')
  print(f'{thanh_dep}{greenb}Nhập {yellowb}[{redb}4{yellowb}] {greenb}Làm job CAMXUCTHUONGCHEO')
  print(f'{thanh_dep}{greenb}Nhập {yellowb}[{redb}5{yellowb}] {greenb}Làm job CAMXUCCMTCHEO')
  print(f'{thanh_dep}{greenb}Nhập {yellowb}[{redb}6{yellowb}] {greenb}Làm job CMTCHEO')
  print(f'{thanh_dep}{greenb}Nhập {yellowb}[{redb}7{yellowb}] {greenb}Làm job FOLLOWCHEO')
  print(f'{thanh_dep}{greenb}Nhập {yellowb}[{redb}8{yellowb}] {greenb}Làm job SHARECHEO')
  print(f'{thanh_dep}{greenb}Nhập {yellowb}[{redb}9{yellowb}] {greenb}Làm job LIKEPAGECHEO')
  bongoc(15)
  mau = [redb,greenb,yellowb,blueb,purpleb,lightblueb,cam]
  nan = random.choice(mau)
  print(f'\033[1;91m[\033[1;97m=.=\033[1;91m] \033[1;37m=>{nan} Có Thể Chọn Nhiều Nhiệm Vụ (Ví Dụ 123...)')
  nhiemvu = input(f'\033[1;91m[\033[1;97m=.=\033[1;91m] \033[1;37m=>{lightblueb} Nhập Số Để Chạy Nhiệm Vụ: ')
  delaymin = int(input(f'\033[1;91m[\033[1;97m=.=\033[1;91m] \033[1;37m=>{purpleb} Nhập delay min: '))
  delaymax = int(input(f'\033[1;91m[\033[1;97m=.=\033[1;91m] \033[1;37m=>{yellowb} Nhập delay max: '))
  print(f'\033[1;91m[\033[1;97m=.=\033[1;91m] \033[1;37m=>{greenb} Sau ______ Nhiệm Vụ Thì Kích Hoạt Chống Block.',end='\r')
  nvblock = int(input(f'\033[1;91m[\033[1;97m=.=\033[1;91m] \033[1;37m=>{greenb} Sau '))
  print(f'\033[1;91m[\033[1;97m=.=\033[1;91m] \033[1;37m=>{greenb} Sau {nvblock} Nhiệm Vụ Nghỉ Ngơi _____ Giây       ',end='\r')
  delaybl = int(input(f'\033[1;91m[\033[1;97m=.=\033[1;91m] \033[1;37m=>{greenb} Sau {nvblock} Nhiệm Vụ Nghỉ Ngơi '))
  doinick = int(input(f'{thanh_dep}{cam}Sau Bao Nhiêu Nhiệm Vụ Thì Đổi Nick: '))
  chonan = input(f'{thanh_dep}{greenb}Bạn Có Muốn Ẩn Id Facebook Không {redb}({yellowb}y/n{redb}):{yellowb} ')
  print(f'{redb}────────────────────────────────────────────────────────────')
  while True:
    if len(listnick) == 0:
      print(f'{red}Đã Xoá Tất Cả Cookie, Vui Lòng Nhập Lại')
      listnick = Nhap_cookie()
      with open('CookieFB_khoi.txt', 'w') as f:
        json.dump(listnick, f)
    for ck in listnick:
      loilike, loicamxuc, loicxcmt, loifl, loicmt, loishare, loilikepage = 0, 0, 0, 0, 0, 0, 0
      fb = Facebook_api(ck)
      info = fb.getinfo()
      if info != False:
        ten = info[0]
        uid = info[1]
      else:
        uid = ck.split('c_user=')[1].split(';')[0]
        print(f'{red}Cookie Tài Khoản {uid} Die', end='\r');sleep(3); print('                                     ', end = '\r' )
        listnick.remove(ck)
        continue
      if chonan == 'y':
        uid2 = uid[:3]+'#'*(len(uid)-6)+uid[-3:]
      else:
        uid2 = uid
      cauhinh = datnick(cookie,uid)
      if '1' in cauhinh:
        print(f'{greenb}Id Facebook:{yellowb} {uid2} {redb}|{yellowb} Tên Tài khoản:{lightblueb} {ten}')
      else:
        print(f'{redb}Cấu Hình Thất Bại Id Facebook:{greenb} {uid} {redb}| {yellowb}Tên Tài khoản:{lightblueb} {ten}')
      khoitool = 0
      while True:
        nvlikevip = 1 if '1' in nhiemvu else 0
        nvlikethuong = 1 if '2' in nhiemvu else 0
        nvreacvip = 1 if '3' in nhiemvu else 0
        nvreac = 1 if '4' in nhiemvu else 0
        nvreaccmt = 1 if '5' in nhiemvu else 0
        nvcmt = 1 if '6' in nhiemvu else 0
        nvfollow = 1 if '7' in nhiemvu else 0
        nvshare = 1 if '8' in nhiemvu else 0
        nvlikepage = 1 if '9' in nhiemvu else 0
        if nvlikevip == 1:
          nvlikevip = getlikevipcheo(cookie)
          like1 = nvlikevip.text
          like2 = nvlikevip.json()
          if len(like2) == 0:
            print(f'{cam}Hết Nhiệm Vụ Like Vip                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            nvlikevip = 0
          elif 'error' in like2:
            print(f'{cam}Lấy nhiệm vụ sau 15 giây                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            delay(15)
            nvlikevip = 0
          else:
            print(f'{cam}Tìm Thấy {lightblueb}{len(like2)} {cam}Nhiệm Vụ Like Vip                      ', end = '\r')
            for x in like2:
              try:
                idpost = x['idpost']
                id = x['idfb']
              except:
                delay(6)
              fb = Facebook_api(ck)
              info = fb.getdata()
              like = fb.reaction(info[0],info[1],id,'LIKE')
              if like == False:
                print(f"{red}FAIL LIKE: {lightblueb}{id}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                loilike += 1
                sleep(10)
              else:
                nhan = nhanxulikevip(cookie,idpost)
                if 'mess' in nhan:
                  xu = getxuttc(cookie)
                  dem += 1
                  time = datetime.now().strftime("%H:%M:%S")
                  print(f'{redb}| {yellowb}{dem}{redb} | {lightblueb}{time}{redb} | {yellowb}LIKEVIP{redb} | {white}{id}{redb} | {yellowb}+1100{redb} | {greenb}{str(format(int(xu),","))}')
                  loilike = 0
                  if dem % doinick == 0:
                    print(f'{whiteb}[{greenb}Total Cookie Facebook: {yellowb}{len(listnick)}{whiteb}] {whiteb}[{greenb}Tổng Xu: {yellowb}{str(format(int(xu),","))}]')
                    khoitool = 1
                    break
                  if dem % nvblock == 0:
                    delayblock(delaybl)
                  else:
                    delay(randint(delaymin, delaymax))
              if loilike >= 12:
                info = fb.getinfo()
                uid = ck.split('c_user=')[1].split(';')[0]
                if info == False:
                  print(f'{redb}Tài khoản Có UID {yellowb}{uid}{redb} Bị Out Hoặc Bị Facebook checkpoint !!')
                else:
                  print(f'{red}Tài Khoản {vang}{ten} {red}Đã Bị Block {vang}Like {red}!!!					')
                listnick.remove(ck)
                khoitool = 1
                break
        if khoitool == 1:
          break
        if nvlikethuong == 1:
          listlikethuong = getlikethuong(cookie)
          liketh1 = listlikethuong.text
          liketh2 = listlikethuong.json()
          if len(liketh2) == 0:
            print(f'{red}Hết Nhiệm Vụ Like Thường                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            nvlikethuong = 0
          elif 'error' in liketh2:
            print(f'{cam}Lấy nhiệm vụ sau 15 giây                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            delay(15)
            nvlikethuong = 0
          else:
            print(f'{cam}Tìm Thấy {lightblueb}{len(liketh2)} {cam}Nhiệm Vụ Like Xu Thường                      ', end = '\r')
            for x in liketh2:
              try:
                idpost = x['idpost']
                id = x['idfb']
              except:
                delay(6)
              fb = Facebook_api(ck)
              info = fb.getdata()
              like = fb.reaction(info[0],info[1],id,'LIKE')
              if like == False:
                print(f"{red}FAIL LIKE: {lightblueb}{id}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                loilike += 1
                sleep(10)
              else:
                nhan = nhanxulikethuong(cookie,idpost)
                if 'mess' in nhan:
                  xu = getxuttc(cookie)
                  dem += 1
                  time = datetime.now().strftime("%H:%M:%S")
                  print(f'{redb}| {yellowb}{dem}{redb} | {lightblueb}{time}{redb} | {yellowb}LIKETHUONG{redb} | {white}{id}{redb} | {yellowb}+400{redb} | {greenb}{str(format(int(xu),","))}')
                  loilike = 0
                  if dem % doinick == 0:
                    print(f'{whiteb}[{greenb}Total Cookie Facebook: {yellowb}{len(listnick)}{whiteb}] {whiteb}[{greenb}Tổng Xu: {yellowb}{str(format(int(xu),","))}]')
                    khoitool = 1
                    break
                  if dem % nvblock == 0:
                    delayblock(delaybl)
                  else:
                    delay(randint(delaymin, delaymax))
              if loilike >= 12:
                info = fb.getinfo()
                uid = ck.split('c_user=')[1].split(';')[0]
                if info == False:
                  print(f'{redb}Tài khoản Có UID {yellowb}{uid}{redb} Bị Out Hoặc Bị Facebook checkpoint !!')
                else:
                  print(f'{red}Tài Khoản {vang}{ten} {red}Đã Bị Block {vang}Like {red}!!!					')
                listnick.remove(ck)
                khoitool = 1
                break
        if khoitool == 1:
          break
        if nvreacvip == 1:
          listcxvip = getcamxucvip(cookie)
          camxuc1 = listcxvip.text
          camxuc2 = listcxvip.json()
          if len(camxuc2) == 0:
            print(f'{cam}Hết Nhiệm Vụ Cảm Xúc Vip                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            nvreacvip = 0
          if 'error' in camxuc2:
            print(f'{cam}Lấy nhiệm vụ sau 15 giây                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            delay(15)
            nvreacvip = 0
          else:
            print(f'{cam}Tìm Thấy {lightblueb}{len(camxuc2)} {cam}Nhiệm Vụ Cảm Xúc Vip                       ', end = '\r')
            for x in camxuc2:
              try:
                idpost = x['idpost']
                loaicx = x['loaicx']
                id = x['idfb']
              except:
                delay(6)
              fb = Facebook_api(ck)
              info = fb.getdata()
              lam = fb.reaction(info[0],info[1],id,loaicx)
              if lam == False:
                print(f"{red}FAIL {loaicx}: {lightblueb}{id}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                loicamxuc += 1
                sleep(10)
              else:
                nhan = nhanxucamxucvip(cookie,idpost,loaicx)
                if 'mess' in nhan:
                  xu = getxuttc(cookie)
                  dem += 1
                  time = datetime.now().strftime("%H:%M:%S")
                  print(f'{redb}| {yellowb}{dem}{redb} | {lightblueb}{time}{redb} | {yellowb}{loaicx}VIP{redb} | {white}{id}{redb} | {yellowb}+1100{redb} | {greenb}{str(format(int(xu),","))}')
                  loicamxuc = 0
                  if dem % doinick == 0:
                    print(f'{whiteb}[{greenb}Total Cookie Facebook: {yellowb}{len(listnick)}{whiteb}] {whiteb}[{greenb}Tổng Xu: {yellowb}{str(format(int(xu),","))}]')
                    khoitool = 1
                    break
                  if dem % nvblock == 0:
                    delayblock(delaybl)
                  else:
                    delay(randint(delaymin, delaymax))
              if loicamxuc >= 12:
                info = fb.getinfo()
                uid = ck.split('c_user=')[1].split(';')[0]
                if info == False:
                  print(f'{redb}Tài khoản Có UID {yellowb}{uid}{redb} Bị Out Hoặc Bị Facebook checkpoint !!')
                else:
                  print(f'{red}Tài Khoản {vang}{ten} {red}Đã Bị Block {vang}CẢM XÚC {red}!!!					')
                  listnick.remove(ck)
                  khoitool = 1
                break
        if khoitool == 1:
          break
        if nvreac == 1:
          listnvcx = getcamxucthuong(cookie)
          camxuc1 = listnvcx.text
          camxuc2 = listnvcx.json()
          if len(camxuc2) == []:
            print(f'{cam}Hết Nhiệm Vụ Cảm Xúc                           ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            nvreac = 0
          elif 'error' in camxuc2:
            print(f'{cam}Lấy nhiệm vụ sau 15 giây                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            delay(15)
            nvreac = 0
          else:
            print(f'{cam}Tìm Thấy {lightblueb}{len(camxuc2)} {cam}Nhiệm Vụ Cảm Xúc                      ', end = '\r')
            for x in camxuc2:
              try:
                idpost = x['idpost']
                loaicx = x['loaicx']
                id = x['idfb']
              except:
                delay(6)
              fb = Facebook_api(ck)
              info = fb.getdata()
              lam = fb.reaction(info[0],info[1],id,loaicx)
              if lam == False:
                print(f"{red}FAIL {loaicx}: {lightblueb}{id}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                loicamxuc += 1
                sleep(10)
              else:
                nhan = nhanxucamxucthuong(cookie,idpost,loaicx)
                if 'mess' in nhan:
                  xu = getxuttc(cookie)
                  dem += 1
                  time = datetime.now().strftime("%H:%M:%S")
                  print(f'{redb}| {yellowb}{dem}{redb} | {lightblueb}{time}{redb} | {yellowb}{loaicx}THUONG{redb} | {white}{id}{redb} | {yellowb}+400{redb} | {greenb}{str(format(int(xu),","))}')
                  loicamxuc = 0
                  if dem % doinick == 0:
                    print(f'{whiteb}[{greenb}Total Cookie Facebook: {yellowb}{len(listnick)}{whiteb}] {whiteb}[{greenb}Tổng Xu: {yellowb}{str(format(int(xu),","))}]')
                    khoitool = 1
                    break
                  if dem % nvblock == 0:
                    delayblock(delaybl)
                  else:
                    delay(randint(delaymin, delaymax))
              if loicamxuc >= 12:
                info = fb.getinfo()
                uid = ck.split('c_user=')[1].split(';')[0]
                if info == False:
                  print(f'{redb}Tài khoản Có UID {yellowb}{uid}{redb} Bị Out Hoặc Bị Facebook checkpoint !!')
                else:
                  print(f'{red}Tài Khoản {vang}{ten} {red}Đã Bị Block {vang}CẢM XÚC {red}!!!					')
                  listnick.remove(ck)
                  khoitool = 1
                break
        if khoitool == 1:
          break
        if nvreaccmt == 1:
          listreaccmt = getcamxuccmt(cookie)
          like1 = listreaccmt.text
          like2 = listreaccmt.json()
          if len(like2) == 0:
            print(f'{cam}Hết Nhiệm Vụ Cảm Xúc Cmt             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            nvreaccmt = 0
          elif 'error' in like2:
            print(f'{cam}Lấy nhiệm vụ sau 15 giây                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            delay(15)
            nvreaccmt = 0
          else:
            print(f'{cam}Tìm Thấy {lightblueb}{len(like2)} {cam}Nhiệm Vụ Cảm Xúc Cmt                     ', end = '\r')
            for x in like2:
              try:
                idpost = x['idpost']
                link = x['link']
                loaicx = x['loaicx']
              except:
                delay(6)
              fb = Facebook_api(ck)
              info = fb.getdata()
              uid = idpost.split('_')[1]
              lam = fb.reactioncmt(info[0],info[1],loaicx,uid)
              if lam == False:
                print(f"{red}FAIL {loaicx}CMT: {lightblueb}{idpost}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                loicxcmt += 1
                sleep(10)
              else:
                nhan = nhanxucamxuccmt(cookie,idpost,loaicx)
                if 'mess' in nhan:
                  xu = getxuttc(cookie)
                  dem += 1
                  time = datetime.now().strftime("%H:%M:%S")
                  print(f'{redb}| {yellowb}{dem}{redb} | {lightblueb}{time}{redb} | {yellowb}{loaicx}CMT{redb} | {white}{uid}{redb} | {yellowb}+600{redb} | {greenb}{str(format(int(xu),","))}')
                  loicxcmt = 0
                  if dem % doinick == 0:
                    print(f'{whiteb}[{greenb}Total Cookie Facebook: {yellowb}{len(listnick)}{whiteb}] {whiteb}[{greenb}Tổng Xu: {yellowb}{str(format(int(xu),","))}]')
                    khoitool = 1
                    break
                  if dem % nvblock == 0:
                    delayblock(delaybl)
                  else:
                    delay(randint(delaymin, delaymax))
              if loicxcmt >= 12:
                info = fb.getinfo()
                uid = ck.split('c_user=')[1].split(';')[0]
                if info == False:
                  print(f'{redb}Tài khoản Có UID {yellowb}{uid}{redb} Bị Out Hoặc Bị Facebook checkpoint !!')
                else:
                  print(f'{red}Tài Khoản {vang}{ten} {red}Đã Bị Block {vang}CẢM XÚC CMT{red}!!!					')
                  listnick.remove(ck)
                  khoitool = 1
                break
        if khoitool == 1:
          break
        if nvcmt == 1:
          listcmt = getcmtpost(cookie)
          like1 = listcmt.text
          like2 = listcmt.json()
          if len(like2) == 0:
            print(f'{cam}Hết Nhiệm Vụ Cmt              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            nvcmt = 0
          elif 'error' in like2:
            print(f'{cam}Lấy nhiệm vụ sau 15 giây                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            delay(15)
            nvcmt = 0
          else:
            print(f'{cam}Tìm Thấy {lightblueb}{len(like2)} {cam}Nhiệm Vụ Cmt                      ', end = '\r')
            for x in like2:
              try:
                idpost = x['idpost']
                ndcmt = json.loads(x["nd"])[0]
              except:
                delay(6)
              fb = Facebook_api(ck)
              info = fb.getdata()
              lam = fb.cmt(info[0],info[1],ndcmt,idpost)
              if lam == False:
                print(f"{red}FAIL {loaicx}CMT: {lightblueb}{idpost}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                loicmt += 1
                sleep(10)
              else:
                nhan = nhanxucmt(cookie,idpost)
                if 'mess' in nhan:
                  xu = getxuttc(cookie)
                  dem += 1
                  time = datetime.now().strftime("%H:%M:%S")
                  print(f'{redb}| {yellowb}{dem}{redb} | {lightblueb}{time}{redb} | {yellowb}CMT{redb} | {white}{uid}{redb} | {yellowb}+1400{redb} | {greenb}{str(format(int(xu),","))}')
                  loicmt = 0
                  if dem % doinick == 0:
                    print(f'{whiteb}[{greenb}Total Cookie Facebook: {yellowb}{len(listnick)}{whiteb}] {whiteb}[{greenb}Tổng Xu: {yellowb}{str(format(int(xu),","))}]')
                    khoitool = 1
                    break
                  if dem % nvblock == 0:
                    delayblock(delaybl)
                  else:
                    delay(randint(delaymin, delaymax))
              if loicmt >= 12:
                info = fb.getinfo()
                uid = ck.split('c_user=')[1].split(';')[0]
                if info == False:
                  print(f'{redb}Tài khoản Có UID {yellowb}{uid}{redb} Bị Out Hoặc Bị Facebook checkpoint !!')
                else:
                  print(f'{red}Tài Khoản {vang}{ten} {red}Đã Bị Block {vang}CMT{red}!!!					')
                  listnick.remove(ck)
                  khoitool = 1
                break
        if khoitool == 1:
          break
        if nvfollow == 1:
          listfollow = getfollowcheo(cookie)
          like1 = listfollow.text
          like2 = listfollow.json()
          if len(like2) == 0:
            print(f'{cam}Hết Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            nvfollow = 0
          elif 'error' in like2:
            print(f'{cam}Lấy nhiệm vụ sau 15 giây                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            delay(15)
            nvfollow = 0
          else:
            print(f'{cam}Tìm Thấy {lightblueb}{len(like2)} {cam}Nhiệm Vụ Follow                      ', end = '\r')
            for x in like2:
              try:
                idpost = x['idpost']
              except:
                delay(6)
              fb = Facebook_api(ck)
              info = fb.getdata()
              lam = fb.follow(info[0],info[1],idpost)
              if lam == False:
                print(f"{red}FAIL FOLLOW: {lightblueb}{idpost}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                loifl += 1
                sleep(10)
              else:
                nhan = nhanxufollow(cookie,idpost)
                if 'mess' in nhan:
                  xu = getxuttc(cookie)
                  dem += 1
                  time = datetime.now().strftime("%H:%M:%S")
                  print(f'{redb}| {yellowb}{dem}{redb} | {lightblueb}{time}{redb} | {yellowb}FOLLOW{redb} | {white}{idpost}{redb} | {yellowb}+700{redb} | {greenb}{str(format(int(xu),","))}')
                  loifl = 0
                  if dem % doinick == 0:
                    print(f'{whiteb}[{greenb}Total Cookie Facebook: {yellowb}{len(listnick)}{whiteb}] {whiteb}[{greenb}Tổng Xu: {yellowb}{str(format(int(xu),","))}]')
                    khoitool = 1
                    break
                  if dem % nvblock == 0:
                    delayblock(delaybl)
                  else:
                    delay(randint(delaymin, delaymax))
              if loifl >= 12:
                info = fb.getinfo()
                uid = ck.split('c_user=')[1].split(';')[0]
                if info == False:
                  print(f'{redb}Tài khoản Có UID {yellowb}{uid}{redb} Bị Out Hoặc Bị Facebook checkpoint !!')
                else:
                  print(f'{red}Tài Khoản {vang}{ten} {red}Đã Bị Block {vang}FOLLOW{red}!!!					')
                  listnick.remove(ck)
                  khoitool = 1
                break
        if khoitool == 1:
          break
        if nvshare == 1:
          listshare = getchiasepost(cookie)
          like1 = listshare.text
          like2 = listshare.json()
          if len(like2) == 0:
            print(f'{cam}Hết Nhiệm Vụ Share              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            nvshare = 0
          elif 'error' in like2:
            print(f'{cam}Lấy nhiệm vụ sau 15 giây                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            delay(15)
            nvshare = 0
          else:
            print(f'{cam}Tìm Thấy {lightblueb}{len(like2)} {cam}Nhiệm Vụ Share                      ', end = '\r')
            for x in like2:
              try:
                idpost = x['idpost']
              except:
                delay(6)
              fb = Facebook_api(ck)
              info = fb.getdata()
              lam = fb.Sharepost(info[0],info[1],idpost)
              if lam == False:
                print(f"{red}FAIL SHARE: {lightblueb}{idpost}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                loishare += 1
                sleep(10)
              else:
                nhan = nhanxusharepost(cookie,idpost)
                if 'mess' in nhan:
                  xu = getxuttc(cookie)
                  dem += 1
                  time = datetime.now().strftime("%H:%M:%S")
                  print(f'{redb}| {yellowb}{dem}{redb} | {lightblueb}{time}{redb} | {yellowb}SHARE{redb} | {white}{idpost}{redb} | {yellowb}+600{redb} | {greenb}{str(format(int(xu),","))}')
                  loishare = 0
                  if dem % nvblock == 0:
                    delayblock(delaybl)
                  else:
                    delay(randint(delaymin, delaymax))
              if loishare >= 12:
                info = fb.getinfo()
                uid = ck.split('c_user=')[1].split(';')[0]
                if info == False:
                  print(f'{redb}Tài khoản Có UID {yellowb}{uid}{redb} Bị Out Hoặc Bị Facebook checkpoint !!')
                else:
                  print(f'{red}Tài Khoản {vang}{ten} {red}Đã Bị Block {vang}SHARE{red}!!!					')
                  listnick.remove(ck)
                  khoitool = 1
                break
        if khoitool == 1:
          break
        if nvlikepage == 1:
          listlikepage = getlikepagecheo(cookie)
          like1 = listlikepage.text
          like2 = listlikepage.json()
          if len(like2) == 0:
            print(f'{cam}Hết Nhiệm Vụ Like Page             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            nvlikepage = 0
          elif 'error' in like2:
            print(f'{cam}Lấy nhiệm vụ sau 15 giây                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
            delay(15)
            nvlikepage = 0
          else:
            print(f'{cam}Tìm Thấy {lightblueb}{len(like2)} {cam}Nhiệm Vụ Like Page                     ', end = '\r')
            for x in like2:
              try:
                idpost = x['idpost']
              except:
                delay(6)
              fb = Facebook_api(ck)
              info = fb.getdata()
              lam = fb.likepage(info[0],info[1],idpost)
              if lam == False:
                print(f"{red}FAIL LIKEPAGE: {lightblueb}{idpost}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                loilikepage += 1
                sleep(10)
              else:
                nhan = nhanxulikepage(cookie,idpost)
                if 'mess' in nhan:
                  xu = getxuttc(cookie)
                  dem += 1
                  time = datetime.now().strftime("%H:%M:%S")
                  print(f'{redb}| {yellowb}{dem}{redb} | {lightblueb}{time}{redb} | {yellowb}LIKEPAGE{redb} | {white}{idpost}{redbhttps://www.facebook.com/share/p/14JnpaxdByG/yellowb}+1300{redb} | {greenb}{str(format(int(xu),","))}')
                  loilikepage = 0
                  if dem % nvblock == 0:
                    delayblock(delaybl)
                  else:
                    delay(randint(delaymin, delaymax))
              if loilikepage >= 12:
                info = fb.getinfo()
                uid = ck.split('c_user=')[1].split(';')[0]
                if info == False:
                  print(f'{redb}Tài khoản Có UID {yellowb}{uid}{redb} Bị Out Hoặc Bị Facebook checkpoint !!')
                else:
                  print(f'{red}Tài Khoản {vang}{ten} {red}Đã Bị Block {vang}LIKEPAGE{red}!!!					')
                  listnick.remove(ck)
                  khoitool = 1
                break
        if khoitool == 1:
          break
        if loilike + loicamxuc + loicxcmt + loifl + loicmt + loishare + loilikepage == 0:
          for i in range(360,-1,-1):
            print(f'{redb}Tất Cả Nhiệm Vụ Đã Hết Vui Lòng Chờ {greenb}{i}{redb} Giây          ', end='\r')
            sleep(1)
if __name__ == '__main__':
	main()
