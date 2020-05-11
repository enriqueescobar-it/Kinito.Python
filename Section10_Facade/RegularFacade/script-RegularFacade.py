from Section10_Facade.RegularFacade.Console import Console

if __name__ == '__main__':
  c = Console()
  c.write('hello')
  ch = c.get_char_at(0)
