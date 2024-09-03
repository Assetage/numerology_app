import streamlit as st

from numerology_app.calculate_context import generate_context
from numerology_app.generate_pdf import generate_report


def main():
    st.title("Numerology Analysis")
    name = st.text_input("Enter the person's name:")
    birthdate = st.text_input("Enter the person's birth date:", "dd.mm.yyyy")

    if st.button("Start Numerological Analysis"):
        context = generate_context(name=name, birthdate=birthdate)
        generate_report(context)
        pdf_path = (
            f'generated_reports/{name.capitalize()}_{birthdate.replace(".", "")}.pdf'
        )
        with open(pdf_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="Download Numerology Analysis",
            data=PDFbyte,
            file_name=f"{name.capitalize()}_{birthdate}.pdf",
            mime="application/octet-stream",
        )
        st.success("Numerology analysis is ready!")


if __name__ == "__main__":
    main()
