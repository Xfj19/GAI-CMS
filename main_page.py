import streamlit as st

# Function to handle navigation
def navigate_to_page(page):
    st.session_state.page = page
    st.experimental_rerun()

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'A'
if 'input_str' not in st.session_state:
    st.session_state.input_str = ''



# Main page A
def page_a():
    st.set_page_config(page_title='资讯动态展示Demo',layout='wide', initial_sidebar_state='collapsed')
    st.title("资讯动态展示Demo")
    conn = st.connection('mysql', type='sql')
    with st.container(height=250):
        st.header("要闻")
        df = conn.query('SELECT * from macro_economy;', ttl=600)
        for row in df.itertuples():
            if st.button(label=row.source+': '+row.title+' ('+str(row.date)+')', use_container_width=True, help=row.source, key=row.id):
                st.session_state.input_str = row.id
                navigate_to_page('B')
    with st.container(height=250):
        col1, col2, col3 = st.columns(3,gap="large")
        with col1:
            st.header("宏观综合")
        with col2:
            st.header("炼油化工")
        with col3:
            st.header("能源行业")

    with st.container(height=150):
        st.header("应用区")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("简报生成",use_container_width=True):
                # st.session_state.input_str = input_text
                navigate_to_page('C')
        with col2:
            if st.button("会议记录",use_container_width=True):
                # st.session_state.input_str = input_text
                navigate_to_page('D')

# Sub page B
def page_b():
    st.title("资讯详情")
    
    if 'input_str' in st.session_state:
        input_str = st.session_state.input_str
        st.write(f"Received input: {input_str}")
    else:
        st.write("No input received")
    query = f"SELECT * FROM macro_economy WHERE id = {input_str};"
    conn = st.connection('mysql', type='sql')
    detailed_info = conn.query(query)   
    # 显示详细信息
    st.write(detailed_info)

    if st.button("返回主页"):
        navigate_to_page('A')

# Sub page C
def page_c():
    st.title("简报生成")
    
    if 'input_str' in st.session_state:
        input_str = st.session_state.input_str
        st.write(f"Received input: {input_str}")
    else:
        st.write("No input received")
    
    if st.button("返回主页"):
        navigate_to_page('A')

# Sub page D
def page_d():
    st.title("会议记录")
    
    if 'input_str' in st.session_state:
        input_str = st.session_state.input_str
        st.write(f"Received input: {input_str}")
    else:
        st.write("No input received")
    
    if st.button("返回主页"):
        navigate_to_page('A')

# Page routing
if st.session_state.page == 'A':
    page_a()
elif st.session_state.page == 'B':
    page_b()
elif st.session_state.page == 'C':
    page_c()
elif st.session_state.page == 'D':
    page_d()