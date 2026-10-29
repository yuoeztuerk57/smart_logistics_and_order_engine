from logistics import (
    PhysicalItem,
    DigitalItem,
    Order,
    black_friday_discount,
    vip_discount,
    ShippingCalculator
)

if __name__ == "__main__":
    print("SMART LOGISTICS & ORDER ENGINE\n")

    tastatur = PhysicalItem("Mechanische Tastatur", 45.00, 1.2)
    monitor = PhysicalItem("4K Monitor", 299.90, 6.5)
    software = DigitalItem("Python Software-Lizenz", 89.00, "https://download.example.com/license")

    order = Order()
    order.add_item(tastatur)
    order.add_item(monitor)
    order.add_item(software)

    print("Übersicht aller bestellten Artikel:")
    for item in order.items:
        print(f" * {item.name}: {item.price:.2f} €")

    teure_produkte = list(filter(lambda item: item.price > 50.0, order.items))
    print("\nGefilterte Produkte (Preis > 50 €):")
    for item in teure_produkte:
        print(f" * {item.name}: {item.price:.2f} €")

    preis_normal = order.calculate_total()
    preis_black_friday = order.calculate_total(black_friday_discount)
    preis_vip = order.calculate_total(vip_discount)

    print("\nRabatt-Kalkulation:")
    print(f"Gesamtsumme (Standard):   {preis_normal:>7.2f} €")
    print(f"Mit Black Friday (-20%):  {preis_black_friday:>7.2f} €")
    print(f"Mit VIP-Rabatt (-15 €):   {preis_vip:>7.2f} €")

    versandkosten = ShippingCalculator.calculate_shipping(order)
    print("\nVersandkosten & Endsumme:")
    print(f"Versandkosten (Physisch): {versandkosten:>7.2f} €")
    print(f"Gesamtbetrag (VIP + Vers.): {preis_vip + versandkosten:>5.2f} €")