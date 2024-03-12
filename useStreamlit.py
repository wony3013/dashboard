import streamlit as st
import streamlit.components.v1 as components
import psutil
import time
def get_info() :
    # CPU 정보 얻기
    cpu_percent = psutil.cpu_percent()
    cpu_count = psutil.cpu_count()
    # 메모리 정보 얻기
    virtual_memory = psutil.virtual_memory()

    total_memory = virtual_memory.total // (1024 * 1024)
    available_memory = virtual_memory.available // (1024 * 1024)
    used_memory = total_memory - available_memory

    totalInfo = {"cpu_percent":cpu_percent,"cpu_count":cpu_count, "total_memory":total_memory, "available_memory":available_memory, "used_memory":used_memory}

    return totalInfo

st.title('CPU/RAM RealTime Status')
with st.container(height=400):
    st.markdown('''<style>[data-testid=stVerticalBlockBorderWrapper]{width:350px}</style>''', unsafe_allow_html=True)
    while(True):
        time.sleep(1)
        info = get_info()
        st.text('CPU : '+str(info['cpu_percent'])+' % RAM : '+str(info['used_memory'])+'/'+str(info['total_memory']))
        js = '''
        <script>
            var body = window.parent.document.querySelector(".st-emotion-cache-g7r313");body.scrollTop = body.scrollHeight;
        </script>
        '''
        st.components.v1.html(js, width=0, height=0, scrolling=False)
        st.markdown('''<style>iframe {display:none} [data-testid=stVerticalBlock]{gap:0}</style>''', unsafe_allow_html=True)

