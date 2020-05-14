from Section21_Strategy.RegularStrategy.AbstractListStrategy import AbstractListStrategy


class MarkdownAbstractListStrategy(AbstractListStrategy):

    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')
