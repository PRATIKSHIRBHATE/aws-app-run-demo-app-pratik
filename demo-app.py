import streamlit as st

def main():
    # Set page title
    st.title('Hello Name App')

    # Create input field
    user_name = st.text_input('Please enter your name:')

    # Add a button
    if st.button('Say Hello'):
        if user_name:
            st.write(f'Hello {user_name}!')
        else:
            st.write('Please enter a name.')

    # Optional: Add some styling and instructions
    st.markdown("""
    ---
    **Instructions:**
    1. Enter your name in the text box
    2. Click the 'Say Hello' button
    """)

if __name__ == "__main__":
    #import os
    #port = int(os.environ.get('PORT', 8080))
    main()