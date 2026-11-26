
import streamlit as st

st.set_page_config(
    page_title="Моята библиотека",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Моята библиотека")
st.write("Добре дошли в моята дигитална библиотека!")

# Initialize books
if "books" not in st.session_state:
    st.session_state.books = [
        "Хари Потър",
        "Малкият принц",
        "Хобит",
        "1984",
        "Под игото"
    ]

# Add a book
st.subheader("➕ Добавяне на книга")

new_book = st.text_input("Въведете заглавие на книга:")

if st.button("Добави книга"):
    if new_book.strip():
        if new_book.strip() not in st.session_state.books:
            st.session_state.books.append(new_book.strip())
            st.success("Книгата е добавена успешно!")
        else:
            st.warning("Тази книга вече съществува!")
    else:
        st.warning("Моля, въведете заглавие!")

st.divider()

# Display all books
st.subheader("📖 Всички книги")

if st.session_state.books:
    for index, book in enumerate(st.session_state.books, 1):
        st.write(f"{index}. 📕 {book}")
else:
    st.info("Библиотеката е празна!")

st.divider()

# Search books
st.subheader("🔍 Търсене на книга")

search = st.text_input("Каква книга търсите?")

if st.button("Търси"):
    if search.strip():
        found_books = [
            book for book in st.session_state.books
            if search.lower() in book.lower()
        ]

        if found_books:
            for book in found_books:
                st.success(f"Намерена книга: {book}")
        else:
            st.warning("Няма такава книга!")
    else:
        st.warning("Моля, въведете заглавие за търсене!")

st.divider()

# Delete a book
st.subheader("🗑️ Изтриване на книга")

if st.session_state.books:
    selected_book = st.selectbox(
        "Изберете книга:",
        st.session_state.books
    )

    if st.button("Изтрий книгата"):
        st.session_state.books.remove(selected_book)
        st.success(f"Изтрита книга: {selected_book}")
        st.rerun()
else:
    st.info("Няма книги за изтриване.")

st.divider()

# Sort books
st.subheader("🔤 Сортиране")

if st.button("Сортирай по азбучен ред"):
    st.session_state.books.sort(key=str.casefold)
    st.success("Книгите са сортирани!")
    st.rerun()

st.divider()

# Statistics
st.subheader("📊 Статистика")

total = len(st.session_state.books)

st.metric("Общ брой книги", total)

st.divider()

# Recommended books gallery
st.subheader("⭐ Препоръчани книги")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://covers.openlibrary.org/b/isbn/9780747532699-M.jpg"
    )
    st.write("Хари Потър")

with col2:
    st.image(
        "https://covers.openlibrary.org/b/isbn/9780156012195-M.jpg"
    )
    st.write("Малкият принц")

with col3:
    st.image(
        "https://covers.openlibrary.org/b/isbn/9780547928227-M.jpg"
    )
    st.write("Хобит")

st.divider()

st.caption("📚 Моята библиотека | Създадено с Python и Streamlit")
