# main.py
import streamlit as st

def main():
    st.set_page_config(page_title="Trading Dashboard", layout="wide")
    st.title("💰 Crypto Trading Bot")
    st.write("Connected to DexScreener API")

if __name__ == "__main__":
    main()