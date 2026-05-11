import streamlit as st

def main():
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
    
    match st.session_state['login_stete']:
        case 'teacher':
            teacher_screen()
        
        case 'student':
            student_screen()
        
        case None:
            home_screen()
main()