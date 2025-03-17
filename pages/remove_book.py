import streamlit as st
import mysql.connector
import pandas as pd
from database.db import get_db_connection
from PIL import Image
import io

st.title("📚 All Books in Library")

conn = get_db_connection()
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()
conn.close()

if books:
    st.markdown("### 📖 Your Digital Bookshelf")
    for book in books:
        with st.container():
            col1, col2 = st.columns([1, 3])
            
            with col1:
                if book['book_image']:
                    img = Image.open(io.BytesIO(book['book_image']))
                    st.image(img, width=150)
                else:
                    st.markdown("📖 No Cover Available")
            
            with col2:
                st.markdown(f"## {book['title']}")
                st.markdown(f"**✍️ Author:** {book['author']}")
                st.markdown(f"**📅 Published Year:** {book['publication_year']}")
                st.markdown(f"**📚 Genre:** {book['genre']}")
                st.markdown(f"**📌 Read Status:** {'✅ Read' if book['read_status'] else '📖 Unread'}")
                
                # Delete Button Only
                if st.button("🗑️ Delete", key=f"delete_{book['title']}"):
                    conn = get_db_connection()
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM books WHERE title = %s", (book['title'],))
                    conn.commit()
                    conn.close()
                    st.success(f"🗑️ Book '{book['title']}' removed successfully!")
            
            st.markdown("---")
else:
    st.warning("📭 No books in the library yet. Add some books to get started!")
