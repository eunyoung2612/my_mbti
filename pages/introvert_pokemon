import streamlit as st

introvert_pokemon = [
    {"name": "라프라스", "dex": 131, "reason": "혼자서도 잔잔한 바다를 유유히 헤엄치는 모습이 인상적인 포켓몬입니다."},
    {"name": "슬로우포크", "dex": 79, "reason": "서두르지 않고 자기만의 속도로 세상을 관찰하는 포켓몬입니다."},
    {"name": "잠만보", "dex": 143, "reason": "혼자 있는 시간과 휴식을 중요하게 여기는 포켓몬입니다."},
    {"name": "고오스", "dex": 92, "reason": "어두운 곳에서 조용히 활동하며 혼자만의 영역을 지키는 포켓몬입니다."},
    {"name": "뮤츠", "dex": 150, "reason": "타인과 거리를 두고 자기 내면에 집중하는 고독한 포켓몬입니다."},
    {"name": "야도란", "dex": 80, "reason": "한 자리에 오래 머무르며 조용히 생각에 잠기는 포켓몬입니다."},
    {"name": "루브도", "dex": 356, "reason": "필요할 때만 반응하고 평소엔 조용히 자리를 지키는 포켓몬입니다."},
    {"name": "이상해꽃", "dex": 3, "reason": "화려하게 나서기보다 묵묵히 자기 자리를 지키는 포켓몬입니다."},
]

def pokemon_image_url(dex_number):
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{dex_number}.png"

st.set_page_config(page_title="내향인 포켓몬 도감", page_icon="🌙")

st.title("🌙 내향인을 위한 포켓몬 도감")
st.write("혼자만의 시간을 소중히 여기는 성향에 어울리는 포켓몬들을 모아봤습니다.")
st.caption("※ 이 목록은 포켓몬의 공식 설정이나 심리학적 분류가 아니라, 이미지에 기반해 임의로 구성한 것입니다.")

cols = st.columns(2)
for i, p in enumerate(introvert_pokemon):
    with cols[i % 2]:
        st.image(pokemon_image_url(p["dex"]), width=200)
        st.markdown(f"### {p['name']}")
        st.write(p['reason'])
        st.divider()
