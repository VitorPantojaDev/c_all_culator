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

#basic math
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

#golden material
elif st.session_state.type_calc == "Material Dourado":
    st.markdown("### 🟨 Material Dourado")

    num_a = st.number_input("Digite o primeiro número: ", value=0)
    dez_a = num_a
    while dez_a > 10:
        st.write("# "+("🟨"*10))
        dez_a = dez_a - 10
    st.write("# "+("🟨"*dez_a))

    num_b = st.number_input("Digite o segundo número: ", value=0)
    dez_b = num_b
    while dez_b > 10:
        st.write("# "+("🟨"*10))
        dez_b = dez_b - 10
    st.write("# "+("🟨"*dez_b))

    operation_input = st.selectbox(
        "Escolha a operação:",
        [
            "Selecione...",
            "+ (Soma)",
            "- (Subtração)",
        ],
    )

    if st.button("Calcular"):
        if "+ (Soma)" in operation_input:
            result = num_a + num_b
            while result > 10:
                st.write("# "+("🟨"*10))
                result = result - 10
            st.write("# "+("🟨"*result))
                           
        elif "- (Subtração)" in operation_input:
            if num_b <= num_a:
                result = num_a - num_b
                while result > 10:
                    st.write("# "+("🟨"*10))
                    result = result - 10
                st.write("# "+("🟨"*result))
            else:
                st.write("## Você não pode tirar mais do que você tem")

#scientific
elif st.session_state.type_calc == "Científica":
    st.markdown("### 🥼 Científica")

    operation_input = st.selectbox(
        "Escolha a operação:",
        [
            "Selecione...",
            "% (Porcentagem)",
            "√² (Raiz Quadrada)",
            "x² (Elevado ao quadrado)",
            "x³ (Elevado ao cubo)",
        ],
    )

    if "% (Porcentagem)" in operation_input:
        num_a = st.number_input("Digite o primeiro número: ", value=0.0)
        num_b = st.number_input("Digite o segundo número: ", value=0.0)
        st.write(num_a, "%", num_b)
        st.success(f"Resultado: {num_a * num_b / 100}")

    elif "√² (Raiz Quadrada)" in operation_input:
        num_a = st.number_input("Digite o seu número: ", value=0.0)
        st.success(f"Resultado: {num_a ** 0.5}")

    elif "x² (Elevado ao quadrado)" in operation_input:
        num_a = st.number_input("Digite o seu número: ", value=0.0)
        st.success(f"Resultado: {num_a ** 2}")
            
    elif "x³ (Elevado ao cubo)" in operation_input:
        num_a = st.number_input("Digite o seu número: ", value=0.0)
        st.success(f"Resultado: {num_a ** 3}")

    else:
        st.warning("Por favor, selecione uma operação válida.")          

#medication dosis
elif st.session_state.type_calc == "Dose de Medicação":
    st.markdown("### 💊 Dose de Medicação")

    weight = st.number_input("Digite o peso do paciente (kg): ", value=0.0)
    dosis = st.number_input("Digite a dose (mg/kg): ", value=0.0)
    conc = st.number_input("Digite a concentração da medicação (mg/ml or mg/pill): ", value=0.0)

    if weight <= 0 or weight <= 0 or conc <= 0:
        st.warning("Por favor, escolha paramêtros válidos.")
    else:
        dosage = dosis * weight / conc
        st.success(f"Dose: {dosage}")

#financial
elif st.session_state.type_calc == "Financeiro":
    st.markdown("### 🪙 Financeiro")

    st.warning("Em andamento")


