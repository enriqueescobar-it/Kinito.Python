from Section21_Strategy.RegularStrategy.AbstractListStrategy import AbstractListStrategy


class HtmlAbstractListStrategy(AbstractListStrategy):

    def start(self, buffer):
        buffer.append('<ul>\n')

    def end(self, buffer):
        buffer.append('</ul>\n')

    def add_list_item(self, buffer, item):
        buffer.append(f'  <li>{item}</li>\n')
