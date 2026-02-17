import streamlit as st
books = [
  "The A.B.C. Murders",
  "Everyone on this train is a suspect",
  "The great Gatsby",
  "Nineteen Eighty-Four",
  "1984",
  "To Kill a Mockingbird",
  "The Hobbit"]
st.title("Book checker app")
st.write("Enter a book title to check if it's it the database")
user_input=st.text_input("Book title")
if st.button("Check book"):
  if user_input.strip()=="":
    st.warning("PLease enter a book title")
  elif user_input in books:
    st.success("The book exists in the database")
  else:
    st.error("The book is not in the database")


new_book=st.text_input("Add book")
if st.button("Add"):
  st.write(new_book)
