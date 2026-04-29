import streamlit as st

st.set_page_config(page_title="Chemistry Lab AI", page_icon="🧪")
st.title("🧪 Химиялық зертхана көмекшісі")
st.write("### Абаева Аруназ бен Фарманова Алинаның ЖИ жобасы")

# Ыдыстар тізімі
glassware = {
    "Бюретка": "Сұйықтықтың нақты көлемін тамшылатып өлшеуге арналған ұзын шыны түтік. Титрлеуде қолданылады.",
    "Колба": "Сұйықтықтарды араластыруға және қыздыруға арналған ыдыс.",
    "Пипетка": "Сұйықтықтың аз мөлшерін дәл өлшеп алуға арналған құрал."
}

tab1, tab2 = st.tabs(["Анықтамалық", "Сұрақ-жауап"])

with tab1:
    selection = st.selectbox("Ыдысты таңдаңыз:", list(glassware.keys()))
    st.success(f"**{selection} туралы мәлімет:**")
    st.write(glassware[selection])

with tab2:
    user_query = st.text_input("Зертханашыдан сұраңыз:")
    if user_query:
        if "титрлеу" in user_query.lower():
            st.info("Титрлеу үшін сізге Бюретка мен Конус тәрізді колба қажет.")
        else:
            st.write("Бұл сұрақ бойынша іздеп көрейін...")
