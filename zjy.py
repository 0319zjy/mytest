import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 页面配置
st.set_page_config(page_title="南宁旅游探索", page_icon="🌿", layout="wide")
st.title("🌿 南宁旅游探索")
st.caption("探索南宁热门景点、游客评分、消费数据及游玩时段建议")


# --- 1. 南宁旅游地图 ---
st.subheader("南宁旅游地图")
# 模拟景点坐标数据（可替换为真实经纬度）
spots_data = pd.DataFrame({
    "景点": ["青秀山", "南宁园博园", "大明山", "三街两巷", "南湖公园"],
    "纬度": [22.8170, 22.7658, 23.4856, 22.8108, 22.8254],
    "经度": [108.3895, 108.4723, 108.3408, 108.3242, 108.3418],
    "类型": ["自然景区", "文化园区", "自然景区", "历史街区", "城市公园"]
})
# 绘制地图
fig_map = px.scatter_mapbox(
    spots_data, lat="纬度", lon="经度", hover_name="景点", hover_data=["类型"],
    zoom=10, mapbox_style="carto-positron"
)
st.plotly_chart(fig_map, use_container_width=True)


# --- 2. 景点评分 ---
st.subheader("⭐ 景点评分")
score_data = pd.DataFrame({
    "景点": ["青秀山", "南宁园博园", "大明山", "三街两巷", "南湖公园"],
    "评分": [4.8, 4.5, 4.7, 4.6, 4.4]
})
fig_score = px.bar(score_data, x="景点", y="评分", color="评分", color_continuous_scale="blues")
st.plotly_chart(fig_score, use_container_width=True)


# --- 3. 不同类型景点消费 ---
st.subheader("💰 不同类型景点消费")
cost_data = pd.DataFrame({
    "类型": ["自然景区", "文化园区", "历史街区", "城市公园"],
    "人均消费(元)": [80, 50, 30, 0]  # 城市公园多免费
})
fig_cost = px.line(cost_data, x="类型", y="人均消费(元)", marker="o", line_color="skyblue")
st.plotly_chart(fig_cost, use_container_width=True)


# --- 4. 游玩高峰时段 ---
st.subheader("⏰ 游玩高峰时段")
time_data = pd.DataFrame({
    "时段": ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00"],
    "游客量(百人)": [30, 50, 20, 45, 60, 35],
    "拥挤指数": [0.6, 0.9, 0.3, 0.8, 1.0, 0.7]
})
fig_time = go.Figure()
fig_time.add_trace(go.Bar(x=time_data["时段"], y=time_data["游客量(百人)"], name="游客量", marker_color="royalblue"))
fig_time.add_trace(go.Line(x=time_data["时段"], y=time_data["拥挤指数"], name="拥挤指数", yaxis="y2", line_color="coral"))
fig_time.update_layout(
    yaxis2=dict(title="拥挤指数", overlaying="y", side="right"),
    legend=dict(x=0, y=1.1, orientation="h")
)
st.plotly_chart(fig_time, use_container_width=True)


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
