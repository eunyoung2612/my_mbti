import streamlit as st

# MBTI 유형별 추천 포켓몬 데이터
mbti_pokemon = {
    "INTJ": {"name": "메타그로스", "reason": "전략적 사고와 강한 목표 지향성을 지닌 포켓몬입니다."},
    "INTP": {"name": "슬로우킹", "reason": "깊은 사고와 분석을 즐기는 지적인 포켓몬입니다."},
    "ENTJ": {"name": "리자몽", "reason": "강한 리더십과 추진력을 상징하는 포켓몬입니다."},
    "ENTP": {"name": "딱구리", "reason": "재치 있고 임기응변에 강한 포켓몬입니다."},
    "INFJ": {"name": "뮤", "reason": "신비롭고 통찰력 있는 이상주의 포켓몬입니다."},
    "INFP": {"name": "라프라스", "reason": "따뜻한 마음과 이상을 소중히 여기는 포켓몬입니다."},
    "ENFJ": {"name": "루카리오", "reason": "타인을 이끌고 돕는 데 능한 포켓몬입니다."},
    "ENFP": {"name": "피카츄", "reason": "밝고 에너지 넘치는 친화력의 상징입니다."},
    "ISTJ": {"name": "개굴닌자", "reason": "원칙과 책임감을 중시하는 포켓몬입니다."},
    "ISFJ": {"name": "잠만보", "reason": "안정적이고 헌신적인 성향의 포켓몬입니다."},
    "ESTJ": {"name": "삼지주", "reason": "체계적이고 관리 능력이 뛰어난 포켓몬입니다."},
    "ESFJ": {"name": "픽시", "reason": "사교적이고 배려심 많은 포켓몬입니다."},
    "ISTP": {"name": "이상해씨", "reason": "실용적이고 적응력이 뛰어난 포켓몬입니다."},
    "ISFP": {"name": "이브이", "reason": "다재다능하고 개성이 뚜렷한 포켓몬입니다."},
    "ESTP": {"name": "부스터", "reason": "즉흥적이고 행동력이 강한 포켓몬입니다."},
    "ESFP": {"name": "고라파덕", "reason": "즉흥적이고 유쾌한 매력의 포켓몬입니다."},
}

st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="🎮")

# 페이지 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "직접 선택"

st.sidebar.title("메뉴")
page = st.sidebar.radio("페이지를 선택하세요", ["직접 선택", "MBTI 간이 테스트"], index=0 if st.session_state.page == "직접 선택" else 1)
st.session_state.page = page


def show_result(mbti_code):
    result = mbti_pokemon[mbti_code]
    st.subheader(f"✨ {mbti_code} 유형에게 추천하는 포켓몬")
    st.markdown(f"### {result['name']}")
    st.write(result['reason'])


# ---------------------------
# 페이지 1: 직접 선택
# ---------------------------
if page == "직접 선택":
    st.title("🎮 MBTI 포켓몬 추천기")
    st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 추천해드립니다.")

    mbti_list = list(mbti_pokemon.keys())
    selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

    if st.button("포켓몬 추천 받기"):
        show_result(selected_mbti)

# ---------------------------
# 페이지 2: 간이 MBTI 테스트
# ---------------------------
else:
    st.title("📝 MBTI 간이 테스트")
    st.write("아래 4개 질문에 답하면 간단히 MBTI 유형을 추정해드립니다.")
    st.caption("※ 질문 1개당 하나의 축(E/I, S/N, T/F, J/P)을 판단하는 단순화된 테스트입니다. 정식 심리검사가 아니니 참고용으로만 봐주세요.")

    q1 = st.radio(
        "1. 주말에 에너지를 얻는 방법은?",
        ["친구들을 만나 어울리며 활력을 얻는다 (E)", "혼자만의 시간을 보내며 재충전한다 (I)"]
    )

    q2 = st.radio(
        "2. 새로운 정보를 받아들일 때 더 편한 방식은?",
        ["구체적인 사실과 경험을 중시한다 (S)", "가능성과 아이디어, 큰 그림을 중시한다 (N)"]
    )

    q3 = st.radio(
        "3. 결정을 내릴 때 더 중요하게 생각하는 것은?",
        ["논리와 원칙에 따라 객관적으로 판단한다 (T)", "사람들의 감정과 관계를 고려해서 판단한다 (F)"]
    )

    q4 = st.radio(
        "4. 일상을 살아가는 스타일은?",
        ["계획을 세우고 정해진 대로 진행하는 게 편하다 (J)", "상황에 따라 유연하게 대처하는 게 편하다 (P)"]
    )

    if st.button("내 MBTI 결과 보기"):
        e_or_i = "E" if q1.endswith("(E)") else "I"
        s_or_n = "S" if q2.endswith("(S)") else "N"
        t_or_f = "T" if q3.endswith("(T)") else "F"
        j_or_p = "J" if q4.endswith("(J)") else "P"

        result_mbti = e_or_i + s_or_n + t_or_f + j_or_p

        st.success(f"당신의 예상 MBTI는 **{result_mbti}** 입니다.")
        show_result(result_mbti)
