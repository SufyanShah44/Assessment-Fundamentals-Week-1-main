"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""

def generate_invoice(receipt_string: str) -> str:
    """Returns a VAT Receipt"""
    lines = receipt_string.splitlines()
    for line in lines:
        if "Total:" in line:
            total = float(line.split("£")[1])

    vat = total * 0.2
    total_with_vat = total + vat

    invoice = "VAT RECEIPT\n"
    invoice += "\n"
    for line in lines:
        invoice += line + "\n"
    invoice +=  f"VAT: £{vat:.2f}\n"
    invoice += f"Total inc VAT: £{total_with_vat:.2f}"

    return invoice # return the invoice string

if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
