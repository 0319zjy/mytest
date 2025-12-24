import streamlit as st
import pandas as pd

# ========== 全局页面配置（只能调用一次，放在最顶部） ==========
st.set_page_config(
    page_title="南宁旅游探索 | 音乐播放器",
    page_icon="🌿",
    layout="wide"
)

# ========== 页面标题与基础信息 ==========
st.title("🌿 南宁旅游探索")
st.caption("探索南宁热门景点、游客评分、消费数据及游玩时段建议")
st.markdown("网站地址：https://zhujiangyuan.streamlit.app")

# ========== 1. 景点风光展示（图片切换） ==========
st.subheader("🖼️ 景点风光展示")

# 初始化图片索引
if "img_idx" not in st.session_state:
    st.session_state.img_idx = 0

# 景点图片数据
image_data = [
    {
        "url": "https://picsum.photos/id/1036/800/500",
        "caption": "青秀山 - 南宁城市绿肺，四季花开不断"
    },
    {
        "url": "https://picsum.photos/id/1039/800/500",
        "caption": "三街两巷 - 百年历史街区，感受老南宁风情"
    },
    {
        "url": "https://picsum.photos/id/1043/800/500",
        "caption": "南湖公园 - 城市中心的生态绿洲，适合休闲漫步"
    }
]

# 图片切换函数（循环切换）
def prev_img():
    st.session_state.img_idx = (st.session_state.img_idx - 1) % len(image_data)

def next_img():
    st.session_state.img_idx = (st.session_state.img_idx + 1) % len(image_data)

# 显示图片和图注
img_container = st.container()
with img_container:
    st.image(
        image_data[st.session_state.img_idx]["url"],
        use_column_width="always"
    )
    st.caption(image_data[st.session_state.img_idx]["caption"])

# 图片切换按钮
col1, col2 = st.columns([1, 1])
with col1:
    st.button("上一张", on_click=prev_img, use_container_width=True)
with col2:
    st.button("下一张", on_click=next_img, use_container_width=True)

# ========== 2. 南宁旅游地图 ==========
st.subheader("🗺️ 南宁旅游地图")
# 景点坐标数据
spots_data = pd.DataFrame({
    "景点": ["青秀山", "南宁园博园", "大明山", "三街两巷", "南湖公园"],
    "纬度": [22.8170, 22.7658, 23.4856, 22.8108, 22.8254],
    "经度": [108.3895, 108.4723, 108.3408, 108.3242, 108.3418],
    "类型": ["自然景区", "文化园区", "自然景区", "历史街区", "城市公园"]
})
# 绘制地图
st.map(
    spots_data,
    latitude="纬度",
    longitude="经度",
    size=200,
    color="#1E90FF"
)

# ========== 3. 简易音乐播放器（核心修复部分） ==========
st.subheader("🎧 闲逛景点推荐音乐")
# 播放器标题
st.markdown("### 🎵 简易音乐播放器")
st.caption("使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制")

# 初始化歌曲索引（循环切歌）
if "current_song_idx" not in st.session_state:
    st.session_state.current_song_idx = 0

# 歌曲数据（修复链接格式、去除多余空格）
songs = [
    {
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "duration": "5:55",
        "cover": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2548752370.jpg",
        "audio": "https://music.163.com/song/media/outer/url?id=167709.mp3"
    },
    {
        "title": "Yesterday",
        "artist": "The Beatles",
        "duration": "2:05",
        "cover": "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2628654266.jpg",
        "audio": "https://music.163.com/song/media/outer/url?id=210869.mp3"
    },
    {
        "title": "Hotel California",
        "artist": "Eagles",
        "duration": "6:30",
        "cover": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2596084686.jpg",
        "audio": "https://music.163.com/song/media/outer/url?id=224703.mp3"
    }
]

# 切歌函数（循环切歌，修复边界问题）
def prev_song():
    st.session_state.current_song_idx = (st.session_state.current_song_idx - 1) % len(songs)

def next_song():
    st.session_state.current_song_idx = (st.session_state.current_song_idx + 1) % len(songs)

# 获取当前歌曲信息
current_song = songs[st.session_state.current_song_idx]

# 播放器布局（封面+歌曲信息+切歌按钮）
player_col1, player_col2 = st.columns([1, 4])
with player_col1:
    # 专辑封面（固定宽度，更美观）
    st.image(current_song["cover"], width=200, caption="专辑封面")

with player_col2:
    # 歌曲信息
    st.markdown(f"### {current_song['title']}")
    st.write(f"**歌手**: {current_song['artist']}")
    st.write(f"**时长**: {current_song['duration']}")
    
    # 切歌按钮（样式更贴近示例）
    btn_col1, btn_col2 = st.columns([1, 1])
    with btn_col1:
        st.button("⏮️ 上一首", on_click=prev_song, use_container_width=True)
    with btn_col2:
        st.button("⏭️ 下一首", on_click=next_song, use_container_width=True)

# 音频播放控件（修复格式问题）
st.audio(
    current_song["audio"],
    format="audio/mp3",
    autoplay=False,
    use_container_width=True
)

# 模拟进度条和时间显示（更贴近示例）
st.progress(0)  # 可结合音频播放进度动态更新，此处为静态示例
st.caption(f"0:00 / {current_song['duration']}")

# ========== 4. 景点视频欣赏 ==========
st.subheader("🎬 景点视频欣赏")
video_data = [
    {
        "title": "青秀山风光全景",
        "url": "https://samplelib.com/lib/preview/mp4/sample-5s.mp4"
    },
    {
        "title": "三街两巷夜景",
        "url": "https://samplelib.com/lib/preview/mp4/sample-10s.mp4"
    }
]

# 视频选择器
selected_video = st.radio("选择视频观看", [v["title"] for v in video_data])
video_url = next(v["url"] for v in video_data if v["title"] == selected_video)
st.video(video_url, format="video/mp4", use_container_width=True)

# ========== 5. 景点评分（柱状图） ==========
st.subheader("⭐ 景点评分")
score_data = pd.DataFrame({
    "景点": ["青秀山", "南宁园博园", "大明山", "三街两巷", "南湖公园"],
    "评分": [4.8, 4.5, 4.7, 4.6, 4.4]
})
st.bar_chart(score_data, x="景点", y="评分", color="#1E90FF")

# ========== 6. 不同类型景点消费（折线图） ==========
st.subheader("💰 不同类型景点消费")
cost_data = pd.DataFrame({
    "类型": ["自然景区", "文化园区", "历史街区", "城市公园"],
    "人均消费(元)": [80, 50, 30, 0]
})
st.line_chart(cost_data, x="类型", y="人均消费(元)", color="#1E90FF")

# ========== 7. 游玩高峰时段 ==========
st.subheader("⏰ 游玩高峰时段")
time_data = pd.DataFrame({
    "时段": ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00"],
    "游客量(百人)": [30, 50, 20, 45, 60, 35],
    "拥挤指数": [0.6, 0.9, 0.3, 0.8, 1.0, 0.7]
})

col1, col2 = st.columns(2)
with col1:
    st.write("游客量分布")
    st.bar_chart(time_data, x="时段", y="游客量(百人)", color="#FF6347")
with col2:
    st.write("拥挤指数")
    st.line_chart(time_data, x="时段", y="拥挤指数", color="#FF6347")

# ========== 8. 景点详情 ==========
st.subheader("📍 景点详情")
with st.expander("查看景点详情", expanded=True):
    st.write("**青秀山**")
    st.write("评分：4.8/5.0 | 门票：20元 | 开放时间：06:00-22:00")
    st.write("**三街两巷**")
    st.write("评分：4.6/5.0 | 门票：免费 | 开放时间：全天")

# ========== 9. 今日游玩推荐 ==========
st.subheader("✨ 今日游玩推荐")
st.success("推荐：青秀山（上午游客较少，可避开午后高峰）")
