import time
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.keypair import Keypair
from solana.transaction import Transaction

# This script demonstrates the concept of transaction expiration in Solana due to blockhash.
# In a real scenario, you would interact with a wallet and a network.
# For this demo, we simulate a delay to cause expiration.

# --- Configuration ---
# Replace with your actual RPC endpoint if you want to run against a live network.
# For demonstration, we'll use a placeholder and simulate the logic.
RPC_URL = "https://api.devnet.solana.com"

# --- Simulation Logic ---

def simulate_transaction_expiration():
    print("--- Solana Blockhash Transaction Expiration Demo ---")

    # In a real scenario, you'd get the latest blockhash from the RPC.
    # For simulation, we'll use a dummy value and then a 'stale' value.
    print("Fetching latest blockhash...")
    # In a real app: latest_blockhash = Client(RPC_URL).get_latest_blockhash().value
    latest_blockhash = {"blockhash": "dummy_latest_blockhash_12345", "lastValidBlockHeight": 100000}
    print(f"Simulated latest blockhash: {latest_blockhash['blockhash']}")

    # Simulate creating a transaction with the latest blockhash
    print("Creating a transaction with the latest blockhash...")
    sender_keypair = Keypair()
    recipient_keypair = Keypair()
    transaction = Transaction(recent_blockhash=latest_blockhash['blockhash'])
    # In a real scenario, you'd add instructions here, e.g., transfer lamports
    # transaction.add(system_program.transfer({...}))
    print("Transaction created.")

    # Simulate a delay that exceeds the block production time
    # Solana's block time is ~400ms. A few seconds delay is enough to make it stale.
    delay_seconds = 5
    print(f"Waiting for {delay_seconds} seconds to simulate transaction expiration...")
    time.sleep(delay_seconds)

    # Simulate attempting to send the transaction after the delay
    print("Attempting to send the transaction after delay...")

    # In a real scenario, the RPC client would check if the blockhash is still valid.
    # If the blockhash is too old (i.e., lastValidBlockHeight is too far in the past),
    # the transaction will be rejected by the network or the client will error out.
    # The error message would typically be 'Transaction Expired' or similar.

    print("\n--- Simulation Outcome ---")
    print("If this were a live transaction, it would likely fail with 'Transaction Expired' or a similar error.")
    print("This is because the 'recent_blockhash' used in the transaction is no longer valid.")
    print("The network requires transactions to be processed within a certain window relative to the blockhash's validity.")
    print("To resolve this, a new transaction must be created using a fresh, current blockhash.")

if __name__ == "__main__":
    simulate_transaction_expiration()
