import streamlit as st

st.header("Português Brasileiro")
if st.button("Inglês"):
    st.switch_page("main.py")

#title
st.title("🧮 Calculadora Multifuncional")
st.subheader("Escolha o tipo de cálculo que você quer fazer")

if "type_calc" not in st.session_state:
    st.session_state.type_calc = None

#sidebar
st.sidebar.write("Tipo de cálculo:")

if st.sidebar.button("Material Dourado"):
    st.session_state.type_calc = "Material Dourado"
if st.sidebar.button("Básica"):
    st.session_state.type_calc = "Básica"
if st.sidebar.button("Científica"):
    st.session_state.type_calc = "Científica"
if st.sidebar.button("Dose de Medicação"):
    st.session_state.type_calc = "Dose de Medicação"
if st.sidebar.button("Financeiro"):
    st.session_state.type_calc = "Financeiro"

type_calc = st.session_state.type_calc

#contas básicas
if st.session_state.type_calc == "Básica":
    st.markdown("### 🔢 Operações Básicas")

    num_a = st.number_input("Digite o primeiro número: ", value=0.0)
    num_b = st.number_input("Digite o segundo número: ", value=0.0)

    operation_input = st.selectbox(
        "Escolhe a operação:",
        [
            "Selecione...",
            "+ (Soma)",
            "- (Subtração)",
            "* (Multiplicação)",
            "/ (Divisão)",
        ],
    )

    if st.button("Calcular"):
        if "+ (Soma)" in operation_input:
            st.success(f"Resultado: {num_a + num_b}")

        elif "- (Subtração)" in operation_input:
            st.success(f"Resultado: {num_a - num_b}")

        elif "* (Multiplicação)" in operation_input:
            st.success(f"Resultado: {num_a * num_b}")

        elif "/ (Divisão)" in operation_input:
            if num_b != 0:
                st.success(f"Resultado: {num_a / num_b}")
            else:
                st.error("Erro: Divisão por zero!")

        else:
            st.warning("Por favor, selecione uma operação válida.")



elif type_calc in ["cientifica", "material dourado", "dose de medicao", "rendimentos"]:
    st.info(f"A seção de cientifica, material dourado, dose de medicao, rendimentos está em desenvolvimento.")
