# 1. 패키지 설치
!pip install streamlit -q
!npm install -g localtunnel -q

# 2. app.py 파일 생성 (문자열 파일 쓰기 방식으로 우회하여 에러 방지)
code = """
import streamlit as st

st.set_page_config(page_title="방 탈출 게임", page_icon="🚪", layout="centered")
st.title("🚪 미스터리 방 탈출")
st.subheader("당신은 낯선 방에 갇혔습니다. 단서를 찾아 탈출하세요!")
st.write("---")

if "stage" not in st.session_state:
    st.session_state.stage = "start"
if "has_key" not in st.session_state:
    st.session_state.has_key = False

if st.session_state.stage == "start":
    st.write("방 한가운데에 서 있습니다. 전면에 **낡은 책상**이 있고, 오른쪽에 **굳게 닫힌 문**이 보입니다.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗄️ 책상 조사하기"):
            st.session_state.stage = "desk"
            st.rerun()
    with col2:
        if st.button("🚪 문으로 가기"):
            st.session_state.stage = "door"
            st.rerun()

elif st.session_state.stage == "desk":
    st.write("### 🗄️ 낡은 책상")
    if not st.session_state.has_key:
        st.write("책상 서랍을 열어보니 반짝이는 **황금 열쇠**가 놓여 있습니다!")
        if st.button("🔑 열쇠 줍기"):
            st.session_state.has_key = True
            st.success("열쇠를 획득했습니다!")
    else:
        st.write("책상 서랍은 텅 비어 있습니다.")
    if st.button("⬅️ 뒤로 가기"):
        st.session_state.stage = "start"
        st.rerun()

elif st.session_state.stage == "door":
    st.write("### 🚪 굳게 닫힌 문")
    st.write("문이 단단히 잠겨 있습니다. 열쇠가 필요해 보입니다.")
    if st.session_state.has_key:
        if st.button("🔓 열쇠로 문 열기"):
            st.session_state.stage = "escape"
            st.rerun()
    else:
        st.warning("문이 잠겨 있어 열 수 없습니다.")
    if st.button("⬅️ 뒤로 가기"):
        st.session_state.stage = "start"
        st.rerun()

elif st.session_state.stage == "escape":
    st.balloons()
    st.success("🎉 축하합니다! 방에서 성공적으로 탈출하셨습니다!")
    if st.button("🔄 처음부터 다시 하기"):
        st.session_state.stage = "start"
        st.session_state.has_key = False
        st.rerun()
"""

with open("app.py", "w", encoding="utf-8") as f:
    f.write(code)

# 3. IP 주소 출력 및 스트리밋 실행
import urllib
print("\n" + "="*50)
print("🔑 인증에 필요한 IP 주소:", urllib.request.urlopen('https://ident.me').read().decode('utf8'))
print("="*50 + "\n")

!streamlit run app.py & npx localtunnel --port 8501
