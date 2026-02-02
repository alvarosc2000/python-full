class LoanLedger:

    def __init__(self):
        self.loan_balances = {}
        self.loan_to_borrower = {}
        self.borrower_loans = {}
        self.borrower_limit = {}
    
    def register_loan(self, loan_id, borrower_id, credit_limit):
        self.loan_balances[loan_id] = 0
        self.loan_to_borrower[loan_id] = borrower_id

        if borrower_id not in self.borrower_loans:
            self.borrower_loans[borrower_id] = []
            self.borrower_limit[borrower_id] = credit_limit
        self.borrower_loans[borrower_id].append(loan_id)

    def add_transaction(self, loan_id, transaction_type, amount):
        borrower_id = self.loan_to_borrower[loan_id]

        if transaction_type == "DISBURSEMENT":
            new_exposure = self.get_borrower_exposure(borrower_id) + amount
            if new_exposure > self.borrower_limit[borrower_id]:
                raise Exception("Limite superado")
            self.loan_balances[loan_id] += amount
        elif transaction_type == "REPAYMENT":
            self.loan_balances[loan_id] -= amount
    

    def get_balance(self, loan_id):
        return self.loan_balances.get(loan_id,0)
    

    def get_borrower_exposure(self, borrower_id):
        return sum(
            self.loan_balances[loan_id] for loan_id in self.borrower_loans.get(borrower_id,[])
        )

    def get_available_credit(self,borrower_id):
        return(
            self.borrower_limit[borrower_id] - self.get_borrower_exposure(borrower_id)
        )

def test_phase_3():
    ledger = LoanLedger()
    ledger.register_loan("L001", "B100", credit_limit=5000)
    ledger.register_loan("L002", "B100", credit_limit=5000)

    ledger.add_transaction("L001", "DISBURSEMENT", 3000)
    ledger.add_transaction("L002", "DISBURSEMENT", 1500)

    try:
        ledger.add_transaction("L001", "DISBURSEMENT", 1000)
        assert False
    except Exception:
        pass

    ledger.add_transaction("L001", "REPAYMENT", 500)
    ledger.add_transaction("L002", "DISBURSEMENT", 800)

    assert ledger.get_available_credit("B100") == 200

    print("Phase 3 tests passed")

test_phase_3()

