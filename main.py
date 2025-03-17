
import streamlit as st


# _______Page Config
st.set_page_config(
    page_title="📚 Library Manager",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ______Pages Seup
about_page = st.Page(
    page="pages/about.py",
    title="Personal Liabrary Manager",
    icon="📝",
    default=True
)

project_1_page = st.Page(
    page="pages/add_book.py",
    title="Add Books",
    icon="➕"
)
project_2_page=st.Page(
    page="pages/search_book.py",
    title="Search Books",
    icon="🔍"
    
)

project_3_page=st.Page(
    page="pages/display_books.py",
    title="Books Collection",
    icon="📚"
    
)
project_4_page = st.Page(
    page="pages/remove_book.py",
    title="Remove Books",
    icon="🗑️",
)


project_5_page=st.Page(
    page="pages/statistics.py",
    title="Liabrary Statistics",
    icon="📊",
)

# ___ Navigation Setup [Without Sections]
# pg =st.navigation(pages=[about_page, project_1_page, project_2_page])

## ___ Navigation Setup [With Sections]
st.logo('assets/library.jpg')
st.sidebar.markdown("---")

pg = st.navigation(
    {
        "info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page, project_4_page, project_5_page]
    }
)

# sidebar_logo = st.selectbox("Code With Fairy🍃")
# ___ Shared on Alll pages

# Custom logo styling at the top


st.sidebar.text("Made With ❤ by Kulsoom Adnan")

# Run Navigations
pg.run()