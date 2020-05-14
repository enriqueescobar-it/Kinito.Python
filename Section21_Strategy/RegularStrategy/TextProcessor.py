from Section21_Strategy.RegularStrategy.HtmlAbstractListStrategy import HtmlAbstractListStrategy
from Section21_Strategy.RegularStrategy.MarkdownAbstractListStrategy import MarkdownAbstractListStrategy
from Section21_Strategy.RegularStrategy.OutputFormatEnum import OutputFormatEnum


class TextProcessor:
    def __init__(self, list_strategy=HtmlAbstractListStrategy()):
        self.buffer = []
        self.list_strategy = list_strategy

    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(
                self.buffer, item
            )
        self.list_strategy.end(self.buffer)

    def set_output_format(self, format):
        if format == OutputFormatEnum.MARKDOWN:
            self.list_strategy = MarkdownAbstractListStrategy()
        elif format == OutputFormatEnum.HTML:
            self.list_strategy = HtmlAbstractListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return ''.join(self.buffer)
