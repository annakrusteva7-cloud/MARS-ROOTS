import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="MARS-ROOTS v4.0 Dashboard", layout="wide")
st.title("🔴 MARS-ROOTS: Mission Control Center")
st.markdown("---")

if 'history' not in st.session_state:
    st.session_state['history'] = pd.DataFrame(columns=['Power', 'Water'])

placeholder = st.empty()

for i in range(20):
    new_data = {'Power': 100 - (i * 1.5), 'Water': 1000 - (i * 5)}
    st.session_state['history'] = pd.concat([st.session_state['history'], pd.DataFrame([new_data])], ignore_index=True)

    with placeholder.container():
        col1, col2 = st.columns(2)
        col1.metric("Power Grid", f"{new_data['Power']:.1f}%")
        col2.metric("Water Reserve", f"{new_data['Water']:.1f} L")
        st.line_chart(st.session_state['history'])
    time.sleep(1)
