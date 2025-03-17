import streamlit as st
from streamlit_extras.let_it_rain import rain
from PIL import Image

# 🔥 Main Title & Introduction
st.markdown(
    """
    <h1 style="text-align: center; font-size: 60px; color: #2C3E50;">📘 Library Manager</h1>
    <h3 style="text-align: center; font-size: 26px; color: #4A4A4A;">The Ultimate Tool to Organize and Manage Your Book Collection</h3>
    <hr style="border: 1px solid #bbb; margin: 20px 0px;">
    """,
    unsafe_allow_html=True
)


# 📸 Load and Display Logo
logo = Image.open("assets/lib.jpg")  # Ensure the image path is correct
# st.image(logo, use_column_width=True)


# 🚀 Features Section
st.markdown("<h2 style='color: #2C3E50; font-size: 40px;'>✨ Key Features</h2>", unsafe_allow_html=True)

features = [
    ("📖 Easy Book Management", [
        "✔️ Add new books with detailed information.",
        "✔️ Edit book details effortlessly.",
        "✔️ Remove books from your collection with one click.",
        "✔️ Categorize books by genres and authors.",
        "✔️ Bulk import books via CSV for quick setup."
    ]),
    ("🔍 Advanced Search & Filters", [
        "✔️ Search books instantly by title, author, or genre.",
        "✔️ Use dynamic filters to refine search results.",
        "✔️ Sort books by date added, author name, or rating."
    ]),
    ("📊 Library Insights & Statistics", [
        "✔️ Track your total book count and progress.",
        "✔️ View reading trends and most-read genres.",
        "✔️ Identify books you haven't read yet."
    ]),
    ("💾 Secure Database Storage", [
        "✔️ Store book details securely using <b>MySQL</b>.",
        "✔️ Cloud-based access to your collection anytime.",
        "✔️ Backup and restore your library effortlessly."
    ]),
    ("🎨 Modern & User-Friendly Design", [
        "✔️ Sleek and intuitive UI for smooth navigation.",
        "✔️ Fully responsive design optimized for all devices.",
        "✔️ Dark mode for a better reading experience."
    ]),
    ("🔔 Smart Notifications & Reminders", [
        "✔️ Set reading goals and get progress alerts.",
        "✔️ Never forget your planned reading list.",
        "✔️ Receive recommendations based on your reading habits."
    ])
]

# 📌 Display Features
for title, points in features:
    st.markdown(f"<h3 style='font-size: 30px;'>{title}</h3>", unsafe_allow_html=True)
    for point in points:
        st.markdown(f"<p style='font-size: 22px;'>{point}</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

# 📖 How to Use the App
st.markdown("<h2 style='color: #2C3E50; font-size: 40px;'>📌 How to Use Library Manager</h2>", unsafe_allow_html=True)
steps = [
    ("🔹 Navigate the App", "Use the sidebar to switch between different sections."),
    ("🔹 Add Books", "Go to the \"Add Book\" section to insert a new book into your library."),
    ("🔹 Search for Books", "Use the search bar to find books by title, author, or category."),
    ("🔹 View Statistics", "Check the \"Statistics\" section for insights into your collection."),
    ("🔹 Manage Your Collection", "Edit or remove books whenever needed."),
    ("🔹 Backup & Restore", "Easily export or restore your book data with one click.")
]
for title, description in steps:
    st.markdown(f"<h3 style='font-size: 28px;'>{title}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{description}</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

# 📌 Call to Action
st.markdown(
    """
    <div style="text-align: center; background-color: #F5F5F5; padding: 20px; border-radius: 10px;">
        <h2 style="font-size: 38px;">🚀 Ready to Organize Your Library?</h2>
        <p style="font-size: 24px;">Start now by adding your first book! 📖</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 📖 Fun Rain Effect
rain(emoji="📚", font_size=35, falling_speed=4, animation_length="infinite")

# 📌 Footer
st.markdown(
    """
    ---
    <div style="text-align: center; font-size: 20px; color: #555;">
        🚀 Developed by <b>[Your Name]</b> | Powered by <b>Streamlit</b> & <b>MySQL</b>
    </div>
    """,
    unsafe_allow_html=True
)
