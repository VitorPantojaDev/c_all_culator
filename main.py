import streamlit as st

st.header("English")
if st.button("Brazilian Portuguese"):
    st.switch_page("pages/main_br.py")

#title
st.title("🧮 Multifunctional Calculator")
st.subheader("Choose the type of calculation you want")

if "type_calc" not in st.session_state:
    st.session_state.type_calc = None

#sidebar
st.sidebar.write("Type of calculation:")

if st.sidebar.button("Golden Material"):
    st.session_state.type_calc = "Golden Material"
if st.sidebar.button("Basic Math"):
    st.session_state.type_calc = "Basic Math"
if st.sidebar.button("Scientific"):
    st.session_state.type_calc = "Scientific"
if st.sidebar.button("Medication Dosis"):
    st.session_state.type_calc = "Medication Dosis"
if st.sidebar.button("Financial"):
    st.session_state.type_calc = "Financial"

type_calc = st.session_state.type_calc

#basic math
if st.session_state.type_calc == "Basic Math":
    st.markdown("### 🔢 Basic Opertation")

    num_a = st.number_input("Type first number: ", value=0.0)
    num_b = st.number_input("Type second number: ", value=0.0)

    operation_input = st.selectbox(
        "Choose the operation:",
        [
            "Select...",
            "+ (Addition)",
            "- (Subtraction)",
            "* (Multiply)",
            "/ (Divide)",
        ],
    )

    if st.button("Calculate"):
        if "+ (Addition)" in operation_input:
            st.success(f"Result: {num_a + num_b}")

        elif "- (Subtraction)" in operation_input:
            st.success(f"Result: {num_a - num_b}")

        elif "* (Multiply)" in operation_input:
            st.success(f"Result: {num_a * num_b}")

        elif "/ (Divide)" in operation_input:
            if num_b != 0:
                st.success(f"Resultado: {num_a / num_b}")
            else:
                st.error("Error: Divide by zero!")

        else:
            st.warning("Please, select a valid operation.")

#golden material
elif st.session_state.type_calc == "Golden Material":
    st.markdown("### 🟨 Golden Mateiral")

    num_a = st.number_input("Type first number: ", value=0)
    dez_a = num_a
    while dez_a > 10:
        st.write("# "+("🟨"*10))
        dez_a = dez_a - 10
    st.write("# "+("🟨"*dez_a))

    num_b = st.number_input("Type second number: ", value=0)
    dez_b = num_b
    while dez_b > 10:
        st.write("# "+("🟨"*10))
        dez_b = dez_b - 10
    st.write("# "+("🟨"*dez_b))

    operation_input = st.selectbox(
        "Choose the operation:",
        [
            "Select...",
            "+ (Addition)",
            "- (Subtraction)",
        ],
    )

    if st.button("Calculate"):
        if "+ (Addition)" in operation_input:
            result = num_a + num_b
            while result > 10:
                st.write("# "+("🟨"*10))
                result = result - 10
            st.write("# "+("🟨"*result))
                           
        elif "- (Subtraction)" in operation_input:
            if num_b <= num_a:
                result = num_a - num_b
                while result > 10:
                    st.write("# "+("🟨"*10))
                    result = result - 10
                st.write("# "+("🟨"*result))
            else:
                st.write("## You can't take away more cubes than you have")

#scientific
elif st.session_state.type_calc == "Scientific":
    st.markdown("### 🥼 Scientific")

    operation_input = st.selectbox(
        "Choose the operation:",
        [
            "Select...",
            "% (Percentage)",
            "√² (Square root)",
            "x² (Squared)",
            "x³ (Cubed)",
        ],
    )

    if "% (Percentage)" in operation_input:
        num_a = st.number_input("Type first number: ", value=0.0)
        num_b = st.number_input("Type second number: ", value=0.0)
        st.write(num_a, "%", num_b)
        st.success(f"Result: {num_a * num_b / 100}")

    elif "√² (Square root)" in operation_input:
        num_a = st.number_input("Type your number: ", value=0.0)
        st.success(f"Result: {num_a ** 0.5}")

    elif "x² (Squared)" in operation_input:
        num_a = st.number_input("Type your number: ", value=0.0)
        st.success(f"Result: {num_a ** 2}")
            
    elif "x³ (Cubed)" in operation_input:
        num_a = st.number_input("Type your number: ", value=0.0)
        st.success(f"Result: {num_a ** 3}")

    else:
        st.warning("Please, select a valid operation.")          

#medication dosis
elif st.session_state.type_calc == "Medication Dosis":
    st.markdown("### 💊 Medication Dosis")

    weight = st.number_input("Type the patient weight (kg): ", value=0.0)
    dosis = st.number_input("Type dosis (mg/kg): ", value=0.0)
    conc = st.number_input("Type medication concentration (mg/ml or mg/pill): ", value=0.0)

    if weight <= 0 or weight <= 0 or conc <= 0:
        st.warning("Please, choose valid parameters.")
    else:
        dosage = dosis * weight / conc
        st.success(f"Dosage: {dosage}")

#financial
elif st.session_state.type_calc == "Financial":
    st.markdown("### 🪙 Financial")

    operation_input = st.selectbox(
        "Choose the financial planning:",
        [
            "Select...",
            "Monthly Expenses",
            "Financial Runaway",
            "Creating Reserve Funding",            
        ],
    )

    if "Monthly Expenses" in operation_input:
        st.write("You can type your total income and total expense or type each expense")
        income = st.number_input("Type your monthly income: ", value=0.0)
        total_expense = st.number_input("Type your total expense: ", value=0.0)

        if total_expense == 0.0:
            rent = st.number_input("Rent/Housing: ", value=0.0)
            water = st.number_input("Water bill: ", value=0.0)
            power = st.number_input("Power bill: ", value=0.0)
            phone = st.number_input("Phone/Internet bill: ", value=0.0)
            school = st.number_input("School/Education costs: ", value=0.0)
            food = st.number_input("Supermarket: ", value=0.0)
            transport = st.number_input("Gasoline/Transport: ", value=0.0)
            credit_card = st.number_input("Credit Card: ", value=0.0)
            loan = st.number_input("Loans: ", value=0.0)
            other = st.number_input("Others: ", value=0.0)

            total_expense_calc = rent+water+power+phone+school+food+transport+credit_card+loan+other
            st.success(f"Total expenses: {total_expense_calc}")

            st.success(f"Balance: {income - total_expense_calc}")

        else:
            st.success(f"Balance: {income - total_expense}")

    elif "Financial Runaway" in operation_input:
        savings = st.number_input("Type your total savings: ", value=0.0)
        monthly_yield = st.number_input("Type approximate monthly yield in % (0,5 suggested for saving account): ", value=0.5)
        withdraw = st.number_input("Type your montly withdraw: ", value=0.0)
        deposit = st.number_input("Type your montly deposit: ", value=0.0)

        if st.button("Duration of the savings in months:"):

            if deposit >= withdraw:
                st.warning("Your savings will last forever.")  

            else:
                duration = 0

                savings_update = withdraw - deposit
        
                while savings >= savings_update:
                    savings = savings - savings_update
                    savings = savings + savings * monthly_yield / 100
                    duration = duration + 1

                st.success(duration)

    elif "Creating Reserve Funding" in operation_input:
        goal = st.number_input("Type your savings goal: ", value=0.0)
        monthly_yield = st.number_input("Type approximate monthly yield in % (0,5 suggested for saving account): ", value=0.5)
        deposit = st.number_input("Type your montly deposit: ", value=0.0)

        if st.button("Calculate the time you need to reach your goal:"):

            if deposit <= 0.0:
                st.warning("Without a monthly deposit you will never reach your goal.")  

            else:
                month = 0
                reserve = 0
                     
                while reserve < goal:
                    reserve = reserve + deposit
                    reserve = reserve + reserve * monthly_yield / 100
                    month = month + 1

                st.success(f"Months to reach your goal: {month}")
                goal_years = round(month / 12)
                st.success(f"Years to reach your goal: {goal_years}")

    else:
        st.warning("Please, select a financial planning.")

#bottom
with st.bottom:

    st.write("Personal Project to practice Python by Vitor A Pantoja")
    link1, link2, link3 = st.columns(3)
    with link1:
        st.link_button("E-mail", "vitorpantoja.dev@gmail.com")
    with link2:
        st.link_button("Github", "https://github.com/VitorPantojaDev")
    with link3:
        st.link_button("Linkedin", "https://www.linkedin.com/in/vitorapantoja/")
