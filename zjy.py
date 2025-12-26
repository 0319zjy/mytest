import streamlit as st
import pandas as pd
import time
from datetime import timedelta

# ========== 全局页面配置（只能调用一次，放在最顶部） ==========
st.set_page_config(
    page_title="南宁旅游探索 | 音乐播放器",
    page_icon="🌿",
    layout="wide"
)

# ========== 自定义CSS样式（优化UI美观度） ==========
st.markdown("""
<style>
    /* 优化按钮样式 */
    div.stButton > button {
        border-radius: 8px;
        height: 3em;
        font-size: 14px;
    }
    /* 优化卡片样式 */
    .stExpander {
        border-radius: 8px;
    }
    /* 调整标题间距 */
    h1, h2, h3 {
        margin-bottom: 0.5em;
    }
    /* 进度条样式 */
    .stProgress > div > div {
        background-color: #1E90FF;
    }
</style>
""", unsafe_allow_html=True)

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
        use_column_width="always",
        caption=image_data[st.session_state.img_idx]["caption"]
    )

# 图片切换按钮
col1, col2 = st.columns([1, 1])
with col1:
    st.button("⬅️ 上一张", on_click=prev_img, use_container_width=True)
with col2:
    st.button("下一张 ➡️", on_click=next_img, use_container_width=True)

# ========== 2. 南宁旅游地图 ==========
st.subheader("🗺️ 南宁旅游地图")
# 景点坐标数据
spots_data = pd.DataFrame({
    "景点": ["青秀山", "南宁园博园", "大明山", "三街两巷", "南湖公园"],
    "纬度": [22.8170, 22.7658, 23.4856, 22.8108, 22.8254],
    "经度": [108.3895, 108.4723, 108.3408, 108.3242, 108.3418],
    "类型": ["自然景区", "文化园区", "自然景区", "历史街区", "城市公园"],
    "评分": [4.8, 4.5, 4.7, 4.6, 4.4]
})
# 绘制地图
st.map(
    spots_data,
    latitude="纬度",
    longitude="经度",
    size=spots_data["评分"] * 50,  # 根据评分调整大小
    color="#1E90FF"
)

# ========== 3. 简易音乐播放器（核心修复部分） ==========
st.subheader("🎧 闲逛景点推荐音乐")
st.markdown("### 🎵 简易音乐播放器")
st.caption("使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制")

# 初始化播放器相关状态
if "current_song_idx" not in st.session_state:
    st.session_state.current_song_idx = 0
if "audio_playing" not in st.session_state:
    st.session_state.audio_playing = False
if "audio_progress" not in st.session_state:
    st.session_state.audio_progress = 0

# 歌曲数据（修复链接格式、补充更多信息）
songs = [
    {
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "duration": "5:55",
        "duration_sec": 355,
        "cover": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2548752370.jpg",
        "audio": "https://music.163.com/song/media/outer/url?id=167709.mp3"
    },
    {
        "title": "Yesterday",
        "artist": "The Beatles",
        "duration": "2:05",
        "duration_sec": 125,
        "cover": "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2628654266.jpg",
        "audio": "https://music.163.com/song/media/outer/url?id=210869.mp3"
    },
    {
        "title": "Hotel California",
        "artist": "Eagles",
        "duration": "6:30",
        "duration_sec": 390,
        "cover": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2596084686.jpg",
        "audio": "https://music.163.com/song/media/outer/url?id=224703.mp3"
    }
]

# 切歌函数（循环切歌，修复边界问题）
def prev_song():
    st.session_state.current_song_idx = (st.session_state.current_song_idx - 1) % len(songs)
    st.session_state.audio_progress = 0  # 切歌重置进度

def next_song():
    st.session_state.current_song_idx = (st.session_state.current_song_idx + 1) % len(songs)
    st.session_state.audio_progress = 0  # 切歌重置进度

# 播放/暂停控制函数
def toggle_play():
    st.session_state.audio_playing = not st.session_state.audio_playing

# 获取当前歌曲信息
current_song = songs[st.session_state.current_song_idx]

# 播放器布局（封面+歌曲信息+控制按钮）
player_col1, player_col2 = st.columns([1, 4])
with player_col1:
    # 专辑封面（固定宽度，更美观）
    st.image(current_song["cover"], width=200, caption="专辑封面", use_column_width="auto")

with player_col2:
    # 歌曲信息
    st.markdown(f"### {current_song['title']}")
    st.write(f"**歌手**: {current_song['artist']}")
    st.write(f"**时长**: {current_song['duration']}")
    
    # 播放控制和切歌按钮
    btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
    with btn_col1:
        st.button("⏮️ 上一首", on_click=prev_song, use_container_width=True)
    with btn_col2:
        play_btn_text = "⏸️ 暂停" if st.session_state.audio_playing else "▶️ 播放"
        st.button(play_btn_text, on_click=toggle_play, use_container_width=True)
    with btn_col3:
        st.button("⏭️ 下一首", on_click=next_song, use_container_width=True)

# 音频播放控件（修复格式问题，增加错误处理）
try:
    st.audio(
        current_song["audio"],
        format="audio/mp3",
        autoplay=st.session_state.audio_playing,
        use_container_width=True
    )
except Exception as e:
    st.warning(f"音频加载失败: {str(e)}")
    st.info("请检查音频链接是否有效，或稍后再试")

# 动态进度条（模拟播放进度）
progress_col1, progress_col2 = st.columns([10, 2])
with progress_col1:
    progress = st.session_state.audio_progress / current_song["duration_sec"] if current_song["duration_sec"] > 0 else 0
    st.progress(min(progress, 1.0))
with progress_col2:
    # 格式化当前播放时间
    current_time = str(timedelta(seconds=int(st.session_state.audio_progress)))
    if current_time.startswith("0:"):
        current_time = current_time[2:]
    st.caption(f"{current_time} / {current_song['duration']}")

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

# 视频选择器（改为下拉框更美观）
selected_video = st.selectbox("选择视频观看", [v["title"] for v in video_data])
video_url = next(v["url"] for v in video_data if v["title"] == selected_video)
st.video(video_url, format="video/mp4", use_container_width=True)

# ========== 5. 景点评分（柱状图） ==========
st.subheader("⭐ 景点评分")
score_data = pd.DataFrame({
    "景点": ["青秀山", "南宁园博园", "大明山", "三街两巷", "南湖公园"],
    "评分": [4.8, 4.5, 4.7, 4.6, 4.4],
    "游客数量(万/月)": [80, 45, 30, 65, 70]
})

# 评分和游客量对比展示
score_col1, score_col2 = st.columns(2)
with score_col1:
    st.write("景点评分")
    st.bar_chart(score_data, x="景点", y="评分", color="#1E90FF")
with score_col2:
    st.write("月游客数量")
    st.bar_chart(score_data, x="景点", y="游客数量(万/月)", color="#FF6347")

# ========== 6. 不同类型景点消费（折线图） ==========
st.subheader("💰 不同类型景点消费")
cost_data = pd.DataFrame({
    "类型": ["自然景区", "文化园区", "历史街区", "城市公园"],
    "人均消费(元)": [80, 50, 30, 0],
    "推荐游玩时长(小时)": [4, 3, 2, 1.5]
})

cost_col1, cost_col2 = st.columns(2)
with cost_col1:
    st.write("人均消费对比")
    st.line_chart(cost_data, x="类型", y="人均消费(元)", color="#1E90FF")
with cost_col2:
    st.write("推荐游玩时长")
    st.line_chart(cost_data, x="类型", y="推荐游玩时长(小时)", color="#32CD32")

# ========== 7. 游玩高峰时段 ==========
st.subheader("⏰ 游玩高峰时段")
time_data = pd.DataFrame({
    "时段": ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00"],
    "游客量(百人)": [30, 50, 20, 45, 60, 35],
    "拥挤指数": [0.6, 0.9, 0.3, 0.8, 1.0, 0.7]
})

time_col1, time_col2 = st.columns(2)
with time_col1:
    st.write("游客量分布")
    st.bar_chart(time_data, x="时段", y="游客量(百人)", color="#FF6347")
with time_col2:
    st.write("拥挤指数")
    st.line_chart(time_data, x="时段", y="拥挤指数", color="#FF6347")

# 高峰时段提示
max_crowd_idx = time_data["拥挤指数"].idxmax()
max_crowd_time = time_data.loc[max_crowd_idx, "时段"]
st.warning(f"⚠️ 游玩提示：每日{max_crowd_time}为游客最高峰期，建议错峰出行")

# ========== 8. 景点详情 ==========
st.subheader("📍 景点详情")
with st.expander("查看景点详情", expanded=True):
    # 使用更清晰的表格展示详情
    detail_data = pd.DataFrame({
        "景点名称": ["青秀山", "南宁园博园", "大明山", "三街两巷", "南湖公园"],
        "评分(5分制)": [4.8, 4.5, 4.7, 4.6, 4.4],
        "门票价格(元)": [20, 60, 90, 0, 0],
        "开放时间": ["06:00-22:00", "09:00-18:00", "08:00-17:00", "全天", "05:00-23:00"],
        "推荐游玩时长(小时)": [4, 3, 5, 2, 1]
    })
    st.dataframe(detail_data, use_container_width=True)

# ========== 9. 今日游玩推荐 ==========
st.subheader("✨ 今日游玩推荐")
# 根据当前时间智能推荐
current_hour = time.localtime().tm_hour
if current_hour < 12:
    recommendation = "青秀山（上午游客较少，可避开午后高峰）"
elif 12 <= current_hour < 18:
    recommendation = "南湖公园（午后休闲散步，欣赏湖光山色）"
else:
    recommendation = "三街两巷（夜晚体验老南宁的烟火气息）"

st.success(f"推荐：{recommendation}")

# ========== 10. 游客反馈收集（新增功能） ==========
st.subheader("📝 游客反馈")
with st.form(key="feedback_form"):
    feedback_spot = st.selectbox("您游玩的景点", ["青秀山", "南宁园博园", "大明山", "三街两巷", "南湖公园"])
    feedback_rating = st.slider("您的评分", 1, 5, 4)
    feedback_text = st.text_area("您的游玩感受（选填）", placeholder="请分享您的游玩体验...")
    submit_btn = st.form_submit_button("提交反馈")
    
    if submit_btn:
        st.success(f"感谢您的反馈！您对{feedback_spot}的评分为{feedback_rating}分。")
        # 这里可以添加保存反馈数据的逻辑
