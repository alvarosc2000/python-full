class LoanLedger:

    def __init__ (self):
        self.loan_balances = {}


    def add_transaction(self, loan_id, transaction_type, amount):
        if loan_id not in self.loan_balances:
            self.loan_balances[loan_id] = 0
        
        if transaction_type == "DISBURSEMENT":
            self.loan_balances[loan_id] += amount
        elif transaction_type == "REPAYMENT":
            self.loan_balances[loan_id] -= amount
    
    def get_balance(self, loan_id):
        return self.loan_balances.get(loan_id,0)
    

if __name__ == "__main__":
    ledger = LoanLedger()

    ledger.add_transaction("L001", "DISBURSEMENT", 1000)
    assert ledger.get_balance("L001") == 1000

    ledger.add_transaction("L001", "REPAYMENT", 300)
    assert ledger.get_balance("L001") == 700

    ledger.add_transaction("L001", "DISBURSEMENT", 500)
    assert ledger.get_balance("L001") == 1200

    print("Phase 1 tests passed ✅")
