import streamlit as st
import pandas as pd

# 页面配置
st.set_page_config(page_title="南宁旅游探索", page_icon="🌿", layout="wide")
st.title("🌿 南宁旅游探索")
st.caption("探索南宁热门景点、游客评分、消费数据及游玩时段建议")

# 网站地址（替换为你的姓名全拼）
st.markdown("网站地址：https://zhujiangyuan.streamlit.app")


# --- 核心：图片切换（上一张/下一张按钮 + 图注）---
st.subheader("🖼️ 景点风光展示")

# 初始化session_state存储当前图片索引
if "img_idx" not in st.session_state:
    st.session_state.img_idx = 0

# 图片+图注数据（替换为真实图片URL）
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

# 切换按钮逻辑
def prev_img():
    st.session_state.img_idx = (st.session_state.img_idx - 1) % len(image_data)

def next_img():
    st.session_state.img_idx = (st.session_state.img_idx + 1) % len(image_data)

# 布局：图片容器 + 按钮 + 图注
img_container = st.container()
with img_container:
    # 显示当前图片
    st.image(
        image_data[st.session_state.img_idx]["url"],
        use_column_width="always"  # 占满列宽，和示例一致
    )
    # 图注（底部显示）
    st.caption(image_data[st.session_state.img_idx]["caption"])

# 按钮行（左右排列）
col1, col2 = st.columns([1, 1])
with col1:
    st.button("上一张", on_click=prev_img, use_container_width=True)
with col2:
    st.button("下一张", on_click=next_img, use_container_width=True)

# --- 1. 南宁旅游地图（改用Streamlit原生地图）---
st.subheader("南宁旅游地图")
# 模拟景点坐标数据（可替换为真实经纬度）
spots_data = pd.DataFrame({
    "景点": ["青秀山", "南宁园博园", "大明山", "三街两巷", "南湖公园"],
    "纬度": [22.8170, 22.7658, 23.4856, 22.8108, 22.8254],
    "经度": [108.3895, 108.4723, 108.3408, 108.3242, 108.3418],
    "类型": ["自然景区", "文化园区", "自然景区", "历史街区", "城市公园"]
})
# Streamlit原生地图（无需plotly）
st.map(spots_data, latitude="纬度", longitude="经度", size=200, color="#1E90FF")

# --- 音频介绍 ---
st.subheader("🎧 闲逛景点推荐音乐")
# 页面基础配置
 st.set_page_config(page_title="简易音乐播放器", page_icon="🎵", layout="centered")
 st.title("🎵 简易音乐播放器")
 st.caption("使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制")
 # 模拟歌曲数据（可替换为真实音频/封面链接）
 songs = [
     {
         "title": "Bohemian Rhapsody",
         "artist": "Queen",
         "duration": "5:55",
         "cover": " https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2548752370.jpg ",
         "audio": " https://music.163.com/song/media/outer/url?id=167709.mp3"
     },
     {
         "title": "Yesterday",
         "artist": "The Beatles",
         "duration": "2:05",
         "cover": " https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2628654266.jpg ",
         "audio": " https://music.163.com/song/media/outer/url?id=210869.mp3 "
     },
     {
         "title": "Hotel California",
         "artist": "Eagles",
         "duration": "6:30",
         "cover": " https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2596084686.jpg ",
         "audio": " https://music.163.com/song/media/outer/url?id=224703.mp3 "
     }
 ]
 # 初始化会话状态（保存当前歌曲索引）
 if "current_song_idx" not in st.session_state:
     st.session_state.current_song_idx = 0
 # 切歌函数
 def prev_song():
     if st.session_state.current_song_idx > 0:
         st.session_state.current_song_idx -= 1
 def next_song():
     if st.session_state.current_song_idx < len(songs) - 1:
         st.session_state.current_song_idx += 1
 # 获取当前歌曲信息
 current_song = songs[st.session_state.current_song_idx]
 # 布局：封面+歌曲信息+切歌按钮
 col1, col2 = st.columns([1, 3])
 with col1:
     st.image(current_song["cover"], width=200)
 with col2:
     st.subheader(current_song["title"])
     st.write(f"歌手: {current_song['artist']}")
     st.write(f"时长: {current_song['duration']}")
     # 切歌按钮
     btn_col1, btn_col2 = st.columns([1, 1])
     with btn_col1:
         st.button("◀️ 上一首", on_click=prev_song, use_container_width=True)
     with btn_col2:
         st.button("下一首 ▶️", on_click=next_song, use_container_width=True)
 # 音频播放控件
 st.audio(current_song["audio"], format="audio/mp3", autoplay=False)
 # 进度条模拟（可选）
 st.progress(0)
 st.caption("0:00 / 6:12")
# --- 新增：视频展示 ---
st.subheader("🎬 景点视频欣赏")
video_data = [
    {
        "title": "青秀山风光全景",
        "url": "https://samplelib.com/lib/preview/mp4/sample-5s.mp4"  # 示例视频
    },
    {
        "title": "三街两巷夜景",
        "url": "https://samplelib.com/lib/preview/mp4/sample-10s.mp4"
    }
]

# 视频选择器
selected_video = st.radio("选择视频观看", [v["title"] for v in video_data])
# 获取选中的视频URL
video_url = next(v["url"] for v in video_data if v["title"] == selected_video)
st.video(video_url, format="video/mp4")


# --- 2. 景点评分（原生柱状图）---
st.subheader("⭐ 景点评分")
score_data = pd.DataFrame({
    "景点": ["青秀山", "南宁园博园", "大明山", "三街两巷", "南湖公园"],
    "评分": [4.8, 4.5, 4.7, 4.6, 4.4]
})
st.bar_chart(score_data, x="景点", y="评分", color="#1E90FF")

# --- 3. 不同类型景点消费（原生折线图）---
st.subheader("💰 不同类型景点消费")
cost_data = pd.DataFrame({
    "类型": ["自然景区", "文化园区", "历史街区", "城市公园"],
    "人均消费(元)": [80, 50, 30, 0]  # 城市公园多免费
})
st.line_chart(cost_data, x="类型", y="人均消费(元)", color="#1E90FF")

# --- 4. 游玩高峰时段（原生双列展示）---
st.subheader("⏰ 游玩高峰时段")
time_data = pd.DataFrame({
    "时段": ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00"],
    "游客量(百人)": [30, 50, 20, 45, 60, 35],
    "拥挤指数": [0.6, 0.9, 0.3, 0.8, 1.0, 0.7]
})
# 分两列展示
col1, col2 = st.columns(2)
with col1:
    st.write("游客量分布")
    st.bar_chart(time_data, x="时段", y="游客量(百人)", color="#FF6347")
with col2:
    st.write("拥挤指数")
    st.line_chart(time_data, x="时段", y="拥挤指数", color="#FF6347")

# --- 5. 景点详情 ---
st.subheader("📍 景点详情")
with st.expander("查看景点详情", expanded=True):
    st.write("**青秀山**")
    st.write("评分：4.8/5.0 | 门票：20元 | 开放时间：06:00-22:00")
    st.write("**三街两巷**")
    st.write("评分：4.6/5.0 | 门票：免费 | 开放时间：全天")

# --- 6. 今日游玩推荐 ---
st.subheader("✨ 今日游玩推荐")
st.success("推荐：青秀山（上午游客较少，可避开午后高峰）")
















