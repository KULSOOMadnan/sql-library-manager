import streamlit as st
import mysql.connector
from database.db import get_db_connection

# 🎨 Custom CSS for UI Styling
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
        .search-box {
            background: linear-gradient(to right, #6a11cb, #2575fc);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-size: 18px;
        }
        .book-card {
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 10px;
        }
        .search-input {
            font-size: 16px;
            padding: 10px;
            width: 100%;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        .search-btn {
            background-color: #ff6f61;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }
        .search-btn:hover {
            background-color: #e65c50;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 📌 Page Title
st.markdown("<h1 class='main-title'>🔍 Search for a Book</h1>", unsafe_allow_html=True)

# 📚 Search Section
st.markdown("<div class='search-box'><strong>Find a book by its Title or Author 📖</strong></div>", unsafe_allow_html=True)

search_type = st.radio("Search by:", ["Title", "Author"], horizontal=True)
search_query = st.text_input("🔎 Enter your search query:")

if st.button("Search 📚"):
    if not search_query.strip():
        st.warning("⚠️ Please enter a search query!")
    else:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # 🔍 Query Based on Search Type
        if search_type == "Title":
            cursor.execute("SELECT * FROM books WHERE title LIKE %s", (f"%{search_query}%",))
        else:
            cursor.execute("SELECT * FROM books WHERE author LIKE %s", (f"%{search_query}%",))

        results = cursor.fetchall()
        conn.close()

        # 🎯 Display Results
        if results:
            st.markdown("### 📚 Search Results:")
            for book in results:
                st.markdown(
                    f"""
                    <div class='book-card'>
                        <h3>📖 {book['title']}</h3>
                        <p><strong>✍️ Author:</strong> {book['author']}</p>
                        <p><strong>📅 Published:</strong> {book['publication_year']}</p>
                        <p><strong>📚 Genre:</strong> {book['genre']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.warning("❌ No matching books found! Try a different search term.")
