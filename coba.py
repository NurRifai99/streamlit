# # # import streamlit as st

# # # # Using object notation
# # # add_selectbox = st.sidebar.selectbox(
# # #     "How would you like to be contacted?",
# # #     ("Email", "Home phone", "Mobile phone")
# # # )

# # # # Using "with" notation
# # # with st.sidebar:
# # #     add_radio = st.radio(
# # #         "Choose a shipping method",
# # #         ("Standard (5-15 days)", "Express (2-5 days)")
# # #     )

# # import streamlit as st
# # import time

# # with st.sidebar:
# #     with st.echo():
# #         st.write("This code will be printed to the sidebar.")

# #     with st.spinner("Loading..."):
# #         time.sleep(5)
# #     st.success("Done!")

 import streamlit as st

st.title("Page 1")  
