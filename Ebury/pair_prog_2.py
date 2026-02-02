class LoanLedger:

    def __init__(self):
        self.load_balances = {}
        self.loan_to_borrower = {}
        self.borrower_loans = {}
    
    def register_loan(self, loan_id, borrower_id):
        self.load_balances[loan_id] = 0
        self.loan_to_borrower[loan_id] = borrower_id

        if borrower_id not in self.borrower_loans:
            self.borrower_loans[borrower_id] = []
        self.borrower_loans[borrower_id].append(loan_id)

    def add_transaction(self, loan_id, transaction_type, amount):
        if loan_id not in self.load_balances:
            self.load_balances[loan_id] = 0
        
        if transaction_type == 'DISBURSEMENT':
            self.load_balances[loan_id] += amount
        elif transaction_type == 'REPAYMENT':
            self.load_balances[loan_id] -= amount
    

    def get_balance(self, loan_id):
        return self.load_balances.get(loan_id,0)


    def get_borrower_exposure(self,borrower_id):
        return sum(self.load_balances[loan_id] for loan_id in self.borrower_loans.get(borrower_id,[]))

def test_phase_2():
    ledger = LoanLedger()
    ledger.register_loan("L001", "B100")
    ledger.register_loan("L002", "B100")
    ledger.register_loan("L003", "B200")

    ledger.add_transaction("L001", "DISBURSEMENT", 1000)
    ledger.add_transaction("L001", "REPAYMENT", 200)
    ledger.add_transaction("L002", "DISBURSEMENT", 500)
    ledger.add_transaction("L003", "DISBURSEMENT", 2000)

    assert ledger.get_balance("L001") == 800
    assert ledger.get_balance("L002") == 500
    assert ledger.get_borrower_exposure("B100") == 1300
    assert ledger.get_borrower_exposure("B200") == 2000

    print("Phase 2 tests passed")

test_phase_2()
