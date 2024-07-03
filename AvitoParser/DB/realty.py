import sqlite3


def check_database(offer):
    offer_id = offer["offer_id"]

    connection = sqlite3.connect("C:\\Users\\123\\PycharmProjects\\AvitoParser\\DB\\realty.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT offer_id FROM offers WHERE offer_id = ?
    """, (offer_id,))

    result = cursor.fetchone()

    if result is None:
        # TODO send_telegram(offer)

        cursor.execute("""
            INSERT INTO offers
            VALUES (NULL, :title, :url, :offer_id, :date, :price,
            :address, :area, :floor)
        """, offer)

        connection.commit()
        print(f'Объявление {offer_id} добавлено в базу данных')

    connection.close()
