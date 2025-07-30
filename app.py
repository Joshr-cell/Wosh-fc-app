import streamlit as st
import time
import requests
import json
import random
import pandas as pd

# --- SETTINGS ---
API_TOKEN = "pWdA8b1q6qRW1AM"
VOL_INDEX = "R_100"
STAKE_PERCENT = 0.01  # 1%
TICK_HISTORY = 10
REPEAT_THRESHOLD = 4

# --- STREAMLIT UI ---
st.set_page_config(page_title="Digit Differ Bot", layout="wide")
st.title("🎯 Deriv Digit Differ Bot - Live Trading")
st.markdown("Monitoring latest ticks and placing Digit Differ trades when overexposure is detected.")

placeholder = st.empty()

# --- VARIABLES ---
ws_url = "wss://ws.binaryws.com/websockets/v3?app_id=1089"
balance = 9.0
tick_data = []

# --- FUNCTIONS ---

def get_last_digits(history):
    return [int(tick[-1]) for tick in history]

def is_overexposed(digits):
    counts = {d: digits.count(d) for d in set(digits)}
    for digit, count in counts.items():
        if count >= REPEAT_THRESHOLD:
            return digit
    return None

def place_digit_differ_contract(forbidden_digit, stake, symbol):
    payload = {
        "ticks": 1,
        "subscribe": 1,
        "passthrough": {"action": "trade"},
        "contract_type": "DIGITDIFF",
        "amount": stake,
        "symbol": symbol,
        "duration": 1,
        "basis": "stake",
        "currency": "USD",
        "barrier": forbidden_digit
    }
    return payload

# --- MAIN LOOP ---
if st.button("Start Live Bot"):
    st.success("⏳ Connecting to Deriv and starting live trading...")
    import websocket

    def on_message(ws, message):
        global tick_data, balance
        data = json.loads(message)

        # Handle tick update
        if "tick" in data:
            tick = data["tick"]["quote"]
            tick_data.append(str(tick))
            if len(tick_data) > TICK_HISTORY:
                tick_data.pop(0)

            last_digits = get_last_digits(tick_data)
            forbidden_digit = is_overexposed(last_digits)

            with placeholder.container():
                st.subheader("📈 Latest Digits")
                st.write(last_digits)
                st.write(f"Detected Overexposed Digit: `{forbidden_digit}`")

            if forbidden_digit is not None:
                stake = round(balance * STAKE_PERCENT, 2)
                contract = place_digit_differ_contract(forbidden_digit, stake, VOL_INDEX)

                ws.send(json.dumps({
                    "authorize": API_TOKEN
                }))
                time.sleep(1)
                ws.send(json.dumps({"buy": 1, **contract}))
                st.warning(f"🎯 Placed Digit Differ trade against `{forbidden_digit}` with stake ${stake}")
                time.sleep(5)

        # Handle buy result
        if "buy" in data:
            st.info(f"📤 Trade Placed: {data['buy']['contract_id']}")

    def on_error(ws, error):
        st.error(f"❌ Error: {error}")

    def on_close(ws):
        st.warning("🔌 WebSocket connection closed.")

    def on_open(ws):
        ws.send(json.dumps({
            "ticks": VOL_INDEX,
            "subscribe": 1
        }))

    ws = websocket.WebSocketApp(
        ws_url,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open
    )

    import _thread
    _thread.start_new_thread(ws.run_forever, ())

