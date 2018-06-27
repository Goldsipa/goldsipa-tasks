# -*- coding: utf-8 -*- 


class Emitter:
    def __init__(self):
        """Создает экземпляр класса Emitter.

        Attributes
        ----------
        events : dict(str: [func])
            словарь событий-обработчиков
        """
        self.events = {}            

    def on(self, event, handler):
        """ связывает обработчик handler с событием event

        Parameters
        ---------
        event : str
            событие
        handler : func
            обработчик
        """
        if event not in self.events.keys():            # проверка на наличие события в словаре
            self.events[event] = []
        if handler not in self.events[event]:           # проверка на наличие обработчика у события
            self.events[event].append(handler)

    def emit(self, event, data):
        """ Генерирует событие event -- вызывает все связанные с ним
            обработчики, в которые передает аргумент data

        Parameters
        ----------
        event : str
            событие
        data
            данные, которые необходимо передать обработчикам
        """
        if event in self.events.keys():
            for handler in self.events[event]:          # вызов всех связанных с событием обработчиков,
                handler(data)