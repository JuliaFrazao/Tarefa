import streamlit as st
notas= []
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def main():
    st.title("Calculadora de Média")
    st.write("Este é um aplicativo simples para calcular a média de notas.")

    # Adicionando notas
    nota = st.number_input("Digite uma nota:", min_value=0.0, max_value=10.0, step=0.1)
    if st.button("Adicionar Nota"):
        notas.append(nota)

    # Exibindo notas adicionadas
    st.write("Notas adicionadas:", notas)

    # Calculando e exibindo a média
    if len(notas) > 0:
        media = calcular_media(notas)
        st.write(f"Média: {media}")
        
if __name__ == "__main__":
   notas = [] 
   main()
    

