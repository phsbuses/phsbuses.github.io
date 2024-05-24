import streamlit
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

hashed_passwords = Hasher(['abc', 'def']).generate()

print(hashed_passwords)
