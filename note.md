# 爬虫

## 代理ip

###



## B站关键词搜索

- https://api.bilibili.com/x/web-interface/wbi/search/default

```
web_location: 333.337
w_rid: 02aed09ec2d7be83881c3187b8d2a611
wts: 1740395309
```

- https://api.bilibili.com/x/web-interface/wbi/search/all/v2

- https://api.bilibili.com/x/web-interface/wbi/search/type

```
search_type: video-----media_bangumi-----media_ft-----live-----article-----bili_user
__refresh__: true
page: 1
page_size: 42会根据不同情况变，不发是不是默认
综合order: click-----pubdate-----dm-----stow
视频order: click-----pubdate-----dm-----stow

duration: 0-4
pubtime_begin_s: 0
pubtime_end_s: 0
platform: pc
keyword: 神经网络与深度学习邱锡鹏
source_tag: 3
tids: 1动画13番剧167国创3音乐129舞蹈4游戏36知识188科技234运动223汽车160生活211美食217动物圈119鬼畜155时尚202资讯5娱乐181影视177纪录片23电影11电视剧
```

- https://api.bilibili.com/x/player/wbi/playurl

```
avid: 114053880021329
bvid: BV1shASe2E7r
cid: 28543484783
qn: 32
fnver: 0
fnval: 2000
fourk: 1
gaia_source: view-card
from_client: BROWSER
session: 6ec89c5f46c8b3eb313689c12cd4f0b3
web_location: 1315873
w_rid: def98d95f1695dd6d4479ee755a48816
wts: 1740402501
gaia_source: pre-load

avid: 114053880021329
bvid: BV1shASe2E7r
cid: 28543484783
qn: 32
fnver: 0
fnval: 2000
fourk: 1
platform: pc
```

## 抖音关键词搜索

- https://www.douyin.com/aweme/v1/web/general/search/stream/
  - 综合信息  –>可获取logid 即search_id
  - type：1、996、

```
aid: 6383
browser_language: zh-CN
browser_name: Chrome
browser_online: true
browser_platform: Win32
browser_version: 133.0.0.0
channel: channel_pc_web
cookie_enabled: true
	count: 10
cpu_core_num: 8
device_memory: 8
device_platform: webapp
downlink: 10
effective_type: 4g
enable_history: 1
engine_name: Blink
engine_version: 133.0.0.0
		filter_selected: {"sort_type":"2","publish_time":"0"}
from_group_id: 
		is_filter_search: 1
keyword: 神经网络
list_type: multi
need_filter_settings: 1
	offset: 0
os_name: Windows
os_version: 10
pc_client_type: 1
pc_libra_divert: Windows
platform: PC
query_correct_type: 1
round_trip_time: 50
screen_height: 1080
screen_width: 1920
	search_channel: aweme_general
	search_source: switch_tab
support_dash: 1
support_h265: 1
uifid: c4a29131752d59acb78af076c3dbdd52744118e38e80b4b96439ef1e20799db0b4e1b80199ec66c165c6b673d009d757ab9665806eb08d7aa0fb330d1531244d449a7eddc803033eb3ab027402d6d1b588531dcc1ac917198d4a63080173c8ceb70d362d3dca76a35e6155ab2f6b97b6efa3a3330d439196388b8e8a25fa2dde4cd1df49d94cbe73623dc2d124bcf4607b094a4f37189ea8febd706e5f816ca2
version_code: 190600
version_name: 19.6.0
webid: 7464257619323651624
```

- https://www.douyin.com/aweme/v1/web/general/search/single/
  - 重要搜索信息


```
device_platform: webapp
aid: 6383
channel: channel_pc_web
	search_channel: aweme_general
enable_history: 1
	filter_selected: {"sort_type":"2","publish_time":"0"}
	keyword: 神经网络
	search_source: tab_search
query_correct_type: 1
	is_filter_search: 1
			from_group_id: 
	offset: 20
	count: 10
need_filter_settings: 0
list_type: multi
			search_id: 20250227222310313C41FA0B916C1D7547
update_version_code: 170400
pc_client_type: 1
pc_libra_divert: Windows
support_h265: 1
support_dash: 1
version_code: 190600
version_name: 19.6.0
cookie_enabled: true
screen_width: 1920
screen_height: 1080
browser_language: zh-CN
browser_platform: Win32
browser_name: Chrome
browser_version: 133.0.0.0
browser_online: true
engine_name: Blink
engine_version: 133.0.0.0
os_name: Windows
os_version: 10
cpu_core_num: 8
device_memory: 8
platform: PC
downlink: 10
effective_type: 4g
round_trip_time: 50
webid: 7464257619323651624
uifid: c4a29131752d59acb78af076c3dbdd52744118e38e80b4b96439ef1e20799db0b4e1b80199ec66c165c6b673d009d757ab9665806eb08d7aa0fb330d1531244d449a7eddc803033eb3ab027402d6d1b588531dcc1ac917198d4a63080173c8ceb70d362d3dca76a35e6155ab2f6b97b6efa3a3330d439196388b8e8a25fa2dde4cd1df49d94cbe73623dc2d124bcf4607b094a4f37189ea8febd706e5f816ca2
```

- https://www.douyin.com/aweme/v1/web/im/user/active/update/
  - 更新logid


```
device_platform: webapp
aid: 6383
channel: channel_pc_web
	action: heartbeat
new_user_login: 0
update_version_code: 170400
pc_client_type: 1
pc_libra_divert: Windows
support_h265: 1
support_dash: 1
version_code: 170400
version_name: 17.4.0
cookie_enabled: true
screen_width: 1920
screen_height: 1080
browser_language: zh-CN
browser_platform: Win32
browser_name: Chrome
browser_version: 133.0.0.0
browser_online: true
engine_name: Blink
engine_version: 133.0.0.0
os_name: Windows
os_version: 10
cpu_core_num: 8
device_memory: 8
platform: PC
downlink: 10
effective_type: 4g
round_trip_time: 50
webid: 7464257619323651624
uifid: c4a29131752d59acb78af076c3dbdd52744118e38e80b4b96439ef1e20799db0b4e1b80199ec66c165c6b673d009d757ab9665806eb08d7aa0fb330d1531244d449a7eddc803033eb3ab027402d6d1b588531dcc1ac917198d4a63080173c8ceb70d362d3dca76a35e6155ab2f6b97b6efa3a3330d439196388b8e8a25fa2dde4cd1df49d94cbe73623dc2d124bcf4607b094a4f37189ea8febd706e5f816ca2
```

- https://www.douyin.com/aweme/v1/web/search/item/
  - 搜索视频栏


```
device_platform: webapp
aid: 6383
channel: channel_pc_web
	search_channel: aweme_video_web
enable_history: 1
		sort_type: 2
		publish_time: 7
		filter_duration: 1-5
		search_range: 2
	keyword: 神经网络
	search_source: switch_tab  tab_search
query_correct_type: 1
	is_filter_search: 0
from_group_id: 
	offset: 20
	count: 10
	need_filter_settings: 0 1 
list_type: multi
	search_id: 20250227222042A774B8A0D53B611D2290   offset的时候有
update_version_code: 170400
pc_client_type: 1
pc_libra_divert: Windows
support_h265: 1
support_dash: 1
version_code: 170400
version_name: 17.4.0
cookie_enabled: true
screen_width: 1920
screen_height: 1080
browser_language: zh-CN
browser_platform: Win32
browser_name: Chrome
browser_version: 133.0.0.0
browser_online: true
engine_name: Blink
engine_version: 133.0.0.0
os_name: Windows
os_version: 10
cpu_core_num: 8
device_memory: 8
platform: PC
downlink: 10
effective_type: 4g
round_trip_time: 50
webid: 7464257619323651624
uifid: c4a29131752d59acb78af076c3dbdd52744118e38e80b4b96439ef1e20799db0b4e1b80199ec66c165c6b673d009d757ab9665806eb08d7aa0fb330d1531244d449a7eddc803033eb3ab027402d6d1b588531dcc1ac917198d4a63080173c8ceb70d362d3dca76a35e6155ab2f6b97b6efa3a3330d439196388b8e8a25fa2dde4cd1df49d94cbe73623dc2d124bcf4607b094a4f37189ea8febd706e5f816ca2
```

- https://www.douyin.com/aweme/v1/web/discover/search/
  - 搜索用户栏


```
device_platform: webapp
aid: 6383
channel: channel_pc_web
search_channel: aweme_user_web
keyword: 神经网络
search_source: switch_tab
query_correct_type: 1
is_filter_search: 0
from_group_id: 
offset: 12
count: 10
need_filter_settings: 0
list_type: multi
search_id: 2025022722521302BE395B55160721A2B7
update_version_code: 170400
pc_client_type: 1
pc_libra_divert: Windows
support_h265: 1
support_dash: 1
version_code: 170400
version_name: 17.4.0
cookie_enabled: true
screen_width: 1920
screen_height: 1080
browser_language: zh-CN
browser_platform: Win32
browser_name: Chrome
browser_version: 133.0.0.0
browser_online: true
engine_name: Blink
engine_version: 133.0.0.0
os_name: Windows
os_version: 10
cpu_core_num: 8
device_memory: 8
platform: PC
downlink: 10
effective_type: 4g
round_trip_time: 50
webid: 7464257619323651624
uifid: c4a29131752d59acb78af076c3dbdd52744118e38e80b4b96439ef1e20799db0b4e1b80199ec66c165c6b673d009d757ab9665806eb08d7aa0fb330d1531244d449a7eddc803033eb3ab027402d6d1b588531dcc1ac917198d4a63080173c8ceb70d362d3dca76a35e6155ab2f6b97b6efa3a3330d439196388b8e8a25fa2dde4cd1df49d94cbe73623dc2d124bcf4607b094a4f37189ea8febd706e5f816ca2
msToken: Du6oxa9SbB_m3L8VvtUJBUpNIY6A3WdciS8c6M8W9CoKTyCL3Hna6r27Qx5ligv_K2OjHur0eZ06_6pNpPfP8VrWbIycNjdmjK1MDl7ZGeB8FqQglKNMJ3bhdpxa90DK22ZFWAId3aeUqogK3X3skcuJSDhD6ecwpXlCQVQBGlRTUA==
a_bogus: dX45DeXjmpAjKdFG8CBKy6BUHzfANsuy3aixWw5leOxrGXUTGSNMgac/axza//TkMWpTwK/HXn4/TfnbQUt0ZoqpKspvug4R005cIW6o8qN4G0JQgrb8CwTFKwMnUR4qa55JiIDI8Ueq6jnAkrdu/d-rH/KKQ5SBB1xRkMucE9s61MgAL3clPQSgThTqnj==
```

- https://www.douyin.com/aweme/v1/web/live/search/
  - 搜索直播栏


```
device_platform: webapp
aid: 6383
channel: channel_pc_web
search_channel: aweme_live
keyword: 神经网络
search_source: switch_tab
query_correct_type: 1
is_filter_search: 0
from_group_id: 
offset: 0
count: 15
need_filter_settings: 1
list_type: multi
update_version_code: 170400
pc_client_type: 1
pc_libra_divert: Windows
support_h265: 1
support_dash: 1
version_code: 170400
version_name: 17.4.0
cookie_enabled: true
screen_width: 1920
screen_height: 1080
browser_language: zh-CN
browser_platform: Win32
browser_name: Chrome
browser_version: 133.0.0.0
browser_online: true
engine_name: Blink
engine_version: 133.0.0.0
os_name: Windows
os_version: 10
cpu_core_num: 8
device_memory: 8
platform: PC
downlink: 10
effective_type: 4g
round_trip_time: 50
webid: 7464257619323651624
uifid: c4a29131752d59acb78af076c3dbdd52744118e38e80b4b96439ef1e20799db0b4e1b80199ec66c165c6b673d009d757ab9665806eb08d7aa0fb330d1531244d449a7eddc803033eb3ab027402d6d1b588531dcc1ac917198d4a63080173c8ceb70d362d3dca76a35e6155ab2f6b97b6efa3a3330d439196388b8e8a25fa2dde4cd1df49d94cbe73623dc2d124bcf4607b094a4f37189ea8febd706e5f816ca2
msToken: a90vGlruGLrdENVIt9DvxqsDMvv-Yuf8yOzPCXgqDWBeJ6zrfF42hKAG5inTiOjHo5MY-I-EFLoKn-ORJhWtkuSWLuaH1yv83R7T2jlz1muFAlmJWUyTQcEXf5SVFVrMkLXBOPbctgzSfKQmlUP___rTfKEHrNiL4L8DGTAcqNxIsA==
a_bogus: Ey0nDw7LY2mnOVFt8cp2y6/UeAV/rP8yzFT2SYclHONpG70GtuNNDntDcowcvdf0uup0wC-H6nlMbEVb/0tiZqrkFmhDu2tbQz55I0XogqN4G0kQDNbECwTzqwMnUbsq-5V7iAkI8UeHgVxAhHQE/dlJH/uF5RWBPZxWkMYbN9Bh10yAE1clPdGdiXsqNE==
```

- https://www.douyin.com/aweme/v1/web/comment/list/

```
device_platform: webapp
aid: 6383
channel: channel_pc_web
aweme_id: 7427381362337778980
		cursor: 0
count: 20
item_type: 0
insert_ids: 
whale_cut_token: 
cut_version: 1
rcFT: 
update_version_code: 170400
pc_client_type: 1
pc_libra_divert: Windows
support_h265: 1
support_dash: 1
version_code: 170400
version_name: 17.4.0
cookie_enabled: true
screen_width: 1920
screen_height: 1080
browser_language: zh-CN
browser_platform: Win32
browser_name: Chrome
browser_version: 133.0.0.0
browser_online: true
engine_name: Blink
engine_version: 133.0.0.0
os_name: Windows
os_version: 10
cpu_core_num: 8
device_memory: 8
platform: PC
downlink: 10
effective_type: 4g
round_trip_time: 50
webid: 7464257619323651624
uifid: c4a29131752d59acb78af076c3dbdd52744118e38e80b4b96439ef1e20799db0b4e1b80199ec66c165c6b673d009d757ab9665806eb08d7aa0fb330d1531244d449a7eddc803033eb3ab027402d6d1b588531dcc1ac917198d4a63080173c8ceb70d362d3dca76a35e6155ab2f6b97b6efa3a3330d439196388b8e8a25fa2dde4cd1df49d94cbe73623dc2d124bcf4607b094a4f37189ea8febd706e5f816ca2
msToken: Ecx8KjEYWayrt_zcPt4viQJdbcvBcIScmmzYSfX-_BfE1objH39Zkk1rRk2Brn-s03PYbHI3nD49egkcS3qnVvu4xD6RiI6zpe3z6eX1Nj86mxl2vFocGVH2t40Rx21Ku2zOH6fVwIUA6zUlUNAIz8wfg07a2CV0dSaRPDxBfwKMAA==
a_bogus: YJUnkHSwQoA5Pd/G8Kp2yWAlnU9ANPuy5liOWPBUy59ATHUTWYNpgxeIrxwOCtiBPRpkwFQHArU/zDdbK07zZF/kwsZfSqsfsUVAIWvLZqi4T0kQLqjLCuTzuwMNURTqe5VXiAg6MUt96VVAkNQD/Q5re/KF5cWBF1OykMTci9B61zgAL3c1PdGkP7Gq9j==

```

- https://www.douyin.com/aweme/v1/web/comment/list/reply/
  - cursor: 3
    total: 4 

```
device_platform: webapp
aid: 6383
channel: channel_pc_web
	item_id: 7427381362337778980
		comment_id: 7454963318399468288
cut_version: 1
cursor: 0
count: 3
item_type: 0
update_version_code: 170400
pc_client_type: 1
pc_libra_divert: Windows
support_h265: 1
support_dash: 1
version_code: 170400
version_name: 17.4.0
cookie_enabled: true
screen_width: 1920
screen_height: 1080
browser_language: zh-CN
browser_platform: Win32
browser_name: Chrome
browser_version: 133.0.0.0
browser_online: true
engine_name: Blink
engine_version: 133.0.0.0
os_name: Windows
os_version: 10
cpu_core_num: 8
device_memory: 8
platform: PC
downlink: 10
effective_type: 4g
round_trip_time: 50
webid: 7464257619323651624
uifid: c4a29131752d59acb78af076c3dbdd52744118e38e80b4b96439ef1e20799db0b4e1b80199ec66c165c6b673d009d757ab9665806eb08d7aa0fb330d1531244d449a7eddc803033eb3ab027402d6d1b588531dcc1ac917198d4a63080173c8ceb70d362d3dca76a35e6155ab2f6b97b6efa3a3330d439196388b8e8a25fa2dde4cd1df49d94cbe73623dc2d124bcf4607b094a4f37189ea8febd706e5f816ca2
msToken: RY49ZWDm9ThxomFuRHUk8KS-CBm5gruKoD38k8ZJYJmNBS3x34p4DQF4IFxiNmmTMPT964SqoKywy48Cakjx6M_oO-OGR5CYi_Cn2xWprnNMye7Q5LEbPYKWKMTCB30tFo-y2XM9alrwkTkN_BJ3HxCKyma-l_AKBwGe_bkQ7xeY5g==
a_bogus: dv45D7SLxq/RPdKSYKB2yfAUb1LMNsSyyBidWrOUCNqEG7tb8YNPLOtqroqOGn7TmSpTwe/H1r-/EjxbQs7hZPqkqmhfuhzy/zVnIhXLZqqmG0iQgNjmCzuzKw0r0bTq-A5Ji1D6gUeq6fVAwHQu/Blry/KFQb8BF1xRk2zci9B6ZzyAL1c3PdbBqhVY


```

- https://www.douyin.com/aweme/v1/web/danmaku/get_v2/
- https://www.douyin.com/aweme/v1/web/danmaku/conf/get/
  - 弹幕

```
device_platform: webapp
aid: 6383
channel: channel_pc_web
app_name: aweme
format: json
group_id: 7389248577308052776
item_id: 7389248577308052776
start_time: 0
end_time: 32000
authentication_token: 
duration: 717160
update_version_code: 170400
pc_client_type: 1
pc_libra_divert: Windows
support_h265: 1
support_dash: 1
version_code: 170400
version_name: 17.4.0
cookie_enabled: true
screen_width: 1920
screen_height: 1080
browser_language: zh-CN
browser_platform: Win32
browser_name: Chrome
browser_version: 133.0.0.0
browser_online: true
engine_name: Blink
engine_version: 133.0.0.0
os_name: Windows
os_version: 10
cpu_core_num: 8
device_memory: 8
platform: PC
downlink: 10
effective_type: 4g
round_trip_time: 50
webid: 7464257619323651624
uifid: c4a29131752d59acb78af076c3dbdd52744118e38e80b4b96439ef1e20799db0b4e1b80199ec66c165c6b673d009d757ab9665806eb08d7aa0fb330d1531244d449a7eddc803033eb3ab027402d6d1b588531dcc1ac917198d4a63080173c8ceb70d362d3dca76a35e6155ab2f6b97b6efa3a3330d439196388b8e8a25fa2dde4cd1df49d94cbe73623dc2d124bcf4607b094a4f37189ea8febd706e5f816ca2
msToken: 3-CEJ8ACRAdNpuq--SAB8SvmsTAPJTdGoUoPyvPr6Apuiqyn8LdU5uuDTQ8tV9vpZ1Ht_2iO5O9U2TwJsxdngpTjEqvjSkU3DffTPJjF2l1U-IGgksnDz9G38C2lEVq8VdtiLYdqneNgQ-tK30VlxyGKyrzIwZUrE3rr4ulQfMoSeg==
a_bogus: E74Rh7XJxp5bPd/bmOBQyUxlm8ElNP8ycBTKbb9UCV7nG1lbaWNFDrSmaozahdRZmSBkwel7AnUAYxVbQ07hZFqpumkkuP06Oz5IIhmL0qqRTFkQErbgCLYzqw0N0R4qlAVJilkI/UeqgndAhqQg/QAJS/uK55uBP3ObkZubx9s6ZzgALZnHPptdO7TKUtxb
```

## 快手关键词搜索

