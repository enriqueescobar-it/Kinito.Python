from Section09_Decorator.DynamicDecorator.FileWithLogging import FileWithLogging

if __name__ == '__main__':
  file = FileWithLogging(open('hello.txt', 'w'))
  file.writelines(['hello', 'world'])
  file.write('testing')
  file.close()
