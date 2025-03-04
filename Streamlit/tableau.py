import streamlit as st
import streamlit.components.v1 as components

def show_dashboard():
    st.header("TV Shows Analysis - Tableau Dashboard")
    tableau_url = "https://public.tableau.com/views/TV-ShowsAnalysis/TV-SHOWSOVERVIEW?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
    html_temp = f'''
    <iframe src="{tableau_url}" width="1000" height="600" style="border:none;"></iframe>
    '''
    components.html(html_temp, width=1000, height=600)

if __name__ == '__main__':
    show_dashboard()