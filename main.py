# Q1 Project
from pyscript import document, display, window


def create_order(e):

    prod1 = document.getElementById('item1')
    prod2 = document.getElementById('item2')
    prod3 = document.getElementById('item3')
    prod4 = document.getElementById('item4')

    subtotal = (
        float(prod1.value) * prod1.checked
        + float(prod2.value) * prod2.checked
        + float(prod3.value) * prod3.checked
        + float(prod4.value) * prod4.checked
    )

    # SKU codes
    sku1 = "MCPAS001"
    sku2 = "MCSPB002"
    sku3 = "MCPIZ003"
    sku4 = "MCWAG004"

    skus = ""

    if prod1.checked:
        skus = skus + sku1 + " "

    if prod2.checked:
        skus = skus + sku2 + " "

    if prod3.checked:
        skus = skus + sku3 + " "

    if prod4.checked:
        skus = skus + sku4

    if skus == "":
        skus = "No items selected"
    display(f"SKU: {skus}" f"The subtotal of your order is: ₱{subtotal:.2f}", target="result")