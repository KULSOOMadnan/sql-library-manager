import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
from database.db import get_db_connection

# 🎨 Custom CSS for Styling
st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
            font-size: 36px;
            color: white;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .stats-container {
            background: linear-gradient(to right, #4facfe, #00f2fe);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-size: 18px;
            margin-bottom: 20px;
        }
        .stat-card {
            background: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            margin: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 📌 Page Title
st.markdown("<h1 class='main-title'>📊 Library Statistics Dashboard</h1>", unsafe_allow_html=True)

# 🔌 Database Connection
conn = get_db_connection()
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM books")
total_books = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM books WHERE read_status = TRUE")
read_books = cursor.fetchone()[0]

conn.close()

# Calculate Read Percentage
read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0

# 📚 Display Statistics in Cards
st.markdown("<div class='stats-container'><strong>📖 Library Overview</strong></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<div class='stat-card'>📚 Total Books: {total_books}</div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='stat-card'>✅ Books Read: {read_books} ({read_percentage:.2f}%)</div>", unsafe_allow_html=True)

# 📈 Bar Chart for Books Read vs. Unread
data = pd.DataFrame({
    "Category": ["Read Books", "Unread Books"],
    "Count": [read_books, total_books - read_books]
})
fig = px.bar(data, x="Category", y="Count", text="Count",
             color="Category", title="Library Reading Status",
             color_discrete_sequence=["#2ca02c", "#d62728"])

st.plotly_chart(fig, use_container_width=True)

# 📊 Progress Bar for Read Books
st.write("📖 **Reading Progress**")
st.progress(read_percentage / 100)
st.write(f"✅ **{read_percentage:.2f}% of your books have been read!**")

