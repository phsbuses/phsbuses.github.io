# import streamlit as st
# import yaml
# from yaml.loader import SafeLoader
# import streamlit_authenticator as stauth
# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)
# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# name, authentication_status, username = authenticator.login(fields={'Form name':'Login', 'Username':'Username', 'Password':'Password','Login':'Login'})
# print(st.session_state["authentication_status"])
# print(st.session_state["username"])
# if st.session_state["authentication_status"]:
#     authenticator.logout()
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state["authentication_status"] is False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] is None:
#     st.warning('Please enter your username and password')

import streamlit as st
from streamlit_sortables import sort_items
from streamlit_server_state import server_state, server_state_lock
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

if 'flag' not in server_state:
    server_state.flag = False
if 'dat' not in server_state:
    server_state.dat = [
    {'header':'Loops','items':['Outer','1234', '2345', '3345']},
    {'items':['Inner','2341', '2314', '1525']},
    {'header':'Extra rows','items':['----','4567']},
    {'items':['----','4676']},
    {'items':['----','4677']},
    {'items':['----','4678']}
    ]
if 'dat2' not in server_state:
    server_state.dat2 = server_state.dat.copy()
if 'show_sorted' not in st.session_state:
    st.session_state.show_sorted = False

name, authentication_status, username = authenticator.login(fields={'Form name':'Login', 'Username':'Username', 'Password':'Password','Login':'Login'})
print(st.session_state["authentication_status"])
print(st.session_state["username"])
if st.session_state["authentication_status"]:
    with st.container(border=True):
        st.subheader('Logout')
        st.checkbox('Verify logout', key='verify_logout')
    if st.session_state.verify_logout:
        authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Admin: Bus drag-and-drop')

    with st.form("my_form"):
        st.write("Add, change, or remove sub-bus number")
        orig_num = st.text_input("Regular Bus Number", "")
        sub_num = st.text_input("Sub-Bus Number", "")
        if st.form_submit_button('Submit'):
            if orig_num == '':
                st.warning("Please enter the original bus number")
            else:
                row_flag = False
                for row in range(6):
                    for i in range(len(server_state.dat[row]['items'])):
                        if (server_state.dat[row]['items'][i][0:4]==orig_num):
                            if sub_num=='':
                                server_state.dat[row]['items'][i] = str(orig_num)
                            else:
                                server_state.dat[row]['items'][i] = str(orig_num)+"\n ("+str(sub_num)+")" 
                            row_flag=True
                if row_flag==False:
                    st.warning("Please enter a valid original bus number")

    if st.button('Show drag and drop' if not st.session_state.show_sorted else 'Hide drag and drop'):
        st.session_state.show_sorted = not st.session_state.show_sorted
    # sorted = sort_items(server_state.dat, multi_containers=True)
    if st.session_state.show_sorted:
        sorted = sort_items(server_state.dat, multi_containers=True)
        server_state.dat = sorted.copy()
    # server_state.dat = sorted.copy()
    # draggable_item = sorted
    # for container in server_state.dat:
    #     if draggable_item in container['items']:
    #         container['items'].insert(0, container['items'].pop(container['items'].index(draggable_item)))

    # server_state.dat = sorted.copy()

    server_state.dat2 = server_state.dat.copy()
    # while (len(data2[0]['items']) < 7):
    #     server_state.dat2[0]['items'].insert(0,'none')
    # while (len(data2[1]['items']) < 7):
    #     server_state.dat2[1]['items'].insert(0,'none')

    data = server_state.dat

    # # st.write(sorted)
    # # if (len(sorted[0]['items'])==0):
    # #     data[0]['items'] = ['----']

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
    st.title('Student: Bus viewing')
elif st.session_state["authentication_status"] is None:
    st.warning('For admins only: please enter your username and password')
    st.title('Student: Bus viewing')

# items1 = server_state.dat2[0]['items']
# cols = st.columns(len(items1))
# for i, item in enumerate(items1):
#     with cols[i]:
#         st.button(item, key=f"sorted3_{i}")

# items2 = server_state.dat2[1]['items']
# cols = st.columns(len(items2))
# for i, item in enumerate(items2):
#     with cols[i]:
#         st.button(item, key=f"sorted4_{i}")

items1 = server_state.dat2[0]['items']
cols = st.columns(9)
for i, item in enumerate(items1):
    with cols[i]:
        st.button(item, key=f"sorted3_{i}")

items2 = server_state.dat2[1]['items']
cols = st.columns(9)
for i, item in enumerate(items2):
    with cols[i]:
        st.button(item, key=f"sorted4_{i}")