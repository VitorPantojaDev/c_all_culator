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

    operation_input = st.selectbox(
        "Escolha o planejamento financeiro:",
        [
            "Selecione...",
            "Gastos Mensais",
            "Fundo de emergência",
            "Criando fundo de reserva",            
        ],
    )

    if "Gastos Mensais" in operation_input:
        st.write("Você pode digitar seu ganho mensal total e seu gasto mensal total ou digitar cada uma das suas despesas")
        income = st.number_input("Digite seu ganho mensal total: ", value=0.0)
        total_expense = st.number_input("Digite seu gasto mensal total: ", value=0.0)

        if total_expense == 0.0:
            rent = st.number_input("Aluguel/Moradia: ", value=0.0)
            water = st.number_input("Conta de água: ", value=0.0)
            power = st.number_input("Conta de luz: ", value=0.0)
            phone = st.number_input("Telefone/Internet: ", value=0.0)
            school = st.number_input("Escola/Custo com educação: ", value=0.0)
            food = st.number_input("Supermercado: ", value=0.0)
            transport = st.number_input("Gasolina/Transporte: ", value=0.0)
            credit_card = st.number_input("Cartão de Crédito: ", value=0.0)
            loan = st.number_input("Emprestimo: ", value=0.0)
            other = st.number_input("Outros: ", value=0.0)

            total_expense_calc = rent+water+power+phone+school+food+transport+credit_card+loan+other
            st.success(f"Despesas totais: {total_expense_calc}")

            st.success(f"Balanço: {income - total_expense_calc}")

        else:
            st.success(f"Balanço: {income - total_expense}")

    elif "Fundo de emergência" in operation_input:
        savings = st.number_input("Digite seu valor guardado: ", value=0.0)
        monthly_yield = st.number_input("Digite o seu rendimento mensal em % (0,5 sugerido para poupança): ", value=0.5)
        withdraw = st.number_input("Digite seu saque mensal: ", value=0.0)
        deposit = st.number_input("Digite seu depósito mensal: ", value=0.0)

        if st.button("Duração do seu valor guardado em meses:"):

            if deposit >= withdraw:
                st.warning("Seu valor guardado vai durar para sempre.")  

            else:
                duration = 0

                savings_update = withdraw - deposit
        
                while savings >= savings_update:
                    savings = savings - savings_update
                    savings = savings + savings * monthly_yield / 100
                    duration = duration + 1

                st.success(duration)

    elif "Criando fundo de reserva" in operation_input:
        goal = st.number_input("Digite seu objetivo: ", value=0.0)
        monthly_yield = st.number_input("Digite o seu rendimento mensal em % (0,5 sugerido para poupança): ", value=0.5)
        deposit = st.number_input("Digite seu depósito mensal: ", value=0.0)

        if st.button("Calcule o tempo que precisa para alcançar seu objetivo:"):

            if deposit <= 0.0:
                st.warning("Sem um depósito mensal você nunca vai alcançar seu objetivo.")  

            else:
                month = 0
                reserve = 0
                     
                while reserve < goal:
                    reserve = reserve + deposit
                    reserve = reserve + reserve * monthly_yield / 100
                    month = month + 1

                st.success(f"Meses para alcançar seu objetivo: {month}")
                goal_years = round(month / 12)
                st.success(f"Anos para alcançar seu objetivo: {goal_years}")

    else:
        st.warning("Por favor, selecione o seu planejamento fincaneiro.")  

#bottom
with st.bottom:

    st.write("Projeto pessoal por Vitor A Pantoja")
    st.write("vitorpantoja.dev@gmail.com")
    link1, link2 = st.columns(2)
    with link1:
        st.link_button("Github", "https://github.com/VitorPantojaDev")
    with link2:
        st.link_button("Linkedin", "https://www.linkedin.com/in/vitorapantoja/")
