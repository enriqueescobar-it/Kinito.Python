from Section11_Flyweight.FlyweightTextFormatting.BetterFormattedText import BetterFormattedText
from Section11_Flyweight.FlyweightTextFormatting.FormattedText import FormattedText

if __name__ == '__main__':
    ft = FormattedText('This is a brave new world')
    ft.capitalize(10, 15)
    print(ft)

    bft = BetterFormattedText('This is a brave new world')
    bft.get_range(16, 19).capitalize = True
    print(bft)
