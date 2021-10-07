import psycopg2
from psycopg2 import Error
from datetime import date

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

from pypostgresql import call_base_see

Builder.load_file("main.kv")

barrel = ''

class ScreenFrame(BoxLayout):
    def XZ(self):
        print("\nScreenFrame.XZ")
        sm.current = "XZ"

    def dacha(self):
        print("\nScreenFrame.dacha")
        sm.current = "dacha"


class Start_Screen(Screen):
    def call_base(self, on_off):
        online_base_call = call_base_see()
        print(int(online_base_call))
        if (int(online_base_call) == 1):
            on_off.text = "Сервер Online"
        else:
            on_off.text = "Сервер НЕДОСТУПЕН"


class XZ_Screen(Screen):

    def zavod1(self, zavod1):
        global barrel
        zavod1.text = "zavod_1_92_25"
        barrel = zavod1.text
        print(barrel)
        zavod1.text = "1 - 92\n\n25m2"

    def zavod2(self, zavod2):
        global barrel
        zavod2.text = "zavod_2_92_25"
        barrel = zavod2.text
        print(barrel)
        zavod2.text = "2 - 92\n\n25m2"

    def zavod3(self, zavod3):
        global barrel
        zavod3.text = "zavod_3_95_15"
        barrel = zavod3.text
        print(barrel)
        zavod3.text = "3 - 95\n\n15m2"

    def zavod4(self, zavod4):
        global barrel
        zavod4.text = "zavod_4_95_10"
        barrel = zavod4.text
        print(barrel)
        zavod4.text = "4 - 95\n\n10m2"

    def zavod5(self, zavod5):
        global barrel
        zavod5.text = "zavod_5_dt_15"
        barrel = zavod5.text
        print(barrel)
        zavod5.text = "5 - ДТ\n\n15m2"

    def zavod6(self, zavod6):
        global barrel
        zavod6.text = "zavod_6_dt_10"
        barrel = zavod6.text
        print(barrel)
        zavod6.text = "6 - ДТ\n\n10m2"


class DACHA_Screen(Screen):

    def dacha1(self, dacha1):
        global barrel
        dacha1.text = "dacha_1_92_25"
        barrel = dacha1.text
        print(barrel)
        dacha1.text = "1 - 92\n\n25m2"

    def dacha2(self, dacha2):
        global barrel
        dacha2.text = "dacha_2_92_25"
        barrel = dacha2.text
        print(barrel)
        dacha2.text = "2 - 92\n\n25m2"

    def dacha3(self, dacha3):
        global barrel
        dacha3.text = "dacha_3_95_25"
        barrel = dacha3.text
        print(barrel)
        dacha3.text = "3 - 95\n\n25m2"

    def dacha4(self, dacha4):
        global barrel
        dacha4.text = "dacha_4_95_25"
        barrel = dacha4.text
        print(barrel)
        dacha4.text = "4 - 95\n\n25m2"

    def dacha5(self, dacha5):
        global barrel
        dacha5.text = "dacha_5_98_25"
        barrel = dacha5.text
        print(barrel)
        dacha5.text = "5 - 98\n\n25m2"

    def dacha6(self, dacha6):
        global barrel
        dacha6.text = "dacha_6_dt_25"
        barrel = dacha6.text
        print(barrel)
        dacha6.text = "6 - ДТ\n\n25m2"


class Save(Screen):
    def job(self, text_0, text_1, text_2, text_3, text_4):

        # Получаем дату сегодня.
        data = date.today()
        print(barrel)
        print(data)
        print(text_0.text)
        print(text_1.text)
        print(text_2.text)
        print(text_3.text)
        print(text_4.text)
        try:
            connection = psycopg2.connect(user="postgres",
                                          # пароль, который указали при установке PostgreSQL
                                          password="Best4KamCH",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="postgres")
            cursor = connection.cursor()
            current_id_table = ('select max(id) from {table}')
            cursor.execute(current_id_table.format(table=barrel))
            n = cursor.fetchone()
            max_id = n[0]
            print(max_id)
            if max_id is None:
                y = [1, text_1.text, text_2.text, text_3.text, text_4.text, data, text_0.text]
                record_to_insert_y = (y)
                postgres_insert_query_y = """ INSERT INTO {table} (id, first_check, reload, second_check, count, date, sale)
                                                   VALUES (%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(postgres_insert_query_y.format(table=barrel), record_to_insert_y)

                connection.commit()
                count = cursor.rowcount
                print(count, "Запись Y успешно добавлена в таблицу")

                if connection:
                    cursor.close()
                    connection.close()
                    print("Соединение с PostgreSQL закрыто")

            else:
                max_id += 1

                z = [max_id, text_1.text, text_2.text, text_3.text, text_4.text, data, text_0.text]
                print(z)

                postgres_insert_query = """ INSERT INTO {table} (id, first_check, reload, second_check, count, date, sale)
                                                   VALUES (%s,%s,%s,%s,%s,%s,%s)"""
                record_to_insert = (z)
                cursor.execute(postgres_insert_query.format(table=barrel), record_to_insert)

                connection.commit()
                count = cursor.rowcount
                print(count, "Запись Z успешно добавлена в таблицу")

                if connection:
                    cursor.close()
                    connection.close()
                    print("Соединение с PostgreSQL закрыто")

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def clear_inputs(self):
        save = self.manager.get_screen('save')
        for child in reversed(save.ids.container.children):
            if isinstance(child, TextInput):
                child.text = ''
                print("CLEAR")

class Finish(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Start_Screen(name='start'))
sm.add_widget(DACHA_Screen(name='dacha'))
sm.add_widget(XZ_Screen(name='XZ'))
sm.add_widget(Save(name='save'))
sm.add_widget(Finish(name='finish'))


class MainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MainApp().run()
