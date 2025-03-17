import streamlit as st
import mysql.connector
from database.db import get_db_connection
from PIL import Image
import io
import random

# 🎯 Page Title
st.title("➕ Add a New Book to Your Library")

# 📌 Instructions
st.markdown("""
### 📌 Instructions:
- Fill in the book title and author's name.
- Select the publication year and genre.
- Choose the read status (Read/Unread).
- (Optional) Upload a book cover image.
- Click the 'Add Book' button to save the book to your library.
""")

# 📌 Genre Options
genre_options = [
    "Fiction", "Non-Fiction", "Mystery", "Thriller", "Science Fiction", "Fantasy", "Biography", "History", "Romance", "Horror", "Self-Help", "Poetry", "Drama", "Adventure", "Comics", "Graphic Novel"
]

# 📌 Fun Facts
fun_facts = [
    "The world's largest book is over 5 meters tall! 📖",
    "Reading can reduce stress by up to 68%. 📚",
    "The first book ever written using a typewriter was 'The Adventures of Tom Sawyer'. 🖋️",
    "There is a book called 'Gadsby' that doesn't contain the letter 'E'! 🔠"
]

# 📌 Input Fields
title = st.text_input("📖 Book Title")
author = st.text_input("✍️ Author")
year = st.number_input("📅 Publication Year", min_value=1000, max_value=9999, step=1)
genre = st.selectbox("📚 Genre", genre_options)
read_status = st.radio("📌 Read Status", ["Unread", "Read"], horizontal=True)
book_image = st.file_uploader("📷 Upload Book Cover (Optional)", type=["jpg", "png", "jpeg", "gif", "bmp", "webp"])

# ✅ Submission Button
if st.button("✅ Add Book"):
    if not title or not author or not genre or not year:
        st.error("⚠️ Please fill in all required fields!")
    else:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # 🖼️ Convert and Resize Image before Storing
            img_data = None
            if book_image is not None:
                img = Image.open(book_image)
                img = img.convert("RGB")  # Convert to RGB if image has an alpha channel
                img = img.resize((300, 400))  # Resize to optimize storage
                img_bytes = io.BytesIO()
                img.save(img_bytes, format="JPEG")  # Convert to bytes
                img_data = img_bytes.getvalue()

            # 🗄️ Insert Data into Database
            cursor.execute(
                "INSERT INTO books (title, author, publication_year, genre, read_status, book_image) VALUES (%s, %s, %s, %s, %s, %s)",
                (title, author, year, genre, read_status == "Read", img_data),
            )
            conn.commit()
            conn.close()
            
            # ✅ Custom Success Message & Fun Fact
            st.success(f"🎉 Great choice! '{title}' has been successfully added to your library. Happy reading! 📚")
            st.info(random.choice(fun_facts))
            

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
