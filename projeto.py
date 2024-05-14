import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    st.title("Conversor de Temperatura")

    temperature = st.number_input("Digite a temperatura:")
    unit = st.selectbox("Selecione a unidade de temperatura:", ("Celsius", "Fahrenheit"))

    if unit == "Celsius":
        converted_temperature = celsius_to_fahrenheit(temperature)
        st.write(f"{temperature} graus Celsius é igual a {converted_temperature:.2f} graus Fahrenheit.")
    else:
        converted_temperature = fahrenheit_to_celsius(temperature)
        st.write(f"{temperature} graus Fahrenheit é igual a {converted_temperature:.2f} graus Celsius.")

if __name__ == "__main__":
    main()
