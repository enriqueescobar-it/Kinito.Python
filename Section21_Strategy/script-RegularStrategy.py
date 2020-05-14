from Section21_Strategy.RegularStrategy.OutputFormatEnum import OutputFormatEnum
# not required but a good idea
from Section21_Strategy.RegularStrategy.TextProcessor import TextProcessor

if __name__ == '__main__':
    items = ['foo', 'bar', 'baz']
    tp = TextProcessor()
    tp.set_output_format(OutputFormatEnum.MARKDOWN)
    tp.append_list(items)
    print(tp)
    tp.set_output_format(OutputFormatEnum.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)
