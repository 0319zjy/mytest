import streamlit as st

# 页面配置
st.set_page_config(page_title="视频中心")
st.title("喜羊羊与灰太狼第一部")

# 视频数据（修正全角符号、补全语法结构）
video_arr = [
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/22/49/34889204922/34889204922-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&gen=playurlv3&os=estghw&og=hw&uipk=5&oi=2067284620&trid=4c54593a709c4440adcb975bf7ddf27O&deadline=1766567848&platform=html5&mid=0&nbs=1&upsig=249ad2f3a6a819f29ecb129402597b94&uparams=e,gen,os,og,uipk,oi,trid,deadline,platform,mid,nbs&bvc=vod&nettype=1&bw=568430&dl=0&f=O_0_0&agrr=1&buvid=&build=7330300&orderid=0,3',
        'title': '喜羊羊与灰太狼-第001集、狼来了（上）'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/72/76/27250917672/27250917672-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&og=hw&trid=0d44221c3d7449fa866a9ef537a9db5O&mid=0&uipk=5&gen=playurlv3&platform=html5&deadline=1766567946&nbs=1&oi=144233936&os=zosbv&upsig=5a86974336cb6b2e42c992a1953a0de0&uparams=e,og,trid,mid,uipk,gen,platform,deadline,nbs,oi,os&bvc=vod&nettype=1&bw=459448&dl=0&f=O_0_0&agrr=1&buvid=&build=7330300&orderid=0,3',
        'title': '喜羊羊与灰太狼-第002集、狼来了（下）'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/31/86/27251508631/27251508631-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766568051&os=estghw&nbs=1&mid=0&platform=html5&gen=playurlv3&og=hw&oi=2067284620&uipk=5&trid=c2f363fc7ae2492cbf2685aa2423737O&upsig=e2763a670ca0cb14f07d4c944f6ab6cd&uparams=e,deadline,os,nbs,mid,platform,gen,og,oi,uipk,trid&bvc=vod&nettype=1&bw=431582&buvid=&build=7330300&dl=0&f=O_0_0&agrr=1&orderid=0,3',
        'title': '喜羊羊与灰太狼-第003集、大小药丸'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/59/38/27251703859/27251703859-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&oi=2067284620&os=estgoss&og=hw&uipk=5&trid=1e37cc6be0f9431d8b399afc15d73faO&deadline=1766568095&nbs=1&gen=playurlv3&platform=html5&upsig=c9f0b313bf5e8b5d99ecd91fdf4bbfa1&uparams=e,mid,oi,os,og,uipk,trid,deadline,nbs,gen,platform&bvc=vod&nettype=1&bw=441640&dl=0&f=O_0_0&agrr=1&buvid=&build=7330300&orderid=0,3',
        'title': '喜羊羊与灰太狼-第004集、昏睡果'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/91/43/25728064391/25728064391-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=7c0d1808481c461bb0f507546782efbO&uipk=5&nbs=1&gen=playurlv3&os=estghw&og=hw&mid=0&deadline=1766568141&platform=html5&oi=1385955528&upsig=2a2c3eea7875ab858ad3ffc1d77e3665&uparams=e,trid,uipk,nbs,gen,os,og,mid,deadline,platform,oi&bvc=vod&nettype=1&bw=450605&build=7330300&dl=0&f=O_0_0&agrr=1&buvid=&orderid=0,3',
        'title': '喜羊羊与灰太狼-第005集、变色狼'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/25/78/27251967825/27251967825-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&oi=144233936&mid=0&uipk=5&trid=50b6b571db324728a43cb9f57dc6d37O&gen=playurlv3&os=estgcos&og=cos&deadline=1766568205&platform=html5&upsig=cc1cf786b2cc2d531f792ace411196da&uparams=e,nbs,oi,mid,uipk,trid,gen,os,og,deadline,platform&bvc=vod&nettype=1&bw=459665&f=O_0_0&agrr=1&buvid=&build=7330300&dl=0&orderid=0,3',
        'title': '喜羊羊与灰太狼-第006集、克隆喜羊羊'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/90/71/27252097190/27252097190-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=estgoss&platform=html5&oi=1385955528&trid=533cf6b29c744e718977d09331081bfO&mid=0&og=ali&nbs=1&uipk=5&deadline=1766568265&gen=playurlv3&upsig=3a72edc1c0d2f6e9936aecaa7123c3fa&uparams=e,os,platform,oi,trid,mid,og,nbs,uipk,deadline,gen&bvc=vod&nettype=1&bw=451121&buvid=&build=7330300&dl=0&f=O_0_0&agrr=1&orderid=0,3',
        'title': '喜羊羊与灰太狼-第007集、自爆兵团'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/20/12/27252821220/27252821220-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=1385955528&platform=html5&gen=playurlv3&uipk=5&trid=655a1d3fdd1449ab9bc9762c3a16f2cO&mid=0&deadline=1766568327&os=estgcos&og=cos&nbs=1&upsig=d9efb67fb33556d923c1859073245e1f&uparams=e,oi,platform,gen,uipk,trid,mid,deadline,os,og,nbs&bvc=vod&nettype=1&bw=452273&dl=0&f=O_0_0&agrr=1&buvid=&build=7330300&orderid=0,3',
        'title': '喜羊羊与灰太狼-第008集、运动会'
    }
]

# 初始化会话状态
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 播放视频（修正索引拼写错误：ind 而非 indl）
st.video(video_arr[st.session_state['ind']]['url'])
# 显示当前视频标题
st.subheader(video_arr[st.session_state['ind']]['title'])

# 定义播放函数
def playVideo(e):
    st.session_state['ind'] = int(e)

# 按每5个一组切分视频列表，生成按钮行
group_size = 5
for i in range(0, len(video_arr), group_size):
    # 生成对应数量的列
    cols = st.columns(group_size)
    # 遍历当前组的元素
    for j, idx in enumerate(range(i, min(i + group_size, len(video_arr)))):
        with cols[j]:
            st.button(f'第{idx + 1}集', on_click=playVideo, args=(idx,))
