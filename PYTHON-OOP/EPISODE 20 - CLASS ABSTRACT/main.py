# membuat class abtract
# ABC = abtract Base Class
from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def click(self):
        print("button click")


class PushButton(Button):

    def click(self):
        print("push button click")


class RadioButton(Button):
    def select(self):  # error karena tidak sesuai dengan abstrac class, harus click
        print("radio button click")


tombol1 = PushButton()

tombol1.click()
